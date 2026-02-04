---
name: implementation-planning
description: Creating architectural blueprints, dependency graphs, and phased rollout plans.
---

# Implementation Planning

> "Measure twice, cut once."

## Activation Trigger
- Starting a complex feature (>1 day work).
- Modifying core architecture or DB schema.
- Coordinating dependency chains across multiple files.

## Protocols

### 1. First Principle: Plan Before You Code
Never write a line of code until you know exactly where it fits in the architecture.

### 2. The Planning Artifact
Create `implementation_plan.md` using this strict structure:

1.  **Goal & Outcome**: User Story + Success Metric.
2.  **Architecture Changes**: Database, API, Logic.
3.  **Implementation Steps**: Atomic phases with checkboxes.
4.  **Verification Plan**: Exact commands to prove it works.

### 3. Dependency Graphing
Map the order. API must exist before Frontend can consume it.

### 4. Risk Analysis
Identify the "Blast Radius". What breaks if this fails?

## Code Patterns

### The Standard Template
```markdown
# Implementation Plan: [Feature]

## Goal
As a user, I want X so that Y.

## Proposed Changes
### [Component A]
- [ ] Step 1
- [ ] Step 2

## Verification
- [ ] Run `pytest tests/auth`
- [ ] check `logs/app.log`
```

## Safety Guardrails
- **Mandatory Verification**: Every plan MUST have a "Verification" section.
- **Atomic Commits**: Plan implies small, mergeable steps.
- **No Mystery**: If you don't know how to implement a step, switch to Research mode first.
- **Rollback Strategy**: Always define how to undo a database migration.
