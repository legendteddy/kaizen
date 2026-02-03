---
name: debug-master
description: Advanced debugging methodology with 4-phase root cause analysis, stack trace interpretation, and systematic problem isolation.
---

# Debug Master — Systematic Problem Solving

This skill provides a **battle-tested debugging methodology**. When bugs appear, you don't guess—you investigate.

## Activation Trigger
- Encountering a runtime error or bug.
- Need to isolate a root cause.
- Analyzing stack traces.

---

## 1. The 4-Phase Debugging Protocol

```
TRACE → ISOLATE → FIX → VERIFY
```

Every debugging session follows this exact sequence.

---

## 2. Phase 1: TRACE

### Objective
Gather evidence. Don't touch code yet.

### Information Collection
```xml
<thinking>
## Bug Report
- **Symptom**: What exactly is happening?
- **Expected**: What should happen instead?
- **Trigger**: What action causes this?
- **Frequency**: Always, sometimes, or random?

## Environment
- OS/Platform: [Windows/Mac/Linux]
- Runtime: [Node version, Python version, etc.]
- Dependencies: [Any recent updates?]

## Evidence
- Error message: [exact text]
- Stack trace: [key frames]
- Logs: [relevant entries]
- Screenshots: [if UI issue]
</thinking>
```

### Stack Trace Reading
```
Stack trace anatomy:

Error: Cannot read property 'id' of undefined    ← Error type + message
    at getUserId (user.js:45:12)                 ← ACTUAL ERROR (top)
    at processRequest (handler.js:23:8)          ← Caller
    at Router.handle (express/router.js:174:12)  ← Framework code
    at Layer.handle (express/layer.js:95:5)      ← Framework code
```

**Rules**:
1. **Top frame** = Where error occurred
2. **Your code** = First frames with your file paths
3. **Framework code** = Usually not the problem
4. **Line:Column** = Exact location (e.g., `45:12`)

---

## 3. Phase 2: ISOLATE

### Objective
Find the **minimal reproduction**. Strip away everything unnecessary.

### Isolation Techniques

#### Binary Search
```
If the bug happens somewhere in 100 lines:
1. Add log at line 50
2. Does bug happen before or after?
3. Narrow to 50 lines, repeat
4. Continue until you find the exact line
```

#### Input Reduction
```javascript
// Full failing input
const data = { users: [...100 items...], config: {...} };

// Reduced (does it still fail?)
const data = { users: [oneItem], config: {} };

// Minimal reproduction
const data = { users: [{ id: null }] };  // ← Found it!
```

#### Component Isolation
```
Full system failing?
1. Test database connection alone
2. Test API endpoint alone
3. Test UI component alone
4. Find which layer is broken
```

### Hypothesis Formation
```xml
<thinking>
## Hypotheses (ordered by likelihood)
1. [Most likely] User object is undefined when passed to function
   - Evidence: Stack trace shows getUserId receiving undefined
   - Test: Add console.log before the call

2. [Possible] Race condition in data loading
   - Evidence: Only happens on slow connections
   - Test: Add artificial delay to check

3. [Unlikely] Framework bug
   - Evidence: None yet
   - Test: Check GitHub issues
</thinking>
```

---

## 4. Phase 3: FIX

### Objective
Apply the **minimal correct fix**. Don't over-engineer.

### Fix Quality Rules

#### Rule 1: Fix the Root Cause
```javascript
// ❌ Symptom fix (masking)
try {
  return user.id;
} catch {
  return null;  // Hides the real problem
}

// ✅ Root cause fix
if (!user) {
  throw new Error('User not found in session');
}
return user.id;
```

#### Rule 2: Preserve Existing Behavior
```javascript
// ❌ Side effects
function fixBug() {
  this.state = newState;  // Unrelated change
  return correctedValue;
}

// ✅ Minimal change
function fixBug() {
  return correctedValue;  // Only fix the bug
}
```

#### Rule 3: Add Guards, Not Catches
```javascript
// ❌ Catching everything
try {
  processAllData(data);
} catch (e) {
  console.log('Something failed');
}

// ✅ Explicit validation
if (!data || !data.items) {
  throw new ValidationError('Data must contain items');
}
processAllData(data);
```

---

## 5. Phase 4: VERIFY

### Objective
Confirm the fix works and doesn't break anything else.

### Verification Checklist
- [ ] Original bug no longer occurs
- [ ] Related functionality still works
- [ ] No new errors in console/logs
- [ ] Edge cases handled
- [ ] Fix makes sense to future readers

### Regression Testing
```
1. Reproduce original bug → Confirm fixed ✓
2. Test happy path → Still works ✓
3. Test edge cases → No new failures ✓
4. Test related features → No regressions ✓
```

---

## 6. Common Bug Patterns

### Null/Undefined References
```javascript
// Symptom: "Cannot read property 'x' of undefined"
// Pattern: Accessing property on non-existent object

// Find: Check the chain of access
user.profile.settings.theme
// Could be: user?, profile?, or settings?

// Fix: Optional chaining + defaults
const theme = user?.profile?.settings?.theme ?? 'default';
```

### Off-by-One Errors
```javascript
// Symptom: Array index out of bounds, missing items

// Pattern: Loop boundaries wrong
for (let i = 0; i <= arr.length; i++)  // ❌ <= is wrong
for (let i = 0; i < arr.length; i++)   // ✅ < is correct
```

### Race Conditions
```javascript
// Symptom: Works sometimes, fails randomly
// Pattern: Async operations complete in unexpected order

// Fix: Properly await or use Promise.all
const data = await fetchAllData();  // Wait for completion
```

### State Management Issues
```javascript
// Symptom: UI shows stale data
// Pattern: State not updating or not triggering re-render

// Check:
// 1. Is state mutation correct? (React: new object, not mutation)
// 2. Is component subscribed to state changes?
// 3. Is state update happening at all?
```

### Memory Leaks
```javascript
// Symptom: Increasing memory usage, slowdowns
// Pattern: Event listeners not cleaned up

// Check:
// 1. setInterval without clearInterval
// 2. addEventListener without removeEventListener
// 3. Subscriptions without unsubscribe
```

---

## 7. Debugging Tools

### Console Methods
```javascript
console.log(value);                     // Basic output
console.table(arrayOfObjects);          // Tabular display
console.group('Section'); ... console.groupEnd();  // Grouped logs
console.trace();                        // Print stack trace
console.time('op'); ... console.timeEnd('op');     // Timing
```

### Strategic Logging
```javascript
// ❌ Useless log
console.log('here');
console.log(data);

// ✅ Structured log
console.log('[processOrder] Input:', {
  orderId: order.id,
  itemCount: order.items?.length,
  timestamp: new Date().toISOString()
});
```

### Breakpoints Strategy
```
1. Set breakpoint at error location
2. Inspect variable values
3. Step backward through call stack
4. Find where incorrect value originated
```

---

## 8. When to Ask for Help

Escalate when:
- Spent 30+ minutes without progress
- Bug requires domain knowledge you don't have
- Issue might be in third-party library
- Reproducing requires special environment

### Help Request Format
```
## Bug Description
[What happens vs. what should happen]

## Reproduction Steps
1. [Step 1]
2. [Step 2]
3. [Bug occurs]

## What I've Tried
- [Hypothesis 1]: [Result]
- [Hypothesis 2]: [Result]

## Relevant Code
[Minimal code snippet]

## Error/Logs
[Exact error message]
```

---

*"Debugging is like being a detective in a crime movie where you are also the murderer."*
