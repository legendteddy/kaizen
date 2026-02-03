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
        """Count skills that are 'Sovereign Grade' (> 2.0KB). Strict!"""
        if not os.path.exists(SKILLS_DIR):
            return 0
        deep_skills = 0
        total_skills = 0
        for sk in os.listdir(SKILLS_DIR):
            path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
            if os.path.exists(path):
                total_skills += 1
                if os.path.getsize(path) > 2000: # Increased from 1500
                    deep_skills += 1
        
        return (deep_skills / total_skills * 100) if total_skills > 0 else 0

    def assess_actionability(self):
        """Check for Executable Checklists (- [ ])"""
        if not os.path.exists(SKILLS_DIR):
            return 0
        actionable = 0
        total = 0
        for sk in os.listdir(SKILLS_DIR):
            path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
            if os.path.exists(path):
                total += 1
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if "- [ ]" in content or "- [x]" in content or "## Checklist" in content:
                        actionable += 1
        return (actionable / total * 100) if total > 0 else 0

    def assess_connectivity(self):
        """Check for Internal Links to other skills"""
        if not os.path.exists(SKILLS_DIR):
            return 0
        connected = 0
        total = 0
        for sk in os.listdir(SKILLS_DIR):
            path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
            if os.path.exists(path):
                total += 1
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Check for markdown links to sibling directories
                    # Regex for [Text](../skill_name) or [Text](./skill_name) or just skill_name
                    # Simple heuristic: Does it contain "(../" or "(./" or "skills/"?
                    if "](./" in content or "](../" in content or "skills/" in content:
                        connected += 1
        return (connected / total * 100) if total > 0 else 0

    def run(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚖️  Running Judgment Day (God Mode)...")
        
        # Track failures
        fails_depth = []
        fails_compliance = []
        fails_intelligence = []
        fails_actionability = []
        fails_connectivity = []
        
        if os.path.exists(SKILLS_DIR):
            for sk in os.listdir(SKILLS_DIR):
                path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
                if not os.path.exists(path): continue
                
                # Check Depth
                if os.path.getsize(path) <= 2000:
                    fails_depth.append(sk)
                
                # Check Content
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Compliance
                    if "## Activation Trigger" not in content or "> " not in content:
                        fails_compliance.append(sk)
                    # Intelligence
                    if "```" not in content:
                        fails_intelligence.append(sk)
                    # Actionability
                    if "- [ ]" not in content and "- [x]" not in content and "## Checklist" not in content:
                        fails_actionability.append(sk)
                    # Connectivity
                    if "](./" not in content and "](../" not in content and "skills/" not in content:
                        fails_connectivity.append(sk)

        skill_count = self.count_skills()
        skill_depth = (1 - (len(fails_depth) / skill_count)) * 100 if skill_count else 0
        compliance = (1 - (len(fails_compliance) / skill_count)) * 100 if skill_count else 0
        intelligence = (1 - (len(fails_intelligence) / skill_count)) * 100 if skill_count else 0
        actionability = (1 - (len(fails_actionability) / skill_count)) * 100 if skill_count else 0
        connectivity = (1 - (len(fails_connectivity) / skill_count)) * 100 if skill_count else 0
        
        # Blended Score (God Mode)
        # 20% Each: Compliance, Intelligence, Depth, Actionability, Connectivity
        scale_score = min(100, (skill_count / 70) * 100)
        
        kaizen_score = (
            (compliance * 0.20) + 
            (intelligence * 0.20) + 
            (skill_depth * 0.20) +
            (actionability * 0.20) +
            (connectivity * 0.20)
        )
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "skill_count": skill_count,
                "compliance": round(compliance, 1),
                "intelligence": round(intelligence, 1),
                "actionability": round(actionability, 1),
                "connectivity": round(connectivity, 1),
                "depth_strict": round(skill_depth, 1)
            },
            "kaizen_score": round(kaizen_score, 1)
        }
        
        self.log_report(report)
        print(f"🏆 God Mode Score: {report['kaizen_score']}/100")
        print(f"   - Compliance: {report['metrics']['compliance']}%")
        print(f"   - Intelligence: {report['metrics']['intelligence']}%")
        print(f"   - Actionability: {report['metrics']['actionability']}%")
        
        print(f"   - Connectivity: {report['metrics']['connectivity']}% (Failed: {len(fails_connectivity)})")
        if fails_connectivity: print(f"     ❌ {fails_connectivity[:5]}... (+{len(fails_connectivity)-5} more)" if len(fails_connectivity) > 5 else f"     ❌ {fails_connectivity}")
        
        print(f"   - Depth (>2KB): {report['metrics']['depth_strict']}% (Failed: {len(fails_depth)})")
        if fails_depth: print(f"     ❌ {fails_depth}")
        
        return report

    def log_report(self, report):
        with open(LOG_FILE, "a", encoding='utf-8') as f:
            f.write(json.dumps(report) + "\n")

if __name__ == "__main__":
    judge = RepoJudge()
    judge.run()
