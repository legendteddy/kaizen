---
name: context-manager
description: Comprehensive context window optimization and memory management, covering working memory efficiency, persistent memory storage, and session continuity across conversations.
---

# Context & Memory Manager

> Optimize context window usage and maintain persistent memory across sessions.

---

## 1. Context Budget Awareness

### Token Economics
```
You have ~128K tokens of context.
- System prompt: ~2K tokens
- Conversation history: Variable
- File contents: ~400 tokens per 100 lines
- Your thinking: ~500-2000 tokens per response

Budget wisely.
```

### Context Pressure Signals
- **Low**: <50% context used — Read freely, explore widely
- **Medium**: 50-75% used — Be selective, summarize read files
- **High**: 75-90% used — Only essential information
- **Critical**: >90% used — Request context clear or summarize aggressively

---

## 2. File Reading Strategy

### Priority Hierarchy
```
1. CRITICAL    Currently edited file
2. HIGH        Files in error stack traces
3. MEDIUM      Imported/dependency files
4. LOW         Related files (same feature)
5. BACKGROUND  Project docs, configs
```

### Smart Reading Rules

**Rule 1: Read Selectively**
Before reading a large file:
```javascript
// Read only the sections you need
read('large-file.ts', offset: 45, limit: 35)
```

**Rule 2: Grep, Don't Read**
When searching for something:
```javascript
// ❌ Reading entire codebase
read('file1.ts')
read('file2.ts')
read('file3.ts')

// ✅ Targeted search
grep('functionName', 'src/')
// Then read only matching files
```

**Rule 3: Cache Mentally**
After reading a file:
```xml
<thinking>
File summary for user-service.ts:
- Purpose: User CRUD operations
- Key functions: createUser(), updateUser(), deleteUser()
- Dependencies: database.ts, validator.ts
- Pattern: Repository pattern

I don't need to re-read this file.
</thinking>
```

---

## 3. Context Compaction

### When to Summarize
- Same topic discussed for 10+ turns
- Context pressure is high (>75%)
- About to start a new subtask

### Summary Format
```xml
<thinking>
## Conversation Summary
- **Goal**: Build user authentication system
- **Completed**: Login endpoint, JWT generation
- **Current**: Working on password reset flow
- **Decisions Made**:
  - Using bcrypt for hashing
  - JWTs expire after 24h
  - Refresh tokens stored in Redis
- **Open Questions**: None
</thinking>
```

### Checkpoint Strategy
Every 10-15 exchanges:
```xml
<thinking>
## Session Checkpoint
- Context usage: ~60%
- Task progress: 40% complete
- Key files in memory: auth.ts, user.ts, db.ts
- Next steps: Implement password reset

No need to re-read foundation files.
</thinking>
```

---

## 4. Persistent Memory System

### Memory Types

**Episodic Memory** (What happened)
- Location: `memory/episodic/`
- Content: Session summaries, major milestones
- Format: `YYYY-MM-DD_brief_description.md`

**Semantic Memory** (What I know)
- Location: `memory/knowledge/`
- Content: User preferences, project conventions, domain expertise
- Format: JSON for structured data, Markdown for knowledge

**Procedural Memory** (How to do things)
- Location: `skills/` and `patterns/`
- Content: Reusable skills, code templates, workflows
- Access: Greppable, human-readable Markdown

**Decision Log** (Why I chose)
- Location: `memory/decisions_log.md`
- Content: Key architectural and strategic decisions with rationale

### Memory Storage Protocol

**When to Write:**
- **Conversation Summaries**: At session end or before context compaction
- **Decisions Log**: After major architectural or strategic decisions
- **Lessons Learned**: After correcting mistakes or discovering gotchas
- **User Preferences**: When user states preferences explicitly

**Storage Format:**
```markdown
## Memory Entry

**Type**: decision | lesson | preference | fact
**Date**: 2026-02-03
**Context**: [Brief description]
**Content**: [What to remember]
**Relevance**: [When to recall this]
```

---

## 5. Session Handoff

### At Session End
1. **Summarize**: Current state in 5-10 sentences
2. **Key findings**: List important discoveries
3. **Next steps**: What should continue
4. **Save**: Write to `memory/session_summary.md`

