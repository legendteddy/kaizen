---
name: ai-benchmarks
description: Standards and tools for verifying AI agent performance and code quality.
---

# Skill: AI Benchmarking & Verification (v1.0)

> "If you can't measure it, you can't improve it."

## Purpose
Provide a rigorous framework for verifying agent performance, prompt effectiveness, and software engineering quality using industry-standard benchmarks.

## Activation Trigger
- User asks to "verify," "benchmark," or "test performance."
- Before a major release or public publication.
- When evaluating the impact of a new skill or prompt.

---

## 1. The Verification Stack (2026 Standards)

### Software Engineering (SWE-bench)
For complex, multi-file software tasks:
- **Protocol**: Reproduce the issue -> Implement fix -> Verify with tests.
- **Metric**: Resolution Rate (Did the agent solve the GitHub issue?).

### Prompt Evaluation (Promptfoo)
For deterministic and high-quality outputs:
- **Assertions**: String matching, JSON schema validation, LLM-as-a-judge rubrics.
- **Testing**: Run 50+ test cases to check for regressions in prompt behavior.

### General Reasoning (AgentBench)
For autonomous decision making:
- **Focus**: Multi-step planning, tool use accuracy, and error recovery.

---

## 2. Internal Kaizen Benchmark

Use this checklist for immediate self-verification:

| Category | Check | Pass/Fail |
|:---|:---|:---:|
| **Correctness** | Does the code solve the specific problem? | |
| **Security** | Are there secrets, injections, or vulnerabilities? | |
| **Efficiency** | Is the token usage optimized? | |
| **Coherence** | Does the change follow project conventions? | |
| **Stability** | Are all imports/exports valid and existing? | |

---

## 3. Implementation Workflow

### Step 1: Baseline
- Record the current performance/output before making changes.
- Use `promptfoo` to capture a snapshot of the current prompt behavior.

### Step 2: Experiment
- Apply the new skill, pattern, or prompt change.
- Run the task in a sandbox environment.

### Step 3: Evaluation
- Compare results against the baseline.
- **LLM-as-Judge**: Ask a separate model instance to critique the output based on a specific rubric.

### Step 4: Verification Commit
- Only commit the change if it passes >90% of the verification criteria.

---

## 4. Tools & Commands

| Tool | Purpose | Command (Example) |
|:---|:---|:---|
| `promptfoo` | Prompt testing | `npx promptfoo eval` |
| `pytest` | Logic verification | `pytest tests/` |
| `ruff` | Linting & Standards | `ruff check .` |
| `tsc` | Type checking | `npx tsc --noEmit` |

---

## 5. Continuous Improvement
Add new failure cases to your local benchmark dataset every time a mistake is caught. This prevents regression and builds the framework's "immune system."