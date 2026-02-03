import json
import sqlite3
from datetime import datetime
from pathlib import Path

from .models import Task, TaskStatus


class BacklogManager:
    def __init__(self, agent_id: str, db_path: Path | None = None):
        self.agent_id = agent_id
        if db_path is None:
            # Look for repo root
            self.db_path = Path(__file__).parent.parent / ".agents" / "kaizen.db"
        else:
            self.db_path = db_path
        
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    context TEXT,
                    status TEXT NOT NULL,
                    priority TEXT NOT NULL,
                    assigned_to TEXT,
                    created_at TEXT NOT NULL,
                    started_at TEXT,
                    completed_at TEXT,
                    result TEXT,
                    metadata TEXT
                )
            """)
            conn.commit()

    def add_task(self, title: str, priority: str = "medium", context: str = ""):
        task = Task(title=title, priority=priority, context=context)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO tasks (id, title, context, status, priority, created_at, metadata) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (task.id, task.title, task.context, task.status.value, task.priority.value, task.created_at.isoformat(), json.dumps(task.metadata))
            )

    def get_pending_task(self) -> Task | None:
        """Atomically claims a pending task using SQLite."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            # Use a transaction to find and update
            cursor.execute(
                "SELECT * FROM tasks WHERE status = ? AND assigned_to IS NULL LIMIT 1", 
                (TaskStatus.PENDING.value,)
            )
            row = cursor.fetchone()
            
            if row:
                task_id = row['id']
                started_at = datetime.utcnow().isoformat()
                cursor.execute(
                    "UPDATE tasks SET status = ?, assigned_to = ?, started_at = ? WHERE id = ?",
                    (TaskStatus.IN_PROGRESS.value, self.agent_id, started_at, task_id)
                )
                conn.commit()
                
                # Convert row to Task object
                data = dict(row)
                data['status'] = TaskStatus(data['status'])
                data['metadata'] = json.loads(data['metadata'])
                return Task(**data)
        return None

    def complete_task(self, task_id: str, success: bool = True, result: str = ""):
        status = TaskStatus.COMPLETED if success else TaskStatus.FAILED
        completed_at = datetime.utcnow().isoformat()
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "UPDATE tasks SET status = ?, completed_at = ?, result = ? WHERE id = ?",
                (status.value, completed_at, result, task_id)
            )