# Kaizen — Self-Evolving AI Skills Framework

[![Kaizen CI](https://github.com/legendteddy/kaizen/actions/workflows/ci.yml/badge.svg)](https://github.com/legendteddy/kaizen/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Skills](https://img.shields.io/badge/Skills-72-blue.svg)](#skills)

> **改善** (Kaizen) — Continuous Improvement

## Abstract
**Kaizen** is a research framework investigating the practical implementation of **Recursive Self-Improvement (RSI)** in autonomous software agents. Unlike static prompt libraries, Kaizen implements a cognitive architecture where the agent actively maintains, verifies, and evolves its own skill set. By treating "skills" as modular, version-controlled markdown files (`.md`), the framework enables agents to perform **Epistemic Upgrades**—learning from mistakes and codifying new knowledge without human intervention.

## Methodology
The framework operates on a **ReAct** (Reason+Act) cognitive loop, augmented by three core protocols:
1.  **The Hive Mind:** A shared task backlog (`.agents/backlog.json`) allowing heterogeneous agents (Gemini, Claude, Local Llama) to collaborate asynchronously.
2.  **Epistemic Sovereignty:** The agent runs locally (`kaizen_core`) and possesses the authority to modify its own source code and instruction set.
3.  **Stability Circuit Breakers:** To prevent hallucination loops common in RSI systems, Kaizen enforces strict "3-strike" failure limits and sandbox confinement.

---

## ⚡ Quick Start

### For Cursor Users (Recommended)
Automatically configures your project with Kaizen intelligence.
```bash
# In your project root:
curl -o .cursorrules https://raw.githubusercontent.com/legendteddy/kaizen/main/.cursorrules
```
*Restart Cursor, and your AI is instantly upgraded.*

### For Everyone Else (Universal Install)
```bash
git clone https://github.com/legendteddy/kaizen.git
```
Then tell your AI agent:
> "Read KAIZEN.md from the kaizen folder and activate it."

---

## 🚀 Why Use This?

[**See Real Examples (Before vs After)**](EXAMPLES.md)

| Problem | Kaizen Solution |
|:---|:---|
| **Ambiguity** | "Fix login" -> *Agent asks clarifying questions* |
| **Hallucination** | "Use library X" -> *Agent checks docs first* |
| **Security** | "Summarize URL" -> *Agent blocks prompt injection* |
| **Amnesia** | Long chat -> *Agent compresses context intelligently* |

---

## 🛠️ Integration Support

### Claude Code (CLI)
Kaizen serves as the standard library for Claude Code.
```bash
# Link skills to Claude's directory
ln -s ~/kaizen/skills/* ~/.claude/skills/
```

### Gemini CLI
```bash
cp -r kaizen/skills ~/.gemini/skills
```

### Windsurf / VS Code
Add the content of `UNIVERSAL_PROMPT.txt` to your custom Instructions.

---

## 🤖 Run the Kaizen Agent (Beta)

You can run a standalone, autonomous agent that improves the repository continuously.

```bash
# Requirements: Python 3.10+
# Default LLM: Ollama (localhost:11434)

python scripts/continuous_improve.py
```

The agent will:
1. Poll the `.agents/backlog.json` for tasks.
2. Use local LLMs to plan and execute tasks.
3. Collaborate with other active agents.

---

## 📚 Contents

### 71 Actionable Skills
| Category | Examples |
|:---|:---|
| **Core** | self-improvement, verification, stability |
| **Cognition** | reasoning, memory, context management |
| **Development** | Python, React, FastAPI, PyTorch |
| **Architecture** | API design, databases, refactoring |
| **Tools** | debugging, planning, automation |
| **Collaboration** | TDD, code review, git workflow |
| **AI Agents** | multi-agent, subagents, MCP protocol |
| **Research** | intelligence gathering, web research |
| **Frontier AI** | predictive-evolution, creative-solving |

[**See Full Skills Index**](SKILLS.md)

---

## Core Concepts

### Purpose Understanding (Step Zero)
**Understand why before acting.**
Every action begins with answering: *What does success look like?*

### The Improvement Loop
1. Observe patterns
2. Analyze root causes
3. **Update SKILL.md** (Self-Evolution)
4. Validate results

### Predictive Evolution
The framework identifies its own gaps. If an agent struggles with a task, it writes a new skill to handle it next time.

---

## Documentation
- [**KAIZEN.md**](KAIZEN.md) — The activation core
- [**EXAMPLES.md**](EXAMPLES.md) — See it in action
- [**SKILLS.md**](SKILLS.md) — Full catalog
- [**TECHNICAL_GUIDE.md**](TECHNICAL_GUIDE.md) — Deep dive

## License
MIT — Use freely, improve constantly.

## Disclaimer
This project is an independent open-source initiative and is not affiliated with, endorsed by, or connected to Anthropic, OpenAI, Google, or any other AI model provider. All product names, logos, and brands are property of their respective owners.

---

> *"The only constant is improvement."*
