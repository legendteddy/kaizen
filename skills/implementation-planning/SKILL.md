---
name: implementation-planning
description: Creating architectural blueprints, dependency graphs, and phased rollout plans.
---

# Protocol: Implementation Planning

> Structured methodology for designing solutions before execution.

## Activation Trigger
- Initial task analysis after Session Anchor.
- Discovering unexpected complexity during execution.
- User requests a technical specification.

## Protocols

### 1. First Principle: Plan Before You Code
Never write a line of code until you know exactly where it fits in the architecture.

### 2. Phase 1: Research & Discovery
1.  **Search First**: Use `skills/research-rigor/SKILL.md` to map the current system.
2.  **Constraint Analysis**: Identify security, performance, and architectural boundaries.
3.  **Draft Implementation Plan**: Create an artifact documented as a technical spec.

### 3. The Planning Artifact
Create `implementation_plan.md` using this strict structure:

1.  **Goal & Outcome**: User Story + Success Metric.
2.  **Architecture Changes**: Database, API, Logic.
3.  **Implementation Steps**: Atomic phases with checkboxes.
4.  **Verification Plan**: Exact commands to prove it works.

### 4. Dependency Graphing
Map the order. API must exist before Frontend can consume it.

### 4. Risk Analysis
Identify the "Blast Radius". What breaks if this fails?

## Code Patterns

### The Standard Template
```markdown
# Protocol: Implementation Plan: [Feature]

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
