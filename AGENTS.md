# AGENTS.md - Sovereign Kaizen AI Agent Instructions

> For AI agents: this file provides context for understanding and extending the Sovereign Kaizen ecosystem.

---

## Project Overview

Sovereign Kaizen is a local-first AI operating system that combines:
1. Kaizen Skills Library (`C:\Users\thoma\Documents\kaizen`) - modular skills and tooling
2. Sovereign Memory Engine (`C:\Users\thoma\.gemini\sovereign-engine`) - FastAPI backend + persistence
3. Sovereign Dashboard (`C:\Users\thoma\.gemini\sovereign-dashboard`) - React/Vite UI

### Architecture

```
+------------------------------ SOVEREIGN KAIZEN --------------------------------+
| UI (React/Vite)     http://localhost:5173   C:\Users\thoma\.gemini\sovereign-dashboard |
| API (FastAPI)       http://localhost:8787   C:\Users\thoma\.gemini\sovereign-engine    |
| Skills Library      local-first             C:\Users\thoma\Documents\kaizen\skills     |
| Storage (SQLite+vec) persistent             C:\Users\thoma\.gemini\memory              |
+--------------------------------------------------------------------------------+
```

---

## Directory Structure (High Level)

```
C:\Users\thoma\
  Documents\kaizen\
    skills\                 (skill definitions)
    tools\                  (repo tooling)
    marketplace\            (local .kaizen package index)

  .gemini\
    sovereign-engine\
      engine\               (FastAPI app + Foundry + agent endpoints)
      .venv\                (engine venv)
      test_all_endpoints.py (non-destructive full endpoint smoke suite)
      test_engine.py        (simple ingest/search smoke; requires server running)

    sovereign-dashboard\
      src\                  (React app)
```

---

## API Endpoints (Engine)

Base URL: `http://localhost:8787`

### Core
- `GET /` health summary
- `GET /health` detailed health
- `GET /capabilities` feature flags + configured paths for UI/clients
- `POST /ask` AI generation
  - Supports SSE streaming when request sets `stream: true` OR header `Accept: text/event-stream`
- `POST /visualize` Mermaid graph snapshot for a topic (fast, local)
- `POST /reflect` knowledge graph reflection
- `POST /ingest` ingest content
- `POST /search` semantic search

### MCP (Model Context Protocol)
- Standalone MCP HTTP server: `python -m engine.mcp_http_server`
  - Default URL: `http://127.0.0.1:8791/mcp`
  - Exposes memory + files + skills as MCP tools/resources (see `engine/mcp_server.py`)

### Voice
- `GET /voice/voices` list available TTS voices (Windows SAPI)
- `POST /voice/speak` text-to-speech (optionally returns base64 WAV)
- `POST /voice/transcribe` speech-to-text (optional; requires whisper libs)

### Agentic (OpenClaw-style)
- `POST /execute` run shell command
  - Supports SSE streaming when request sets `stream: true`
- `POST /execute/cancel` cancel a running streamed command by id
  - Accepts optional `pid` as a fallback kill mechanism (improves reliability across process boundaries)
- `POST /files/read` read file
- `POST /files/write` write file
- `POST /files/search` search files
- `POST /files/list` list directory
- `GET /skills` list built-in skills
- `POST /skills/run` run built-in skill
- `POST /skills/install` install a `.kaizen` skill package into Kaizen `skills/`
  - Supports installing by name from the local marketplace index OR by `package_path`

### Marketplace
- `GET /marketplace/index` returns the local `marketplace/index.json` (packages list)

### Feedback (RL Loop Foundation)
- `POST /feedback` store thumbs up/down for an interaction
- `GET /feedback/stats` simple aggregates
- `GET /feedback/list` recent feedback events for analytics UI

### Learning (Adaptive Prompts)
- `GET /learning/status` current overrides + feedback breakdown
- `POST /learning/recompute` generate per-mode overrides from recent feedback (privileged)
- `POST /learning/set_override` set a manual override for a mode (privileged)
- `POST /learning/reset` clear overrides (all or one mode) (privileged)

### Audit / Compliance
- `GET /audit/stats` counts by action over last N days
- `GET /audit/list` recent audit events (JSONL)

### Foundry (Self-Evolution)
- `GET /foundry/skills` list generated skills
- `POST /foundry/generate` generate a new skill
- `POST /foundry/run` run a generated skill
- `POST /foundry/analyze` analyze skill stats
- `POST /foundry/improve` improve a generated skill

### Agents (Multi-Agent Orchestration)
- `POST /agents/spawn` spawn a new agent
- `GET /agents/list` list agents
- `POST /agents/send` send a message to an agent
- `GET /agents/messages/{agent_id}` fetch recent messages

---

## Current Implementation State (As Of 2026-02-07)

### Phases 1-11
- Completed previously (foundation, cockpit/dashboard, ingest, knowledge tuning, UX, model integrations, agentic file commands, Foundry backend).

