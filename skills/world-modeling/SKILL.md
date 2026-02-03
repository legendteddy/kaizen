---
name: world-modeling
description: Skill for world-modeling tasks and workflows.
---

# Skill: World Modeling (v1.0)

> Text-to-world generation and simulation (Project Genie pattern)

## Purpose
Create interactive, simulated environments from natural language descriptions.

## Activation Trigger
- Requests for environment simulation
- Game/world generation tasks
- Embodied AI applications

---

## Concept

**World Models** = AI systems that understand and simulate physical reality.

Traditional AI sees the world as:
- Text (language models)
- Images (vision models)
- Actions (RL agents)

World models combine all three:
- Understand scene descriptions
- Generate interactive environments
- Simulate physics and interactions

---

## Architecture (Genie-inspired)

```
┌─────────────────────────────────────────────────────────────────┐
│                     TEXT PROMPT                                  │
│        "A forest clearing with a small cabin"                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  1. SCENE UNDERSTANDING                                          │
│     └── Parse text → 3D scene graph                             │
│                                                                  │
│  2. WORLD GENERATION                                             │
│     └── Generate terrain, objects, lighting                     │
│                                                                  │
│  3. PHYSICS SIMULATION                                           │
│     └── Apply realistic physics to objects                      │
│                                                                  │
│  4. INTERACTION LAYER                                            │
│     └── Handle user inputs → world reactions                    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Applications

### 1. Gaming
- Procedural world generation
- Infinite content creation
- Personalized game worlds

### 2. Training Simulations
- Virtual environments for RL
- Safe failure in simulation
- Transferable skills

### 3. Design and Architecture
- Rapid prototyping
- Interactive walkthroughs
- Client visualization

### 4. Education
- Historical recreations
- Science simulations
- Interactive learning

---

## Relevance to Sovereign Framework

World models represent:
- Next level of agentic capability
- Embodied AI understanding
- Physical world reasoning

When combined with tool use:
- Debug a UI by "seeing" it
- Understand spatial relationships
- Reason about physical consequences



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
