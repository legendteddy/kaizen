import os
import shlex
import subprocess
from pathlib import Path


class SecurityError(Exception):
    pass

class ToolManager:
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root.resolve()
        
        # Strict allowlist for shell commands
        self.ALLOWED_COMMANDS = {
            "ls", "dir", "grep", "find", 
            "python", "pytest", 
            "git", "echo", "cat", "type"
        }

    def _validate_path(self, path_str: str) -> Path:
        """Enforces a 'jail' mechanism. No accessing parent dirs."""
        try:
            # Resolve the absolute path
            target = (self.workspace_root / path_str).resolve()
            
            # Check if it starts with the workspace root
            if not str(target).startswith(str(self.workspace_root)):
                raise SecurityError(f"Access Denied: Path '{path_str}' escapes workspace.")
            
            return target
        except Exception as e:
            raise SecurityError(f"Invalid path: {e}") from e

    def _validate_command(self, command: str):
        """Prevents dangerous shell execution."""
        # 1. Block chaining operators
        if any(char in command for char in [";", "&&", "||", "|", "`", "$("]):
            raise SecurityError("Chained commands/pipes are blocked in Safe Mode.")
            
        # 2. Check the executable
        parts = shlex.split(command, posix=False) # posix=False for Windows compatibility
        if not parts:
            raise SecurityError("Empty command")
            
        executable = parts[0]
        if executable not in self.ALLOWED_COMMANDS:
            raise SecurityError(f"Command '{executable}' is not in the allowlist.")

    def read_file(self, file_path: str) -> str:
        try:
            target = self._validate_path(file_path)
            if not target.exists():
                return f"Error: File {file_path} does not exist."
            if not target.is_file():
                return f"Error: {file_path} is not a file."
                
            with open(target, encoding='utf-8') as f:
                return f.read()
        except SecurityError as e:
            return f"SECURITY ALERT: {e}"
        except Exception as e:
            return f"Error reading file: {e}"

    def run_shell(self, command: str) -> str:
        try:
            self._validate_command(command)
            
            result = subprocess.run(
                command, 
                shell=True, 
                cwd=self.workspace_root, 
                capture_output=True, 
                text=True,
                timeout=30 # Timeout to prevent infinite loops
            )
            return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
            
        except SecurityError as e:
            return f"SECURITY ALERT: {e}"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out (30s limit)."
        except Exception as e:
            return f"Error executing command: {e}"

    def list_files(self, dir_path: str = ".") -> str:
        try:
            target = self._validate_path(dir_path)
            if not target.exists():
                return "Error: Directory does not exist."
            return "\n".join(os.listdir(target))
        except SecurityError as e:
            return f"SECURITY ALERT: {e}"

    def write_file(self, file_path: str, content: str) -> str:
        """Writes content to a file. Overwrites if exists."""
        try:
            target = self._validate_path(file_path)
            
            # Ensure parent directory exists
            target.parent.mkdir(parents=True, exist_ok=True)
            
            with open(target, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Success: Wrote to {file_path}"
        except SecurityError as e:
            return f"SECURITY ALERT: {e}"
        except Exception as e:
            return f"Error writing file: {e}"