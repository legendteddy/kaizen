import os
import re

# Resolve paths relative to the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(SCRIPT_DIR)
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")
INDEX_FILE = os.path.join(ROOT_DIR, "SKILLS.md")

def get_skill_info(skill_path):
    readme_path = os.path.join(skill_path, "SKILL.md")
    if not os.path.exists(readme_path):
        return None
    
    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Extract description from frontmatter
    match = re.search(r'description:\s*(.+)', content)
    description = match.group(1).strip() if match else "No description"
    
    return description

def generate_index():
    categories = {
        "Core": ["self-improvement", "verification", "stability-protocols", "sovereign-identity"],
        "Development": ["python", "react", "typescript", "clean-code"],
        "Tools": ["debug", "git", "test"],
        "Uncategorized": []
    }
    
    skills = []
    
    # scan directories
    for item in os.listdir(SKILLS_DIR):
        full_path = os.path.join(SKILLS_DIR, item)
        if os.path.isdir(full_path):
            desc = get_skill_info(full_path)
            if desc:
                skills.append({"name": item, "desc": desc})
    
    skills.sort(key=lambda x: x['name'])
    
    # Write Index
    with open(INDEX_FILE, 'w', encoding='utf-8') as f:
        f.write(f"# Skills Index ({len(skills)} Actionable Skills)\n\n")
        f.write("| Skill | Description |\n")
        f.write("|:---|:---|")
        
        for skill in skills:
            link = f"skills/{skill['name']}/"
            f.write(f"| [{skill['name']}]({link}) | {skill['desc']} |\n")
            
    print(f"✅ Generated index for {len(skills)} skills.")

if __name__ == "__main__":
    generate_index()
