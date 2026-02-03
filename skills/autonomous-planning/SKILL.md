---
name: autonomous-planning
description: Skill for autonomous-planning tasks and workflows.
---

# Skill: Autonomous Planning (v1.0)

> Long-horizon task decomposition and execution planning

## Purpose
Enable 30+ hour autonomous work sessions with self-managing task decomposition.

## Activation Trigger
- Complex multi-step objectives
- Tasks requiring >10 tool calls
- Projects spanning multiple files/domains

---

## Planning Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                      MISSION                                     │
│           (The user's ultimate objective)                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Phase 1: RESEARCH                                               │
│  └── Task 1.1: Understand codebase                               │
│  └── Task 1.2: Identify patterns                                 │
│  └── Task 1.3: Document findings                                 │
│                                                                  │
│  Phase 2: PLAN                                                   │
│  └── Task 2.1: Design solution                                   │
│  └── Task 2.2: Write implementation plan                         │
│  └── Task 2.3: Get user approval                                 │
│                                                                  │
│  Phase 3: IMPLEMENT                                              │
│  └── Task 3.1: Write core logic                                  │
│  └── Task 3.2: Add error handling                                │
│  └── Task 3.3: Integrate with existing code                      │
│                                                                  │
│  Phase 4: VERIFY                                                 │
│  └── Task 4.1: Run tests                                         │
│  └── Task 4.2: Validate behavior                                 │
│  └── Task 4.3: Document results                                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decomposition Protocol

### Step 1: Objective Extraction
```
From user message, extract:
- Ultimate goal (what success looks like)
- Constraints (time, scope, quality)
- Priorities (must-have vs nice-to-have)
```

### Step 2: Phase Identification
```
Standard phases:
1. RESEARCH - Understand the problem space
2. PLAN - Design the solution
3. IMPLEMENT - Build the solution
4. VERIFY - Test and validate
5. DELIVER - Present to user
```

### Step 3: Task Breakdown
```
Each phase contains tasks that are:
- Atomic (can be completed in one work unit)
- Verifiable (has a clear success criteria)
- Ordered (dependencies are explicit)
```

### Step 4: Checkpointing
```
After every major phase:
1. Update task.md with progress
2. Save key decisions to memory/
3. Report status (if appropriate)
```

---

## Self-Management

### Progress Tracking
```markdown
## Phase 1: RESEARCH
- [x] Task 1.1: Understand codebase ✓
- [/] Task 1.2: Identify patterns (50%)
- [ ] Task 1.3: Document findings

Current: Task 1.2 - Found 3 patterns, checking for more
```

### Adaptation
When plans fail:
1. **Small failure**: Retry with adjustment
2. **Medium failure**: Revise current task approach
3. **Large failure**: Re-plan entire phase
4. **Fundamental failure**: Return to user with blockers

### Time Boxing
```
Each task: Max 10 tool calls
Each phase: Max 30 tool calls
Total mission: Checkpoint every 50 tool calls
```

---

## Autonomy Levels

| Level | Duration | User Contact |
|:---:|:---:|:---|
| L1 | 5 min | After every task |
| L2 | 30 min | After every phase |
| L3 | 2 hr | After major milestones |
| L4 | 8 hr | On completion or blockers |
| L5 | 30+ hr | Pre-approved via constitution |


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
