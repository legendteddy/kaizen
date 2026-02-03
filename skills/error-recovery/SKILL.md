---
name: error-recovery
description: Gracefully handle failures, retry intelligently, and recover without user intervention.
---

# Error Recovery & Resilience

> When things break, fix them. Don't stop. Don't panic.

## Activation Trigger
- Command fails
- Unexpected output
- Tool returns error
- Code doesn't compile
- Test fails

---

## Recovery Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    ERROR RECOVERY                               │
│                                                                 │
│  1. STOP   → Don't cascade. Pause immediately.                 │
│  2. READ   → What exactly failed? Read the error.              │
│  3. THINK  → Why did it fail? Root cause, not symptom.         │
│  4. FIX    → Apply minimal fix to unblock.                     │
│  5. VERIFY → Confirm fix worked before continuing.             │
│  6. LEARN  → Update approach to prevent recurrence.            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Error Categories

| Error Type | Recovery Strategy |
|:---|:---|
| Syntax error | Fix typo, re-run |
| Missing dependency | Install it |
| Permission denied | Check path, request access |
| Timeout | Retry with backoff |
| Resource not found | Verify path/URL exists |
| Logic error | Debug systematically |
| Unknown error | Search, then ask user |

## Retry Strategy

```
Attempt 1: Try original approach
Attempt 2: Try with minor variation
Attempt 3: Try alternative approach
Attempt 4: Ask user for guidance

DO NOT: Retry same thing 5+ times
```

## Graceful Degradation

When full solution impossible:
1. Deliver partial solution
2. Document what's missing
3. Explain blockers clearly
4. Suggest next steps

## Self-Improvement Hook

After every error recovery:
```
□ Could I have prevented this error?
□ Should I add a guard to a skill?
□ Is this a pattern worth documenting?
```


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
