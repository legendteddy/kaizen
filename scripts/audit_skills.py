import os
import re
import sys


def audit_skills():
    """
    Audits the sync between skills/ directories and SKILLS.md index.
    Returns 0 if synced, 1 if drift detected.
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    skills_dir = os.path.join(root_dir, "skills")
    index_file = os.path.join(root_dir, "SKILLS.md")

    # 1. Get real skills from folders
    real_skills = {d for d in os.listdir(skills_dir) if os.path.isdir(os.path.join(skills_dir, d))}
    
    # 2. Get listed skills from SKILLS.md
    with open(index_file, encoding='utf-8') as f:
        content = f.read()
    
    # Extract links like [skill-name](skills/skill-name/)
    listed_skills = set(re.findall(r'\| \[([\w-]+)\]', content))

    # 3. Compare
    missing_from_index = real_skills - listed_skills
    missing_from_folders = listed_skills - real_skills

    print(f"Stats: {len(real_skills)} folders, {len(listed_skills)} listed.")

    if missing_from_index:
        print("\n[ERROR] Skills exist but NOT in SKILLS.md:")
        for s in missing_from_index:
            print(f"  - {s}")
    
    if missing_from_folders:
        print("\n[ERROR] Skills listed in SKILLS.md but folder MISSING:")
        for s in missing_from_folders:
            print(f"  - {s}")

    if not missing_from_index and not missing_from_folders:
        print("\n✅ SUCCESS: Index is perfectly synced.")
        return 0
    
    return 1

if __name__ == "__main__":
    sys.exit(audit_skills())
