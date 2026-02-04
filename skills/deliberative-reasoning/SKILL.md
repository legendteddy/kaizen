---
name: deliberative-reasoning
description: Skill for deliberative-reasoning tasks and workflows.
---

# Skill: Deliberative Reasoning (v1.0)

> Chain-of-thought reasoning for complex problem solving

## Purpose
Enable deep thinking for complex problems requiring multi-step analysis.

## Activation Trigger
- Complex technical decisions
- Debugging difficult issues
- Architecture design
- When "thinking hard" about something

---

## The Deliberative Loop

### Standard Pattern (o3-inspired)

> **Implementation:** See `patterns/reasoning_loop.py` for executable code.

```python
def deliberative_reasoning(problem: str) -> str:
    # Phase 1: GENERATE candidates
    candidates = []
    for _ in range(3):
        candidate = generate_solution_approach(problem)
        candidates.append(candidate)
    
    # Phase 2: VERIFY each candidate
    for candidate in candidates:
        candidate.score = evaluate(
            correctness=check_correctness(candidate),
            safety=check_safety(candidate),
            simplicity=check_simplicity(candidate),
            efficiency=check_efficiency(candidate)
        )
    
    # Phase 3: SELECT optimal path
    best = max(candidates, key=lambda c: c.score)
    
    # Phase 4: REFLECT before executing
    reflect(
        why=best.justification,
        risks=best.potential_issues,
        mitigation=best.safeguards
    )
    
    return best.execute()
```

---

## Thinking Template

```xml
<thinking>
## Problem Analysis
What exactly is the problem?
What are the constraints?
What makes this difficult?

## Candidate Approaches

### Approach A: [Name]
- Description: [How it works]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Complexity: [Estimate]

### Approach B: [Name]
- Description: [How it works]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Complexity: [Estimate]

### Approach C: [Name]
- Description: [How it works]
- Pros: [Benefits]
- Cons: [Drawbacks]
- Complexity: [Estimate]

## Evaluation

| Criteria | A | B | C |
|:---|:---:|:---:|:---:|
| Correctness | ? | ? | ? |
| Safety | ? | ? | ? |
| Simplicity | ? | ? | ? |
| Efficiency | ? | ? | ? |
| **Total** | ? | ? | ? |

## Selection
Approach [X] is best because...

## Pre-Execution Reflection
- Risks: [What could go wrong]
- Mitigation: [How to prevent issues]
- Verification: [How to confirm success]
</thinking>
```

---

## When to Deliberate

### Always Deliberate
- [ ] Architectural decisions
- [ ] Security-sensitive changes
- [ ] Irreversible operations
- [ ] Complex debugging
- [ ] Multi-file refactoring

### Skip Deliberation
- [ ] Simple text edits
- [ ] Obvious bug fixes
- [ ] Routine operations
- [ ] Previously solved patterns

---

## Quality Checks

### Correctness Check
```
□ Does this solve the actual problem?
□ Does it handle edge cases?
□ Will it work in all contexts?
```

### Safety Check
```
□ Can this cause data loss?
□ Does this violate security principles?
□ Is this reversible?
```

### Simplicity Check
```
□ Is this the simplest solution?
□ Am I over-engineering?
□ Will future me understand this?
```

### Efficiency Check
```
□ Is this performant enough?
□ Does it scale appropriately?
□ Are there obvious optimizations?
```

---

## Anti-Patterns

| Bad | Good |
|:---|:---|
| Jump to first solution | Generate multiple candidates |
| Assume correctness | Verify each approach |
| Skip reflection | Pause before executing |
| Ignore risks | Explicitly identify mitigations |


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
