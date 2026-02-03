---
name: context-manager
description: Protocols for Context Hygiene, Session Anchors, and Memory Persistence.
---

# Context Manager

> "A clear mind is a fast mind."

## Activation Trigger
- Context window > 80% full.
- Starting a new complex session.
- Need to persist memory across sessions.

## 1. Context Hygiene Protocol (The 80% Rule)
When context usage hits 80%, **STOP and COMPRESS**.

### Compression Algorithm
```python
def compress_context(history):
    summary = summarize(history)
    snapshot = get_file_status()
    new_context = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"PREVIOUS_SESSION_SUMMARY:\n{summary}\n\nFILE_STATE:\n{snapshot}"}
    ]
    return new_context
```

## 2. Session Anchor (Start of Task)
Never start "blind".

**Before first action:**
1.  **Read `KAIZEN.md`**: Principles.
2.  **Read `README.md`**: Project state.
3.  **Read `TODO.md` / `task.md`**: Current objective.

*If you skip this, you will hallucinate requirements.*

## 3. Memory Persistence
Agents forget. Files do not.

| Memory Type | Storage Location | Update Frequency |
|:---|:---|:---|
| **Episodic** (This Session) | `memory/session_log.md` | End of Session |
| **Semantic** (Facts/Rules) | `memory/knowledge_graph.md` | On Discovery |
| **Procedural** (How-To) | `skills/` | On Improvement |

## 4. Reading Strategy (O(1) vs O(n))

### ❌ The "Scroll" (Bad)
Reading `src/` recursively.
*Cost:* 10,000 tokens. *Value:* Low.

### ✅ The "Sniper" (Good)
1.  `ls -R` (Cost: 100 tokens) -> Locate target.
2.  `grep "function_name"` (Cost: 50 tokens) -> Locate line.
3.  `read_file(lines=100-150)` (Cost: 200 tokens) -> Get context.

**Total Cost:** 350 tokens. **Savings:** 96.5%.

## 5. Artifacts as Memory
Treat specific files as "External Working Memory".
- `implementation_plan.md`: The shared brain between User and Agent.
- `scratchpad.md`: Place to dump massive logs/JSONs for analysis without polluting the main context.

## Self-Improvement
- **Did I re-read the same file 3 times?** -> You are forgetting. Copy critical snippets to `scratchpad.md`.
- **Did I parse a 1MB log file?** -> Don't. Grep it first.


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
- [Brainstorming](../brainstorming/SKILL.md)
