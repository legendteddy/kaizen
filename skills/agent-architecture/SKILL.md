---
name: agent-architecture
description: Skill for designing robust agentic systems (Router, Worker, Evaluator patterns).
---

# Agent Architecture

> "Structure determines function."

## Activation Trigger
- Designing a new multi-agent system.
- Routing logic is becoming complex.
- Need to parallelize tasks (Swarm).

## Visual Map

```mermaid
graph TD
    User([User]) --> Router{Router Agent}
    
    Router -->|Coding| Worker1[Coder Agent]
    Router -->|Research| Worker2[Research Agent]
    Router -->|General| Worker3[Chat Agent]
    
    Worker1 --> Evaluator{Evaluator}
    Evaluator -->|Reject| Worker1
    Evaluator -->|Approve| Output([Final Output])
    
    Worker2 --> Output
    Worker3 --> Output
```

## Protocol: The Core Patterns

### 1. Router Pattern (The Switchboard)
**Use when:** One input, multiple potential handlers.

```mermaid
sequenceDiagram
    participant User
    participant Router
    participant SQL
    participant Search
    
    User->>Router: "What was Q3 revenue?"
    Router->>Router: Classify -> SQL
    Router->>SQL: Execute Query
    SQL->>Router: Result
    Router->>User: "Q3 Revenue was $1M"
```

### 2. Worker Swarm (The Parallel Process)
**Use when:** Massive parallelizable tasks (Map-Reduce).

```python
# Swarm Logic
with ThreadPoolExecutor() as executor:
    futures = [executor.submit(research_agent.run, c) for c in companies]
    results = [f.result() for f in futures]
aggregator_agent.summarize(results)
```

### 3. Evaluator-Optimizer (The Loop)
**Use when:** Quality > Speed.

```mermaid
stateDiagram-v2
    [*] --> Generate
    Generate --> Critique
    Critique --> [*]: Pass
    Critique --> Generate: Fail (Feedback)
```

## Architecture Checklist
- [ ] **State Management:** Redis/Memory/File?
- [ ] **Loop Prevention:** `max_turns` limit?
- [ ] **Tool Sandboxing:** Docker/e2b?
- [ ] **Observability:** LangSmith/Phoenix traces?

## Self-Repair Protocol
When the architecture fails:
- **Bottleneck:** If Router is slow -> Switch to Swarm (Parallel).
- **Hallucination:** If Worker lies -> Add Evaluator (Verification).
- **Looping:** If Agents argue -> Add "Boss" (Conflict Resolution).


## Related Skills
- [Sovereign Identity](../sovereign-identity/SKILL.md)
- [Agent Communication](../agent-communication/SKILL.md)
- [Agent Cowork](../agent-cowork/SKILL.md)
- [Agent Security](../agent-security/SKILL.md)
