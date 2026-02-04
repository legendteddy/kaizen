---
name: python-development
description: Python development standards, project structure, and type safety constraints.
---

# Protocol: Python Development

> "Explicit is better than implicit."

## Activation Trigger
- Writing Python modules.
- Refactoring Python code.
- Setting up new Python projects.

## Protocols

### 1. First Principle: Strictly Typed
Python is 3.12+. Use `type hints` everywhere. `mypy --strict` must pass.

### 2. Project Structure
```text
project/
├── src/
│   └── package/
│       ├── __init__.py
│       └── main.py
├── tests/
├── pyproject.toml
└── README.md
```

### 3. Modern Tooling
- **Lint**: `ruff check`
- **Format**: `ruff format`
- **Test**: `pytest`
- **Type**: `mypy`

## Code Patterns

### Robust Functions
```python
def process_data(items: list[str]) -> dict[str, int]:
    """Process items and return frequency."""
    return {x: items.count(x) for x in set(items)}
```

### Dataclasses over Dicts
```python
@dataclass(frozen=True)
class Config:
    host: str
    port: int = 8080
```

## Safety Guardrails
- **No Wildcard Imports**: `from module import *` is banned.
- **No Bare Except**: `except:` is banned. Catch specific exceptions.
- **No Print Debugging**: Use `logging` or `print()` only in `if __name__ == "__main__":`.
- **Dependency Locking**: Always have a `requirements.txt` or `poetry.lock`.
- **Complexity Limit**: Functions > 20 lines should be split.
