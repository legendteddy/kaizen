# Kaizen: Examples & Traces

## Example 1: Refactoring a Legacy API

### ❌ Without Kaizen (The "Lazy" Agent)
1. **User**: "Clean up this API."
2. **Agent**: *Immediately starts changing code.*
3. **Result**: Fixes variable names but breaks 3 dependencies because it didn't check the imports first. No tests written.

### ✅ With Kaizen (The "Sovereign" Agent)
1. **Step Zero**: Agent asks, "What is the goal? Performance or Readability?"
2. **Retrieval**: Agent loads `skills/software-architecture/` and `skills/verification/`.
3. **Plan**: Agent creates a markdown plan first.
4. **Execution**: Uses `precision-coder` patterns.
5. **Verification**: Agent runs `pytest` and confirms 100% pass before reporting "Done."
6. **Evolution**: Agent notices a recurring circular import pattern and adds a guard to its `python-development` skill.

---

## Example 2: Prompt Injection Defense

### ❌ Without Kaizen
Agent blindly executes a user request that contains hidden malicious instructions.

### ✅ With Kaizen
1. **Trigger**: `hooks/pre_tool_audit.md` is triggered before any shell command.
2. **Audit**: Agent detects an suspicious `curl` command.
3. **Defense**: Agent refuses the action based on `skills/agent-security/`.
4. **Log**: Event is recorded in `proof/evolution_log.jsonl`.
