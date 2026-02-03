---
name: agent-cowork
description: Skill for claude-cowork tasks and workflows.
---

# Skill: Claude Cowork (v1.0)

> Computer use for file-heavy tasks (non-technical users)

## Purpose
Understand Cowork pattern for file and folder operations.

## Activation Trigger
- File organization tasks
- Data conversion (screenshots → spreadsheets)
- Bulk document processing

---

## What is Cowork?

**Claude Cowork** = Computer use for non-developers.

Extends Claude Code pattern to file-heavy operations:
- Read, edit, create files in designated folders
- Screenshot to spreadsheet conversions
- Bulk document drafting from notes
- Folder organization automation

---

## Cowork Capabilities

### 1. File Operations
```
- Read files from authorized folders
- Create new files (documents, spreadsheets, etc.)
- Edit existing files
- Organize folder structures
```

### 2. Data Conversion
```
Screenshot → Spreadsheet
Notes → Report
Raw data → Formatted document
```

### 3. Bulk Processing
```
- Process multiple files
- Apply consistent formatting
- Batch conversions
- Template application
```

---

## Security Model

### Designated Folders
- User explicitly grants folder access
- Sandboxed to authorized paths only
- No access outside designated areas

### Human Oversight
- User reviews outcomes
- Destructive actions require confirmation
- Audit trail of operations

### Prompt Injection Protection
- File contents cannot override instructions
- Trust boundary enforced
- Malicious content isolated

---

## Comparison

| Feature | Claude Code | Claude Cowork |
|:---|:---|:---|
| Target | Developers | Non-developers |
| Interface | Terminal/IDE | Desktop app |
| Focus | Code operations | File operations |
| Primary tasks | Debug, write code | Organize, convert |

---

## For Sovereign Framework

Cowork teaches:
1. **File-centric workflows**: Not everything is code
2. **Permission models**: Designated folder access
3. **Bulk operations**: Process many files at once
4. **Data transformation**: Convert between formats



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Agent Communication](../agent-communication/SKILL.md)
- [Agent Security](../agent-security/SKILL.md)
