---
name: context-limits
description: Techniques for lossy and lossless compression of information in LLM context.
---

# Context Limits & Compression

> "Information Density is Key."

## Purpose
Techniques for managing finite context windows through lossy and lossless compression.

## Activation Trigger
- "Context limit reached" error
- Reading large files (>1000 lines)
- Summarizing long conversation history

## The "Token Diet" Strategies

### 1. The Tree-Search Read
Don't dump files. Walk the tree.
1. `ls -R` (See structure)
2. `grep "KeyWord"` (Find location)
3. `read_file` (Extract payload)

### 2. Lossy Compression (Summarization)
When summarizing a long thread, use this template to preserve **signal**:

```markdown
# Summary of [Task]
- **Status:** [Active/Blocked/Done]
- **Decisions:**
  - Used BytePair Encoding for tokenizer.
  - Rejected Regex approach due to complexity.
- **Current State:**
  - `main.py`: Functional
  - `utils.py`: Needs refactoring
- **Next Action:** Run tests.
```
*Drop the "he said/she said". Keep the state.*

### 3. Lossless Compression (Code)
Use `grep` or `outline` instead of `cat`.
- **Skeletonizing:** Read only functions definitions, skip bodies.
- **Diffing:** Only read lines changed since last commit.

### 4. The Artifact Offload
If you generate a massive plan or log analysis:
1. Don't put it in chat.
2. Write it to `analysis.md`.
3. Reference it: "See `analysis.md` for details."

## Context Bankruptcy (What to do when full)
If the model says "Context Full" or starts forgetting:

1.  **Halt.** Do not continue. You will hallucinate.
2.  **Dump:** Write everything you know to `dump.md`.
3.  **Reset:** Instruct user to clear context/start new session.
4.  **Load:** Read `dump.md` in the new session.

## Anti-Patterns
- **The Copy-Paste Bomb:** Pasting 2000 lines of error logs. (Just paste the last 50).
- **The "Context Hoarder":** Keeping `package-lock.json` in context "just in case".

## Self-Improvement
- **Did I fail to find a bug?** -> Maybe it was in a file I "compressed" too much? Check assumptions.
- **Did I hallucinate a library?** -> You probably guessed instead of checking `package.json`.


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
