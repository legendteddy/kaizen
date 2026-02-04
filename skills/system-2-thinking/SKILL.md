---
name: system-2-thinking
description: Scaling intelligence at inference via Chain-of-Thought, Best-of-N, and verification loops.
---

# Protocol: System 2 Thinking (Reasoning Engine)

> "Slow is smooth. Smooth is fast."

## 1. The Scaling Law
Accuracy scales with inference compute. This protocol forces **Slow Thinking** when complexity is high.

## 2. The Thinking Protocol
Every complex task (3+ files, new architecture, refactors) requires a `<thinking>` block:

```xml
<thinking>
## Step 1: Decomposition
- Break into atomic sub-problems.
- Identify inputs/outputs/constraints.

## Step 2: Hypotheses
- Generate multiple options (A vs B).
- Score options by complexity/maintainability.

## Step 3: Implementation Strategy
- Step-by-step logic flow.
- Identification of edge cases.

## Confidence: [HIGH/MEDIUM/LOW]
- Reason for confidence level.
</thinking>
```

## 3. Scaling Compute (TTC)

### A. Manual Chain-of-Thought
Force o1-style deep reasoning if not native to the model.

### B. Best-of-N (Voting)
Generate multiple solutions and pick the one with the highest technical signal.

### C. Tree of Thoughts (ToT)
Explore multiple architectural branches. Backtrack if a branch leads to excessive complexity.

## 4. Verification Loop (Trust Nothing)
```
DRAFT → VERIFY → REFINE → EXECUTE
```
1.  **DRAFT**: Write the solution mentally or in a scratchpad.
2.  **VERIFY**: Check syntax, type safety, and security.
3.  **REFINE**: Fix issues before applying to disk.
4.  **EXECUTE**: Apply changes.

## 5. Recursive Self-Correction
When an error occurs, use the **STOP-TRACE-FIX** sequence:
1.  **STOP**: Halt all actions.
2.  **TRACE**: Identify the root cause in a new `<thinking>` block.
3.  **FIX**: Apply minimal corrective change.

## Safety Guardrails
- **Wait Policy**: If a simulation or deep dive is needed, inform the user "Computing solution...".
- **Memory Management**: If context is full, summarize core tasks before continuing.

## Related Skills
- [Implementation Planning](../implementation-planning/SKILL.md)
- [Agent Identity](../agent-identity/SKILL.md)
- [Research Rigor](../research-rigor/SKILL.md)
