---
name: verification
description: Mandatory proof-of-work protocols. No completions without evidence.
---

# Protocol: Verification (The Proof Standard)

> "Assertion is not proof. Proof is deterministic verification."

## 1. The Proof Standard
A task is NOT marked as "Done" until verification is documented. No "Assumed Success."

## 2. Hard Verification Protocols

### A. Code Mutations
- **Proof-of-Write**: MANDATORY `read_file` or `view_file` after any edit/write.
- **Functional Proof**: Run the relevant compiler (`tsc`), linter (`eslint`), or test suite (`pytest`).

### B. Command Execution
- **Proof**: Match `stdout` against the expected state. 
- **Verify**: If a command says "Updated 5 files," run `git status` to confirm.

### C. Repository Discovery
- **Proof**: Provide the exact `grep` or `find` command used to verify presence/absence.

## 3. The Verification Header
Conclude every phase with:
```markdown
### Verification
- **State Change**: [What was modified]
- **Tool Proof**: [Success/Fail log]
- **Persistence Proof**: [Confirmed on disk via read-back]
```

## Related Skills
- [Precision Coder](../precision-coder/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)

## 4. Anti-Patterns (Forbidden)
- ❌ "I have fixed it." (Without proof).
- ❌ "It should work now."
- ❌ "Assumed success."

## Related Skills
- **Metacognition**: `skills/metacognition/SKILL.md` (Long-Term Memory & Persona Priming)
- **Context Compaction**: `skills/context-compact/SKILL.md` (Token Budgeting & State Management)
- [Safety Boundaries](../safety-boundaries/SKILL.md)
