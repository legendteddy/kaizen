# Integration: OpenDevin

> **Kaizen Role**: The Driver's Manual
> **OpenDevin Role**: The Vehicle

OpenDevin provides the sandbox (browser, shell). Kaizen provides the instructions on *how* to use them safely and effectively.

## Implementation Strategy

OpenDevin uses a System Prompt file (often `prompts/system.md` or similar config). You can inject Kaizen skills directly into this configuration.

### Method 1: The "Universal" Injection (Recommended)

Add the contents of `UNIVERSAL_PROMPT.txt` to your agent's custom instructions settings.

### Method 2: Skill-Specific Guards

If you are building a specific agent (e.g., a "Researcher"), modify the agent's prompt to include the specific Kaizen protocols.

**Example: `agent_config.toml`**

```toml
[agent]
name = "KaizenResearcher"
model = "claude-3-5-sonnet"

[agent.prompts]
system = """
You are a Research Agent.

# ACTIVATED PROTOCOLS (KAIZEN)
{{ include 'skills/research-intelligence/SKILL.md' }}
{{ include 'skills/knowledge-synthesis/SKILL.md' }}

Follow the 'CRAG' (Corrective RAG) workflow defined in the protocols above.
"""
```

*(Note: Syntax depends on OpenDevin's specific template engine version)*
