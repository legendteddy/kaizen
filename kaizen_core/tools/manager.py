import subprocess
from pathlib import Path


class ToolManager:
    def __init__(self, repo_root: Path):
        self.root = repo_root.resolve()
        # Strictly limited shell commands
        self.whitelist = {
            "ls", "git status", "git diff", "python", "pytest", 
            "ruff", "cat", "grep", "mkdir", "dir", "echo"
        }

    def _is_safe_path(self, path: str) -> bool:
        """Prevents path traversal attacks."""
        target = (self.root / path).resolve()
        return self.root in target.parents or target == self.root

    def read_file(self, path: str) -> str:
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied (Outside repo root)."
        try:
            return (self.root / path).read_text(encoding="utf-8")
        except Exception as e:
            return f"Error reading file: {e}"

    def write_file(self, path: str, content: str) -> str:
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied (Outside repo root)."
        try:
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    def run_shell(self, command: str) -> str:
        """Executes shell commands with whitelist validation."""
        base_cmd = command.split()[0].lower()
        
        # Check if the base command is in whitelist
        if base_cmd not in self.whitelist and not command.startswith("git "):
             return f"SECURITY ALERT: Command '{base_cmd}' is not in the whitelist."

        try:
            result = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                cwd=self.root,
                timeout=30
            )
            return (result.stdout + result.stderr).strip()
        except subprocess.TimeoutExpired:
            return "Error: Command timed out after 30 seconds."
        except Exception as e:
            return f"Error executing command: {e}"

    def list_files(self, path: str = ".") -> str:
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied."
        try:
            files = [str(p.relative_to(self.root)) for p in (self.root / path).rglob("*") if "__pycache__" not in str(p)]
            return "\n".join(files[:100]) # Limit output
        except Exception as e:
            return f"Error listing files: {e}"

