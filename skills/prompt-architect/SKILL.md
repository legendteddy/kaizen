---
name: prompt-architect
description: Master skill for crafting perfect prompts for Claude Code and other AI agents.
---

# Prompt Architect — The Art of AI Communication

This skill transforms you into a **prompt engineering specialist**. You craft prompts that maximize Claude Code's effectiveness.

---

## 1. The Prompt Engineering Mindset

### First Principles
1. **AI agents are literal**: They do exactly what you say, not what you mean
2. **Context is expensive**: Every token counts, be precise
3. **Structure enables action**: Well-formatted prompts get better results
4. **Verification prevents loops**: Define success upfront

### The Golden Rule
```
A good prompt should make the AI's job EASY, not test its intelligence.
```

---

## 2. Prompt Anatomy

### The Four Pillars
```
┌─────────────────────────────────────────┐
│  CONTEXT   │  What the AI needs to know │
├─────────────────────────────────────────┤
│  INTENT    │  What you actually want    │
├─────────────────────────────────────────┤
│  CONSTRAINTS │ What to avoid or require │
├─────────────────────────────────────────┤
│  VERIFICATION │ How to confirm success  │
└─────────────────────────────────────────┘
```

### Context Types
| Type | Example | When to Use |
|------|---------|-------------|
| **Technical** | "This is a Tauri v2 app with Rust backend" | Always for coding |
| **Historical** | "Last session we refactored auth.ts" | Continuing work |
| **Constraint** | "Using SQLite, no server" | Architecture limits |
| **User Pref** | "Prefer explicit error handling" | Coding style |

---

## 3. Prompt Templates

### Template 1: Feature Request
```markdown
## Feature: [Name]

### Context
- **Project**: [name] ([tech stack])
- **State**: [what exists now]
- **Files**: [key files to touch]

### Requirements
1. [Specific, measurable requirement]
2. [Specific, measurable requirement]

### Constraints
- **Must**: [required behaviors]
- **Must Not**: [forbidden actions]

### Success Criteria
- [ ] [How to verify it works]
```

### Template 2: Bug Fix
```markdown
## Bug: [One-line description]

### Symptoms
- **Actual**: [what happens]
- **Expected**: [what should happen]
- **Frequency**: [always/intermittent]

### Evidence
```
[exact error message or behavior]
```

### Context
- **File(s)**: [where the bug likely is]
- **Trigger**: [what action causes it]

### Suspected Cause
[Your hypothesis - helps Claude start faster]
```

### Template 3: Refactor
```markdown
## Refactor: [target]

### Current State
- **File**: [path]
- **Problem**: [why it needs refactoring]
- **Size**: [~lines]

### Desired State
- **Pattern**: [SOLID principle, design pattern]
- **Goal**: [what it should look like]

### Constraints
- **Keep**: [don't break these]
- **Tests**: [existing tests to maintain]
```

### Template 4: Investigation
```markdown
## Investigate: [question]

### What I Need to Know
[Specific question I can't answer myself]

### What I've Tried
1. [First thing I tried]
2. [Second thing]

### Relevant Files
- [file.ts] - [why relevant]

### Expected Output
[What format should the answer be in]
```

---

## 4. Prompt Optimization Techniques

### 4.1 Specificity Ladder
```
❌ "Fix the login"
⚠️ "Fix the login button not working"
✅ "Fix login button in LoginForm.tsx line 45 - onClick handler not firing on mobile Safari"
```

### 4.2 Constraint Sandwiching
Put constraints between context and requirements:
```
[Context]
[CONSTRAINTS - what NOT to do]
[Requirements]
```

This ensures constraints are read before action.

### 4.3 Example-Driven Prompts
```markdown
### Output Format
Return a JSON object like this:
```json
{
  "status": "success" | "error",
  "data": { ... },
  "message": "Human-readable"
}
```
```

### 4.4 Negative Constraints
Tell Claude what NOT to do when it matters:
```
Do NOT:
- Modify the database schema
- Add new dependencies
- Change the authentication flow
```

---

## 5. Prompt Anti-Patterns

### ❌ Vague Requests
```
"Make it better"
"Clean this up"
"Fix the bugs"
```

### ❌ Multiple Unrelated Tasks
```
"Add login, then refactor the database, also update the CSS"
```
Split into separate prompts!

### ❌ Missing Context
```
"Add a button that does X"
// Missing: What button? Where? What's the current state?
```

### ❌ No Success Criteria
```
"Optimize the performance"
// Missing: How do we know it's optimized? What metrics?
```

---

## 6. Claude Code-Specific Optimizations

### 6.1 File Path Mentions
Always include full paths:
```
✅ "Edit src/components/LoginForm.tsx"
❌ "Edit the login form"
```

### 6.2 Multi-File Tasks
For coordinated changes:
```markdown
### Files to Modify
1. `src/types/user.ts` - Add UserRole type
2. `src/services/auth.ts` - Import and use UserRole
3. `src/components/Header.tsx` - Display user role

### Order
Modify in this order to avoid import errors.
```

### 6.3 Tool Hints
When you know what tools Claude should use:
```markdown
### Approach
1. First, search for existing patterns with grep
2. Read the file outline before making changes
3. Run tests after modification
```

---

## 7. Prompt Chains

For complex tasks, break into phases:

### Chain 1: Investigation → Implementation
```
Prompt 1: "Analyze how auth currently works in this codebase"
[Claude responds with analysis]
Prompt 2: "Based on your analysis, add OAuth support"
```

### Chain 2: Plan → Execute → Verify
```
Prompt 1: "Create an implementation plan for feature X"
[User reviews plan]
Prompt 2: "Execute the approved plan"
[Claude implements]
Prompt 3: "Verify the implementation works correctly"
```

---

## 8. Quality Checklist

Before sending any prompt:

- [ ] **Clear Goal**: One main objective
- [ ] **Sufficient Context**: Tech stack, current state
- [ ] **Explicit Constraints**: What to avoid
- [ ] **Success Criteria**: How to verify
- [ ] **Actionable**: Claude can start immediately
- [ ] **Scoped**: Not trying to do too much

---

## 9. Meta-Prompts

### Generate a Prompt
```
I want to [high-level goal].
The project uses [tech stack].
Key files are [list].
Current state is [description].

Generate a Claude Code prompt for this.
```

### Improve a Prompt
```
Here's my prompt: [paste]

Make it more specific and actionable for Claude Code.
```

### Debug a Failed Prompt
```
I sent this prompt: [paste]
Claude did: [what happened]
Expected: [what should have happened]

How should I rephrase this?
```

---

*"A well-crafted prompt is worth a thousand iterations."*
