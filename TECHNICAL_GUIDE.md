# Technical Guide: How Kaizen Works

This document explains the underlying mechanics of the Kaizen framework and how it achieves "Self-Evolution."

---

## 1. The Neuro-Symbolic Link

Kaizen operates on the principle that an AI Agent's **System Prompt** (Neural) is limited by its context window, while its **Tools** (Symbolic) can access an infinite library of knowledge on the file system.

### The Lifecycle
1. **Activation**: The agent ingest `KAIZEN.md` and `UNIVERSAL_PROMPT.txt`. This aligns its "Cognitive Weights" toward Purpose Understanding.
2. **Retrieval**: When a task is assigned, the agent uses `grep` or `list_directory` to find a relevant skill in `skills/`.
3. **Execution**: The agent follows the **Step-by-Step Protocol** inside the `SKILL.md`, overriding its default (often lazy) behaviors.
4. **Validation**: The agent uses the `verification` skill to prove the work is correct.

---

## 2. Mechanics of Self-Evolution

Evolution is not "magical learning." it is **Structured State Persistence**.

### The Feedback Loop
If an agent fails a task:
1. It analyzes the error using the `debug-master` skill.
2. It identifies a "missing guard" or "new pattern."
3. It **writes back** to the relevant `SKILL.md` or logs the insight in `proof/evolution_log.jsonl`.
4. In the next session, the agent reads the updated skill, preventing the repeat error.

---

## 3. Integration Architecture

| Component | Role | Logic |
|:---|:---|:---|
| `KAIZEN.md` | The Constitution | High-level rules & ethics |
| `skills/` | The Cortex | Domain-specific procedures |
| `hooks/` | The Autonomic System | Triggers for safety and quality |
| `proof/` | The Long-term Memory | Evidence of improvement and logs |

---

## 4. Verification Stack

We recommend and use:
- **SWE-bench**: For software engineering accuracy.
- **Promptfoo**: For prompt regression testing.
- **Unit Tests**: Standard `unittest` or `pytest` for the framework scripts.
