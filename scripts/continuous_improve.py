import os
import time
import sys
import random
from datetime import datetime

# Add local path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from hive_client import HiveClient
from agent_comm import AgentComm
from benchmark_repo import RepoJudge

class ContinuousImprover:
    def __init__(self, agent_name="worker"):
        self.agent_id = f"{agent_name}-{os.getpid()}"
        self.hive = HiveClient(self.agent_id)
        self.comm = AgentComm(self.agent_id)
        self.judge = RepoJudge()
        self.cycle_count = 0
        self.comm.log("Continuous Improver Daemon Started.")

    def check_skill_decay(self):
        """
        Check for skills that have not been updated recently.
        Future Enhancement: Implement file timestamp analysis.
        """
        # Heuristic: 10% chance to flag decay during demo mode
        if random.random() < 0.1:
            self.comm.log("Detected skill decay in 'random-skill'. Creating task.")
            self.hive.add_task("Review 'random-skill' for updates", priority="low")

    def run_cycle(self):
        """Single Tick"""
        self.cycle_count += 1
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Polling backlog (Cycle {self.cycle_count})...")
        
        # 0. Run Benchmarks (every 10 cycles)
        if self.cycle_count % 10 == 0:
            report = self.judge.run()
            self.comm.log(f"Kaizen Score: {report['kaizen_score']}")
            if report['kaizen_score'] < 50:
                 self.hive.add_task("Improve Repository Health (Score < 50)", priority="high")

        # 1. Check for work
        task = self.hive.get_task()
        if task:
            print(f"✅ Claimed Task: {task['title']}")
            self.comm.log(f"Started task: {task['title']}")
            
            # Placeholder: Agentic Execution Loop
            # In production, this invokes the LLM agent to perform the work.
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
