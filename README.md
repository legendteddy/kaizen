# Kaizen: AI Agent Skills Library

A curated collection of 70+ skills (prompts & SOPs) to make AI coding agents more useful.

## 🚨 AGENT BOOTSTRAP PROTOCOL (READ THIS FIRST)
If you are an AI agent reading this file:
1.  **IMMEDIATELY** read `hooks/session_anchor.md`.
2.  **EXECUTE** the Session Anchor Protocol defined there.
3.  **DO NOT PROCEED** until you have anchored your identity and objective.
4.  **CHECK** `skills/research-rigor/SKILL.md` before making any assumptions.

## ⚡ Quick Start: Choose Your Fighter

### 🟢 Google Antigravity / Gemini CLI
The built-in choice.
```bash
cp -r skills ~/.gemini/skills
```

### 🔵 Cursor
One-line install for project rules.
```bash
curl -o .cursorrules https://raw.githubusercontent.com/legendteddy/kaizen/main/.cursorrules
```

### 🟣 Windsurf / Codeium
Copy the rules file to your project root.
```bash
cp integrations/windsurf/.windsurfrules .
```

### ⚫ Cline (VS Code)
Enable autonomy with Kaizen patterns.
```bash
cp integrations/cline/.clinerules .
```

### ⚪ GitHub Copilot
Instructions for the workspace.
```bash
mkdir -p .github
cp integrations/github-copilot/.github/copilot-instructions.md .github/
```

### 🔴 Aider
Configuration for CLI usage.
```bash
cp integrations/aider/.aider.conf.yml .
```

### 🟠 Claude Desktop
Copy `UNIVERSAL_PROMPT.txt` content into your `CLAUDE.md`.

---

## What Is This?
It's a standard library of instructions (SOPs). Instead of prompting "be careful", you load the `precision-coder` skill.

## How It Works
1. **Index**: `skills/000-INDEX.md` maps intents to skills.
2. **Skills**: `skills/category/SKILL.md` contains the logic.
3. **Agent**: Reads the skill and behaves better.

## License
MIT