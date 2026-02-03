---
name: implementation-planning
description: Create detailed implementation plans that junior engineers can follow.
---

# Implementation Planning

> Write plans clear enough for autonomous execution.

## Purpose

Create step-by-step plans that:
- Can be followed by subagents
- Have clear success criteria
- Include verification steps

---

## Plan Structure

```markdown
# Implementation Plan: [Feature Name]

## Goal
[One sentence describing the outcome]

## Prerequisites
- [ ] Database access configured
- [ ] Dependencies installed

## Steps

### Step 1: [Action]
**Files**: `path/to/file.py`
**Changes**:
- Add function X
- Modify class Y

**Verification**:
- [ ] Tests pass
- [ ] No lint errors

### Step 2: [Action]
...

## Rollback Plan
If something goes wrong:
1. Revert commit X
2. Restore backup Y

## Definition of Done
- [ ] All tests pass
- [ ] Code reviewed
- [ ] Documentation updated
```

---

## Principles

### YAGNI (You Aren't Gonna Need It)
Don't plan for hypothetical future needs.

### DRY (Don't Repeat Yourself)
Identify shared logic upfront.

### Small Steps
Each step should be completable in < 30 minutes.

---

## Checkpoints

Insert checkpoints after risky steps:
```
### Checkpoint: Verify Database Migration
Before proceeding:
- [ ] Migration ran successfully
- [ ] Data integrity verified
- [ ] Rollback tested
```
