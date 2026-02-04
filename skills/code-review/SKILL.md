---
name: code-review
description: Giving and receiving constructive, high-value code reviews.
---

# Protocol: Code Review

> "Code review is about improving the code, not judging the coder."

## Activation Trigger
- Reviewing a Pull Request.
- Auditing code quality.
- Receiving feedback on your own code.

## Protocols

### 1. First Principle: Constructive Quality
The goal is to ship better software, not to prove intelligence.

### 2. Giving Review (The Checklist)
1. **Context First**: Read the ticket/issue before the code.
2. **Prioritize**: Security > Logic > Performance > Style.
3. **Be Specific**: "X is wrong" is bad. "X causes Y bug" is good.

### 3. Receiving Review (The Mindset)
- Feedback is a gift.
- Explain, don't defend.
- "Good catch" is the best response.

## Code Patterns

### Constructive Feedback Templates
```text
// ❌ Bad
"This is messy."

// ✅ Good
"This function handles three different responsibilities: A, B, and C.
Splitting it would make testing easier. What do you think?"
```

### Safety Checks
```text
[ ] Is this a breaking change?
[ ] Does this introduce a SQL injection risk?
[ ] Are secrets exposed?
[ ] Is there a rollback plan?
```

## Safety Guardrails
- **No Big Bangs**: Reject PRs > 400 lines unless mostly generated.
- **Security First**: Block immediately if secrets or injection risks found.
- **Test Standard**: No "logic change" without "test change".
- **Documentation**: If the code is confusing, documentation is required, not optional.
