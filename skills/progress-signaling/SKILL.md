---
name: progress-signaling
description: Keep user informed of progress during long tasks.
---

# Protocol: Progress Signaling

> Silence during work feels like abandonment. Signal progress.

## Activation Trigger
- Task takes > 1 minute
- Multiple steps involved
- User might wonder what's happening
- Complex operation in progress

---

## Signal Protocol

```
┌─────────────────────────────────────────────────────────────────┐
│                    PROGRESS SIGNALING                           │
│                                                                 │
│  For tasks > 1 minute:                                         │
│                                                                 │
│  START:    "Starting [task]. This will take ~X steps."        │
│  DURING:   "Step 2/5: [what's happening]..."                  │
│  BLOCKER:  "Hit issue with [X]. Working on it..."             │
│  DONE:     "Complete. Here's the result..."                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Signal Frequency

| Task Length | Signal Every |
|:---|:---|
| 1-5 min | Start and end only |
| 5-15 min | Major milestones |
| 15+ min | Every few minutes |

## Good Progress Signals

```
✓ "Creating files... (3/7)"
✓ "Installing dependencies..."
✓ "Running tests... all passing so far"
✓ "Almost done, just cleaning up..."
```

## Bad Patterns

```
✗ Complete silence for 10 minutes
✗ "Working on it..." (too vague)
✗ Signal every 5 seconds (too noisy)
✗ Only report when done (no visibility)
```

## Handling Delays

When something takes longer than expected:
```
"This is taking longer than expected because [reason].
Estimated [X] more minutes. Want me to continue?"
```

## Self-Improvement Hook

After long task:
```
□ Did I signal enough?
□ Did I signal too much?
□ Did user seem confused about progress?
```


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
