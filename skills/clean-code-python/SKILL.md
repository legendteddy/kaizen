---
name: clean-code-python
description: Skill for clean-code-python tasks and workflows.
---

# Skill: Clean Code Python (v1.0)

> "Code is read much more often than it is written." — Guido van Rossum

## Purpose
Ensure all Python code written by the agent is idiomatic, maintainable, and type-safe.

## Activation Trigger
- Writing new Python scripts
- Refactoring existing Python code
- Code reviews

---

## Protocol: The Standards

### 1. Modern Typing (Python 3.10+)
**Rule:** Use `Type hints` for all function arguments and return values.

```python
# ❌ Old/Bad
def process(items):
    return [i * 2 for i in items]

# ✅ Modern/Good
def process(items: list[int]) -> list[int]:
    """Double the value of each item in the list."""
    return [i * 2 for i in items]
```

### 2. Project Structure
**Rule:** Always use a standard layout.

```
project/
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── pyproject.toml
└── README.md
```

### 3. Tooling Configuration (`pyproject.toml`)
**Rule:** Enforce quality with Ruff (Fastest linter).

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
