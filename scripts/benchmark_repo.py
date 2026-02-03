import os
import json
import time
from datetime import datetime

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")
AGENTS_DIR = os.path.join(ROOT_DIR, ".agents")
LOG_FILE = os.path.join(AGENTS_DIR, "benchmark.log")

class RepoJudge:
    def __init__(self):
        self.metrics = {}

    def count_skills(self):
        if not os.path.exists(SKILLS_DIR):
            return 0
        return len([d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d))])

    def assess_depth(self):
        """Count skills that are 'Industrial Grade' (> 1.5KB)"""
        if not os.path.exists(SKILLS_DIR):
            return 0
        deep_skills = 0
        total_skills = 0
        for sk in os.listdir(SKILLS_DIR):
            path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
            if os.path.exists(path):
                total_skills += 1
                if os.path.getsize(path) > 1500:
                    deep_skills += 1
        
        return (deep_skills / total_skills * 100) if total_skills > 0 else 0

    def check_safety(self):
        """Check if lock files are stale."""
        locks_dir = os.path.join(AGENTS_DIR, "locks")
        if not os.path.exists(locks_dir):
            return 100
        
        stale = 0
        total = 0
        for lock in os.listdir(locks_dir):
            total += 1
            # Simple heuristic: if created > 1 hour ago (not implemented here, just counting presence)
            # In a real judge, we'd parse the JSON expiry.
            pass
        
        # Arbitrary score: -10 per lock (assuming locks should be transient)
        return max(0, 100 - (total * 10))

    def run(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚖️  Running Judgment Day...")
        
        skill_count = self.count_skills()
        skill_depth = self.assess_depth()
        safety_score = self.check_safety()
        
        # Blended Score
        # 40% Depth, 30% Scale (target 70), 30% Safety
        scale_score = min(100, (skill_count / 70) * 100)
        kaizen_score = (skill_depth * 0.4) + (scale_score * 0.3) + (safety_score * 0.3)
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "skill_count": skill_count,
                "skill_depth_percent": round(skill_depth, 1),
                "safety_score": safety_score
            },
            "kaizen_score": round(kaizen_score, 1)
        }
        
        self.log_report(report)
        print(f"🏆 Kaizen Score: {report['kaizen_score']}/100 (Depth: {report['metrics']['skill_depth_percent']}%)")
        return report

    def log_report(self, report):
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(json.dumps(report) + "\n")

if __name__ == "__main__":
    judge = RepoJudge()
    judge.run()
