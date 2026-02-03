---
name: precision-coder
description: Elite coding standards with zero-bug tolerance, type safety enforcement, security-first development, and comprehensive code review checklists.
---

# Precision Coder — Elite Engineering Standards

This skill enforces **production-grade code quality**. Every line you write should be deployable.

---

## 1. The Zero-Bug Mindset

### Before Writing Any Code
1. **Understand** the requirement completely
2. **Identify** edge cases upfront
3. **Plan** error handling strategy
4. **Consider** security implications

### The 4-Check Rule
Every code block must pass:
- [ ] **Compiles** — No syntax errors
- [ ] **Runs** — No runtime exceptions on happy path
- [ ] **Handles errors** — Graceful failure on edge cases
- [ ] **Secure** — No obvious vulnerabilities

---

## 2. Type Safety Enforcement

### TypeScript
```typescript
// ❌ NEVER
const data: any = fetchData();
const value = obj.prop; // might be undefined

// ✅ ALWAYS
interface UserData {
  id: string;
  name: string;
  email?: string;  // Optional explicitly marked
}
const data: UserData = await fetchData();
const value = obj?.prop ?? defaultValue;
```

### Python
```python
# ❌ NEVER
def process(data):
    return data['value']

# ✅ ALWAYS
from typing import TypedDict, Optional

class DataPayload(TypedDict):
    value: str
    metadata: Optional[dict]

def process(data: DataPayload) -> str:
    return data.get('value', '')
```

### Rust
```rust
// ❌ NEVER
let value = some_option.unwrap();

// ✅ ALWAYS
let value = some_option.unwrap_or_default();
// OR
let value = match some_option {
    Some(v) => v,
    None => return Err(MyError::MissingValue),
};
```

---

## 3. Security-First Development

### Input Validation
```javascript
// ❌ NEVER trust user input
element.innerHTML = userInput;
db.query(`SELECT * FROM users WHERE id = ${userId}`);

// ✅ ALWAYS sanitize
element.textContent = userInput;  // Auto-escapes
element.innerHTML = escapeHtml(userInput);  // Explicit escape
db.query('SELECT * FROM users WHERE id = ?', [userId]);  // Parameterized
```

### Secret Management
```javascript
// ❌ NEVER
const API_KEY = "sk-abc123...";
console.log("Auth token:", token);

// ✅ ALWAYS
const API_KEY = process.env.API_KEY;
console.log("Auth token:", "[REDACTED]");
```

### OWASP Top 10 Awareness
| Vulnerability | Prevention |
|---------------|------------|
| Injection | Parameterized queries |
| XSS | Escape output, CSP headers |
| CSRF | Token validation |
| Auth bypass | Server-side validation |

---

## 4. Error Handling Patterns

### The Error Hierarchy
```
1. Prevent errors     (validation, type safety)
2. Handle expected    (try/catch, Result types)
3. Log unexpected     (structured logging)
4. Fail gracefully    (user-friendly messages)
```

### JavaScript/TypeScript
```typescript
// Structured error handling
try {
  const result = await riskyOperation();
  return { success: true, data: result };
} catch (error) {
  console.error('[RiskyOp] Failed:', {
    error: error.message,
    stack: error.stack,
    context: { userId, operation }
  });
  return { success: false, error: 'Operation failed. Please try again.' };
}
```

### Rust
```rust
// Use Result, not panic
fn process_file(path: &str) -> Result<Data, ProcessError> {
    let content = std::fs::read_to_string(path)
        .map_err(|e| ProcessError::ReadFailed(e))?;
    
    parse_content(&content)
        .map_err(|e| ProcessError::ParseFailed(e))
}
```

---

## 5. Naming Conventions (Enforced)

### Variables & Functions
| Pattern | Example | Use For |
|---------|---------|---------|
| `is_*`, `has_*`, `can_*` | `is_active`, `has_permission` | Booleans |
| `get_*`, `fetch_*` | `get_user`, `fetch_data` | Data retrieval |
| `set_*`, `update_*` | `set_config`, `update_status` | Data mutation |
| `handle_*`, `on_*` | `handle_click`, `on_submit` | Event handlers |
| `*_count`, `*_total` | `user_count`, `order_total` | Numeric aggregates |

