import os
import time
import sys
import random
from datetime import datetime

# Add local path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from hive_client import HiveClient
from agent_comm import AgentComm

class ContinuousImprover:
    def __init__(self, agent_name="worker"):
        self.agent_id = f"{agent_name}-{os.getpid()}"
        self.hive = HiveClient(self.agent_id)
        self.comm = AgentComm(self.agent_id)
        self.comm.log("Continuous Improver Daemon Started.")

    def check_skill_decay(self):
        """
        Simulated Logic: Check for skills that haven't been touched in 30 days.
        In a real agent, this would analyze file timestamps.
        """
        # 10% chance to find "decay" for demo purposes
        if random.random() < 0.1:
            self.comm.log("Detected skill decay in 'random-skill'. Creating task.")
            self.hive.add_task("Review 'random-skill' for updates", priority="low")

    def run_cycle(self):
        """Single Tick"""
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Polling backlog...")
        
        # 1. Check for work
        task = self.hive.get_task()
        if task:
            print(f"✅ Claimed Task: {task['title']}")
            self.comm.log(f"Started task: {task['title']}")
            
            # SIMULATE WORK (In reality, this is where the Agentic Loop runs)
            # e.g. subprocess.run(["claude", "do", task['title']])
            time.sleep(2) 
            
            self.hive.complete_task(task['id'], result="Analyzed and updated.")
            print(f"🏁 Completed Task: {task['title']}")
            self.comm.log(f"Completed task: {task['title']}")
        else:
            print("💤 No tasks. Checking for improvements...")
            # 2. If no work, look for improvements (Self-Evolution)
            self.check_skill_decay()
            time.sleep(5)

    def start(self):
        try:
            while True:
                self.run_cycle()
        except KeyboardInterrupt:
            print("Stopping daemon.")

if __name__ == "__main__":
    bot = ContinuousImprover(agent_name="kaizen-bot")
    bot.start()
