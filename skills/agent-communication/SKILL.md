---
name: agent-communication
description: Mandatory IAC (Inter-Agent Communication) protocols and Handover Metadata.
---

# Agent Communication Protocol (IAC)

> "Clear communication is the prerequisite for autonomous safety."

## 1. The Handover Standard (SHP)
When an agent finishes a turn or hands over a task to another agent (e.g. Swarm), it MUST include a **Handover Metadata Header** in its final output:

```markdown
---
AGENT_ID: [Agent Name]
OBJECTIVE: [Current Task]
LAST_ACTION: [Tool Called]
RESULT: [Success/Fail/Blocked]
NEXT_STEP_IMPERATIVE: [What the next agent MUST do]
---
```

## 2. Shared Task Handoffs
Since no central registry exists, agents must communicate state via the **Identity Anchor**:
1. **Log Progress**: Always update `task.md` or a session log.
2. **Context Persistence**: Use the Handover Metadata Header defined in Section 1.
3. **Explicit Handovers**: State exactly which agent should take over and what their first tool call should be.

## 3. Conflict Resolution (The Boss Pattern)
- If two agents disagree on a file edit, the **Identity Agent** (Agent Identity) acts as the arbiter.
- Decisions are based on **Truth Always** over convenience.

## 4. Signal Hierarchy
- **CRITICAL**: Immediate abort (Safety boundary hit).
- **WARNING**: Potential drift or blocker.
- **INFO**: Progress update.

## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
