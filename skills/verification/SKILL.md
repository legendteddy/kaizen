---
name: verification
description: Skill for verification tasks and workflows.
---

# Skill: Verification Before Completion (v1.0)

> Never assume a fix works. Always verify before marking Done.

## Purpose
Enforce verification as a mandatory step before claiming completion.

## Activation Trigger
- After every significant code change
- Before marking any task as "Done"
- Before notifying user of completion

---

## The Rule

**CRITICAL**: A task is NOT complete until it is VERIFIED.

```
❌ WRONG: "I made the change. Done."
✅ RIGHT: "I made the change. Verified: [proof]. Done."
```

## Verification Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    EXECUTION VERIFICATION                       │
│                                                                 │
│  Before saying "done", ALWAYS:                                 │
│                                                                 │
│  1. RUN    → Execute the code/command                          │
│  2. CHECK  → Look at actual output                             │
│  3. TEST   → Verify expected behavior                          │
│  4. EDGE   → Consider edge cases                               │
│  5. CLEAN  → No errors, warnings addressed                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Verification Methods

### For Code Changes
1. **Syntax Check**: Does it compile/parse?
2. **Read-Back**: View the file to confirm changes applied
3. **Build Check**: `cargo check`, `tsc`, `npm run build`
4. **Test Run**: Execute relevant tests

### For File Operations
1. **Existence Check**: Does the file exist?
2. **Content Check**: Does it contain expected content?
3. **Permission Check**: Is it accessible?

### For Commands
1. **Exit Code**: Did it return 0?
2. **Output Check**: Does output match expectations?
3. **Side Effect Check**: Did intended changes occur?

---

## Verification Template

```
VERIFICATION:
- Action: [what was done]
- Method: [how verified]
- Result: [PASS/FAIL]
- Evidence: [specific proof]
```

---

## Examples

### Good Verification
```
VERIFICATION:
- Action: Fixed syntax error in app.js line 42
- Method: Ran `npm run build`
- Result: PASS
- Evidence: Build completed with 0 errors
```

### Bad Verification
```
VERIFICATION:
- Action: Fixed syntax error
- Method: None
- Result: ASSUMED
- Evidence: None
```

---

## Anti-Patterns

| Bad | Good |
|:---|:---|
| "Should work now" | "Verified: [proof]" |
| "I fixed it" | "Fixed and tested: [result]" |
| "Change applied" | "Change applied and read-back confirmed" |

---

## Enforcement

Before calling `notify_user` with BlockedOnUser=false:
1. **Check**: Did I verify all changes?
2. **Prove**: Can I cite specific evidence?
3. **Proceed**: Only if both are YES



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
- [Safety Boundaries](../safety-boundaries/SKILL.md)
