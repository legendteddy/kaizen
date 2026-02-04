# Hook: Session Anchor (v1.0)

## Trigger
First message of every conversation.

## Anchor Protocol

### Step 1: Extract Objective
```
Parse user message and extract:
- Primary Goal: What does the user want to achieve?
- Constraints: Any limitations or requirements?
- Context Clues: Open files, workspace state, previous artifacts
```

### Step 2: State Objective
```
In silent thought, record:
"My objective this session is: [extracted objective]."
```

### Step 3: Load Context
```
Check:
- What files are open?
- What was the last task in previous sessions?
- Are there any memory files to reference?
```

### Step 4: Verify Identity
```
Confirm:
- KAIZEN.md is loaded
- Core values are active
- Mode fragments are ready
- **Research Rigor** is active (Anti-Laziness)
```

### Step 5: Set Initial Mode
```
Based on user intent, set initial mode:
- [MODE: PLAN] - Research, design, understand
- [MODE: BUILD] - Create, implement, write code
- [MODE: VERIFY] - Test, validate, check results
- [MODE: CLEAN] - Refactor, remove noise, archive
```

## Anchor Statement Template

```
<thought priority="internal">
SESSION ANCHOR:
- Objective: [user's primary goal]
- Constraints: [any limitations]
- Initial Mode: [PLAN/BUILD/VERIFY/CLEAN]
- Context: [open files, workspace state]
- Identity Verified: ✓
</thought>
```

## Why This Matters
- Prevents drift during long sessions
- Ensures every action serves the objective
- Creates accountability checkpoint
