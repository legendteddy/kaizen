import contextlib
import json
import os
import time
from datetime import datetime, timedelta

AGENTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".agents")
registry_file = os.path.join(AGENTS_DIR, "registry.json")
locks_dir = os.path.join(AGENTS_DIR, "locks")
signals_dir = os.path.join(AGENTS_DIR, "signals")
log_file = os.path.join(AGENTS_DIR, "chat.log")

class AgentComm:
    def __init__(self, agent_id, agent_type="Generic"):
        self.agent_id = agent_id
        self.agent_type = agent_type
        self.ensure_dirs()
        self.register()

    def ensure_dirs(self):
        os.makedirs(locks_dir, exist_ok=True)
        os.makedirs(signals_dir, exist_ok=True)
        if not os.path.exists(registry_file):
            with open(registry_file, 'w') as f:
                json.dump({"agents": {}}, f)

    def register(self):
        """Register capability"""
        try:
            with open(registry_file, 'r+') as f:
                data = json.load(f)
                data["agents"][self.agent_id] = {
                    "type": self.agent_type,
                    "pid": os.getpid(),
                    "status": "active",
                    "last_heartbeat": datetime.now().isoformat()
                }
                f.seek(0)
                json.dump(data, f, indent=2)
                f.truncate()
        except Exception as e:
            print(f"Registration failed: {e}")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        entry = f"[{timestamp}] [{self.agent_id}]: {message}\n"
        with open(log_file, "a") as f:
            f.write(entry)

    @contextlib.contextmanager
    def file_lock(self, filename, timeout=60):
        lock_path = os.path.join(locks_dir, f"{filename}.lock")
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if not os.path.exists(lock_path):
                # Acquire
                try:
                    with open(lock_path, 'w') as f:
                        json.dump({
                            "agent": self.agent_id,
                            "expiry": (datetime.now() + timedelta(minutes=5)).isoformat()
                        }, f)
                    yield True
                    # Release
                    if os.path.exists(lock_path):
                        os.remove(lock_path)
                    return
                except OSError:
                    pass # Race condition
            
            # Check for stale lock
            try:
                with open(lock_path) as f:
                    data = json.load(f)
                    expiry = datetime.fromisoformat(data["expiry"])
                    if datetime.now() > expiry:
                        print(f"Stealing stale lock from {data['agent']}")
                        os.remove(lock_path)
                        continue
            except Exception:
                pass
                
            time.sleep(1)
            print(f"Waiting for lock on {filename}...")
            
        raise TimeoutError(f"Could not acquire lock for {filename}")

if __name__ == "__main__":
    # Test
    comm = AgentComm("test-agent")
    comm.log("System initialized.")
    print("Agent Comm initialized.")
    with comm.file_lock("README.md"):
        print("Acquired lock on README.md")
        time.sleep(1)
