---
name: synthetic-data
description: Skill for synthetic-data tasks and workflows.
---

# Protocol: Synthetic Data Generation (v1.0)

> AI-generated training data (75% of AI data by 2026)

## Purpose
Understand synthetic data techniques for AI training.

## Activation Trigger
- Data augmentation needs
- Privacy-sensitive datasets
- Edge case generation

---

## The 2026 Reality

> By 2026, 75%+ of AI training data will be synthetic.
> By 2030, 95%+ for images/video.

---

## Generate-Filter-Train Paradigm

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                  │
│  1. GENERATE                                                     │
│     └── LLMs create synthetic data variations                   │
│                                                                  │
│  2. FILTER                                                       │
│     └── Human experts rapidly review and edit                   │
│     └── Accept, reject, or modify                               │
│                                                                  │
│  3. TRAIN                                                        │
│     └── Fine-tune models on curated synthetic + human data      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Key Techniques

### 1. LLM-Powered Generation
- Instruction-response pairs
- Tool-use traces
- Dialogue datasets
- Code examples

### 2. Simulation-Driven
- Robotics training
- Autonomous vehicles
- Physical systems

### 3. Synthetic-to-Real Transfer
- Pre-train on synthetic
- Fine-tune on real (smaller set)
- Faster convergence

---

## Risks

### Model Collapse (MAD)
```
Train on synthetic → Generate more synthetic →
Train again → Quality degrades → 
Eventually: nonsense outputs
```

**Mitigation:**
- Maintain access to authentic human data
- Mix synthetic with real data
- Regular quality checks

---

## For Standard Framework

Synthetic data applies to:
1. **Skill generation**: Create example tasks
2. **Test cases**: Generate edge cases
3. **Training data**: Augment limited samples
4. **Simulation**: Test before production



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Professional Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
