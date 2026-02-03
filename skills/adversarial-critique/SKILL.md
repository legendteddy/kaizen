---
name: adversarial-critique
description: Skill for adversarial-critique tasks and workflows.
---

# Skill: Adversarial Critique (Sentinel)

> "Global Sentinel" - Adversarial critique agent for strategy review

## Purpose
Peer-review all high-level intents before deployment to physical or digital execution layers.

## Activation Trigger
- Before major strategic decisions
- When reviewing bids, proposals, or plans
- Risk assessment for cross-border operations

---

## Critique Framework

### 1. ROI Check
```
□ Does the action have clear ROI?
□ Is the markup/profit margin acceptable?
□ What's the worst-case scenario?
```

### 2. Inventory/Resource Risk
```
□ How much resource is committed to this action?
□ What percentage of total capacity?
□ Is there a fallback if this fails?
```

### 3. Geopolitical Friction
```
Region → Friction Level
- Brunei Darussalam: LOW
- Malaysia: LOW
- Regional: MEDIUM
- International: HIGH

□ Does friction level exceed acceptable threshold?
□ Are compliance buffers in place?
```

### 4. Compliance Check
```
□ Are all regulatory requirements met?
□ Is documentation complete?
□ Is human review required?
```

---

## Verdict Template

```json
{
  "action_id": "xxx",
  "status": "PASSED|FLAGGED|BLOCKED",
  "issues": ["issue 1", "issue 2"],
  "recommendations": ["rec 1", "rec 2"]
}
```

---

## Thresholds (Configurable)

| Parameter | Default |
|:---|:---|
| `min_markup_pct` | 25% |
| `max_inventory_risk` | 30% |
| `geopolitical_friction_limit` | MEDIUM |
| `compliance_required` | TRUE |

---

## Sentinel Protocol

Before any major action:
1. **PAUSE**: Stop before execution
2. **CRITIQUE**: Run through all checks
3. **VERDICT**: PASSED, FLAGGED, or BLOCKED
4. **PROCEED**: Only if PASSED or human override

## Action Checklist
- [ ] **ROI:** Is the profit margin > 25%?
- [ ] **Inventory:** Is risk exposure < 30% of capacity?
- [ ] **Friction:** Is the operation compliant with local laws?
- [ ] **Scenario:** Have you simulated the worst-case outcome?
- [ ] **Verdict:** Is the final status clearly PASSED or BLOCKED?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
