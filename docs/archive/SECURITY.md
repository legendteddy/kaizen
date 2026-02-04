# Kaizen Security Policy

> "Trust, but verify. Then verify again."

## 1. The Sandbox Protocol
The Kaizen Agent (`kaizen_core`) runs in a strictly enforced sandbox to prevent accidental or malicious damage.

### Path Confinement (Jail)
- The agent **CANNOT** read or write files outside the repository root.
- Attempts to access parent directories (`../`) or absolute paths (`/etc/passwd`, `C:\Windows`) are blocked by `_validate_path`.
- Symlinks that escape the jail are treated as security violations.

### Command Whitelist
The agent **CANNOT** run arbitrary shell commands. Only the following tools are permitted:
- `ls`, `dir` (Listing)
- `grep`, `find` (Search)
- `python`, `pytest` (Execution)
- `git` (Version Control)
- `echo`, `cat`, `type` (File Ops)

**Blocked:** `rm`, `mv`, `chmod`, `ssh`, `curl` (unless via specific API), piping (`|`), chaining (`&&`).

## 2. Preventing "Trojan" Behavior
To prevent the agent from becoming a backdoor:

1.  **Local Execution Only:** The agent runs on *your* machine, not a cloud server. It listens to *your* local backlog.
2.  **No Remote Fetching:** The agent does not poll external URLs for tasks. It only reads `.agents/backlog.json`.
3.  **Timeout Limits:** All commands time out after 30 seconds to prevent infinite loops or denial-of-service.

## 3. Human Oversight
The agent logs all actions to stdout. You can audit its behavior by watching the terminal or checking the task result in `backlog.json`.

## 4. Reporting Vulnerabilities
If you find a way to break the sandbox, please open an issue immediately.