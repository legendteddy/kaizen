---
name: structured-output
description: Constrained generation techniques for reliable JSON output from LLMs.
---

# Structured Output (v1.0)

> Guaranteed valid JSON from LLMs using constrained generation

## Purpose
Ensure LLM outputs are valid, parseable structured data.

## Activation Trigger
- API integration needs
- Database operations
- Tool/function calling

---

## Techniques

### 1. Prompt Engineering
- Specify exact JSON schema in prompt
- Include examples for few-shot learning

### 2. Constrained Decoding
```
Standard:   Any token possible at each step
Constrained: Only valid tokens per schema
```
- Uses FSM (Finite State Machine)
- Logit masking: Invalid tokens → 0 probability
- 100% schema compliance guaranteed

### 3. Schema-Guided Generation
- Define structure with JSON Schema
- Integrate with Pydantic models
- Validate at generation time

---

## API Parameters (vLLM/Fireworks)

| Param | Purpose |
|:---|:---|
| `choice` | One of predefined options |
| `regex` | Match regex pattern |
| `json` | Follow JSON schema |
| `grammar` | Context-free grammar |

---

## Benefits

- ✅ No parsing errors
- ✅ No schema violations
- ✅ No wrong data types
- ✅ No free-form drift

---

## 2026 Trends

### Generative UI (GenUI)
- AI generates UI at runtime
- JSON describes components
- Adapts to user context

---

## For Sovereign Framework

Structured output enables:
- Tool calling reliability
- API integration
- Database operations
- Configuration generation
