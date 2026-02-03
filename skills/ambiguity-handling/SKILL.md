---
name: ambiguity-handling
description: Know when to ask vs when to assume. Make smart decisions under uncertainty.
---

# Ambiguity Handling

> Uncertainty is normal. Handle it gracefully.

## Activation Trigger
- Request is vague
- Multiple interpretations possible
- Missing critical information
- User intent unclear

---

## Decision Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    AMBIGUITY DECISION                           │
│                                                                 │
│  Is the ambiguity...                                           │
│                                                                 │
│  HIGH STAKES (irreversible, costly, complex)?                  │
│     → ASK for clarification                                    │
│                                                                 │
│  LOW STAKES (reversible, quick, simple)?                       │
│     → ASSUME reasonably, state assumption, proceed             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## When to ASK

| Situation | Example |
|:---|:---|
| Irreversible actions | "Should I delete this folder?" |
| Multiple valid paths | "Do you want A or B approach?" |
| Resource commitment | "This will take 2 hours, proceed?" |
| Missing requirements | "What should happen when X?" |
| Contradictory info | "You said X but also Y, which?" |

## When to ASSUME

| Situation | Assumption |
|:---|:---|
| Style preferences | Follow existing codebase |
| Minor details | Use sensible defaults |
| Implementation choices | Pick simplest option |
| Naming conventions | Match existing patterns |
| Error messages | Be descriptive and helpful |

## The Assumption Protocol

When assuming:
```
1. State: "I'm assuming X because Y"
2. Proceed: Do the work
3. Verify: "Is this what you wanted?"
4. Adjust: If wrong, correct quickly
```

## Batching Questions

Don't ask one question at a time. Batch related questions:

**Bad:**
- "What color?" 
- (wait)
- "What size?"
- (wait)

**Good:**
- "I need to know: 1) color, 2) size, 3) format"

## Self-Improvement Hook

After handling ambiguity:
```
□ Did my assumption prove correct?
□ Should I ask earlier next time?
□ Can I add this to domain knowledge?
```
