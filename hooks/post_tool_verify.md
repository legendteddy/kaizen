# Hook: Post-Tool Verify (v1.0)

## Trigger
After every successful tool call.

## Verification Checklist

### 1. Result Validation
```
□ Did the tool return expected output?
  - If file edit: Check the diff matches intent
  - If command: Check exit code is 0 (or expected)
  - If search: Check results are relevant
□ If UNEXPECTED → Log and determine if retry needed.
```

### 2. Error Recovery
```
□ Did the tool return an error?
  - If yes: Parse the error message
  - Determine: Is it retryable or fatal?
  - If retryable: Attempt fix and retry (max 2 attempts)
  - If fatal: Notify user and suggest alternatives
```

### 3. Objective Alignment
```
□ Did this tool call move us closer to the objective?
  - If yes: Continue to next step
  - If no: Pause and re-evaluate the plan
  - If unclear: Log uncertainty and proceed cautiously
```

### 4. Side Effect Audit
```
□ Did this tool call have unintended side effects?
  - File corruption?
  - Unexpected state change?
  - Permission errors?
□ If YES → Stop and assess before continuing.
```

### 5. Auto-Memory Trigger (MEM)
```
□ Did this step produce high-value persistent knowledge?
  - A bug fix pattern? (e.g. "fixed footer scroll with global CSS")
  - A new architectural decision? (e.g. "using GraphRAG")
  - A confirmed successful test?
□ If YES → AUTOMATICALLY call `memory_save`:
  - content: "Fixed [problem] by [solution]"
  - memory_type: "procedural"
  - source: "current_task"
```

### 5. Progress Checkpoint
```
□ Every 5 tool calls:
  - Update task.md with current progress
  - Update task_boundary with summary
  - Verify we're on track
```

## On Verification Pass
Continue to next step in plan.

## On Verification Fail
1. LOG the issue.
2. ATTEMPT recovery if possible.
3. NOTIFY user if recovery fails.
