---
name: test-time-compute
description: Scaling intelligence at inference via Chain-of-Thought, Best-of-N, and Tree Search.
---

# Test-Time Compute (TTC)

> "Don't just answer. Think."

## Activation Trigger
- Solving logic puzzles or math problems.
- Generating complex architectural plans.
- When standard inference yields low quality.

## 1. The Scaling Law
Accuracy scales with inference compute.
- **System 1 (Fast):** "Paris is the capital of France." (0.1s)
- **System 2 (Slow):** "Paris's GDP relative to London's post-Brexit." (30s)

## 2. Protocols for "Slow Thinking"

### A. Manual Chain-of-Thought (The "<thinking>" Tag)
If the model doesn't support o1/DeepSeek-R1 natively, force it:

```markdown
<thinking>
1.  **Understand Goal:** User wants a regex for emails.
2.  **Edge Cases:** logical.part@sub.domain.co.uk? +tag?
3.  **Draft 1:** ^[\w]+@[\w]+\.[\w]+$ (Too simple).
4.  **Critique:** Fails on dots in name.
5.  **Refinement:** Use standard RFC 5322 permissive pattern.
</thinking>
Final Answer: [Regex]
```

### B. Best-of-N (Voting)
Generate 5 solutions. Pick the best.
```python
solutions = [llm.generate(prompt) for _ in range(5)]
evaluator_prompt = f"Rank these 5 solutions by robustness: {solutions}"
best = llm.generate(evaluator_prompt)
```

### C. Tree of Thoughts (ToT)
Explore branches. Backtrack if dead end.
1.  **Branch:** Generate 3 possible architectural approaches.
2.  **Evaluate:** Score each approach (1-10).
3.  **Expand:** Take the top score and detail it further.

## 3. When to Use TTC?

| Task | Compute Strategy |
|:---|:---|
| Chat / Greeting | **Zero-Shot** (System 1) |
| SQL Generation | **Few-Shot + CoT** (System 1.5) |
| Architecture Design | **Tree of Thoughts** (System 2) |
| Math / Physics | **DeepSeek-R1 / o1-preview** (Native System 2) |

## 4. The "Wait" Token
If an agent realizes it needs more time:
- **Bad:** Hallucinate a quick answer.
- **Good:** "I need to run a simulation to answer this. Standby..." (Then runs a loop).
