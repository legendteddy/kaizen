---
name: swarm-orchestrator
description: Manages local swarm sub-agents. Allows spawning background jobs to Ollama via the swarm bus.
---

# Swarm Orchestrator (Phase 6)

This skill enables "Parallel Brain" operations by delegating tasks to local background workers.

## 🐝 Swarm Protocols

### 1. Spawning a "Prime" Job (Gemini CLI)
The Gemini CLI is our most intelligent worker. It uses local Google Auth.
To spawn a Prime Job, set the model to `gemini-cli`:
```json
{
  "id": "UUID",
  "status": "pending",
  "prompt": "The detailed task for the sub-agent",
  "model": "gemini-cli",
  "priority": "high",
  "created_at": "ISO8601"
}
```

### 2. Spawning a "Base" Job (Ollama)
For simple, fast tasks (poems, summaries), use local Ollama models.

### 2. Launching Workers
If no workers are active (check `last_pulse` in `swarm_bus.json`), execute the worker script in background mode with appropriate system paths.

### 3. Monitoring & Collection
*   **Step 1:** Read `swarm_bus.json`.
*   **Step 2:** Identify `completed` jobs.
*   **Step 3:** Collect `result` and move the job to `history`.
*   **Step 4:** Summarize the findings for the user.

## 🛡️ Safety Gates
1. **Concurrency Limit:** Do not spawn more than 3 background jobs at once to avoid GPU thrashing.
2. **Context Isolation:** Sub-agents only see the prompt provided. Important context must be passed explicitly.
3. **Self-Monitoring:** If a job stays `processing` for > 5 minutes, mark it as `failed` and retry or escalate.
