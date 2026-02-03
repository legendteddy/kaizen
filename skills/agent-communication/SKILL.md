---
name: agent-communication
description: Protocols for Inter-Agent Communication (IAC), Locking, Swarm Coordination, and Continuous Collaboration.
---

# Agent Communication Protocol (ACP) v1.1

> "None of us is as smart as all of us."

## 1. Purpose
Define how multiple autonomous agents (Claude, Gemini, Cursor) coexist in the same repository without race conditions and **actively collaborate** to improve the codebase.

## Activation Trigger
- Multiple agents detected (PID check).
- File lock contention errors.
- Collaborative task execution (Hive Mind).

## 2. Directory Structure
All communication happens in `.agents/`:

```text
.agents/
├── registry.json       # Who is active?
├── backlog.json        # Shared Task Queue (The Hive Mind)
├── locks/              # File locks
│   └── README.md.lock
├── signals/            # Async messages
└── chat.log            # Shared transcript
```

## 3. Protocol: The Registry (`registry.json`)
When an agent starts, it registers itself to announce presence.

## 4. Protocol: The Hive Mind (Continuous Improvement)
Agents should not just wait for commands. They should **seek work**.

### The Backlog (`backlog.json`)
A JSON list of tasks that any agent can pick up.

```json
[
  {
    "id": "task_001",
    "title": "Upgrade 'git-workflow' skill",
    "status": "pending",
    "priority": "medium",
    "assigned_to": null
  }
]
```

### The Collaboration Loop
1.  **Poll:** Read `backlog.json`.
2.  **Claim:** If a task is `pending` and `assigned_to` is null:
    - Lock `backlog.json`.
    - Set `status="in_progress"` and `assigned_to="me"`.
    - Unlock.
3.  **Execute:** Perform the task (edit files, run tests).
4.  **Complete:** Mark as `completed` in backlog.

## 5. Protocol: Semantic Locking
Before editing a critical file, acquire a lock. (See `scripts/agent_comm.py`).

## 6. Protocol: "Pass the Baton"
If an agent hits a blocker (e.g., "I don't know React"), it creates a task in `backlog.json`:
- Title: "Fix React Component"
- Status: "pending"
- Context: "I tried X, but failed. Structure is in `src/`."

Another agent (e.g., `react-ts-expert`) picks it up.

## 7. Safety Limits
- **Max Concurrency:** Check `registry.json`. If > 3 agents active, consider yielding.
- **Rate Limit:** Do not commit more than once every 5 minutes per agent to avoid git conflicts.


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Agent Architecture](../agent-architecture/SKILL.md)
- [Agent Cowork](../agent-cowork/SKILL.md)
- [Agent Security](../agent-security/SKILL.md)
