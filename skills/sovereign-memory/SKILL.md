# Sovereign Memory Integration

## Description
Protocol for using the Sovereign Memory Engine — a local GraphRAG-powered persistent memory system.

## Prerequisites
- Memory engine running: `python -m engine.server` (port 8787)
- Or MCP server configured in your AI tool

## When to Use Memory

### SAVE when:
- User teaches you something project-specific
- You discover a bug/solution pattern
- You learn user preferences
- Important architectural decisions are made

### SEARCH when:
- Query references "last time", "before", "previously"
- User asks about past projects/conversations
- You need context about recurring patterns
- Debugging a familiar-sounding issue

## MCP Tools

```
memory_save(content, memory_type, source)
memory_search(query, limit)  
memory_reflect(topic)
```

## HTTP API

```bash
# Save
curl -X POST http://localhost:8787/ingest \
  -d '{"content": "...", "memory_type": "semantic"}'

# Search
curl -X POST http://localhost:8787/search \
  -d '{"query": "...", "limit": 5}'
```

## Memory Types

| Type | Use For |
|------|---------|
| `episodic` | Full conversation snapshots |
| `semantic` | Facts, concepts, decisions |
| `procedural` | Code patterns, how-tos |

## Quality Signal

The engine returns a `crag_score` (0-1):
- **> 0.7**: High confidence results
- **0.5-0.7**: Use with caution
- **< 0.5**: Fallback triggered (results unreliable)
