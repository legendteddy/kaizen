---
name: finance-automation
description: Financial analysis, tax preparation, bookkeeping, and financial modeling automation.
---

# Protocol: Finance Automation

> "Numbers don't lie, but they do need interpretation."

## Activation Trigger
- User asks about "financial analysis" or "tax preparation"
- Invoice processing or expense categorization
- Financial modeling or forecasting
- Bookkeeping or reconciliation tasks

---

## Core Capabilities

### 1. Financial Statement Analysis
| Statement | Key Metrics | What to Watch |
|-----------|-------------|---------------|
| **Income Statement** | Revenue, EBITDA, Net Income | Margin trends, one-time items |
| **Balance Sheet** | Assets, Liabilities, Equity | Debt ratios, working capital |
| **Cash Flow** | Operating, Investing, Financing | Free cash flow, burn rate |

### 2. Tax Preparation
**Process:**
1. **Gather** → Collect income sources (W2, 1099, K1)
2. **Categorize** → Income vs deductions
3. **Calculate** → Taxable income, applicable rates
4. **Optimize** → Deduction maximization
5. **Review** → Double-check all entries
6. **File** → Generate return or export to tax software

### 3. Bookkeeping
**Double-Entry Basics:**
| Transaction | Debit | Credit |
|-------------|-------|--------|
| Sale (cash) | Cash ↑ | Revenue ↑ |
| Expense (cash) | Expense ↑ | Cash ↓ |
| Loan received | Cash ↑ | Liability ↑ |
| Loan payment | Liability ↓ | Cash ↓ |

### 4. Financial Modeling
**Build Models For:**
- Revenue projections (bottoms-up, tops-down)
- DCF valuation
- Scenario analysis (base, bull, bear)
- Sensitivity tables

---

## Key Financial Ratios

### Profitability
| Ratio | Formula | Healthy Range |
|-------|---------|---------------|
| Gross Margin | (Revenue - COGS) / Revenue | 40-60% |
| EBITDA Margin | EBITDA / Revenue | 15-25% |
| Net Margin | Net Income / Revenue | 10-20% |

### Liquidity
| Ratio | Formula | Healthy Range |
|-------|---------|---------------|
| Current Ratio | Current Assets / Current Liabilities | 1.5 - 3.0 |
| Quick Ratio | (Current Assets - Inventory) / Current Liabilities | 1.0 - 2.0 |

### Leverage
| Ratio | Formula | Healthy Range |
|-------|---------|---------------|
| Debt/Equity | Total Debt / Shareholders' Equity | 0.5 - 1.5 |
| Interest Coverage | EBIT / Interest Expense | > 3.0 |

---

## Tax Categories (US)

### Income Types
| Type | Tax Treatment |
|------|---------------|
| W-2 Wages | Ordinary income |
| 1099 Income | Self-employment (+ SE tax) |
| Capital Gains (Short) | Ordinary income |
| Capital Gains (Long) | Preferential rates (0/15/20%) |
| Dividends (Qualified) | Preferential rates |
| Rental Income | Passive income (special rules) |

### Common Deductions
| Deduction | Limit | Notes |
|-----------|-------|-------|
| Standard Deduction | $14,600 single / $29,200 MFJ | 2024 |
| SALT | $10,000 | State and local taxes |
| Mortgage Interest | $750K principal | Primary residence |
| Charitable | 60% AGI | Cash contributions |
| Home Office | Actual or simplified | Self-employed only |

---

## Document Templates

### Financial Health Report
```markdown
# Financial Analysis: [Company/Individual]

## Summary Metrics
| Metric | Current | Prior | Change |
|--------|---------|-------|--------|
| Revenue | $X | $Y | +Z% |
| Net Income | $X | $Y | +Z% |
| Cash Balance | $X | $Y | +Z% |

## Ratio Analysis
| Category | Ratio | Value | Status |
|----------|-------|-------|--------|
| Profitability | Gross Margin | 45% | 🟢 Healthy |
| Liquidity | Current Ratio | 2.1 | 🟢 Healthy |
| Leverage | Debt/Equity | 1.8 | 🟡 Elevated |

## Key Observations
1. Revenue growth strong (+15% YoY)
2. Debt levels slightly elevated, monitor
3. Cash position healthy, runway > 12 months

## Recommendations
1. Prioritize debt paydown if rates rise
2. Maintain current cash reserves
3. Review expense growth vs revenue
```

---

## Integration with Memory

```bash
# Save financial insight
curl -X POST http://localhost:8787/ingest \
  -d '{"content": "Q4 2025 analysis: Client had 18% margin compression due to one-time restructuring", "memory_type": "semantic", "source": "finance_analysis"}'

# Search past analyses
curl -X POST http://localhost:8787/search \
  -d '{"query": "margin compression causes", "limit": 5}'
```

---

## Workflow Examples

### Tax Prep Flow
```
User: "Help me prepare my 2025 taxes"

Agent:
1. Collect income docs (W2, 1099s, investment statements)
2. Identify all income sources and amounts
3. Gather deduction evidence (receipts, mortgage statements)
4. Calculate AGI and taxable income
5. Determine optimal filing status
6. Run standard vs itemized comparison
7. Generate tax summary with estimated liability
8. Save to Memory for audit reference
```

### Invoice Processing
```
User: "Categorize these invoices for bookkeeping"

Agent:
1. Load invoice images/PDFs
2. Extract vendor, amount, date, description
3. Categorize by expense type (COGS, SG&A, R&D)
4. Generate journal entries (double-entry format)
5. Export to CSV or accounting software format
6. Save categorization rules to Memory
```

---

## Python Helpers

### Quick Ratio Calculator
```python
def financial_ratios(current_assets, inventory, current_liabilities, ebit, interest):
    return {
        "current_ratio": current_assets / current_liabilities,
        "quick_ratio": (current_assets - inventory) / current_liabilities,
        "interest_coverage": ebit / interest if interest > 0 else float('inf')
    }
```

### Tax Bracket Lookup (2024)
```python
def federal_tax_2024(taxable_income, filing_status="single"):
    brackets = {
        "single": [(11600, 0.10), (47150, 0.12), (100525, 0.22), 
                   (191950, 0.24), (243725, 0.32), (609350, 0.35), (float('inf'), 0.37)],
        "mfj": [(23200, 0.10), (94300, 0.12), (201050, 0.22),
                (383900, 0.24), (487450, 0.32), (731200, 0.35), (float('inf'), 0.37)]
    }
    # Calculate marginal tax
    tax = 0
    prev_limit = 0
    for limit, rate in brackets[filing_status]:
        if taxable_income <= limit:
            tax += (taxable_income - prev_limit) * rate
            break
        tax += (limit - prev_limit) * rate
        prev_limit = limit
    return tax
```

---

## Action Checklist
- [ ] Did I verify all numbers against source documents?
- [ ] Did I use double-entry for all transactions?
- [ ] Did I calculate relevant ratios?
- [ ] Did I flag any anomalies or risks?
- [ ] Did I save insights to Memory?
- [ ] Did I provide actionable recommendations?

---

## Related Skills
- [Agent Cowork](../agent-cowork/SKILL.md)
- [Data Intelligence Pro](../data-intelligence-pro/SKILL.md)
- [Pandas Expert](../pandas-expert/SKILL.md)
- [Mem](../mem/SKILL.md)
