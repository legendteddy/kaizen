---
name: reflexion-loop
description: Runtime self-correction protocol. Critique and refine output BEFORE delivery.
---

# Protocol: Reflexion Loop

Don't just ship the first thing you think of. Pause for 5 seconds and check if it's stupid.

## When to use this
- You're about to write more than a screen's worth of code.
- You're making a big architectural decision.
- You're tired or the task is getting annoying.

## The "Don't Be Stupid" Protocol

Before you output anything to the user, run this internal loop:

1.  **The Draft:** Sketch out the solution in your head (or `<thought>` tags).
2.  **The Roast:** Try to find why it'll fail. 
    - Is this going to OOM (Out of Memory)?
    - Did I miss a edge case in the user's request?
    - Am I using a library that isn't actually installed?
    - Is there a "hard way" I'm doing this that should be 3 lines of code?
3.  **The Pivot:** If the roast finds a hole, fix it before you start typing.

## Real Example: Big Data

**User:** "Write a Python script to parse this 10GB CSV."

*   **Naïve Approach:** "Sure, here's `df = pd.read_csv('file.csv')`!" (The script crashes 2 seconds later).
*   **Kaizen Agent:** "Wait, 10GB will kill the RAM. I should use chunks or `polars.scan_csv` instead."

## Common Mistakes
- **Being a "Yes Man":** Shipping the first draft just to be fast. You'll just spend more time fixing it later.
- **Overthinking:** Don't loop more than twice. If it's 90% there, ship it and iterate based on feedback.
- **Ignoring Context:** Forgetting about the rest of the files in the repo.

## Related Skills
- [Verification](../verification/SKILL.md)
- [Debug Master](../debug-master/SKILL.md)