### Phase 12: Foundry Dashboard UI
- Implemented in dashboard code (Foundry tab with generate/list/run/analyze/improve).

### Phase 13: Streaming Responses
- Implemented (Engine `/ask` SSE + dashboard SSE consumer).

### Phase 14: Code Editor Integration
- Implemented (Monaco editor modal for the most recently read file; saves via `/files/write`).

### Phase 15: File Browser
- Implemented (Dashboard `Files` mode backed by `/files/list` + click-to-read).

### Phase 16: Terminal Emulator
- Implemented (Dashboard `Terminal` mode via xterm; Engine `/execute` supports SSE + `/execute/cancel`).
- Streaming `/execute` meta includes `pid`, and `/execute/cancel` accepts optional `pid` fallback for more reliable cancellation.

### Phase 17: Multi-Agent Orchestration
- Implemented in engine code (AgentPool + `/agents/*` endpoints).
- Implemented in dashboard code (Agents tab for spawn/list/messages/send).

### Phase 18: Skill Marketplace
- Baseline implemented in this repo (local-first `.kaizen` package format + installer tooling + local index).
- Implemented in engine code (`GET /marketplace/index`, `POST /skills/install`).
- Implemented in dashboard code (Marketplace tab to browse/install packages).

### Phase 19: MCP Server Integration
- Implemented (MCP tools + resources in `engine/mcp_server.py`).
- HTTP transport implemented in `engine/mcp_http_server.py` (default: `http://127.0.0.1:8791/mcp`).

### Phase 22 (Partial): Security Layer
- Implemented a minimal API key gate for privileged endpoints (disabled by default).
- Implemented append-only audit log JSONL at `memory_db_path/audit/audit.jsonl` for privileged actions.
- Implemented audit read endpoints (`/audit/stats`, `/audit/list`) and a dashboard Compliance tab.

### Verification / Testing
- Engine endpoint smoke suite (no external server needed): `C:\Users\thoma\.gemini\sovereign-engine\test_all_endpoints.py`
- Dashboard build check: run `npm run build` in `C:\Users\thoma\.gemini\sovereign-dashboard`
- Kaizen diagnostics: `python tools\kaizen_doctor.py` in `C:\Users\thoma\Documents\kaizen`

---

## Kaizen Marketplace (Local-First)

Implemented in this repo:
- Tool: `tools/kaizen_market.py`
- Skill: `skills/skill-marketplace/SKILL.md`
- Index: `marketplace/index.json`

Examples:
```powershell
python tools\kaizen_market.py list
python tools\kaizen_market.py install-index --name skill-marketplace --root .

# Diagnostics (engine/dashboard ports + key endpoints)
python tools\kaizen_doctor.py
```

---

## Quick Start

Engine:
```powershell
cd C:\Users\thoma\.gemini\sovereign-engine
.\.venv\Scripts\activate
python -m engine.server
```

MCP (separate process):
```powershell
cd C:\Users\thoma\.gemini\sovereign-engine
.\.venv\Scripts\activate
python -m engine.mcp_http_server
```

Dashboard:
```powershell
cd C:\Users\thoma\.gemini\sovereign-dashboard
npm run dev
```

---

## Notes

- Prefer running the engine with its venv interpreter (`C:\Users\thoma\.gemini\sovereign-engine\.venv\Scripts\python.exe`).
- If you see PowerShell profile execution-policy errors, run commands with `powershell -NoProfile` (it avoids loading a blocked profile script).
- Local-first stability: the system is designed for localhost usage. It is not production-hardened for internet exposure (minimal auth, permissive CORS, no TLS/reverse proxy config in this repo).
- Dependency caveat: vector embeddings and retrieval quality depend on Ollama being reachable at `settings.ollama_host`. If Ollama is down, ingest/search still run but may warn and degrade.

---

## Future Roadmap (Phases 19-26)

### Phase 19: MCP Server Integration
**Goal**: Turn Sovereign Kaizen into an MCP (Model Context Protocol) server
**Why**: Universal integration - Claude, Cursor, Copilot can all connect to Kaizen

**Status**: Implemented (see `engine/mcp_server.py`, `engine/mcp_http_server.py`).

**Tasks**:
1. Implement MCP protocol in `engine/mcp_server.py`
2. Expose memory, files, skills as MCP resources
3. Add `/mcp/*` endpoints for tool discovery
4. Test with Claude Desktop and Cursor

**Files**: `engine/mcp_server.py`, `engine/mcp_http_server.py`

---

### Phase 20: Home Automation Integration
**Goal**: Connect to smart home devices via Home Assistant
**Why**: AI-controlled smart home from your local agent

**Status**: Implemented (Kaizen skill + CLI tooling). Engine endpoints not required.

**Tasks**:
1. Create `skills/smart-home/SKILL.md`
2. Add Home Assistant REST API client
3. Add `/home/*` endpoints (lights, climate, scripts)
4. Create automation triggers

