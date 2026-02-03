import subprocess
import os
from pathlib import Path

class ToolManager:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root

    def read_file(self, file_path: str) -> str:
        target = self.workspace_root / file_path
        if not target.exists():
            return f"Error: File {file_path} does not exist."
        with open(target, 'r', encoding='utf-8') as f:
            return f.read()

    def run_shell(self, command: str) -> str:
        # Safety check: simplistic
        if "rm -rf" in command:
            return "Error: Command blocked for safety."
            
        try:
            result = subprocess.run(
                command, 
                shell=True, 
                cwd=self.workspace_root, 
                capture_output=True, 
                text=True
            )
            return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
        except Exception as e:
            return f"Error executing command: {e}"

    def list_files(self, dir_path: str = ".") -> str:
        target = self.workspace_root / dir_path
        if not target.exists():
            return "Error: Directory does not exist."
        return "\n".join(os.listdir(target))