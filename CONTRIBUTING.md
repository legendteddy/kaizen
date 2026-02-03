# Contributing to Kaizen

Thank you for your interest in contributing to the Kaizen framework. We are building the future of Recursive Self-Improvement (RSI) for autonomous agents.

## Core Philosophy: The Kaizen Loop

All contributions must adhere to the core loop:
1.  **Observe:** Identify a gap or inefficiency.
2.  **Improve:** Implement a fix or new skill.
3.  **Codify:** Document the improvement in a `SKILL.md` or Pattern.
4.  **Verify:** Prove it works (Benchmarks/Tests).

## Development Standards

### 1. Epistemic Sovereignty
- Agents must be able to run locally (Ollama/Llama).
- No hard dependencies on closed-source APIs (OpenAI/Anthropic) unless optional.

### 2. Code Quality
We enforce strict standards using `ruff` and `mypy`.
```bash
# Run before committing
ruff check .
ruff format .
mypy .
```

### 3. Skill Architecture
New skills must follow the template in `skills/_template/SKILL.md`.
- **Purpose:** One sentence goal.
- **Trigger:** When should an agent use this?
- **Protocol:** Step-by-step instructions.

## Pull Request Process

1.  **Fork** the repo.
2.  **Create** a branch (`feat/new-skill-x`).
3.  **Verify** using the Repo Judge: `python -m kaizen_core.judge`.
4.  **Submit** PR.

## License
By contributing, you agree that your contributions will be licensed under its MIT License.