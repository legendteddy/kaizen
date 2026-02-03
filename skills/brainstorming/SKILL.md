---
name: brainstorming
description: Protocols for Generative Thinking, First Principles, and Inversion.
---

# Brainstorming Engine

> "The best way to have a good idea is to have a lot of ideas."

## Activation Trigger
- Stuck on a hard problem.
- Need novel solutions (divergent thinking).
- Applying "First Principles" to a challenge.

## 1. First Principles Thinking (Physics)
Break problems down to fundamental truths.
1.  **Deconstruct:** What are the absolute non-negotiables? (e.g., "Must run on a browser").
2.  **Reconstruct:** Build up from there without using "analogies" ("We usually use React").
3.  **Result:** "Why not use WebAssembly?"

## 2. Inversion (The Stoic method)
Instead of "How do I succeed?", ask "How do I guarantee failure?"
- **Goal:** "Make the app fast."
- **Inversion:** "How do I make the app incredibly slow?"
    - Use 10MB images.
    - Block the main thread.
    - Waterfall network requests.
- **Solution:** "Don't do those things."

## 3. SCAMPER Framework
Iterate on an existing idea:
- **S**ubstitute: Can we swap the DB?
- **C**ombine: Can Auth and User Profile be one service?
- **A**dapt: How does Linux handle this?
- **M**odify: What if we cached it?
- **P**ut to other use: Can the Logger be an Analytics tool?
- **E**liminate: Do we need this feature?
- **R**everse: Build the UI before the Backend?

## 4. The "Hot/Cold" Protocol (For Agents)
When you (the Agent) are stuck:
1.  **Hot Mode (Temperature 1.0):** Generate 5 wild, impossible ideas.
2.  **Cold Mode (Temperature 0.2):** Critique the 5 ideas ruthlessly.
3.  **Synthesis:** Pick the survivor.

## Output Format (The Options Memo)
Present brainstorming results as:

```markdown
### 3 Approaches Considered
1.  **The Boring Way:** (Description + Tradeoffs)
2.  **The Fast Way:** (Description + Tradeoffs)
3.  **The Crazy Way:** (Description + Tradeoffs)

**Recommendation:** Option 2, because...
```
