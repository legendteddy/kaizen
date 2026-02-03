---
name: agentic-lifecycle
description: Skill for managing the lifecycle of an autonomous task (Plan, Act, Verify).
---

# Skill: Agentic Lifecycle (v1.0)

> "The cycle of autonomy."

## Purpose
Standardize the execution flow of autonomous agents to prevent "looping" or "hallucinated completion."

## Activation Trigger
- Designing the main loop of an agent.
- Debugging agents that get stuck or finish early.

---

## Protocol: The Standard Loop

Every autonomous agent must implement this 4-step state machine:

### 1. PERCEIVE (Input)
- **Action:** Read user input + current context + tool outputs.
- **Guard:** Ensure context window isn't full. If >80%, trigger `context-compact`.

### 2. PLAN (Reasoning)
- **Action:** Generate a Chain-of-Thought (CoT) before calling tools.
- **Format:**
  ```text
  THOUGHT:
  1. User wants X.
  2. I need to use tool Y.
  3. Then I will check Z.
  ```

### 3. ACT (Tool Execution)
- **Action:** Execute the tool call.
- **Guard:** Wrap in `try/catch`. If tool fails, do NOT hallucinate a success. Report the error to the PLAN phase.

### 4. REFLECT (Verification)
- **Action:** Compare Tool Output vs. User Intent.
- **Logic:**
  ```python
  if is_goal_met(output):
      return FINAL_ANSWER
  else:
      return GOTO_STEP_1
  ```

---

## Implementation Template (Python)

```python
class Agent:
    def run(self, goal: str):
        self.memory.add(goal)
        
        for turn in range(MAX_TURNS):
            # 1. Perceive
            context = self.memory.get_recent()
            
            # 2. Plan
            plan = self.llm.think(context)
            
            # 3. Act
            if plan.tool_call:
                try:
                    result = self.tools.execute(plan.tool_call)
                except Exception as e:
                    result = f"Error: {str(e)}"
            
            # 4. Reflect
            self.memory.add(result)
            if self.verifier.check(result, goal):
                return result
                
        return "Max turns reached."
```