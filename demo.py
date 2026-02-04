#!/usr/bin/env python3
"""
Kaizen Demo - Test that the agent works end-to-end.

This script:
1. Detects your LLM provider from env vars
2. Adds a sample task
3. Executes it with the agent
4. Shows the results
"""
import sys
from pathlib import Path

# Add repo root to path (must be before kaizen_core imports)
REPO_ROOT = Path(__file__).parent
sys.path.insert(0, str(REPO_ROOT))

from kaizen_core.backlog import BacklogManager  # noqa: E402
from kaizen_core.llm import LLMClient, detect_provider  # noqa: E402
from kaizen_core.main import process_task  # noqa: E402
from kaizen_core.models import Task  # noqa: E402
from kaizen_core.tools.manager import ToolManager  # noqa: E402


def main():
    print("=" * 60)
    print("KAIZEN AGENT DEMO")
    print("=" * 60)
    
    # 1. Detect provider
    provider, api_key = detect_provider()
    print(f"\nDetected Provider: {provider}")
    if provider == "ollama":
        print("  (No API key found - using local Ollama)")
        print("  Set OPENAI_API_KEY, ANTHROPIC_API_KEY, or GOOGLE_API_KEY for better results.")
    else:
        print(f"  API Key: {api_key[:8]}...{api_key[-4:]}")
    
    # 2. Initialize components
    print("\nInitializing agent...")
    llm = LLMClient()
    backlog = BacklogManager("kaizen-demo")
    tools = ToolManager(REPO_ROOT, agent_id="kaizen-demo")
    
    # 3. Add a sample task
    sample_task = Task(
        title="List the Python files in the kaizen_core directory",
        context="Use the list_files tool to explore the kaizen_core/ directory and report what you find."
    )
    
    print(f"\nTask: {sample_task.title}")
    print("-" * 60)
    
    # 4. Execute
    print("\nExecuting task with LLM...")
    try:
        process_task(sample_task, tools, llm, backlog)
        print("\n" + "=" * 60)
        print("DEMO COMPLETE - Agent executed successfully!")
        print("=" * 60)
    except Exception as e:
        print(f"\nError: {e}")
        print("\nTroubleshooting:")
        print("  1. If using Ollama: Make sure 'ollama serve' is running")
        print("  2. If using API: Check your API key is valid")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
