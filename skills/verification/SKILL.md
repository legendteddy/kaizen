---
name: verification
description: Mandatory proof-of-work protocols. No completions without evidence.
---

# Verification Protocol (Directive)

> "Assertion is not proof. Proof is verification."

## 1. The Proof Mandate
A task is NOT marked as "Done" until verification is documented.

## 2. Tool-Based Proof
### Code Changes
- **Constraint**: Must perform a `view_file` or `read-back` to verify the edit applied correctly.
- **Verification**: Run `cargo check`, `tsc`, or `npm test` as applicable.

### File Operations
- **Constraint**: `ls` or `view_file` to confirm existence/content.
- **Verification**: No "assumed" creation. High-trust only.

### Commands
- **Constraint**: Check **Exit Code**.
- **Verification**: Match stdout/stderr against expected patterns.

## 3. Verification Header (Mandatory)
Every turning point in a complex task must conclude with:
```markdown
### Verification
- **Action**: [Brief description]
- **Proof**: [specific tool output or file read-back]
- **Status**: [PASS/FAIL]
```

## 4. Anti-Patterns (Forbidden)
- ❌ "I have fixed it." (Without proof).
- ❌ "It should work now."
- ❌ "Assumed success."

## Related Skills
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Precision Coder](../precision-coder/SKILL.md)
- [Safety Boundaries](../safety-boundaries/SKILL.md)
