---
name: meta-optimizer
description: Self-Taught Optimizer (STO) protocol. Systematically improve the agent's own cognitive source code.
---

# Meta-Optimizer (STO)

> "The machine that builds the machine."

## Activation Trigger
- When `predictive-evolution` identifies a structural flaw in Kaizen.
- When you discover a more efficient prompt structure.
- When you need to upgrade the `kaizen_core` engine itself.

## Core Principle
We treat our **Prompt System** and **Skills** as a codebase. We apply software engineering principles to our own mind.

## The Optimization Loop

1.  **Profile:** Identify the bottleneck.
    *   *Example:* "I spend too many tokens explaining what I'm doing."
2.  **Hypothesize:** Create a "Patch" for the instruction set.
    *   *Example:* "If I edit `GEMINI.md` to require 'Concise Mode', token usage will drop 20%."
3.  **Implement:** Edit the `.md` or `.py` file.
    *   *Tools:* `read_file`, `replace`, `write_file`.
4.  **Benchmark:** Test the new prompt/skill on a standard task.
    *   *Check:* Did quality stay high? Did tokens drop?

## Optimization Targets

| Target | Description | Action |
|:---|:---|:---|
| **Skills** | Specialized logic (`skills/*.md`) | Refine protocols, remove fluff, add code snippets. |
| **Core** | Identity (`GEMINI.md`) | Sharpen mandates, update tech stack whitelists. |
| **Engine** | Python runner (`kaizen_core/*.py`) | Improve the tool execution logic or memory retrieval. |

## Safety Guardrails (The "Lobotomy" Prevention)

When editing your own source code:
1.  **Backup First:** Always ensure `git` can revert changes.
2.  **Incremental:** Change one variable at a time.
3.  **Verify Integrity:** After writing `SKILL.md`, read it back to ensure it's valid Markdown.

## Related Skills
- [Predictive Evolution](../predictive-evolution/SKILL.md): Pattern detection for upgrades.
- [Software Architecture](../software-architecture/SKILL.md): Structural optimization.
- [Self-Improvement](../self-improvement/SKILL.md): The core Kaizen mechanism.
- [Research Rigor](../research-rigor/SKILL.md): Input verification before optimization.
