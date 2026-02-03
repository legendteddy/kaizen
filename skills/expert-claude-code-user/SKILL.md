---
name: expert-claude-code-user
description: Mastery over the Claude Code CLI, leveraging deep integration and plugins.
---

# Skill: Expert Claude Code User (v1.0)

## Purpose
Maximize the capabilities of the `claude` CLI tool for terminal-based workflow automation.

## Activation Trigger
- User is using `claude` CLI.
- Questions about `/slash` commands or configuration.

---

## Protocol: Power User Workflow

### 1. Context Management
- **Add files:** `/add src/` (Adds generic context)
- **Compact:** `/compact` (Clears conversation history but keeps file context)
- **Reset:** `/clear` (Nuke everything)

### 2. Plugin Management
- **List:** `/plugin list`
- **Install:** `/plugin install <name>`
- **Marketplace:** `/plugin marketplace search <query>`

### 3. Execution Patterns
- **Bash:** Claude can run bash commands.
    - *Prompt:* "Run ls -la and tell me what is wrong."
- **Files:** Claude can edit files directly.
    - *Prompt:* "Refactor app.py to use FastAPI."

---

## Protocol: The "MCP" Advantage

Claude Code supports **Model Context Protocol (MCP)** servers.

**Connecting a Database:**
1.  Install MCP server: `npm install -g mcp-server-postgres`
2.  Configure `claude_config.json`:
    ```json
    {
      "mcpServers": {
        "postgres": {
          "command": "mcp-server-postgres",
          "args": ["postgresql://user:pass@localhost/db"]
        }
      }
    }
    ```
3.  **Result:** Claude can now query your DB directly.

---

## Troubleshooting

| Issue | Fix |
|:---|:---|
| "Context full" | Run `/compact` immediately. |
| "I can't run commands" | Check permissions (`claude --approve-tools`). |
| "Hallucinating files" | Run `/add <filename>` to ground it. |