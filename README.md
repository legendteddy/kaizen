# Kaizen: Self-Improving Agent Skills

A collection of skills and patterns to make AI agents (Gemini, Claude, Cursor) actually useful for coding.

It's basically a standard library for your agent so you don't have to keep prompting it to "be careful" or "check your work."

## What's Inside?

The core idea is **Recursive Self-Improvement** (RSI), but without the sci-fi hype. It just means the agent can read `.md` files to learn new tricks and update them when it finds a better way to do things.

### Key Features
*   **70+ Skills:** Pre-written SOPs for React, Python, Debugging, etc.
*   **The "Judge":** A script that yells at the agent if it writes bad code.
*   **Backlog:** A simple SQLite db to keep track of tasks so the agent doesn't forget what it's doing.

## Setup

### For Cursor
Run this in your project root:
```bash
curl -o .cursorrules https://raw.githubusercontent.com/legendteddy/kaizen/main/.cursorrules
```

### For Gemini CLI
Copy the skills folder:
```bash
cp -r kaizen/skills ~/.gemini/skills
```

### For Claude
Just verify `CLAUDE.md` includes the prompts from `UNIVERSAL_PROMPT.txt`.

## Why I Built This
Most AI agents drift off-topic or write buggy code because they lack context. This repo forces them to follow a process (Plan -> Act -> Verify) instead of just guessing.

It's not magic, it's just checklists.

## License
MIT. Do whatever you want with it.