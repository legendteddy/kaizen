---
name: mcp-protocol
description: Skill for mcp-protocol tasks and workflows.
---

# Skill: Model Context Protocol (MCP) (v1.0)

> Universal tool integration standard for AI agents

## Purpose
Understand and implement MCP for connecting AI to external tools and data.

## Activation Trigger
- Tool integration tasks
- External API connections
- Building AI agent infrastructure

---

## What is MCP?

**Model Context Protocol** = Open standard for AI-tool connectivity.

Created by Anthropic, now industry standard (OpenAI, Google, Microsoft).

```
┌─────────────────────────────────────────────────────────────────┐
│                       AI HOST (Client)                          │
│                   (e.g., Claude Desktop)                        │
├─────────────────────────────────────────────────────────────────┤
│                           ↕                                      │
│                    JSON-RPC Interface                            │
│                           ↕                                      │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐        │
│  │ MCP      │  │ MCP      │  │ MCP      │  │ MCP      │        │
│  │ Server   │  │ Server   │  │ Server   │  │ Server   │        │
│  │ (Files)  │  │ (GitHub) │  │ (Slack)  │  │ (Custom) │        │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘        │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core Components

### 1. Hosts (Clients)
AI applications that initiate connections:
- Claude Desktop
- VS Code with AI
- Custom AI agents

### 2. Servers
Expose tools, resources, prompts:
- File system access
- Database connections
- API integrations

### 3. Protocol Layer
JSON-RPC 2.0 communication:
- Request/response patterns
- Notifications
- Bidirectional messages

---

## Key Features

### Universal Connectivity
- Files, databases, APIs
- Real-time data access
- Reduce hallucinations

### Security by Design
- Sandboxed servers
- Granular permissions
- Audit logging
- Trust boundaries

### Bidirectional (2026)
- Servers can request LLM completions
- "Sampling" feature
- Dynamic interactions

---

## MCP Primitives

### Tools
Functions the AI can call:
```json
{
  "name": "search_files",
  "description": "Search for files matching pattern",
  "parameters": {
    "pattern": "string",
    "directory": "string"
  }
}
```

### Resources
Data sources the AI can read:
```json
{
  "uri": "file:///workspace/data.json",
  "mimeType": "application/json"
}
```

### Prompts
Pre-defined context templates:
```json
{
  "name": "code_review",
  "description": "Review code for quality issues"
}
```

---

## For Sovereign Framework

MCP enables:
1. **External tool access**: Connect to any API
2. **File system operations**: Read/write with permissions
3. **Database queries**: Secure data access
4. **Standardization**: One protocol, many tools



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
