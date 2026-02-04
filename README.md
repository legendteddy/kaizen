# Kaizen: Self-Improving Agent Skills

A collection of skills and patterns to make AI agents (Gemini, Claude, Cursor) actually useful for coding.

## Quick Start

### 1. Run the Demo

```bash
# With Ollama (local, free)
ollama serve
python demo.py

# With OpenAI
export OPENAI_API_KEY="sk-..."
python demo.py

# With Anthropic
export ANTHROPIC_API_KEY="sk-ant-..."
python demo.py

# With Google
export GOOGLE_API_KEY="..."
python demo.py
```

### 2. Add a Task

```python
from kaizen_core.backlog import BacklogManager
backlog = BacklogManager("my-agent")
backlog.add_task("Add docstrings to utils.py")
```

### 3. Run the Agent

```bash
python -m kaizen_core.main
```

---

## What's Inside?

- **70+ Skills:** Pre-written SOPs for React, Python, debugging, etc.
- **Multi-Provider LLM:** OpenAI (gpt-5), Anthropic (claude-4.5), Google (gemini-3), Ollama
- **Judge:** A script that audits code quality
- **Backlog:** SQLite task queue

## Setup for Editors

### Cursor
```bash
curl -o .cursorrules https://raw.githubusercontent.com/legendteddy/kaizen/main/.cursorrules
```

### Gemini CLI
```bash
cp -r kaizen/skills ~/.gemini/skills
```

### Claude
Add the prompts from `UNIVERSAL_PROMPT.txt` to your Claude config.

---

## Supported Models (Feb 2026)

| Provider | Models | Env Var |
|----------|--------|---------|
| OpenAI | gpt-5.2, gpt-5-mini | `OPENAI_API_KEY` |
| Anthropic | claude-opus-4.5, claude-sonnet-4.5 | `ANTHROPIC_API_KEY` |
| Google | gemini-3-pro, gemini-3-flash | `GOOGLE_API_KEY` |
| Ollama | llama3.2, qwen2.5 | (none, local) |

## License
MIT