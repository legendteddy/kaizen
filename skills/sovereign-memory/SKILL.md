# Sovereign Memory Integration

---
description: Protocol for using the Sovereign Memory Engine (GraphRAG + CRAG)
---

## 🏗️ System Blueprint

**Location**: `Documents\sovereign-memory\`
**Architecture**: Hybrid GraphRAG + Vector Search + CRAG Quality Control

```
┌─────────────────────────────────────────────────────────────┐
│              SOVEREIGN MEMORY ENGINE                        │
│   ┌───────────┐   ┌───────────┐   ┌───────────────────┐     │
│   │  MCP      │   │  REST API │   │  CRAG + Self-RAG  │     │
│   │  Server   │   │  :8787    │   │  Quality Control  │     │
│   └───────────┘   └───────────┘   └───────────────────┘     │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Dependencies

The engine requires the following stack to be active:

| Component | Technology | Requirement |
|-----------|------------|-------------|
| **Runtime** | Python 3.10+ | `uvicorn`, `fastapi` |
| **Vectors** | ChromaDB | Local persistence |
| **Embeddings** | Ollama | `ollama pull nomic-embed-text` |
| **Self-RAG** | Ollama | `ollama pull llama3.2` (optional) |
| **Graph** | NetworkX | In-memory graph processing |

## 🚀 Usage Protocol

### 1. Prerequisites
Ensure the engine is running before making calls:
```powershell
cd Documents\sovereign-memory
.\.venv\Scripts\Activate.ps1
python -m engine.server
```

### 2. When to Use Memory

| Context | Action | Why? |
|---------|--------|------|
| **Bug Fix** | `memory_save` | Record the fix for future regressions |
| **New Project** | `memory_save` | Store architectural decisions |
| **"Recall..."** | `memory_search` | User asks about past context |
| **Debugging** | `memory_search` | Check if this error was solved before |

### 3. MCP Tools (Native)

For Cursor, Cline, and Claude:

```typescript
// Save important context
await use_mcp_tool("sovereign-memory", "memory_save", {
  content: "Fixed footer scroll bug by globalizing .whatsapp-float CSS",
  memory_type: "semantic", // or "procedural" for code patterns
  source: "task_123"
});

// Recall past solutions
const result = await use_mcp_tool("sovereign-memory", "memory_search", {
  query: "how to fix footer scroll bug",
  limit: 3
});
```

### 4. HTTP API (Universal)

For generic scripts or CLI tools:

```bash
# Save
curl -X POST http://localhost:8787/ingest \
  -H "Content-Type: application/json" \
  -d '{"content": "...", "memory_type": "semantic"}'

# Search
curl -X POST http://localhost:8787/search \
  -H "Content-Type: application/json" \
  -d '{"query": "...", "limit": 5}'
```

## 🧠 Quality Signals (CRAG)

The engine returns a `crag_score` (0.0 - 1.0) with every search.

- **> 0.7 (High)**: Use results directly.
- **0.5 - 0.7 (Medium)**: Use with caution, verify against current context.
- **< 0.5 (Low)**: **IGNORE RESULTS**. Trigger fallback (web search or ask user).
