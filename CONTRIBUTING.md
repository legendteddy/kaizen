# Contributing to Kaizen

Thank you for your interest in contributing to Kaizen! This framework grows through community contributions.

## How to Contribute

### Adding a New Skill

1. **Check for duplicates** — Search `skills/` to ensure your skill doesn't overlap with existing ones
2. **Create the skill folder** — `skills/your-skill-name/`
3. **Add SKILL.md** with this format:

```markdown
---
name: your-skill-name
description: Brief description of what this skill enables.
---

# Your Skill Name

> One-line summary

## Purpose
Why this skill exists.

## Activation Trigger
When this skill should be used.

---

## Content
Your skill content here.
```

4. **Submit a PR** with a clear description

### Improving Existing Skills

- Fix typos and improve clarity
- Add missing edge cases
- Update with new techniques
- Remove outdated information

### Adding Patterns

Patterns are reusable code templates. Add to `patterns/` with clear documentation.

### Adding Hooks

Hooks are lifecycle triggers. Propose new hooks that would benefit all users.

## Guidelines

- **Keep it universal** — Skills should work across all AI platforms
- **Be concise** — Agents have limited context windows
- **Test your skill** — Verify it works before submitting
- **No proprietary content** — Don't copy from closed sources
- **Paraphrase, don't plagiarize** — If inspired by something, rewrite in your own words

## Code of Conduct

- Be respectful and constructive
- Focus on improving the framework
- Help others learn

## Questions?

Open an issue if you have questions about contributing.
