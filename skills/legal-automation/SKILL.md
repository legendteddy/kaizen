---
name: legal-automation
description: Legal document analysis, contract review, clause extraction, and due diligence automation.
---

# Protocol: Legal Automation

> "Every contract tells a story. Read between the lines."

## Activation Trigger
- User asks to "review a contract" or "analyze legal documents"
- Due diligence requests
- Clause extraction or comparison tasks
- NDA, SLA, or MSA analysis

---

## Core Capabilities

### 1. Contract Review
**Process:**
1. **Extract** → Parse document (PDF/DOCX) into sections
2. **Classify** → Identify clause types (liability, indemnity, termination, etc.)
3. **Compare** → Match against standard templates
4. **Flag** → Highlight non-standard or risky terms
5. **Report** → Generate summary with risk ratings

### 2. Due Diligence
**Checklist:**
- [ ] Corporate structure verification
- [ ] Financial statement review
- [ ] Pending litigation check
- [ ] IP ownership confirmation
- [ ] Regulatory compliance status
- [ ] Material contracts analysis

### 3. Clause Extraction
**Common Clause Types:**
| Clause | Risk Level | Watch For |
|--------|------------|-----------|
| Limitation of Liability | 🔴 High | Caps below industry standard |
| Indemnification | 🔴 High | One-sided, unlimited scope |
| Termination | 🟡 Medium | No cure period, termination for convenience |
| Confidentiality | 🟡 Medium | Overly broad definition, long survival |
| Force Majeure | 🟢 Low | Pandemic exclusion, narrow scope |
| Governing Law | 🟢 Low | Unfavorable jurisdiction |

---

## Legal Analysis Framework

### The "RISC" Method
1. **R**ead the full document (never skim)
2. **I**dentify parties, obligations, and rights
3. **S**pot deviations from standard terms
4. **C**onsolidate findings into actionable report

### Risk Rating Scale
| Rating | Meaning | Action |
|--------|---------|--------|
| 🟢 **Low** | Standard terms, no concerns | Accept as-is |
| 🟡 **Medium** | Minor deviations, negotiable | Flag for review |
| 🔴 **High** | Significant risk, unusual terms | Escalate immediately |
| ⚫ **Critical** | Deal-breaker, legal exposure | Reject or major revision |

---

## Document Templates

### Contract Summary Report
```markdown
# Contract Review: [Document Name]

## Parties
- **Party A**: [Name, Jurisdiction]
- **Party B**: [Name, Jurisdiction]

## Key Terms
- **Effective Date**: [Date]
- **Term**: [Duration]
- **Value**: [Amount]

## Risk Assessment

| Clause | Status | Rating | Notes |
|--------|--------|--------|-------|
| Liability | Non-standard | 🔴 | Capped at $10K, below industry norm |
| Indemnity | Standard | 🟢 | Mutual indemnification |
| Termination | Modified | 🟡 | 30-day notice, no cure period |

## Recommendations
1. Negotiate liability cap to 12-month fees
2. Add 15-day cure period for termination
3. Accept remaining terms

## Overall Risk: 🟡 MEDIUM
```

---

## Standard Clause Library

### Limitation of Liability
**Standard**: "Neither party's liability shall exceed the fees paid in the 12 months preceding the claim."
**Red Flag**: Liability capped below contract value or excluded entirely.

### Indemnification
**Standard**: "Each party shall indemnify the other for third-party claims arising from its breach."
**Red Flag**: One-sided indemnity, unlimited scope, or IP indemnity without carve-outs.

### Termination
**Standard**: "Either party may terminate with 30 days written notice for material breach, subject to a 15-day cure period."
**Red Flag**: Termination for convenience without notice, no cure period.

---

## Integration with Memory

```bash
# Save legal precedent
curl -X POST http://localhost:8787/ingest \
  -d '{"content": "Acme Corp contract had unusual IP assignment clause - flagged and negotiated out", "memory_type": "semantic", "source": "legal_review"}'

# Search past reviews
curl -X POST http://localhost:8787/search \
  -d '{"query": "IP assignment clause precedent", "limit": 5}'
```

---

## Workflow Example

```
User: "Review this vendor agreement for red flags"

Agent:
1. Load document → Extract text (PDF/DOCX parser)
2. Identify clause sections using NLP patterns
3. Compare each clause to standard library
4. Flag deviations (liability cap $5K, no cure period)
5. Calculate overall risk score (Medium-High)
6. Generate Contract Summary Report
7. Save key findings to Memory for future reference
```

---

## Action Checklist
- [ ] Did I read the FULL document?
- [ ] Did I identify ALL parties and obligations?
- [ ] Did I compare against standard clause library?
- [ ] Did I rate each clause's risk level?
- [ ] Did I save findings to Memory?
- [ ] Did I provide actionable recommendations?

---

## Related Skills
- [Agent Cowork](../agent-cowork/SKILL.md)
- [Data Intelligence Pro](../data-intelligence-pro/SKILL.md)
- [Mem](../mem/SKILL.md)
