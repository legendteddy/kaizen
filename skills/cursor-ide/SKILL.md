---
name: cursor-ide
description: Skill for cursor-ide tasks and workflows.
---

# Protocol: Protocol: Cursor IDE Patterns (v1.0)

> AI-first IDE patterns for agentic coding

## Purpose
Apply Cursor-style agentic coding patterns in any environment.

## Activation Trigger
- Multi-file editing tasks
- Complex refactoring
- Autonomous implementation requests

---

## Core Patterns

### 1. Agent Mode
AI works autonomously:
```
- Identifies files to create/modify
- Makes architectural decisions
- Executes terminal commands
- Analyzes errors and fixes them
```

### 2. Composer Mode
Multi-file editing from high-level instructions:
```
User: "Create a login page and connect it to the API"
AI:
  1. Plans architecture
  2. Generates new files
  3. Modifies existing files
  4. Maintains consistency
```

### 3. Plan Mode
Structured workflow:
```
1. RESEARCH: Analyze codebase
2. CLARIFY: Ask questions
3. PLAN: Generate implementation plan
4. APPROVE: Wait for user confirmation
5. EXECUTE: Generate code
```

---

## Codebase Understanding

Key principle: AI "sees" entire project as cohesive unit.

| Aspect | Benefit |
|:---|:---|
| Dependencies | Knows what imports what |
| Patterns | Follows existing conventions |
| Structure | Understands folder organization |
| Context | Relevant suggestions |

---

## Multi-File Operations

### Before Multi-File Edit
```
□ Map all files to touch
□ Identify dependencies between changes
□ Plan order of modifications
□ Consider rollback strategy
```

### During Multi-File Edit
```
□ Maintain consistency
□ Update imports/exports
□ Preserve existing patterns
□ Test as you go
```

---

## For Standard Framework

Cursor patterns align with our approach:
1. **Plan Mode** = Our PLANNING phase
2. **Agent Mode** = Our EXECUTION phase
3. **Codebase context** = Our grep-first retrieval
4. **Multi-file** = Our Composer-style operations

> **Reference Pattern:** See `patterns/agentic_ide.md` for the full architectural breakdown.



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
