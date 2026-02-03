import time
import sys
import os
import re
from pathlib import Path
from .backlog import BacklogManager
from .llm import LLMClient
from .tools import ToolManager

# Constants
REPO_ROOT = Path(__file__).parent.parent
AGENT_ID = f"kaizen-core-{os.getpid()}"
MAX_TURNS = 5

def main():
    print(f"🚀 Kaizen Agent ({AGENT_ID}) started.")
    print(f"📂 Workspace: {REPO_ROOT}")
    
    backlog = BacklogManager(AGENT_ID)
    tools = ToolManager(REPO_ROOT)
    llm = LLMClient() 

    while True:
        print("👀 Polling backlog...")
        task = backlog.get_pending_task()
        
        if task:
            print(f"⚡ Claimed Task: {task['title']}")
            process_task(task, tools, llm, backlog)
        else:
            time.sleep(5) 

def process_task(task, tools, llm, backlog):
    try:
        # 1. Gather Context
        kaizen_principles = tools.read_file("KAIZEN.md")
        files = tools.list_files(".")
        history = []
        
        system_prompt = f"""
You are an autonomous AI agent working in the Kaizen framework.
Your goal is to complete the assigned task by executing tools.

# Core Principles
{kaizen_principles[:1000]}...

# Available Tools
- read_file(path) -> str
- write_file(path, content) -> str
- run_shell(command) -> str
- list_files(path) -> str

# Protocol
1. THINK: Analyze the situation and decide next step.
2. ACT: Execute a tool using this format:
   TOOL: tool_name(arg1="value", arg2="value")
3. OBSERVE: Read the tool output.
4. REPEAT: Loop until task is done.
5. FINISH: When done, output "FINISHED: <summary>"

# IMPORTANT
- Only one tool call per turn.
- To write a file, you MUST use `write_file`.
- Do not hallucinate file contents. Read them first.
"""
        
        initial_user_prompt = f"""
TASK: {task['title']}
CONTEXT: {task.get('context', 'None')}
WORKSPACE: {files}

Begin.
"""
        history.append({"role": "user", "content": initial_user_prompt})

        for turn in range(MAX_TURNS):
            print(f"🔄 Turn {turn+1}/{MAX_TURNS}")
            
            # CALL LLM
            response = llm.complete(system_prompt, format_history(history))
            print(f"🤖 Agent:\n{response}")
            history.append({"role": "assistant", "content": response})

            # CHECK FOR FINISH
            if "FINISHED:" in response:
                summary = response.split("FINISHED:", 1)[1].strip()
                backlog.complete_task(task['id'], success=True, result=summary)
                print("✅ Task Completed.")
                return

            # PARSE AND EXECUTE TOOL
            tool_call = parse_tool_call(response)
            if tool_call:
                name, args = tool_call
                print(f"🛠️ Executing: {name} {args}")
                
                output = execute_tool(name, args, tools)
                print(f"📄 Output:\n{output[:200]}...") # Truncate log
                
                history.append({"role": "user", "content": f"TOOL_OUTPUT: {output}"})
            else:
                print("⚠️ No tool call detected. Prompting agent to act...")
                history.append({"role": "user", "content": "Please execute a tool or say FINISHED."})

        # If we run out of turns
        backlog.complete_task(task['id'], success=False, result="Task timed out (Max turns reached).")
        print("❌ Task Timed Out.")
        
    except Exception as e:
        print(f"❌ Task Failed: {e}")
        backlog.complete_task(task['id'], success=False, result=str(e))

def format_history(history):
    # Convert list of dicts to string for simple LLMs
    return "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in history])

def parse_tool_call(text):
    # Regex for TOOL: name(arg="val")
    # Very basic parsing, fragile but works for MVP
    match = re.search(r'TOOL:\s*(\w+)\((.*)\)', text, re.DOTALL)
    if match:
        name = match.group(1)
        args_str = match.group(2)
        
        # Parse args (hacky)
        args = {}
        # path="foo.txt", content="bar"
        # This regex is a simplification and fails on complex strings with commas
        # Ideally use an LLM that outputs JSON
        
        # Simple parser for path="value"
        path_match = re.search(r'path=["\']([^"\']+)["\']', args_str)
        if path_match: args['path'] = path_match.group(1)
        
        content_match = re.search(r'content=["\']([\s\S]*)["\']', args_str)
        if content_match: args['content'] = content_match.group(1)
        
        cmd_match = re.search(r'command=["\']([^"\']+)["\']', args_str)
        if cmd_match: args['command'] = cmd_match.group(1)
        
        return name, args
    return None

def execute_tool(name, args, tools):
    if name == "read_file":
        return tools.read_file(args.get('path', ''))
    elif name == "write_file":
        return tools.write_file(args.get('path', ''), args.get('content', ''))
    elif name == "run_shell":
        return tools.run_shell(args.get('command', ''))
    elif name == "list_files":
        return tools.list_files(args.get('path', '.'))
    return "Error: Unknown tool."

if __name__ == "__main__":
    main()
