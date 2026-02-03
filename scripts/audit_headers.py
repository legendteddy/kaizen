import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")

def audit():
    missing = []
    for skill in os.listdir(SKILLS_DIR):
        path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
        if not os.path.exists(path):
            continue
            
        with open(path, encoding="utf-8") as f:
            content = f.read()
            
        if "Activation Trigger" not in content:
            missing.append(skill)
            
    print(f"Found {len(missing)} skills missing 'Activation Trigger':")
    for m in missing:
        print(f"- {m}")

if __name__ == "__main__":
    audit()
