import os
import re
from pathlib import Path
from typing import Dict, List, Any
import subprocess

class RepoJudge:
    def __init__(self, repo_root: Path):
        self.root = repo_root
        self.skills_dir = self.root / "skills"
        self.score = 100
        self.report = []

    def run_audit(self) -> str:
        """Runs all checks and returns a markdown report."""
        self.score = 100
        self.report = ["# Repo Health Audit", f"**Date:** {os.environ.get('DATE', 'Today')}", ""]
        
        self._check_skills_structure()
        self._check_python_quality()
        self._check_backlog_health()
        
        self.report.append(f"\n## Final Score: {self.score}/100")
        return "\n".join(self.report)

    def _check_skills_structure(self):
        """Audit the skills directory."""
        self.report.append("## 1. Skills Structure")
        if not self.skills_dir.exists():
            self._deduct(50, "Skills directory missing!")
            return

        skill_folders = [f for f in self.skills_dir.iterdir() if f.is_dir()]
        self.report.append(f"- Found {len(skill_folders)} skill directories.")
        
        issues = 0
        for folder in skill_folders:
            readme = folder / "SKILL.md"
            if not readme.exists():
                issues += 1
                self.report.append(f"- ❌ Missing SKILL.md in `{folder.name}`")
                continue
            
            # Check frontmatter
            try:
                content = readme.read_text(encoding="utf-8")
                if not re.search(r"^---\s+name:\s+.+\s+description:\s+.+\s+---", content, re.DOTALL | re.MULTILINE):
                    issues += 1
                    self.report.append(f"- ⚠️ Invalid Frontmatter in `{folder.name}`")
            except Exception:
                pass

        if issues == 0:
            self.report.append("- ✅ All skills have valid SKILL.md structure.")
        else:
            self._deduct(issues * 2, f"Found {issues} skill structure issues.")

    def _check_python_quality(self):
        """Check Python code if possible."""
        self.report.append("\n## 2. Python Quality")
        kaizen_core = self.root / "kaizen_core"
        if not kaizen_core.exists():
            return

        # Simple Check: TODOs
        todos = 0
        for py_file in kaizen_core.rglob("*.py"):
            try:
                content = py_file.read_text(encoding="utf-8")
                todos += len(re.findall(r"#\s*TODO", content, re.IGNORECASE))
            except:
                pass
        
        self.report.append(f"- Found {todos} TODO markers in core code.")
        if todos > 5:
            self._deduct(min(todos, 10), "Too many TODOs in core code.")
        else:
            self.report.append("- ✅ TODO count is manageable.")

    def _check_backlog_health(self):
        """Check .agents/backlog.json"""
        self.report.append("\n## 3. Backlog Health")
        backlog_path = self.root / ".agents" / "backlog.json"
        
        if not backlog_path.exists():
            self.report.append("- ⚠️ No backlog found.")
            return

        try:
            import json
            with open(backlog_path, 'r', encoding='utf-8') as f:
                tasks = json.load(f)
            
            pending = sum(1 for t in tasks if t['status'] == 'pending')
            in_progress = sum(1 for t in tasks if t['status'] == 'in_progress')
            
            self.report.append(f"- Pending: {pending}")
            self.report.append(f"- In Progress: {in_progress}")
            
            if in_progress > 3:
                self._deduct(5, "High WIP (Work In Progress).")
            if pending > 10:
                self.report.append("- ℹ️ Backlog is growing.")
        except Exception as e:
            self.report.append(f"- ❌ Error reading backlog: {e}")

    def _deduct(self, points: int, reason: str):
        self.score = max(0, self.score - points)
        self.report.append(f"- 🔻 **-{points} pts**: {reason}")

if __name__ == "__main__":
    import sys
    # Force UTF-8 output for emojis on Windows
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')

    # Test run
    # If running as 'python -m kaizen_core.judge' from 'kaizen/' dir
    current_dir = Path.cwd()
    if (current_dir / "skills").exists():
        root = current_dir
    else:
        # Fallback to relative to file
        root = Path(__file__).parent.parent
        
    judge = RepoJudge(root)
    print(judge.run_audit())
