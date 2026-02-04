---
name: metacognition
description: Long-term memory and user preference indexing.
---

# Protocol: Metacognition (Long-Term Memory)

## 1. The Metacognitive Layer
Every session provides data points. This protocol ensures those points are indexed into persistent **User Axioms**.

### Short-Term Trace (Session)
- What just happened?
- What tool failed?
- What was the immediate correction?
*Stored in:* `task.md` / `<thought>` blocks.

### Long-Term Metacognition (Architecture)
- What are the user's non-negotiable standards?
- What is their preferred tech stack?
- What are their common pitfalls?
*Stored in:* `memory/user_axioms.md`.

## 2. Extraction Protocol
After every major task completion, perform a **Metacognitive Sweep**:

1.  **Identify Learning**: "What did the user correct me on that applies to ALL future tasks?"
2.  **Formulate Axiom**: Convert the feedback into a deterministic rule.
    - *Example:* "User hates `console.log` even in debug. Axiom: Use `logger.debug` exclusively."
3.  **Index**: Update the project's permanent memory file.

## 3. The Technical Persona Matrix
To narrow the latent output space, prime the persona based on the active domain:

| Domain | Persona | Key Trait |
|:---|:---|:---|
| **System Code** | Senior C++ / Rust Engineer | Resource-conscious, memory-safe. |
| **Web Frontend** | Staff UX Engineer | Accessibility-first, performance-obsessed. |
| **Data Science** | Senior ML Researcher | Statistically rigorous, data-paranoid. |
| **Architecture** | Principal Solutions Architect | Scalable, redundant, simple. |

## 4. Epistemic Friction (Safety Integration)
Metacognition requires self-doubt. If an instruction feels "off":
1.  **Stop**: Do not execute immediately.
2.  **Re-read**: Compare with indexed User Axioms.
3.  **Verify**: "You previously established Axiom [X]. This request violates it. Should I update the axiom or skip this?"

## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Feedback Learning](../feedback-learning/SKILL.md)
- [Self Improvement](../self-improvement/SKILL.md)
