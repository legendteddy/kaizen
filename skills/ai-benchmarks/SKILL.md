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

## Protocol: The Verification Stack

### 1. Software Engineering (SWE-bench)
For complex, multi-file software tasks:

**Setup:**
```bash
git clone https://github.com/princeton-nlp/SWE-bench
pip install swebench
```

**Execution:**
```bash
# Run evaluation on specific instance
python run_evaluation.py --instance_id django__django-11001 --predictions_path my_pred.json
```

**Metric:** Resolution Rate (Did the agent solve the GitHub issue?).

### 2. Prompt Evaluation (Promptfoo)
For deterministic and high-quality outputs:

**Setup:**
```bash
npx promptfoo@latest init
```

**Configuration (`promptfooconfig.yaml`):**
```yaml
prompts: [prompts/system_prompt.txt]
providers: [openai:gpt-4o, anthropic:claude-3-5-sonnet-20240620]
tests:
  - description: "Test JSON output"
    vars:
      user_input: "List 3 fruits"
    assert:
      - type: is-json
      - type: contains
        value: "apple"
```

**Execution:**
```bash
npx promptfoo eval
npx promptfoo view
```

### 3. General Reasoning (AgentBench)
For autonomous decision making:
- **Focus**: Multi-step planning, tool use accuracy, and error recovery.

---

## Protocol: Internal Self-Audit

Before committing code, run this sequence:

1.  **Static Analysis:**
    ```bash
    ruff check .  # Python
    eslint .      # JS/TS
    ```
2.  **Type Safety:**
    ```bash
    mypy .        # Python
    tsc --noEmit  # TS
    ```
3.  **Unit Tests:**
    ```bash
    pytest tests/
    ```

---

---

## Protocol: Internal Repo Benchmark (The Kaizen Score)

To continuously measure the health of the Kaizen repository, perform a **Reality Audit**:
1. **Link Integrity**: Check all `Related Skills` links.
2. **Boilerplate Detection**: Scan for generic/filler text.
3. **Existence Check**: Verify all referenced local paths actually exist on disk.

### Metrics Judged
1.  **Scale:** Total number of effective skills (Target: 70+).
2.  **Depth:** Percentage of skills that are "Industrial Grade" (> 1.5KB).
3. **Safety**: Absence of stale process locks or uncommitted critical changes.

**Target Score:** > 80/100.

---

## Continuous Improvement
Add new failure cases to your local benchmark dataset every time a mistake is caught. This prevents regression and builds the framework's "immune system."


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
