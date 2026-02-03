---
name: clean-code-python
description: Enforces Pythonic standards, PEP 8, and Uncle Bob's Clean Code principles.
---

# Clean Code Python
Enforces Pythonic standards, PEP 8, and Uncle Bob's Clean Code principles.

## Instructions
- **Naming:**
  - Variables = Nouns (`user_list`, not `get_users`).
  - Functions = Verbs (`calculate_total`, not `total_calculation`).
  - Classes = PascalCase (`UserManager`).
- **Functions:** Keep them small (<20 lines preferred). One function = One purpose.
- **Typing:** Strict Type Hints (`def func(a: int) -> str:`). No `Any` unless absolutely necessary.
- **Docstrings:** Required for all public modules, classes, and complex functions.
- **Control Flow:** Avoid deep nesting. Return early (Guard Clauses) instead of big `else` blocks.

## Capabilities
- Can audit code for cyclomatic complexity.
- Can refactor monolithic functions into smaller helpers.
- Can add type hints to legacy code.