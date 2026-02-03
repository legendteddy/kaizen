# Integration: LangGraph

> **Kaizen Role**: The Cognitive Node
> **LangGraph Role**: The Execution Graph

LangGraph manages the *flow* of your agent. Kaizen manages the *logic* inside the nodes.

## Implementation Pattern

In your LangGraph node, load the specific Kaizen skill into the system prompt before execution.

```python
from langgraph.graph import StateGraph, END
from langchain_anthropic import ChatAnthropic
import os

# 1. Kaizen Loader Helper
def load_skill(skill_name):
    path = os.path.expanduser(f"~/.kaizen/skills/{skill_name}/SKILL.md")
    with open(path, "r") as f:
        return f.read()

# 2. Define the Node
def reasoning_node(state):
    # INJECT KAIZEN INTELLIGENCE
    reasoning_skill = load_skill("deliberative-reasoning")
    
    prompt = f"""
    {reasoning_skill}
    
    User Request: {state['input']}
    """
    
    model = ChatAnthropic(model="claude-3-5-sonnet-20240620")
    response = model.invoke(prompt)
    return {"reasoning": response.content}

# 3. Build Graph
workflow = StateGraph(dict)
workflow.add_node("think", reasoning_node)
workflow.set_entry_point("think")
workflow.add_edge("think", END)
app = workflow.compile()
```

## Recommended Skills for Nodes

| Graph Node | Recommended Kaizen Skill |
|:---|:---|
| `planner` | `skills/autonomous-planning` |
| `coder` | `skills/python-development` |
| `reviewer` | `skills/code-review` |
| `debugger` | `skills/debug-master` |
