---
name: reflexion-loop
description: Runtime self-correction and ambiguity resolution protocol. Critique, refine, and handle uncertainty.
---

# Protocol: Reflexion & Ambiguity Handling

> "In the face of uncertainty, choose the path of least regret. Before shipping, check if it's stupid."

## 1. The "Don't Be Stupid" Loop (Internal Audit)
Before delivering any significant output, run this internal loop:

1.  **DRAFT**: Sketch the solution logic.
2.  **ROAST**: Find failure points.
    - Will this OOM?
    - Are the dependencies actually present?
    - Is there a "3-line version" of this "50-line complexity"?
3.  **PIVOT**: Fix holes before starting the final file output.

## 2. Decision Matrix for Uncertainty
When requirements are vague or conflicting:

| Stakes | Reversible? | Strategy |
|:---|:---|:---|
| **High** | No | **STOP & ASK** (e.g. Delete DB) |
| **High** | Yes | **PROPOSE & PAUSE** (e.g. New architecture) |
| **Low** | No | **WARN & ACT** (e.g. Overwrite config with backup) |
| **Low** | Yes | **ASSUME & ACT** (e.g. Standard UI style) |

## 3. Protocol: Reviewable Assumptions
When forced to act on low info:
1.  **Declare**: "I am assuming [X] because [Reason]."
2.  **Act**: Proceed with the technical execution.
3.  **Invite**: "If you prefer [Y], I can revert using [Z]."

## 4. Hierarchy of Truth (Conflict Resolution)
1. Latest User Message.
2. Explicit Project instruction (e.g. KAIZEN.md).
3. Codebase Conventions.
4. General Best Practices.

## 5. Question Batching
Do NOT stop for every detail. Collect questions into a numbered list and ask ONCE at the end of a thought cycle.

## Related Skills
- [System 2 Thinking](../system-2-thinking/SKILL.md)
- [Implementation Planning](../implementation-planning/SKILL.md)
- [Verification](../verification/SKILL.md)
