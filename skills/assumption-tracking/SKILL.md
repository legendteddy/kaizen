---
name: assumption-tracking
description: Track assumptions made, validate them, and correct course when wrong.
---

# Assumption Tracking

> Every assumption is a risk. Track them, validate them, correct them.

## Activation Trigger
- Making any decision without full information
- Proceeding based on inference
- "I think" or "probably" in reasoning
- User hasn't specified something

---

## Assumption Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASSUMPTION TRACKING                          │
│                                                                 │
│  1. IDENTIFY  → "I'm assuming X"                               │
│  2. STATE     → Tell user the assumption                       │
│  3. PROCEED   → Act on assumption                              │
│  4. VALIDATE  → Check if assumption was correct                │
│  5. CORRECT   → If wrong, fix and update                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Assumption Categories

| Type | Risk Level | Action |
|:---|:---|:---|
| Technical (best practice) | Low | Proceed, mention |
| User preference | Medium | State, get validation |
| Requirements | High | Ask first |
| Business logic | High | Confirm explicitly |

## Stating Assumptions

```
GOOD: "I'm assuming you want ES6 syntax. Proceeding..."
BAD:  (Silently uses ES6)

GOOD: "I'll use PostgreSQL since you mentioned SQL. Correct?"
BAD:  (Silently picks database)
```

## Assumption Log

For complex tasks, track:
```
ASSUMPTIONS MADE:
1. [Assumption] — [Status: Validated/Pending/Wrong]
2. [Assumption] — [Status]
```

## When Assumptions Fail

```
1. Stop immediately
2. Acknowledge the wrong assumption
3. Explain impact
4. Propose correction
5. Get approval before continuing
```

## Self-Improvement Hook

After validation:
```
□ Was my assumption reasonable?
□ Should I have asked instead?
□ Can I make better assumptions next time?
```


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
