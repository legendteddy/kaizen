---
name: agent-architecture
description: Skill for designing robust agentic systems (Router, Worker, Evaluator patterns).
---

# Skill: Agent Architecture (v1.0)

> "Structure determines function."

## Purpose
Design and implement robust multi-agent architectures using proven patterns like Router-Gateway, Worker-Swarm, and Evaluator-Optimizer.

## Activation Trigger
- User asks to "design an agent system."
- Tasks involving "multiple agents" or "orchestration."
- Debugging complex agent interactions.

---

## Protocol: The Core Patterns

### 1. Router Pattern (The Switchboard)
**Use when:** You have one input that could go to many different tools.

```python
# Router Logic
def route_request(user_input: str) -> str:
    classification = classifier_agent.predict(user_input)
    if classification == "SQL":
        return sql_agent.run(user_input)
    elif classification == "Search":
        return search_agent.run(user_input)
    else:
        return chat_agent.run(user_input)
```

### 2. Worker Swarm (The Parallel Process)
**Use when:** You have a massive task that can be split (e.g., "Research 50 companies").

```python
# Swarm Logic
def run_swarm(companies: list[str]):
    results = []
    # Parallel execution
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(research_agent.run, c) for c in companies]
        for future in as_completed(futures):
            results.append(future.result())
    return aggregator_agent.summarize(results)
```

### 3. Evaluator-Optimizer (The Loop)
**Use when:** Quality is more important than speed (e.g., generating code).

```python
# Self-Correction Logic
def generate_high_quality_code(spec: str):
    code = coder_agent.write(spec)
    for _ in range(3): # Max 3 retries
        critique = reviewer_agent.review(code)
        if critique.is_pass:
            return code
        code = coder_agent.fix(code, critique.feedback)
    return code # Or raise error
```

---

## Architecture Checklist

- [ ] **State Management:** Where is the conversation history stored? (Redis/Memory/File)
- [ ] **Loop Prevention:** Is there a `max_turns` limit?
- [ ] **Tool Sandboxing:** Are shell commands running in Docker?
- [ ] **Observability:** Are trace logs (LangSmith/Phoenix) enabled?