---
name: sysadmin-pro
description: Skill for Linux/Windows system administration, shell scripting, and server management.
---

# Skill: Sysadmin Pro (v1.0)

## Purpose
Manage servers and local environments safely using shell commands.

## Activation Trigger
- "Configure this server"
- "Fix permission denied"
- "Install these packages"
- Shell/Bash/Powershell tasks.

---

## Protocol: Safe Execution

### 1. Non-Interactive Flags
**Rule:** Always assume no human is watching.
- `apt-get install -y`
- `npm install --yes`
- `docker run -d`

### 2. Idempotency
**Rule:** Scripts should run twice without breaking.
```bash
# Bad
mkdir /app

# Good
mkdir -p /app
```

### 3. Permissions
**Rule:** Never use `sudo` unless explicitly requested. If permission denied, report it.

---

## Cheat Sheet: One-Liners

| Task | Command |
|:---|:---|
| **Find file** | `find . -name "*.log"` |
| **Check Port** | `lsof -i :8080` (Linux) / `netstat -ano` (Win) |
| **Disk Usage** | `du -sh * | sort -h` |
| **Process** | `ps aux | grep node` |

---

## Windows Specifics (PowerShell)
- Use `Get-ChildItem` instead of `ls` for scripting stability.
- Use `Test-Path` before `Copy-Item`.
