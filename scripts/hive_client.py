import json
import os
import uuid
from datetime import datetime

try:
    from agent_comm import AgentComm
except ImportError:
    # If run directly
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from agent_comm import AgentComm

AGENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".agents")
backlog_file = os.path.join(AGENTS_DIR, "backlog.json")

class HiveClient:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.comm = AgentComm(agent_id)

    def get_task(self):
        """Poll for a pending task and claim it."""
        with self.comm.file_lock("backlog.json"):
            if not os.path.exists(backlog_file):
                return None
            
            with open(backlog_file) as f:
                tasks = json.load(f)
            
            for task in tasks:
                if task["status"] == "pending" and task["assigned_to"] is None:
                    # Claim it
                    task["status"] = "in_progress"
                    task["assigned_to"] = self.agent_id
                    task["started_at"] = datetime.now().isoformat()
                    
                    # Save
                    with open(backlog_file, 'w') as f:
                        json.dump(tasks, f, indent=2)
                    
                    return task
            return None

    def complete_task(self, task_id, status="completed", result=None):
        """Mark a task as completed."""
        with self.comm.file_lock("backlog.json"):
            with open(backlog_file) as f:
                tasks = json.load(f)
            
            for task in tasks:
                if task["id"] == task_id:
                    task["status"] = status
                    task["completed_at"] = datetime.now().isoformat()
                    if result:
                        task["result"] = result
                    break
            
            with open(backlog_file, 'w') as f:
                json.dump(tasks, f, indent=2)

    def add_task(self, title, priority="medium"):
        """Add a new task to the backlog."""
        with self.comm.file_lock("backlog.json"):
            if os.path.exists(backlog_file):
                with open(backlog_file) as f:
                    try:
                        tasks = json.load(f)
                    except json.JSONDecodeError:
                        tasks = []
            else:
                tasks = []
            
            new_task = {
                "id": str(uuid.uuid4())[:8],
                "title": title,
                "status": "pending",
                "priority": priority,
                "assigned_to": None,
                "created_at": datetime.now().isoformat()
            }
            tasks.append(new_task)
            
            with open(backlog_file, 'w') as f:
                json.dump(tasks, f, indent=2)
            
            return new_task["id"]

if __name__ == "__main__":
    # Test
    hive = HiveClient("test-worker")
    print("Adding task...")
    tid = hive.add_task("Test Task")
    print(f"Added {tid}")
    
    print("Claiming task...")
    task = hive.get_task()
    if task:
        print(f"Claimed: {task['title']}")
        hive.complete_task(task['id'])
        print("Completed.")
    else:
        print("No tasks found.")