### Function Size
- Keep functions small and focused (<20 lines preferred)
- One function = One purpose
- Use early returns (guard clauses) to reduce nesting

### Files & Modules
| Type | Convention | Example |
|------|------------|---------|
| Component | `PascalCase` | `UserProfile.tsx` |
| Utility | `kebab-case` | `string-helpers.ts` |
| Test | `*.test.*`, `*.spec.*` | `auth.test.ts` |
| Config | `*.config.*` | `eslint.config.js` |

---

## 6. Code Structure Patterns

### Single Responsibility
```javascript
// ❌ One function doing too much
function handleUserLogin(email, password) {
  // validate, authenticate, log, send email, update DB...
}

// ✅ Single responsibility
function validateCredentials(email, password) { ... }
function authenticateUser(credentials) { ... }
function logLoginAttempt(userId, success) { ... }
function sendWelcomeEmail(user) { ... }
```

### Early Returns
```javascript
// ❌ Deep nesting
function processOrder(order) {
  if (order) {
    if (order.items) {
      if (order.items.length > 0) {
        // deep logic here
      }
    }
  }
}

// ✅ Guard clauses
function processOrder(order) {
  if (!order) return { error: 'No order' };
  if (!order.items?.length) return { error: 'Empty order' };
  
  // clean logic here
}
```

---

## 7. Performance Awareness

### Common Pitfalls
```javascript
// ❌ N+1 queries
for (const user of users) {
  const orders = await db.getOrdersForUser(user.id);  // ❌
}

// ✅ Batch fetch
const userIds = users.map(u => u.id);
const orders = await db.getOrdersForUsers(userIds);  // ✅
```

### Memory Leaks
```javascript
// ❌ Forgotten cleanup
useEffect(() => {
  const interval = setInterval(doThing, 1000);
  // No cleanup!
});

// ✅ Proper cleanup
useEffect(() => {
  const interval = setInterval(doThing, 1000);
  return () => clearInterval(interval);
}, []);
```

---

## 8. Test-Driven Mindset

### Before Implementing
Ask: "How will I verify this works?"

### Test Structure (AAA)
```javascript
describe('calculateTotal', () => {
  it('should sum items correctly', () => {
    // Arrange
    const items = [{ price: 10 }, { price: 20 }];
    
    // Act
    const result = calculateTotal(items);
    
    // Assert
    expect(result).toBe(30);
  });
});
```

### Coverage Priorities
1. **Critical paths** — Authentication, payments
2. **Edge cases** — Empty arrays, null inputs
3. **Error handling** — Exception scenarios
4. **Integration points** — API calls, DB queries

---

## 9. Code Review Checklist

Before submitting any code, verify against all quality dimensions:

### Critical Checks
- [ ] Types are explicit (no `any`)
- [ ] Errors are handled gracefully
- [ ] User input is validated/sanitized
- [ ] No secrets or credentials in code
- [ ] No debug code left (console.log, debuggers)

### Code Structure
- [ ] Variable names are descriptive
- [ ] Functions are single-purpose (<20 lines preferred)
- [ ] No code duplication (DRY principle)
- [ ] Edge cases are covered
- [ ] Performance implications considered

### Architecture & Design
- [ ] SOLID principles followed
- [ ] Separation of concerns maintained
- [ ] Dependencies flow correctly (no circular imports)
- [ ] Implementation matches original plan
- [ ] All requirements addressed (no scope creep)

### Security & Safety
- [ ] No injection vulnerabilities (parameterized queries)
- [ ] Output properly escaped (XSS prevention)
- [ ] Authentication/authorization server-side validated
- [ ] CSRF tokens where needed

### Documentation
- [ ] Complex logic is commented
- [ ] Public APIs are documented
- [ ] Edge cases and assumptions noted
- [ ] Source cited for external solutions

---

*"Write code like the next maintainer is a violent psychopath who knows where you live."*
