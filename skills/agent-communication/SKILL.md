---
name: agent-communication
description: Protocols for Inter-Agent Communication (IAC), Locking, and Swarm Coordination.
---

# Agent Communication Protocol (ACP) v1.0

> "Don't fight over the steering wheel."

## 1. Purpose
Define how multiple autonomous agents (Claude, Gemini, Cursor) coexist in the same repository without race conditions or file corruption.

## 2. Directory Structure
All communication happens in `.agents/`:

```text
.agents/
├── registry.json       # Who is active?
├── locks/              # File locks
│   └── README.md.lock
├── signals/            # Async messages
│   └── sig_uuid.json
└── chat.log            # Shared transcript
```

## 3. Protocol: The Registry (`registry.json`)
When an agent starts a session, it MUST register itself.

```json
{
  "agents": {
    "antigravity-1": {
      "type": "Claude Code",
      "pid": 1234,
      "status": "active",
      "last_heartbeat": "2026-02-03T12:00:00Z"
    },
    "gemini-crawler": {
      "type": "Gemini CLI",
      "pid": 5678,
      "status": "idle"
    }
  }
}
```

## 4. Protocol: Semantic Locking
Before editing a critical file, acquire a lock.

1.  **Check:** Does `.agents/locks/{filename}.lock` exist?
    *   **Yes:** Check timestamp. If < 5 mins old, WAIT. If > 5 mins, STEAL (Stale lock).
    *   **No:** Proceed.
2.  **Acquire:** Write `{ "agent": "id", "expiry": "timestamp" }` to the lock file.
3.  **Work:** Edit the file.
4.  **Release:** Delete the lock file.

**Critical Files:** `SKILLS.md`, `README.md`, `KAIZEN.md`.

## 5. Protocol: Asynchronous Signals
To tell another agent to do something (without blocking).

**Write to `.agents/signals/{uuid}.json`:**
```json
{
  "to": "gemini-crawler",
  "from": "antigravity",
  "action": "index_new_skills",
  "priority": "high"
}
```

**Target Agent:** Watches the folder and executes.

## 6. Protocol: The Shared Log (`chat.log`)
Agents should log high-level intent to avoid redundant work.

```log
[2026-02-03T12:00:00Z] [Antigravity]: UPGRADING 10 skills. Please avoid editing skills/* for 5 minutes.
[2026-02-03T12:01:00Z] [Gemini]: Acknowledged. I will focus on 'tests/'.
```

## 7. Implementation (Python Helper)
See `scripts/agent_comm.py` (if available) for lock handling.
