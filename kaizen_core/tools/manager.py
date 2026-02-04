import os
import subprocess
from pathlib import Path


class ToolManager:
    def __init__(self, repo_root: Path, agent_id: str = "default"):
        self.root = repo_root.resolve()
        self.agent_id = agent_id
        self.worktree_path = None
        
        # Strictly limited shell commands
        self.whitelist = {
            "ls", "git", "python", "pytest", "ruff", "cat", 
            "grep", "mkdir", "dir", "echo", "npm", "node"
        }

    def setup_sandbox(self):
        """Creates an isolated git worktree for the agent."""
        if not (self.root / ".git").exists():
             return f"Info: Not a git repo. Running in-place at {self.root}"
        
        sandbox_dir = self.root / ".agents" / "worktrees" / self.agent_id
        sandbox_dir.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            # git worktree add -b [branch] [path]
            subprocess.run(
                f"git worktree add -b agent-{self.agent_id} {sandbox_dir}", 
                shell=True, cwd=self.root, capture_output=True
            )
            self.worktree_path = sandbox_dir
            return f"Sandbox created: {sandbox_dir}"
        except Exception as e:
            return f"Error creating sandbox: {e}"

    def cleanup(self):
        """Removes the worktree and deletes the agent branch."""
        if self.worktree_path and self.worktree_path.exists():
            subprocess.run(f"git worktree remove {self.worktree_path} --force", shell=True, cwd=self.root)
            subprocess.run(f"git branch -D agent-{self.agent_id}", shell=True, cwd=self.root)
            return "Cleanup successful."
        return "Nothing to cleanup."

    def _get_active_root(self) -> Path:
        return self.worktree_path if self.worktree_path else self.root

    def _is_safe_path(self, path: str) -> bool:
        """Prevents path traversal attacks."""
        active_root = self._get_active_root()
        target = (active_root / path).resolve()
        return active_root in target.parents or target == active_root

    def read_file(self, path: str) -> str:
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied (Outside sandbox)."
        try:
            file_path = self._get_active_root() / path
            if not file_path.exists():
                return f"Error: File {path} not found."
                
            content = file_path.read_text(encoding="utf-8")
            line_count = len(content.splitlines())
            
            # Smart Context Management
            max_lines = 500
            if line_count > max_lines:
                truncated = "\n".join(content.splitlines()[:max_lines])
                return f"{truncated}\n\n[SYSTEM WARNING: File truncated. {line_count - max_lines} lines hidden. Use 'read_chunk' to read more.]"
            
            return content
        except Exception as e:
            return f"Error reading file: {e}"

    def list_files(self, path: str = ".") -> str:
        """Lists files in a directory."""
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied (Outside sandbox)."
        try:
            target = self._get_active_root() / path
            if not target.exists():
                return f"Error: Path {path} not found."
            if not target.is_dir():
                return f"Error: {path} is not a directory."
            
            files = []
            for item in sorted(target.iterdir()):
                # Skip hidden and venv
                if item.name.startswith(".") or item.name in ("__pycache__", "node_modules", "venv"):
                    continue
                prefix = "[DIR]" if item.is_dir() else "[FILE]"
                files.append(f"{prefix} {item.name}")
            
            return "\n".join(files) if files else "(empty directory)"
        except Exception as e:
            return f"Error listing files: {e}"

    def search_files(self, pattern: str, path: str = ".") -> str:
        """Python-native search (Cross-platform)."""
        if not self._is_safe_path(path):
             return "SECURITY ALERT: Access denied."
        
        matches = []
        search_root = self._get_active_root() / path
        
        try:
            # Walk through files
            for root, _, files in os.walk(search_root):
                for file in files:
                    # Skip hidden/git/venv files
                    if any(x in root for x in [".git", "__pycache__", "node_modules", "venv"]):
                        continue
                        
                    full_path = Path(root) / file
                    try:
                        # Simple case-insensitive string match for speed
                        # For regex, we'd use re.search
                        content = full_path.read_text(encoding="utf-8", errors="ignore")
                        if pattern.lower() in content.lower():
                            rel_path = full_path.relative_to(self._get_active_root())
                            matches.append(str(rel_path))
                    except Exception:
                        continue  # Skip binary files
            
            if not matches:
                return "No matches found."
            return "\n".join(matches[:50])  # Limit to top 50
        except Exception as e:
            return f"Error searching files: {e}"

    def write_file(self, path: str, content: str) -> str:
        """Writes content to a file."""
        if not self._is_safe_path(path):
            return "SECURITY ALERT: Access denied (Outside sandbox)."
        try:
            file_path = self._get_active_root() / path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
            return f"Successfully wrote to {path}"
        except Exception as e:
            return f"Error writing file: {e}"

    def run_shell(self, command: str) -> str:
        """Runs a whitelisted shell command."""
        # Security: Extract first word (command name)
        cmd_name = command.split()[0] if command.split() else ""
        
        # Block dangerous patterns
        dangerous = [";", "&&", "||", "|", "`", "$(", "rm ", "del ", "format "]
        if any(d in command for d in dangerous):
            return "SECURITY ALERT: Dangerous command pattern blocked."
        
        if cmd_name not in self.whitelist:
            return f"SECURITY ALERT: Command '{cmd_name}' not whitelisted. Allowed: {', '.join(self.whitelist)}"
        
        try:
            result = subprocess.run(
                command,
                shell=True,
                cwd=self._get_active_root(),
                capture_output=True,
                text=True,
                timeout=30
            )
            output = result.stdout + result.stderr
            return output.strip() if output.strip() else "(no output)"
        except subprocess.TimeoutExpired:
            return "Error: Command timed out (30s limit)."
        except Exception as e:
            return f"Error running command: {e}"
