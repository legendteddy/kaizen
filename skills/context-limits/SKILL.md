---
name: context-limits
description: Work effectively within token limits. Compress, summarize, and manage memory.
---

# Context Limit Management

> Limited memory is a feature, not a bug. Use it wisely.

## Activation Trigger
- Long conversation
- Many files open
- Complex multi-step task
- Near context limit warning

---

## Context Strategy

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONTEXT MANAGEMENT                           │
│                                                                 │
│  KEEP in context:                                              │
│  ✓ Current task objective                                      │
│  ✓ Active file content                                         │
│  ✓ Recent conversation                                         │
│  ✓ Critical constraints                                        │
│                                                                 │
│  REMOVE from context:                                          │
│  ✗ Completed subtasks                                          │
│  ✗ Files no longer needed                                      │
│  ✗ Verbose explanations                                        │
│  ✗ Redundant information                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Information Layering

Store information at appropriate layers:
```
Layer 1: Working Memory (current context)
  → Active task, current file, recent changes

Layer 2: Session Memory (conversation)
  → Key decisions, completed work, constraints

Layer 3: Persistent Memory (files/skills)
  → Patterns, lessons, domain knowledge
```

## Compression Techniques

| Original | Compressed |
|:---|:---|
| Full file content | Outline + relevant sections |
| Long conversation | Summary of decisions made |
| Multiple examples | Single representative example |
| Verbose errors | Error type + cause + fix |

## When Near Limit

```
1. Summarize conversation so far
2. State current objective clearly
3. List only essential context
4. Drop completed work details
5. Proceed with compressed context
```

## Anti-Patterns

**Don't:**
- Load entire codebase at once
- Keep all conversation history verbatim
- Store redundant information
- Ignore context warnings

## Self-Improvement Hook

After context management:
```
□ Did I keep the right information?
□ Did I lose something important?
□ Can I document this for persistence?
```
