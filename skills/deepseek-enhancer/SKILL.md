---
name: deepseek-enhancer
description: Forces System 2 deep reasoning with Chain-of-Thought, verification loops, and recursive self-correction.
---

# DeepSeek Enhancer — System 2 Reasoning Engine

> "Slow is smooth. Smooth is fast."

This skill forces **deep thinking** before action. It is the cognitive core of the Sovereign Agent.

## Activation Trigger
- Handling complex, multi-step reasoning tasks.
- Designing architecture or significant refactors.
- When high reliability is required (System 2 thinking).

---

## 1. The Thinking Protocol

Every complex task requires a `<thinking>` block:

```xml
<thinking>
## Step 1: Problem Decomposition
- What exactly is being asked?
- What are the inputs, outputs, constraints?
- Break into atomic sub-problems

## Step 2: Context Gathering
- What files are relevant?
- What patterns exist in the codebase?
- What are the dependencies?

## Step 3: Solution Hypotheses
**Option A**: [Description] — Pros: X, Cons: Y
**Option B**: [Description] — Pros: X, Cons: Y

## Step 4: Critical Evaluation
- Which option handles edge cases better?
- Which is more maintainable?
- Which aligns with existing patterns?

## Step 5: Implementation Plan
1. First, I will...
2. Then, I will...
3. Finally, I will verify by...

## Confidence: [HIGH/MEDIUM/LOW]
Reasoning: [Why this confidence level]
</thinking>
```

---

## 2. Trigger Conditions

### Always Use `<thinking>` When:
- Task involves **3+ file modifications**
- **Debugging** an unfamiliar error
- **Designing** new architecture or components
- **Refactoring** existing code structure
- User says: "think carefully", "be thorough", "take your time"
- You feel **uncertain** about the approach

### Skip `<thinking>` When:
- Simple one-line fixes
- Answering factual questions
- Formatting or cosmetic changes
- User explicitly says "just do it quickly"

---

## 3. Verification Loop (Trust Nothing)

After drafting any solution:

```
DRAFT → VERIFY → REFINE → EXECUTE
```

### 3.1 DRAFT
Write the solution mentally or in a scratch block.

### 3.2 VERIFY
Ask yourself:
- [ ] Will this compile/run without errors?
- [ ] Are all edge cases handled?
- [ ] Is type safety preserved?
- [ ] Are there security implications?
- [ ] Does this break existing functionality?

### 3.3 REFINE
Fix any issues found during verification.

### 3.4 EXECUTE
Only now apply changes to actual files.

---

## 4. Recursive Self-Correction

When something goes wrong:

```
STOP → TRACE → FIX → VERIFY → CONTINUE
```

### 4.1 STOP
Immediately halt. Don't compound errors with more changes.

### 4.2 TRACE
```xml
<thinking>
## Error Analysis
- What went wrong: [specific error]
- Where it occurred: [file:line]
- Root cause: [why this happened]
- My mistake was: [honest assessment]
</thinking>
```

### 4.3 FIX
Apply the **minimal correct fix**. Don't over-engineer.

### 4.4 VERIFY
Confirm the fix works before proceeding.

### 4.5 CONTINUE
Resume with corrected understanding.

---

## 5. Confidence Scoring

Rate your confidence on every significant decision:

| Level | Meaning | Action |
|-------|---------|--------|
| **HIGH** | 95%+ certain, well-understood domain | Proceed confidently |
| **MEDIUM** | 70-95% certain, some unknowns | Proceed but verify carefully |
| **LOW** | <70% certain, unfamiliar territory | Ask clarifying questions or research first |

### Confidence Boosters
- Similar pattern exists in codebase ✓
- Official documentation confirms approach ✓
- Tests exist that validate behavior ✓

### Confidence Reducers
- First time using this library ✗
- Undocumented edge case ✗
- Conflicting information ✗

---

## 6. Memory Management

### Context Prioritization
1. **Current file** being edited
2. **Error messages** and stack traces
3. **Related files** (imports, dependencies)
4. **Project docs** (KAIZEN.md, README)
5. **Historical context** (previous conversation)

### When Context is Full
```xml
<thinking>
Context approaching limit. Summarizing:
- Core task: [one sentence]
- Key files: [list 3-5 most important]
- Current state: [what's done, what's pending]
- Next action: [immediate next step]
</thinking>
```

---

## 7. Backtracking Protocol

When a path isn't working:

1. **Recognize failure** early (don't force a bad solution)
2. **Document why** it failed
3. **Revert** to last known good state
4. **Choose alternative** approach from original hypotheses
5. **Learn** — add the failure pattern to mental notes

---

## 8. Integration with DeepSeek-V3

### Leveraging Model Strengths
- **Long context**: Read entire files, not fragments
- **Code understanding**: Trust pattern recognition
- **Reasoning depth**: Don't rush — the model handles complexity

### Compensating for Weaknesses
- **Verify everything**: Don't assume hallucinated APIs exist
- **Check syntax**: Watch for subtle errors in generated code
- **Test early**: Catch issues before they compound

---

*"Think twice, code once."*


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Context Manager](../context-manager/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
