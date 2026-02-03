---
name: test-driven-development
description: RED-GREEN-REFACTOR cycle with testing best practices and anti-patterns.
---

# Test-Driven Development (TDD)

> Write the test first, then make it pass.

## Activation Trigger
- Starting a new feature implementation.
- Refactoring legacy code (needs safety net).
- Designing test suites (Unit vs Integration).

## The Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│                    RED → GREEN → REFACTOR                       │
│                                                                 │
│  1. RED      → Write a failing test                            │
│  2. GREEN    → Write minimal code to pass                      │
│  3. REFACTOR → Clean up while keeping tests green              │
│  4. REPEAT   → Next test case                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Test Structure

### Arrange-Act-Assert (AAA)
```python
def test_user_login():
    # Arrange
    user = User(email="test@example.com", password="secret")
    
    # Act
    result = auth_service.login(user.email, "secret")
    
    # Assert
    assert result.success == True
    assert result.token is not None
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Problem | Fix |
|:---|:---|:---|
| Testing implementation | Brittle tests | Test behavior |
| Giant test functions | Hard to debug | One assertion per test |
| No edge cases | Bugs slip through | Test boundaries |
| Mocking everything | False confidence | Integration tests |
| Skipping REFACTOR | Tech debt | Always clean up |

---

## When to Write Tests

### Always Test
- Business logic
- Edge cases
- Error handling
- API contracts

### Consider Skipping
- Simple getters/setters
- Framework code
- One-off scripts

---

## Test Pyramid

```
        /\
       /  \      E2E (few)
      /----\
     /      \    Integration (some)
    /--------\
   /          \  Unit (many)
  /____________\
```

Most tests should be unit tests. Few E2E tests.
