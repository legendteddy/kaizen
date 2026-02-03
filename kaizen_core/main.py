import os
import re
import time
from pathlib import Path

from .backlog import BacklogManager
from .llm import LLMClient
from .models import Task
from .tools.manager import ToolManager

# Constants
REPO_ROOT = Path(__file__).parent.parent
AGENT_ID = f"kaizen-core-{os.getpid()}"
MAX_TURNS = 10 # Increased for complex tasks

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

def process_task(task: Task, tools: ToolManager, llm: LLMClient, backlog: BacklogManager):
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
- read_file(path)
- write_file(path, content)
- run_shell(command)
- list_files(path)

# Protocol
1. THINK: Analyze the situation and decide next step.
2. ACT: Execute a tool using XML format.

# IMPORTANT
- Only one tool call per turn.
- Do not hallucinate file contents. Read them first.
"""
        
        initial_user_prompt = f"""
TASK: {task.title}
CONTEXT: {task.context or 'None'}
WORKSPACE: {files}

Begin.
"""
        history.append({"role": "user", "content": initial_user_prompt})

        consecutive_failures = 0
        max_failures = 3

        for turn in range(MAX_TURNS):
            print(f"🔄 Turn {turn+1}/{MAX_TURNS}")
            
            # CALL LLM
            response = llm.complete(system_prompt, format_history(history))
            print(f"🤖 Agent:\n{response}")
            history.append({"role": "assistant", "content": response})

            # CHECK FOR FINISH
            if "FINISHED:" in response:
                summary = response.split("FINISHED:", 1)[1].strip()
                backlog.complete_task(task.id, success=True, result=summary)
                print("✅ Task Completed.")
                return

            # PARSE AND EXECUTE TOOL
            tool_call = parse_tool_call(response)
            if tool_call:
                name, args = tool_call
                print(f"🛠️  Proposing: {name} {args}")

                # --- REFLEXION LOOP (AGI LEVEL 1) ---
                # "Measure twice, cut once."
                print("🤔 Critiquing action...")
                critique = llm.critique_action(
                    proposed_action=f"{name} {args}", 
                    context=format_history(history[-2:]) # Last 2 turns context
                )

                if not critique.get("approved", True):
                    print(f"🛑 CRITIC REJECTED: {critique['feedback']}")
                    history.append({
                        "role": "user", 
                        "content": f"CRITIC_INTERVENTION: Action blocked. Feedback: {critique['feedback']}. Please revise your plan."
                    })
                    continue  # SKIP EXECUTION, FORCE RETRY
                
                print(f"✅ Critic Approved: {critique.get('feedback', 'Go ahead')}")
                # ------------------------------------
                
                output = execute_tool(name, args, tools)
                
                # STABILITY CHECK: If tool output is an error, count as failure
                if output.startswith("Error") or output.startswith("SECURITY ALERT"):
                    consecutive_failures += 1
                    print(f"⚠️ Tool Failure ({consecutive_failures}/{max_failures})")
                else:
                    consecutive_failures = 0 # Reset on success
                
                print(f"📄 Output:\n{output[:200]}...") # Truncate log
                history.append({"role": "user", "content": f"TOOL_OUTPUT: {output}"})
            else:
                consecutive_failures += 1
                print(f"⚠️ No tool call detected ({consecutive_failures}/{max_failures}).")
                history.append({"role": "user", "content": "Error: No valid tool call found. You MUST use XML format."})

            # CIRCUIT BREAKER
            if consecutive_failures >= max_failures:
                error_msg = "Circuit Breaker Tripped: Too many consecutive failures/hallucinations."
                print(f"❌ {error_msg}")
                backlog.complete_task(task.id, success=False, result=error_msg)
                return

        # If we run out of turns
        backlog.complete_task(task.id, success=False, result="Task timed out (Max turns reached).")
        print("❌ Task Timed Out.")
        
    except Exception as e:
        print(f"❌ Task Failed: {e}")
        backlog.complete_task(task.id, success=False, result=str(e))

def format_history(history):
    return "\n".join([f"{msg['role'].upper()}: {msg['content']}" for msg in history])

def parse_tool_call(text):
    """
    Parses tool calls from LLM output.
    Supports:
    1. XML: <tool name="write_file" path="x">content</tool>
    2. Legacy: TOOL: name(arg="val")
    """
    # 1. Try XML parsing (Robust)
    # <tool name="write_file" path="skills/test.md">Content here</tool>
    xml_match = re.search(r'<tool\s+name=["\'](\w+)["\']\s*([^>]*)>(.*?)</tool>', text, re.DOTALL)
    if xml_match:
        name = xml_match.group(1)
        attrs_str = xml_match.group(2)
        content = xml_match.group(3)
        
        args = {"content": content}
        
        # Parse attributes: key="value"
        for attr in re.finditer(r'(\w+)=["\']([^"\\]+)["\\]', attrs_str):
            args[attr.group(1)] = attr.group(2)
            
        return name, args

    # 2. Try XML self-closing (for commands)
    # <tool name="run_shell" command="ls -la" />
    xml_simple = re.search(r'<tool\s+name=["\'](\w+)["\']\s*([^>]*?)\s*/>', text, re.DOTALL)
    if xml_simple:
        name = xml_simple.group(1)
        attrs_str = xml_simple.group(2)
        args = {}
        for attr in re.finditer(r'(\w+)=["\']([^"\\]+)["\\]', attrs_str):
            args[attr.group(1)] = attr.group(2)
        return name, args

    # 3. Legacy Fallback (Fragile)
    match = re.search(r'TOOL:\s*(\w+)\((.*)\)', text, re.DOTALL)
    if match:
        name = match.group(1)
        args_str = match.group(2)
        args = {}
        
        path_match = re.search(r'path=["\']([^"\\]+)["\\]', args_str)
        if path_match:
            args['path'] = path_match.group(1)
        
        content_match = re.search(r'content=["\']([\s\S]*)["\\]', args_str)
        if content_match:
            args['content'] = content_match.group(1)
        
        cmd_match = re.search(r'command=["\']([^"\\]+)["\\]', args_str)
        if cmd_match:
            args['command'] = cmd_match.group(1)
        
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