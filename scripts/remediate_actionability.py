import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")

CHECKLIST_TEMPLATE = """

## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?
"""

count = 0
for sk in os.listdir(SKILLS_DIR):
    path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for existing checklist or checkboxes
        if "- [ ]" not in content and "- [x]" not in content:
            print(f"Patching {sk}...")
            with open(path, 'a', encoding='utf-8') as f:
                f.write(CHECKLIST_TEMPLATE)
            count += 1

print(f"✅ Successfully patched {count} skills with Standard Checklists.")
