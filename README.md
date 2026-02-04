# Kaizen: AI Agent Skills Library

A curated collection of 70+ skills (prompts & SOPs) to make AI coding agents more useful.

## AGENT BOOTSTRAP PROTOCOL (MANDATORY)

1. **Identity Anchor**: Read `skills/agent-identity/SKILL.md` immediately.
2. **Objective Extraction**: Extract the session goal and state it in silent thought.
3. **Research First**: Before acting, verify current repository state via `skills/research-rigor/SKILL.md`.
4. **Context Check**: Confirm all relevant files are loaded or indexed.

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
Kaizen is a standard library of technical protocols written by engineers for AI agents. It replaces vague prompts with structured Standard Operating Procedures (SOPs) to ensure high-reliability execution and minimal cognitive drift.

### How It Works

1. **Skill Discovery**: Consult [000-INDEX.md](file:///c:/Users/thoma/Documents/kaizen/skills/000-INDEX.md).
2. **Modular Execution**: Read the relevant `skills/{domain}/SKILL.md` before starting work.
3. **Lifecycle Management**: Use [hooks/](file:///c:/Users/thoma/Documents/kaizen/hooks/) to maintain state across sessions.
4. **Identity Enforcement**: Agents must follow the [Agent Identity](file:///c:/Users/thoma/Documents/kaizen/skills/agent-identity/SKILL.md) protocol.

## License
MIT