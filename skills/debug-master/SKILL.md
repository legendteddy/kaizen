---
name: debug-master
description: Advanced debugging methodology with 4-phase root cause analysis and systematic problem isolation.
---

# Debug Master (Systematic Problem Solving)

> "The bug is not in the code. The bug is in your mental model."

## Activation Trigger
- Encountering a runtime error or bug.
- Need to isolate a root cause.
- Analyzing stack traces.

## Protocols

### 1. First Principle: TRACE → ISOLATE → FIX → VERIFY
Never skip a step. Fixing without isolating is just guessing.

### 2. Phase 1: TRACE (Gather Evidence)
Before touching code, collect:
- **Symptom**: What exactly happened?
- **Stack Trace**: Read the top user-code frame.
- **Environment**: OS, dependency versions.

### 3. Phase 2: ISOLATE (Minimal Reproduction)
Strip away noise until you have a minimal failing case.
- **Bisect**: Comment out half the code. Does it still fail?
- **Mock**: Replace database/API with static data.

### 4. Phase 3: FIX (Root Cause)
Apply the minimal correct fix.
- **Rule**: guards, not catches (Avoid `try/catch` masking).
- **Rule**: Fix the cause, not the symptom.

### 5. Phase 4: VERIFY (Regression Test)
- Confirm the bug is gone.
- Confirm no new bugs created.

## Code Patterns

### Robust Error Handling
```javascript
// ❌ Bad: Masking errors
try { 
  fn(); 
} catch (e) { 
  console.log("oops"); 
}

// ✅ Good: Explicit Guards
if (!user) throw new Error("Missing User");
fn();
```

### Strategic Logging
```javascript
console.group("[AuthService]");
console.log("Input:", { id, token }); // Structured data
console.groupEnd();
```

## Safety Guardrails
- **Never** fix a bug you haven't reproduced.
- **Never** deploy a fix without a regression test.
- **Never** add "blind catches" (`except pass`) just to silence an error.
- **Always** verify backups before modifying database state.
