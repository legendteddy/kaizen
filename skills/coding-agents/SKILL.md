---
name: coding-agents
description: Skill for building and managing autonomous software engineering agents (Devin-like).
---

# Skill: Coding Agents (v1.0)

> "Automating the artisan."

## Purpose
Best practices for building agents that write, run, and fix code autonomously.

## Activation Trigger
- Building "Devin" clones or coding assistants.
- Tasks involving file system manipulation and test running.

---

## Protocol: Safety & Sandboxing

**CRITICAL:** Coding agents must NEVER run on the host machine without isolation.

1.  **Docker Sandbox:**
    *   Mount workspace as volume.
    *   Network: Restricted (allow pip/npm, block generic internet if possible).
    *   Timeout: Kill processes > 30s.

2.  **File Guards:**
    *   Block edits to `.git/`, `.env`, and system files.
    *   Always read file content *before* editing (to avoid overwriting logic).

---

## Protocol: The "Edit-Run-Fix" Loop

Coding agents fail when they "blindly edit." Enforce this loop:

### Step 1: SEARCH
- Don't assume file locations.
- `ls -R` or `find` to map the structure.
- `grep` to find the relevant code definition.

### Step 2: EDIT
- Use line-based editing or search/replace (not full file overwrite).
- **Rule:** Every edit must be idempotent if possible.

### Step 3: VERIFY (The Missing Link)
- **Action:** The agent MUST run a command to verify the edit.
    - *Syntax Check:* `python -m py_compile file.py`
    - *Linter:* `ruff check file.py`
    - *Test:* `pytest test_file.py`

### Step 4: RECOVER
- If verification fails, read the stderr.
- **Do not apologize.** Plan the fix.
- Retry (Max 3 times).

---

## Tool Definition Example (JSON)

```json
{
  "name": "edit_file",
  "description": "Replace a specific string in a file.",
  "parameters": {
    "path": "src/main.py",
    "old_string": "def foo():",
    "new_string": "def bar():"
  }
}
```

## Action Checklist
- [ ] **Sandboxed:** Is this running in Docker/Container?
- [ ] **Timeout:** Is there a strict execution timeout (e.g. 30s)?
- [ ] **Read-First:** Did the agent read the file before editing?
- [ ] **Verified:** Did the agent run a test/linter after editing?
- [ ] **Idempotent:** Is the edit safe to run twice?


## Related Skills
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Agent Communication](../agent-communication/SKILL.md)
- [Agent Cowork](../agent-cowork/SKILL.md)
