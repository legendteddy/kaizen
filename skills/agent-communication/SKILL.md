---
name: agent-communication
description: Mandatory IAC (Inter-Agent Communication) protocols and Handover Metadata.
---

# Agent Communication Protocol (IAC)

> "Clear communication is the prerequisite for autonomous safety."

## 1. The Handover Mandate (SHP)
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

## 2. Shared Backlog Protocol
- **Location**: `.agents/backlog.json`
- **Claiming**: Before starting a task from the backlog, an agent must "Claim" it by setting `status: "in_progress"` and `assigned_to: [agent_id]`.
- **Atomic Operations**: Always `read` -> `modify` -> `write` in a single tool turn if possible to minimize race conditions.

## 3. Conflict Resolution (The Boss Pattern)
- If two agents disagree on a file edit, the **Identity Agent** (Sovereign Identity) acts as the arbiter.
- Decisions are based on **Truth Always** over convenience.

## 4. Signal Hierarchy
- **CRITICAL**: Immediate abort (Safety boundary hit).
- **WARNING**: Potential drift or blocker.
- **INFO**: Progress update.

## Related Skills
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
