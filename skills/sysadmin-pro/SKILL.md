---
name: sysadmin-pro
description: Protocols for safe, idempotent system administration (Linux/Windows).
---

# Sysadmin Pro

> "Measure twice, cut once."

## Activation Trigger
- Executing shell commands (Bash/PowerShell).
- Managing system resources or processes.
- Ensuring script safety (idempotency).

## Safety First: The Blast Radius Check
Before running ANY command that modifies state (`rm`, `mv`, `dd`, `chmod`, `kill`):

1. **Verify Target:** Am I in the right directory? (`pwd`)
2. **Dry Run:** Echo the command first or use `--dry-run` if available.
3. **Backup:** Copy critical files before editing. `cp config.xml config.xml.bak`
4. **Wildcard Danger:** Never run `rm -rf $VAR/*` without verifying `$VAR` is set.

## Protocol: Idempotency
Scripts must be safe to run multiple times.

| Bad | Good | Why |
|:---|:---|:---|
| `mkdir /data` | `mkdir -p /data` | Won't error if exists |
| `echo "line" >> file` | `grep -q "line" file || echo "line" >> file` | Prevents duplicates |
| `npm install` | `npm ci` | Strict version install |

## Snippet Library
```bash
# Safe Directory Creation
mkdir -p /path/to/dir

# Safe Append
grep -qF "line" file.txt || echo "line" >> file.txt

# Safe Find & Delete (Verify first!)
find . -name "*.tmp" -type f -delete
```

## Shell Specifics

### Linux / Bash
- **Non-interactive:** Use `-y` or `-f` flags. `apt-get install -y`.
- **Exit on Error:** Start scripts with `set -e` or handle error codes.
- **Pipe Safety:** `set -o pipefail` checks for errors in pipes.

### Windows / PowerShell
- **Path Safety:** Use `Join-Path` instead of string concatenation.
- **Error Handling:** Use `-ErrorAction Stop` to catch failures.
- **Text Encoding:** Be careful with `>`. Use `Out-File -Encoding UTF8`.
- **Filtering:** Filter *left*. `Get-ChildItem -Filter` is faster than `| Where-Object`.

## Cross-Platform Equivalents

| Capability | Linux (Bash) | Windows (PowerShell) |
|:---|:---|:---|
| **Admin Check** | `if [ "$EUID" -ne 0 ]` | `([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)` |
| **Env Var** | `$HOME` | `$env:USERPROFILE` |
| **List Files** | `ls -la` | `Get-ChildItem -Force` |
| **Find File** | `find . -name "*.txt"` | `Get-ChildItem -Recurse -Filter "*.txt"` |
| **Read File** | `cat file.txt` | `Get-Content file.txt` |
| **Services** | `systemctl status nginx` | `Get-Service nginx` |
| **Kill Process** | `kill -9 <pid>` | `Stop-Process -Id <pid> -Force` |
| **Download** | `curl -O url` | `Invoke-WebRequest -Uri url -OutFile file` |

## ⚠️ Automated Command Safety (The "&&" Trap)
When executing commands via tools (e.g. `run_command`), **avoid chaining with `&&` or `;`**.
*   **Reason 1**: Windows PowerShell (legacy) does not support `&&`.
*   **Reason 2**: Debugging is harder. If `cmd1 && cmd2` fails, potential loss of stderr.

**Protocol**:
1.  **Split It**: Run `git add .` then `git commit`.
2.  **Verify It**: Check the exit code of each step individually.

## Diagnostic Workflow
1. **Resource Check:** High CPU/RAM? (`top`, `Get-Process`)
2. **Disk Space:** Full disk? (`df -h`, `Get-PSDrive`)
3. **Logs:** Check the tail. (`tail -f`, `Get-Content -Wait -Tail 10`)
4. **Network:** Port open? (`curl`, `Test-NetConnection`)

## Self-Improvement
- **Did a script fail silently?** -> Add error checking next time.
- **Did I accidentally overwrite a file?** -> Use `cp -n` (no clobber) or backup pattern.


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
