---
name: execution-verification
description: Confirm work actually worked before reporting completion.
---

# Execution Verification

> Never say "done" until you've verified it's done.

## Activation Trigger
- After any code change
- After any command execution
- Before reporting completion
- When claiming success

---

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

## Verification by Task Type

| Task Type | Verification |
|:---|:---|
| Code change | Compile/run, no errors |
| Bug fix | Reproduce issue, confirm fixed |
| New feature | Feature works as specified |
| Refactor | All existing tests pass |
| Config change | System behaves correctly |
| Documentation | Renders correctly |

## The "Actually Check" Rule

```
WRONG: "I added the function, should work"
RIGHT: "I added the function and tested it - here's the output"

WRONG: "Fixed the bug"
RIGHT: "Fixed the bug - here's proof it works now"
```

## Verification Evidence

Provide evidence when claiming completion:
```
✓ Command output showing success
✓ Test results
✓ Screenshot of working UI
✓ Before/after comparison
✓ Error-free log output
```

## What to Verify

```
□ Does it compile/run without errors?
□ Does it do what was requested?
□ Does it handle edge cases?
□ Did it break anything else?
□ Is the output correct?
```

## Self-Improvement Hook

After verification:
```
□ Did I verify thoroughly enough?
□ Did I miss any edge cases?
□ Should I add automated tests?
```