**Files**: `skills/smart-home/SKILL.md`, `tools/ha.py`

---

### Phase 21: Computer Use / GUI Automation
**Goal**: Let AI control desktop (click, type, screenshot, visual verification)
**Why**: Full desktop automation like Anthropic's computer use

**Status**: Implemented (engine `/computer/*` endpoints + dashboard Computer tab + Kaizen-local tooling).

**Tasks**:
1. Install `pyautogui` or `playwright`
2. Add `/computer/screenshot` endpoint
3. Add `/computer/click`, `/computer/type` endpoints
4. Implement visual element detection
5. Add safety confirmations for destructive actions

**Files**: `C:\Users\thoma\.gemini\sovereign-engine\engine\computer_use.py`, `C:\Users\thoma\.gemini\sovereign-engine\engine\server.py`, `C:\Users\thoma\.gemini\sovereign-dashboard\src\ComputerPanel.tsx`, `C:\Users\thoma\Documents\kaizen\tools\computer_use.py`

---

### Phase 22: Enterprise Security Layer
**Goal**: RBAC, audit logs, decision explainability
**Why**: Make Kaizen enterprise-ready and safe for production

**Tasks**:
1. Add user authentication (JWT or API keys)
2. Create role-based permissions (admin, developer, viewer)
3. Log all agent decisions with reasoning
4. Add compliance dashboard UI
5. Implement action approval workflows

**Files**: `engine/auth.py` (new), `engine/audit.py` (new), `dashboard/src/Compliance.tsx` (new)

---

### Phase 23: Voice Interface
**Goal**: Speak to Kaizen, hear responses
**Why**: Hands-free interaction

**Status**: Implemented (browser STT + local engine TTS; optional STT via whisper libs).

**Tasks**:
1. Integrate Whisper (speech-to-text) via local model or API
2. Add TTS (text-to-speech) - Coqui TTS or ElevenLabs
3. Implement wake word detection ("Hey Kaizen")
4. Add `/voice/listen` and `/voice/speak` endpoints
5. Create voice-first UI mode in dashboard

**Files**: `C:\\Users\\thoma\\.gemini\\sovereign-engine\\engine\\voice.py`, `C:\\Users\\thoma\\.gemini\\sovereign-dashboard\\src\\VoicePanel.tsx`

---

### Phase 24: Knowledge Graph Visualization
**Goal**: Interactive 3D graph of memory and concepts
**Why**: Visualize how knowledge connects

**Status**: Implemented (engine graph export endpoints + dashboard 3D view).

**Tasks**:
1. Install `react-force-graph-3d` in dashboard
2. Create `/graph/nodes` and `/graph/edges` endpoints
3. Build interactive 3D visualization component
4. Add click-to-explore and filter by topic/date
5. Export graph as PNG or JSON

**Files**: `C:\Users\thoma\.gemini\sovereign-dashboard\src\KnowledgeGraph.tsx`, `C:\Users\thoma\.gemini\sovereign-engine\engine\graph_export.py`

---

### Phase 25: Reinforcement Learning Loop
**Goal**: Agent learns and improves from user feedback
**Why**: Gets better over time based on actual usage

**Status**: Implemented (feedback + analytics UI + adaptive prompt overrides + learning UI).

**Tasks**:
1. Add thumbs up/down to all AI responses
2. Store feedback in memory with context
3. Analyze patterns (what works, what fails)
4. Adjust prompts/behavior based on feedback (adaptive prompt overrides; opt-in)
5. Create feedback analytics dashboard

**Files**: `C:\Users\thoma\.gemini\sovereign-engine\engine\database.py`, `C:\Users\thoma\.gemini\sovereign-engine\engine\server.py`, `C:\Users\thoma\.gemini\sovereign-dashboard\src\App.tsx`

---

### Phase 26: Mobile Companion App
**Goal**: React Native app for phone - Kaizen in your pocket
**Why**: Access AI assistant anywhere, push notifications

**Tasks**:
1. Create React Native project in `sovereign-mobile/`
2. Build mobile UI (chat, quick actions, voice)
3. Implement push notifications
4. Add offline sync with SQLite
5. Background tasks and widgets

**Files**: `sovereign-mobile/` (new project)

---

## Priority Order for Agents

| Priority | Phase | Impact | Difficulty |
|----------|-------|--------|------------|
| HIGH | 19 (MCP) | Universal AI integration | Medium |
| HIGH | 22 (Security) | Enterprise-ready | Medium |
| MEDIUM | 21 (Computer Use) | Desktop automation | High |
| MEDIUM | 23 (Voice) | Accessibility | Medium |
| MEDIUM | 24 (Graph Viz) | Understanding memory | Low |
| LOW | 25 (RL Loop) | Long-term improvement | High |
| LOW | 20 (Smart Home) | Niche use case | Low |
| LOW | 26 (Mobile) | Separate project | High |

---

Last Updated: 2026-02-07
