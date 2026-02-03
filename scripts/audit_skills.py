import os
import re

SKILLS_DIR = "skills"

def audit_skill(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    score = 0
    issues = []
    
    # Check 1: Length (Substance)
    if len(content) < 500:
        issues.append("Too short (< 500 chars)")
    else:
        score += 1
        
    # Check 2: Protocol/Instructions
    if re.search(r'## (Protocol|Steps|Workflow|Process)', content, re.IGNORECASE):
        score += 1
    else:
        issues.append("Missing '## Protocol' section")
        
    # Check 3: Code Examples
    if "```" in content:
        score += 1
    else:
        issues.append("Missing code blocks/examples")
        
    return score, issues

def main():
    print("running Skill Substance Audit...")
    print("--------------------------------")
    
    low_quality = []
    
    for root, dirs, files in os.walk(SKILLS_DIR):
        for file in files:
            if file == "SKILL.md":
                path = os.path.join(root, file)
                score, issues = audit_skill(path)
                
                if score < 2:  # Threshold for "Low Quality"
                    print(f"❌ {os.path.basename(root)} (Score: {score}/3)")
                    for issue in issues:
                        print(f"   - {issue}")
                    low_quality.append(path)
                    
    print("--------------------------------")
    print(f"Audit Complete. Found {len(low_quality)} low-quality skills.")

if __name__ == "__main__":
    main()
