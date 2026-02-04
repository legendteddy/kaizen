---
name: expert-claude-code-user
description: Mastery over the Claude Code CLI, leveraging deep integration and plugins.
---

# Protocol: Expert Claude Code User (v1.0)

> "The CLI is the IDE of the future."

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

## 6. Advanced Plugin Ideas
Extending Claude Code with custom tools:
- **`mcp-server-git`**: Advanced manipulation of git history.
- **`mcp-server-brave`**: Web search integration for real-time docs.
- **`mcp-server-filesystem`**: Safer, sandboxed file operations.

## Self-Improvement
- **Did I use `ls` manually?** -> Use `/add .` next time.
- **Did I copy-paste code?** -> Use `/edit` to apply directly.

## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Professional Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Context Manager](../context-manager/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
