---
name: test-driven-development
description: The RED-GREEN-REFACTOR cycle and testing antipatterns.
---

# Test-Driven Development (TDD)

> "Write the test first, then make it pass."

## Activation Trigger
- Implementing complex logic.
- Fixing a bug (Reproduce first).
- Refactoring legacy code.

## Protocols

### 1. First Principle: Red-Green-Refactor
1. **Red**: Write a failing test.
2. **Green**: Write minimal code to pass.
3. **Refactor**: Clean up the code.

### 2. AAA Pattern
- **Arrange**: Setup state.
- **Act**: Call the function.
- **Assert**: Check results.

### 3. The Test Pyramid
Unit (70%) > Integration (20%) > E2E (10%).

## Code Patterns

### The Standard Test
```python
def test_login_success():
    # Arrange
    user = create_test_user("valid@example.com")
    
    # Act
    token = login(user.email, "password")
    
    # Assert
    assert token is not None
    assert token.starts_with("eyJ")
```

## Safety Guardrails
- **Test Behavior, Not Implementation**: Don't test private methods.
- **One Assert Per Concept**: Don't check 5 unrelated things in one test.
- **No Sleep**: Never use `time.sleep()` in tests. Use polling/await.
- **Isolate**: Tests must not depend on order or shared global state.
- **Speed**: Unit tests must run in milliseconds. If it hits DB, it's Integration.
