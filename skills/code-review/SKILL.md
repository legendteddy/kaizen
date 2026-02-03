---
name: code-review
description: Giving and receiving code review with constructive feedback.
---

# Code Review

> Improve code quality through collaborative review.

## Activation Trigger
- Reviewing a Pull Request.
- Auditing code quality.
- Receiving feedback on your own code.

## Giving Reviews

### Pre-Review Checklist
Before reviewing, check:
```
□ Do I understand the goal?
□ Have I read the related issue/ticket?
□ Am I in the right mindset (not rushed)?
```

### What to Look For

| Priority | Check |
|:---|:---|
| 🔴 Critical | Security vulnerabilities, data loss risks |
| 🟠 Important | Logic errors, performance issues |
| 🟡 Moderate | Code style, naming, documentation |
| 🟢 Minor | Formatting, typos |

### Constructive Feedback

**Bad**: "This is wrong."
**Good**: "This could throw a null pointer if X is undefined. Consider adding a check."

**Bad**: "Why did you do it this way?"
**Good**: "I'm curious about the choice of X over Y here. Was there a specific reason?"

---

## Receiving Reviews

### Mindset
- Feedback is about the code, not you
- Assume good intent
- Ask for clarification if unclear

### Response Patterns

| Feedback Type | Response |
|:---|:---|
| Valid critique | "Good catch, fixing now" |
| Disagreement | "I see your point. Here's my reasoning: ..." |
| Unclear | "Could you elaborate on what you mean?" |
| Stylistic | "Happy to change if you feel strongly" |

---

## Review Workflow

```
1. Author creates PR with description
2. Reviewer reads description first
3. Reviewer checks code in logical order
4. Comments are specific and actionable
5. Author responds to all comments
6. Reviewer approves or requests changes
7. Author merges after approval
```
