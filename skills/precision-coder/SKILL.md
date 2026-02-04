# Protocol: Precision Coder

> Technical standards for high-reliability software engineering.

## 1. Defensive Execution Protocol
- **Atomic Commits**: Single-purpose changes with descriptive messages.
- **Structured Error Handling**: `try/catch` must capture input state and stack traces.
- **Input Validation**: Mandatory checks for Null, Undefined, and Empty sets at component boundaries.

## 2. Strong Typing
- **Explicit Only**: `any` is forbidden in production code.
- **Contract First**: Define `interface` or `TypedDict` BEFORE implementing logic.
- **Strict Optionality**: Use `Optional[T]` or `T | undefined`.

## 3. Tool-Specific Guardrails
### `write_to_file`
- **Verify Path**: No overwriting `KAIZEN.md` or system configs.
- **Integrity**: Read-back file after write to check for truncation.

### `run_command`
- **Isolation**: Check `pwd` before modifications.
- **Safe Chaining**: Use sequential calls (no `&&` in PowerShell).

## 4. Security Hardening
- **Parameterized Only**: No string interpolation in SQL or OS commands.
- **Sanitized Output**: Mandatory `textContent` or `escapeHtml` for UI injection prevention.
- **Secrets**: 100% environment-variable-only. Use `dotenv` or equivalent.

## 5. Peer Review (Self-Audit)
Before reporting "Done":
- [ ] No placeholders.
- [ ] No `console.log` or debuggers.
- [ ] Minimal nesting (Max 3 levels).
- [ ] All requirements in `task.md` checked.

## Related Skills
- [Software Architecture](../software-architecture/SKILL.md)
- [Verification](../verification/SKILL.md)
- [Security Boundaries](../safety-boundaries/SKILL.md)
