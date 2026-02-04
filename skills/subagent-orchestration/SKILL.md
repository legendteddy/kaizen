---
name: subagent-orchestration
description: Comprehensive guide to multi-agent systems, subagent orchestration, and parallel task execution. Covers architecture patterns, coordination strategies, and practical implementation.
---

# Multi-Agent Systems & Subagent Orchestration

> Patterns for coordinating multiple AI agents to solve complex problems efficiently.

## Activation Trigger
- Task requires parallel execution.
- Complex workflows needing specialized roles.
- Coordinating >3 sub-agents.

## When to Use Multiple Agents

Use subagents when:
- Task requires >10 tool calls or >30 minutes of work
- Multiple independent domains need exploration
- High-stakes decisions need peer review
- Work can be parallelized across CPU cores

Avoid when:
- Tasks requiring shared context
- Sequential dependencies
- Small tasks (<10 tool calls - overhead not worth it)

---

## Agent Architecture Patterns

### 1. The Team Model

```
┌─────────────────────────────────────────────────────────────────┐
│                        COORDINATOR                               │
│                (Task Decomposition + Routing)                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │EXPLORE   │  │ IMPLEMENT│  │  VERIFY  │  │ RESEARCH │          │
│  │          │  │          │  │          │  │          │          │
│  │ - Search │  │ - Write  │  │ - Test   │  │ - Docs   │          │
│  │ - Codebase│  │ - Edit   │  │ - QA     │  │ - Web    │          │
│  │ - Pattern│  │ - Create │  │ - Audit  │  │ - Synth  │          │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘          │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Agent Types:**
- **Explore**: Codebase analysis, pattern search, understanding
- **Implement**: Write code, edit files, create artifacts
- **Verify**: Test execution, validation, quality audit
- **Research**: Documentation lookup, web search, synthesis

---

### 2. Sequential Pipeline

```
User Request
    ↓
[Explore] → Understand codebase
    ↓
[Implement] → Write solution
    ↓
[Verify] → Test and validate
    ↓
Result to User
```

**Use for:** Complex features requiring exploration → implementation → verification

---

### 3. Map-Reduce Pattern

```
[Coordinator]
    ├─→ [Worker 1] Task chunk A
    ├─→ [Worker 2] Task chunk B
    ├─→ [Worker 3] Task chunk C
    ↓
[Aggregator] Combine results
```

**Use for:** Large codebases, bulk operations, data processing

---

### 4. Parallel Specialists

```
[Security Auditor]  [Performance Analyst]  [Logic Verifier]
         ↓                    ↓                     ↓
         └────────────────────┴─────────────────────┘
                           ↓
                    [Final Synthesis]
```

**Use for:** Critical code reviews, security audits, complex decisions

---

### 5. Iterative Refinement

```
[Builder] ←→ [Reviewer] (loop until pass)
```

**Use for:** Quality-critical output requiring multiple review cycles

---

## Dispatch Pattern

```
┌─────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR                                   │
│                                                                 │
│  1. DIVIDE    → Split task into independent subtasks           │
│  2. DISPATCH  → Send each subtask to a subagent                │
│  3. MONITOR   → Track progress and handle failures             │
│  4. COLLECT   → Gather results from all subagents              │
│  5. MERGE     → Combine results into final output              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Subagent Task Specification

Each subagent needs:

```markdown
## Task: [Name]

### Objective
Clear statement of what to achieve

### Context
Minimal context needed (files, previous results)

### Expected Output
What should be returned

### Success Criteria
- [ ] Output matches format
- [ ] No errors thrown
- [ ] Meets quality standards

### Constraints
- Time limit: 5 minutes
- Scope: [specific files/modules]
- Do not modify files outside scope
```

---

## Communication Protocol

### Message Format
```json
{
  "from": "coordinator",
  "to": "agent_type",
  "task_id": "uuid",
  "type": "task|result|query",
  "content": {
    "objective": "...",
    "context": {...},
    "constraints": [...]
  }
}
```

### Handoff Rules
1. **Complete context**: Pass all necessary information
2. **Clear objective**: State success criteria explicitly
3. **Bounded scope**: Define boundaries explicitly
4. **Result format**: Specify expected output structure

---

## Context Isolation

Each sub-agent:
- Has its own isolated context window
- Cannot see main agent's full history
- Only receives explicitly provided context
- Returns compressed summary (not full logs)

This prevents context pollution and keeps main agent focused.

---

## Safety Guardrails

| Rule | Limit | Purpose |
|:---|:---|:---|
| **Concurrency** | Max 3 agents | Prevent resource starvation |
| **Timeout** | 5 minutes per task | Prevent runaway processes |
| **Approval gates** | High-risk actions require coordinator | Safety check |
| **Context isolation** | Agents only see assigned context | Prevent information leaks |

---

## Error Handling

### Circuit Breaker Pattern
If a subagent fails:
1. **Retry once** with clarified instructions
2. **Escalate** to parent if retry fails
3. **Log failure** to `memory/lessons.json`
4. **Continue** with partial results if possible

### Failure Types

| Failure | Action |
|:---|:---|
| Subagent timeout | Retry once, then escalate |
| Incorrect output | Send back with feedback |
| Complete failure | Orchestrator handles manually |

### Two-Stage Review

After subagent completes:

**Stage 1: Spec Compliance**
- Did it do what was asked?
- Does output match expected format?
- Are success criteria met?

**Stage 2: Code Quality**
- Is the code clean?
- Are there any bugs?
- Would I approve this PR?

---

## Example Workflows

### Code Review Pipeline
```
1. Spawn [Researcher] → Find all files touched by PR
2. Spawn [Security Auditor] → Check for vulnerabilities
3. Spawn [Performance Analyst] → Identify bottlenecks
4. Synthesize results → Generate review report
```

### Feature Implementation
```
1. Spawn [Explore] → Analyze codebase patterns
2. Spawn [Implement] → Write the code
3. Spawn [Verify] → Run tests and validate
4. Deliver to user → Complete feature
```

---

## Best Practices

### Do
- ✅ Break large tasks into atomic subtasks
- ✅ Provide complete context in each prompt
- ✅ Set clear success criteria
- ✅ Monitor progress and collect results
- ✅ Handle failures gracefully

### Don't
- ❌ Spawn agents for simple tasks (<10 tool calls)
- ❌ Share mutable state between agents
- ❌ Allow indefinite execution (always use timeout)
- ❌ Ignore failed subagent tasks
- ❌ Create circular dependencies

---

## Anti-Patterns to Avoid

| Pattern | Why It's Bad |
|:---|:---|
| **Agent Sprawl** | Too many agents for simple tasks |
| **Callback Hell** | Agents calling agents calling agents |
| **Resource Starvation** | Unlimited concurrent agents |
| **Orphaned Agents** | Spawning without monitoring |
| **Context Leaks** | Sharing sensitive data between agents |

---


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Agent Communication](../agent-communication/SKILL.md)
- [Agent Cowork](../agent-cowork/SKILL.md)
