# Kaizen: AI Agent Skills Library

A curated collection of 70+ skills (prompts & SOPs) to make AI coding agents more useful.

## What Is This?

It's a standard library of instructions for AI agents. Copy the skills into your agent's context and it will follow proven patterns instead of guessing.

**Works with:** Cursor, Claude Desktop, Gemini CLI, Windsurf, Aider, etc.

## Quick Start

### Cursor
```bash
curl -o .cursorrules https://raw.githubusercontent.com/legendteddy/kaizen/main/.cursorrules
```

### Gemini CLI
```bash
cp -r skills ~/.gemini/skills
```

### Claude Desktop
Copy the contents of `UNIVERSAL_PROMPT.txt` into your project's `CLAUDE.md`.

## What's Inside

```
skills/
├── react-patterns/       # Component patterns, hooks
├── python-automation/    # Scripts, file ops
├── debugging/            # Root cause analysis
├── code-review/          # PR review checklists
├── testing/              # TDD, coverage
└── ... (70+ total)
```

Each skill is a markdown file with:
- Context about when to use it
- Step-by-step instructions
- Common pitfalls to avoid

## License
MIT
