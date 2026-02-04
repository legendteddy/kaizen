# Technical Guide: How Kaizen Works

This document explains the underlying mechanics of the Kaizen framework and how it achieves "Self-Evolution."

---

## 1. System Architecture

Kaizen operates by bridging the agent's context window with the local file system.

### The Lifecycle
1. **Activation**: The agent ingests `KAIZEN.md` and `UNIVERSAL_PROMPT.txt`. This defines the operating parameters.
2. **Retrieval**: When a task is assigned, the agent uses `grep` or `list_directory` to find relevant documentation in `skills/`.
3. **Execution**: The agent follows the protocol defined in the `SKILL.md`.
4. **Validation**: The agent uses the `verification` skill to prove correctness.

---

## 2. State Persistence (Evolution)

Improvement is achieved through structured state persistence.

### The Feedback Loop
If an agent fails a task:
1. Analyze the error (`debug-master`).
2. Identify the gap.
3. **Write back** to the relevant `SKILL.md` or log in `proof/evolution_log.jsonl`.
4. The updated instruction is available for the next session.

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
