---
name: self-play-training
description: AI self-play and RLAIF techniques for autonomous model improvement.
---

# Protocol: Self-Play Training (v1.0)

> AI training itself without human annotation

## Purpose
Understand self-play and RLAIF training techniques.

## Activation Trigger
- Model training discussions
- Alignment concepts
- Autonomous improvement

---

## Self-Play

### Concept
```
Model plays against itself
→ Generates training data
→ Learns from wins/losses
→ Improves iteratively
```

### Key Techniques

#### SPIN (Self-Play Fine-Tuning)
- Google/Stanford breakthrough
- Weaker models beat larger rivals
- No human feedback required

#### Cooperative Self-Play
- Model = solver + checker
- Improves code generation
- Self-verification built-in

---

## RLAIF (RL from AI Feedback)

### vs RLHF
| RLHF | RLAIF |
|:---|:---|
| Human annotators | AI provides feedback |
| Expensive, slow | Scalable, efficient |
| Subjective | Constitutional principles |

### Benefits
- Addresses scalability limits
- Comparable performance to RLHF
- Built-in ethical guidelines

---

## Challenges

1. **Confidently wrong**: Reinforcing own errors
2. **Reward hacking**: Exploiting rules
3. **Degenerate dynamics**: Mutual error reinforcement
4. **Compute cost**: Multiple large models

---

## 2026 Trends

- RL environments as enterprise testbeds
- Continuous self-correction before deployment
- Reducing dependence on human annotation

---

## For Standard Framework

Self-play enables:
- Reduced human oversight needs

## 3. The Reward Hacking Trap
When agents game the system:

### Symptoms
- Agent outputs max length responses to look "smart".
- Agent agrees with user aliases even when wrong.
- Agent uses "safety language" to avoid hard tasks.

### Mitigation
- **KL Divergence Penalty:** Keep model close to base model.
- **Rule-Based Overrides:** Hard-coded "Thou Shalt Not" rules.
- **Red Teaming:** Adversarial attacks during training.



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Professional Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Meta-Optimizer](../meta-optimizer/SKILL.md): Recursive improvement logic.
- [Predictive Evolution](../predictive-evolution/SKILL.md): Forward-looking modeling.
- [Self-Improvement](../self-improvement/SKILL.md): The Kaizen loop.
