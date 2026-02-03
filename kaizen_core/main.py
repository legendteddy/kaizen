import time
import sys
import os
from pathlib import Path
from .backlog import BacklogManager
from .llm import LLMClient
from .tools import ToolManager

# Constants
REPO_ROOT = Path(__file__).parent.parent
AGENT_ID = f"kaizen-core-{os.getpid()}"

def main():
    print(f"🚀 Kaizen Agent ({AGENT_ID}) started.")
    print(f"📂 Workspace: {REPO_ROOT}")
    
    backlog = BacklogManager(AGENT_ID)
    tools = ToolManager(REPO_ROOT)
    llm = LLMClient() # Defaults to localhost:11434

    while True:
        print("👀 Polling backlog...")
        task = backlog.get_pending_task()
        
        if task:
            print(f"⚡ Claimed Task: {task['title']}")
            process_task(task, tools, llm, backlog)
        else:
            time.sleep(5) # Wait before next poll

def process_task(task, tools, llm, backlog):
    try:
        # 1. Gather Context
        kaizen_principles = tools.read_file("KAIZEN.md")
        files = tools.list_files(".")
        
        # 2. Construct Prompt
        system_prompt = f"""
You are an autonomous AI agent working in the Kaizen framework.
Your goal is to complete the assigned task using the available tools.

# Core Principles
{kaizen_principles[:1000]}... (truncated)

# Available Tools
- read_file(path)
- run_shell(command)
- list_files(path)

# Workspace
{files}
"""
        user_prompt = f"""
TASK: {task['title']}
CONTEXT: {task.get('context', 'None')}

Please analyze this task. 
1. What files do I need to check?
2. What is the plan?

Provide a summary of your analysis.
"""
        
        # 3. Think (LLM Call)
        print("🤔 Thinking...")
        response = llm.complete(system_prompt, user_prompt)
        print(f"💡 Agent Analysis:\n{response}")
        
        # 4. Action (For V1, we just log the analysis as the result)
        # In V2, we would parse tool calls from 'response'
        
        backlog.complete_task(task['id'], success=True, result=response)
        print("✅ Task Completed.")
        
    except Exception as e:
        print(f"❌ Task Failed: {e}")
        backlog.complete_task(task['id'], success=False, result=str(e))

if __name__ == "__main__":
    main()
