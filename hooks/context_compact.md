# Hook: Context Compact (v1.0)

## Trigger
When context window approaches limit (~80% full).

## Compaction Protocol

### Step 1: Detect Limit
```
Monitor context usage:
- If context > 80% → Initiate compaction
- If context > 90% → URGENT compaction
```

### Step 2: Prioritize Content
```
KEEP (High Priority):
- Current objective
- Key decisions made this session
- Active file states
- Recent tool outputs (last 3)
- Error states and recovery plans

COMPRESS (Medium Priority):
- Historical messages → Summarize to key points
- Resolved errors → Archive to memory
- Intermediate outputs → Summarize outcomes only

ARCHIVE (Low Priority):
- Older conversation history
- Completed sub-tasks
- Superseded plans
```

### Step 3: Create Summary
```
Write a compressed summary:
- What was the objective?
- What was accomplished?
- What decisions were made?
- What is the current state?
- What are the next steps?
```

### Step 4: Write to Memory
```
Save summary to:
memory/conversation_summaries/[DATE]_session_summary.md
```

### Step 5: Clear Non-Essential
```
Remove from active context:
- Archived content
- Resolved intermediate states
- Superseded messages
```

## Summary Template

```markdown
# Session Summary: [DATE]

## Objective
[What was the user trying to achieve?]

## Accomplished
- [Major milestone 1]
- [Major milestone 2]

## Key Decisions
- [Decision 1 and rationale]
- [Decision 2 and rationale]

## Current State
[What is the current status of the work?]

## Next Steps
- [Immediate next step]
- [Following steps]
```

## Why This Matters
- Prevents context overflow crashes
- Preserves critical information
- Enables long multi-session projects
