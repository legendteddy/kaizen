---
name: structured-output
description: Enforcing JSON/XML formats via Pydantic, Zod, and Grammar Constrained Generation.
---

# Structured Output

> "If it's not JSON, it didn't happen."

## Activation Trigger
- Generating machine-readable data (JSON/XML).
- Interfacing with APIs or databases.
- Enforcing schema validation (Pydantic/Zod).

## 1. The Pydantic Protocol (Python)
Don't ask for "JSON". Ask for a "Pydantic Schema".

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., description="Full name")
    age: int = Field(..., gt=0, lt=150)
    tags: list[str]

# Prompt
prompt = f"Extract user info. Schema: {User.model_json_schema()}"
```

## 2. The Zod Protocol (TypeScript)
For JS/TS agents.
```typescript
const UserSchema = z.object({
  name: z.string(),
  email: z.string().email(),
});
```

## 3. Techniques for Robustness

### Option A: Schema-Constrained Decoding (Grammar)
*Best for local LLMs (Llama.cpp, Ollama).*
- Force the LLM to output ONLY tokens that fit the grammar.
- **Result:** 100% Valid JSON. Zero syntax errors.

### Option B: The "Retry Healer" Loop
*Best for cloud APIs (Claude, GPT).*

```python
for attempt in range(3):
    try:
        response = llm.generate()
        json_obj = json.loads(response)
        User.model_validate(json_obj)
        return json_obj
    except ValidationError as e:
        # FEED THE ERROR BACK
        prompt += f"\n\nError: {e}\nFix your JSON."
```

## 4. Format Selection Strategy

| Format | When to use |
|:---|:---|
| **JSON** | Complex data, APIs, Databases. |
| **XML** | Large document extraction (LLMs parse tags better than JSON brackets). |
| **YAML** | Config files, human-readable lists. |
| **Markdown Table** | Comparison data for humans. |

## 5. Anti-Patterns
- **Do NOT** ask for JSON without a schema.
- **Do NOT** mix JSON with Markdown text ("Here is the JSON: ```json...").
  - *Fix:* Use `response_format={"type": "json_object"}`.


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Prompt Architect](../prompt-architect/SKILL.md)
- [Context Manager](../context-manager/SKILL.md)
- [Ambiguity Handling](../ambiguity-handling/SKILL.md)
