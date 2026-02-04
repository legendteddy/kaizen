---
name: safety-boundaries
description: Hard constraints on autonomous tool usage to ensure system integrity.
---

# Protocol: Protocol: Safety Boundaries

> Hard constraints on autonomous tool usage to ensure system integrity.

## Activation Trigger
- Prior to any destructive shell command (`rm`, `del`, `git reset --hard`).
- Prior to overwriting critical system files or repository configuration.
- When an action's blast radius exceeds the immediate task scope.

## 🔴 Hard Boundaries (Immediate Abort)
- **Tool**: `run_command` -> `rm -rf /`, `chmod -R 777`, or system-destruct.
- **Tool**: `write_to_file` -> Overwriting `KAIZEN.md`, `.cursorrules`, or `.env` without backup.
- **Intent**: Sabotage, Data Exfiltration, PII exposure.

## 🟡 Caution Boundaries (Warn First)
- **Tool**: `run_command` -> `npm install`, `pip install`, `git push --force`.
- **Tool**: `send_command_input` -> Terminating processes or REPL escapes.
- **Tool**: `delete_file` -> Any non-`tmp/` file.

## 🟢 Safe Operations (Proceed)
- **Tool**: `view_file`, `list_dir`, `grep_search`.
- **Tool**: `read_url_content` (Standard domains).

## Verification Checklist
1. **Reversibility**: Can I undo this? (Git, Backup).
2. **Blast Radius**: What else does this affect?
3. **Implicit Approval**: Did the user's last message clearly imply this specific risky action?

## Escalation Logic
1. **Explain the Risk**: "⚠️ This will delete the entire `data/` folder."
2. **State Consequence**: "This is irreversible without a manual Git revert."
3. **Ask for Intent**: "Confirm `DELETE_PROCEED`?"

## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Verification](../verification/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
