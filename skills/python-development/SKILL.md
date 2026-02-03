---
name: python-development
description: Skill for python-development tasks and workflows.
---

# Skill: Python Development (v1.0)

> Professional Python development patterns and best practices

## Purpose
Ensure Python code follows professional standards and modern patterns.

## Activation Trigger
- Writing Python scripts or modules
- Debugging Python code
- Python project setup

---

## Project Structure

```
project/
├── src/
│   └── package_name/
│       ├── __init__.py
│       ├── main.py
│       └── utils/
├── tests/
│   └── test_main.py
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Code Patterns

### Type Hints
```python
def process_data(items: list[str], count: int = 10) -> dict[str, int]:
    """Process items and return frequency dict."""
    return {item: items.count(item) for item in set(items[:count])}
```

### Dataclasses
```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Config:
    name: str
    debug: bool = False
    max_retries: int = 3
    timeout: Optional[float] = None
```

### Context Managers
```python
from contextlib import contextmanager

@contextmanager
def managed_resource(name: str):
    resource = acquire_resource(name)
    try:
        yield resource
    finally:
        release_resource(resource)
```

### Error Handling
```python
class AppError(Exception):
    """Base exception for application."""
    pass

class ValidationError(AppError):
    """Raised when validation fails."""
    pass

def validate(data: dict) -> None:
    if not data.get("required_field"):
        raise ValidationError("Missing required_field")
```

---

## Best Practices

| Practice | Description |
|:---|:---|
| Use pathlib | `Path` over string paths |
| Use f-strings | `f"{var}"` over `.format()` |
| Use enumerate | `for i, item in enumerate(lst)` |
| Use comprehensions | List/dict/set comprehensions |
| Use walrus operator | `if (n := len(data)) > 10:` |

---

## Testing Pattern

```python
import pytest

def test_process_data():
    result = process_data(["a", "b", "a"], count=3)
    assert result == {"a": 2, "b": 1}

def test_process_data_empty():
    result = process_data([])
    assert result == {}

@pytest.fixture
def sample_config():
    return Config(name="test", debug=True)
```

---

## Tooling Configuration (`pyproject.toml`)

Enforce quality with Ruff.

```toml
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"] # Pycodestyle, Pyflakes, Isort, Pyupgrade, Bugbear
```

---

## Protocol: Implementation Workflow

1.  **Draft**: Write working code first.
2.  **Type**: Add `mypy` compatible hints.
3.  **Lint**: Run `ruff check --fix .`.
4.  **Format**: Run `ruff format .`.
5.  **Test**: Write at least one `pytest` case for happy path.

---

## Anti-Patterns

| Pattern | Why it's bad | Fix |
|:---|:---|:---|
| `from module import *` | Pollutes namespace, hard to trace | Import specific names |
| `except Exception:` | Catches Ctrl-C and SystemExit | `except Exception as e:` |
| `print()` debugging | Clutters stdout | Use `logging` or `rich` |

---

## Common Libraries

| Purpose | Library |
|:---|:---|
| HTTP requests | `httpx` or `requests` |
| CLI | `typer` or `click` |
| Data validation | `pydantic` |
| Async | `asyncio` |
| Testing | `pytest` |
| Linting | `ruff` |



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
- [Fastapi Expert](../fastapi-expert/SKILL.md)
