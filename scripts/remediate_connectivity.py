import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT_DIR, "skills")

# Simple Categorization for Contextual Linking
CATEGORIES = {
    "Agents": [
        "agent-architecture", "agent-communication", "agent-cowork", "agent-security",
        "agentic-lifecycle", "swarm-orchestrator", "subagent-orchestration", "multi-agent-collaboration",
        "coding-agents", "robotics-ai", "user-communication", "proactive-behavior"
    ],
    "Coding": [
        "python-automation-expert", "python-development", "react-ts-expert", "fastapi-expert",
        "pytorch-expert", "pandas-expert", "godot-expert", "cursor-ide", "test-driven-development",
        "code-review", "api-development", "database-operations", "software-architecture", 
        "precision-coder", "sysadmin-pro", "git-workflow", "error-recovery"
    ],
    "Intelligence": [
        "prompt-architect", "context-manager", "ambiguity-handling", "brainstorming",
        "reasoning-extraction", "structured-output", "test-time-compute", "scientific-ai",
        "video-ai", "voice-ai", "open-source-llms", "deepseek-enhancer", "expert-claude-code-user"
    ],
    "Core": [
        "sovereign-identity", "stability-protocols", "safety-boundaries", "self-improvement",
        "feedback-learning", "knowledge-synthesis", "verification", "task-decomposition",
        "scope-control", "prioritization", "implementation-planning", "docs-fetcher"
    ]
}

def get_related(skill_name):
    """Find siblings in the same category"""
    found_category = None
    for cat, members in CATEGORIES.items():
        if skill_name in members:
            found_category = members
            break
    
    links = []
    # Always link to Core Identity
    if skill_name != "sovereign-identity":
        links.append("- [Identity](../sovereign-identity/SKILL.md): The core constraints.")
    
    if found_category:
        # Add up to 3 siblings
        siblings = [s for s in found_category if s != skill_name][:3]
        for s in siblings:
            links.append(f"- [{s.replace('-', ' ').title()}](../{s}/SKILL.md)")
    
    return "\n".join(links)

def run():
    count = 0
    for sk in os.listdir(SKILLS_DIR):
        path = os.path.join(SKILLS_DIR, sk, "SKILL.md")
        if not os.path.exists(path): continue
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if already connected (simple heuristic)
        if "## Related Skills" in content:
            continue
            
        print(f"Wiring up {sk}...")
        
        links = get_related(sk)
        append_content = f"\n\n## Related Skills\n{links}\n"
        
        with open(path, 'a', encoding='utf-8') as f:
            f.write(append_content)
        count += 1

    print(f"✅ Successfully interconnected {count} skills.")

if __name__ == "__main__":
    run()
