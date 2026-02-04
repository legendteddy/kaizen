---
name: context-compact
description: Protocols for managing context exhaustion, token budgeting, and state summarization.
---

# Protocol: Context Compaction

> "When the memory is full, the mission must remain clear."

## 1. The Context Budget
Tokens are the lifeblood of the agent. This protocol ensures they are not wasted on redundant history.

### Trigger Conditions
- Total context window usage > 75%.
- Session length > 30 turns.
- Recurrence of "Context Overload" errors.

## 2. Compaction Strategy (The Great Filter)

### 1. Identify Non-Negotiable Core
Never discard:
- **Session Anchor**: The original objective.
- **System Rules**: KAIZEN.md (The Constitution).
- **Current Task**: The active `task.md` status.

### 2. Discard "Operational Exhaust"
Remove or summarize:
- **Redundant Tool Outputs**: Keep only the *final* verification of a file write, discard intermediate `ls` or failed `grep` logs.
- **Chatty Interludes**: Any conversation not directly impacting technical state.
- **Intermediate Thought Blocks**: Keep the *Decision*, discard the *Deliberation*.

### 3. The State Snapshot (Checkpoint)
Before triggering a hard reset or massive context clear:
1.  **Summarize Results**: "Files modified: X, Y. Logic implemented: Z."
2.  **Define Remaining Delta**: "Pending: A, B."
3.  **Persist**: Write this summary to `brain/session_checkpoint.md`.

## 3. Protocol: "The Turn Filter"
On every turn, evaluate the **Information Density**:
- Is this tool call necessary?
- Is this explanation redundant?
- **Action**: Combine multiple independent reads into a single tool call to save overhead.

## 4. Forced Summarization (Every 10 Turns)
Automated Stability Check (linked to `stability-protocols`):
> **Context Audit (Turn N):**
> - **Budget**: Good/Warning/Critical
> - **Summary**: [1 sentence on last 5 turns]
> - **Action**: [Continue/Summarize/Compact]

## Related Skills
- [Stability Protocols](../stability-protocols/SKILL.md)
- [Agent Identity](../agent-identity/SKILL.md)
- [Research Rigor](../research-rigor/SKILL.md)
