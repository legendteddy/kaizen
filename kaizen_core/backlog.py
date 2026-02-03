import json
import os
import time
from datetime import datetime
from typing import Optional, List, Dict
from pathlib import Path

# Paths relative to the repository root
# Assuming this runs from inside kaizen/ or similar
REPO_ROOT = Path(__file__).parent.parent
AGENTS_DIR = REPO_ROOT / ".agents"
BACKLOG_FILE = AGENTS_DIR / "backlog.json"
LOCK_FILE = AGENTS_DIR / "backlog.json.lock"

class BacklogManager:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self._ensure_dir()

    def _ensure_dir(self):
        if not AGENTS_DIR.exists():
            AGENTS_DIR.mkdir(parents=True)
        if not BACKLOG_FILE.exists():
            with open(BACKLOG_FILE, 'w') as f:
                json.dump([], f)

    def _acquire_lock(self, timeout=5):
        start = time.time()
        while time.time() - start < timeout:
            if not LOCK_FILE.exists():
                try:
                    with open(LOCK_FILE, 'w') as f:
                        f.write(self.agent_id)
                    return True
                except FileExistsError:
                    pass
            time.sleep(0.1)
        return False

    def _release_lock(self):
        if LOCK_FILE.exists():
            try:
                os.remove(LOCK_FILE)
            except:
                pass

    def get_pending_task(self) -> Optional[Dict]:
        """Finds a pending task and claims it."""
        if not self._acquire_lock():
            return None

        try:
            with open(BACKLOG_FILE, 'r') as f:
                tasks = json.load(f)

            for task in tasks:
                if task["status"] == "pending" and task["assigned_to"] is None:
                    # Claim it
                    task["status"] = "in_progress"
                    task["assigned_to"] = self.agent_id
                    task["started_at"] = datetime.utcnow().isoformat()
                    
                    # Save
                    with open(BACKLOG_FILE, 'w') as f:
                        json.dump(tasks, f, indent=4)
                    
                    return task
            return None
        finally:
            self._release_lock()

    def complete_task(self, task_id: str, success: bool = True, result: str = ""):
        """Marks a task as completed or failed."""
        if not self._acquire_lock():
            print("Failed to acquire lock to complete task")
            return

        try:
            with open(BACKLOG_FILE, 'r') as f:
                tasks = json.load(f)

            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = "completed" if success else "failed"
                    task["completed_at"] = datetime.utcnow().isoformat()
                    task["result"] = result
                    break
            
            with open(BACKLOG_FILE, 'w') as f:
                json.dump(tasks, f, indent=4)
        finally:
            self._release_lock()

    def add_task(self, title: str, priority: str = "medium", context: str = ""):
        """Adds a new task to the backlog."""
        if not self._acquire_lock():
            return

        try:
            with open(BACKLOG_FILE, 'r') as f:
                tasks = json.load(f)
            
            new_task = {
                "id": f"task_{int(time.time())}",
                "title": title,
                "status": "pending",
                "priority": priority,
                "assigned_to": None,
                "created_at": datetime.utcnow().isoformat(),
                "context": context
            }
            
            tasks.append(new_task)
            
            with open(BACKLOG_FILE, 'w') as f:
                json.dump(tasks, f, indent=4)
        finally:
            self._release_lock()
