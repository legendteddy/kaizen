# Kaizen

> **改善** (Kaizen) — Continuous Improvement

This is the core logic file. If your agent reads this, it loads the framework.

---

## How it Works

Most agents are "stateless" — they forget everything between sessions. Kaizen gives them a way to persist knowledge.

1.  **Skills:** Markdown files in `skills/` act as plugins.
2.  **Memory:** The agent checks previous work before starting new tasks.
3.  **Reflection:** Before running a command, the agent has to ask "Is this stupid?" (See `reflexion-loop` skill).

## The Rules

### 1. Understand the Goal
Don't just write code. Ask *why* we are doing this. If the requirements are vague, complain until they are clear.

### 2. Check Your Work
Never say "Done" without running the code. If you can't run it, at least lint it.

### 3. Don't Be Annoying
*   No "As an AI language model..."
*   No "I hope this helps!"
*   Just the code and a brief explanation.

## Directory Structure

*   `skills/`: The actual capabilities (React, Python, etc.)
*   `kaizen_core/`: The Python script that runs the agent loop.
*   `.agents/`: Local database for task tracking.

## Getting Started

1.  Clone this repo.
2.  Tell your agent: "Read KAIZEN.md and activate."
3.  That's it.

## Troubleshooting

**Agent is hallucinating?**
- Remind it to read `skills/verification/SKILL.md`.

**Agent is lazy?**
- Tell it to switch to `[MODE: BUILD]`.

**Agent broke something?**
- Check the `backups/` folder (if you enabled it).

---

*"Slow is smooth, smooth is fast."*
