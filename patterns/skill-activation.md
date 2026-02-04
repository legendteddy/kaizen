---
name: skill-activation
description: Standard operating procedure for activating specific skills.
---

# Pattern: Skill Activation (Self-Loading)

> "A Sovereign Agent knows what it doesn't know."

## Context
When a user asks: *"Activate [Skill Name]"* or *"Can you use [Skill]?"*

## Protocol

### 1. Research Rigor (Grep First)
**NEVER** assume a skill exists or has a specific file name.
*   `find_by_name("[skill-name]", "skills/")` to check exact matches.
*   `grep_search("[keyword]", "skills/")` to find semantic matches if exact fails.

### 2. Ingest Protocol
Once the file is located (`skills/domain/SKILL.md`):
*   `view_file` the full content.
*   Read:
    *   **Activation Trigger**: Does this match the user's intent?
    *   **Protocols**: What rules must I now follow?
    *   **Safety**: What is now forbidden?

### 3. State Transformation (The Announcement)
You must explicitly confirm the state change to the user.

**Template:**
```markdown
# ACTIVATING SKILL: [Skill Name] - [Short Description]

I have verified and read `[path/to/SKILL.md]`.

**Protocol Active:**
*   **Rule 1**: [Key constraint]
*   **Rule 2**: [Key constraint]

*System aligned. Awaiting objective.*
```