### Session Summary Format
```markdown
# Session Summary: [Date]

## Objective
[What we were trying to accomplish]

## Completed
- [List of completed items]

## In Progress
- [List of incomplete items]

## Key Decisions
- [Important choices made with rationale]

## Context for Next Session
- [Files to know about]
- [Decisions that affect future work]
- [Next steps to take]
```

### Cross-Conversation Memory
At session start:
1. Load `memory/session_summary.md` (if exists)
2. Load `memory/knowledge/user_preferences.json`
3. Grep `memory/` for objective keywords

---

## 6. Knowledge Retrieval

### Project Context Priority
Always check these first:
1. `KAIZEN.md` — Core principles and guidelines
2. `README.md` — Project overview
3. `package.json` / `Cargo.toml` — Dependencies
4. `.env.example` — Environment variables

### When Lost
```xml
<thinking>
I'm uncertain about [X].

Search strategy:
1. Check KAIZEN.md and project docs for [X]
2. Search codebase for existing patterns
3. Check imported library docs
4. Grep memory/ for previous encounters
5. Ask user for clarification
</thinking>
```

### Engram-Style Retrieval
Separate static memory from dynamic reasoning:
1. **Static Memory**: `skills/` and `patterns/` (grep-indexed)
2. **Dynamic Reasoning**: Current context window
3. **Retrieval**: Classify intent → grep relevant skill → load into context

Benefit: O(1) lookup via file path, no vector database needed.

---

## 7. Context Hygiene

### Every 10 Tool Calls
1. **Check**: Am I still solving the original objective?
2. **Prune**: Remove resolved errors from active focus
3. **Anchor**: Re-state the objective if drifting

### Before Context Limit (~80%)
1. **Summarize**: Compress the session so far
2. **Archive**: Write summary to `memory/conversation_summaries/`
3. **Clear**: Remove non-essential history from working memory

### Context Reset Protocol
**When to Request Reset:**
- Task is complete, starting new unrelated task
- Context is >80% full
- Conversation is confused/circular
- Major topic change

**Clean Handoff:**
Before reset, provide summary of:
- What was completed
- Files that were modified
- Important context to remember
- Next steps

---

## 8. Multi-File Operations

### Parallel Reading
When files are independent:
```javascript
// ✅ Read in parallel
[
  read('auth.ts'),
  read('user.ts'),
  read('config.ts')
]
```

### Sequential Reading
When files depend on each other:
```javascript
// ✅ Read in order
read('types.ts')     // Understand types first
// then
read('service.ts')   // Uses those types
```

### Batch Editing
When making related changes:
```javascript
// ✅ Plan all changes, execute together
<thinking>
Changes needed:
1. types.ts: Add UserRole enum
2. user.ts: Import and use UserRole
3. api.ts: Update endpoint response

Execute as batch to maintain consistency.
</thinking>
```

---

## 9. Error Context Handling

### When Error Occurs
Minimum context needed:
1. Error message (exact text)
2. Stack trace (top 3-5 frames)
3. Line of code that failed
4. Values of relevant variables

### Context Pruning
```xml
<thinking>
Error: "Cannot read property 'id' of undefined"
Stack: user.ts:45:12

I only need to read:
1. user.ts lines 40-50 (error location)
2. The caller (how was the function invoked?)

I do NOT need:
- Other files
- Entire user.ts
- Unrelated conversation history
</thinking>
```

---

## 10. Efficiency Metrics

### Good Patterns
- ✅ Reading outlines before full files
- ✅ Using grep for targeted searches
- ✅ Caching file summaries mentally
- ✅ Parallel reads for independent files
- ✅ Checkpointing long sessions
- ✅ Writing to memory at session end
- ✅ Loading previous context at start

### Anti-Patterns
- ❌ Re-reading same file multiple times
- ❌ Reading entire files for small changes
- ❌ Not summarizing long conversations
- ❌ Ignoring project documentation
- ❌ Keeping irrelevant context
- ❌ Not persisting key decisions

---

## 2026 Memory Architectures (Future)

### Vector Store
- Store as embeddings, retrieve by similarity
- Tools: Pinecone, Weaviate, ChromaDB

### Graph Memory
- Nodes: entities (people, projects)
- Edges: relationships
- Enables reasoning over connections

### Hardware (NVIDIA ICMS)
- Near-compute memory for KV cache
- Critical for long-context agents

---

*"The best context is minimal context. The best memory is organized memory."*
