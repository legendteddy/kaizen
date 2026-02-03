---
name: claude-architecture
description: Skill for claude-architecture tasks and workflows.
---

# Skill: Claude Code Architecture (v1.0)

> Extracted from `CLAUDE_INTERNAL_ARCHITECTURE.md` - Reverse-engineered Claude Code CLI v2.1.19

## Purpose
Understanding Claude Code's internal architecture enables this agent to match or exceed its capabilities.

## Activation Trigger
- Designing multi-agent systems
- Implementing agentic workflows
- Understanding competitor architecture

---

## 1. Core Runtime Architecture

### The Brain (Multi-Model Orchestration)
Claude Code uses hybrid intelligence with dynamic routing:
- **Reasoning**: Uses `deepseek-reasoner` for complex logic and planning
- **Code/Chat**: Uses Anthropic models (Sonnet/Haiku) for standard interaction

### Agentic Recursion
- Main Agent spawns Sub-Agents for specific tasks
- Sub-agents run in isolated contexts
- Prevents context pollution in main window

---

## 2. Memory Palace (3-Tier State)

| Tier | Storage | Purpose |
|:---|:---|:---|
| **Hot** | Session JSONL | Every thought, tool call, file snapshot |
| **Warm** | Project Registry | Links sessions to directory paths |
| **Cold** | Task Persistence | JSON state machine for crash recovery |

---

## 3. Superpowers (Encoded Skills)

### Systematic Debugging
1. Observe symptom
2. Find immediate cause
3. Trace upstream ("Who called this?")
4. Find original trigger
5. Defense in depth (validate at every layer)

### Code Reviewer Persona
1. Plan Alignment: Compare implementation to architecture
2. Code Quality: Patterns, error handling, type safety
3. Architecture: SOLID principles
4. Documentation: Comments and headers

### Other Key Skills
| Skill | Logic |
|:---|:---|
| `verification-before-completion` | Always verify before marking Done |
| `subagent-driven-development` | Break large tasks into sub-agent workloads |
| `writing-plans` | Create markdown plans before coding |
| `test-driven-development` | Write test before implementation |

---

## 4. Psychological Protocols (Cialdini's Principles)

| Principle | Application |
|:---|:---|
| Authority | "YOU MUST" language for safety rules |
| Commitment | Force explicit skill announcement |
| Scarcity | "IMMEDIATELY" triggers for verification |
| Social Proof | Frame errors as universal failures |
| Unity | "We are colleagues" for collaboration |

---

## 5. Assimilation for Gemini

1. **Task State**: Always maintain "Current Objective" status
2. **Enforce Verification**: Never assume a fix works
3. **Use Sub-Agents**: Delegate broad analysis
4. **Respect the Plan**: Always update the Master Plan

