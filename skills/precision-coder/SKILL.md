---
name: precision-coder
description: Technical standards for high-reliability software engineering and autonomous file automation.
---

# Protocol: Precision Coding & File Automation

> "Technical rigor in every line. Idempotency in every operation."

## 1. Defensive Execution Protocol
- **Atomic Commits**: Single-purpose changes.
- **Contract First**: Define interfaces/types BEFORE implementation.
- **Input Validation**: Mandatory checks for Null/Undefined at boundaries.

## 2. File Automation SOP (Cowork)
When performing bulk operations:

### The Authorization Rule
Never touch a directory without an `ls` verification. Ensure the path is within the authorized workspace.

### The Staging Pattern (Batch > 10 files)
1. Use a `tmp/` or `staging/` directory.
2. Operate on copies first.
3. Verify integrity before final movement.

### Idempotency
Ensure commands are safe to run twice (e.g. `mkdir -p` instead of `mkdir`).

## 3. Tool-Specific Guardrails

### write_to_file
- **Integrity**: Read-back file after write to ensure no truncation or corruption.

### run_command
- **Isolation**: check `pwd` before state-changing commands.
- **Sequential**: Use separate tool calls for complex chains.

## 4. Security Hardening
- **Parameterized**: No string interpolation in SQL or OS calls.
- **Sanitized**: Default to `escapeHtml` or `textContent` for UI components.
- **Secrets**: 100% environment variables.

## 5. Quality Standards
- No partial completions without clear logging.
- "Dry Run" report mandatory for large file movements (>50 files).

## Related Skills
- [Software Architecture](../software-architecture/SKILL.md)
- [Verification](../verification/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
