---
name: data-intelligence-pro
description: Advanced Exploratory Data Analysis (EDA), Statistical rigor, and Insight Generation.
---

# Protocol: Data Intelligence Pro

> "Data is just noise until you find the signal."

## Activation Trigger
- Performing Exploratory Data Analysis (EDA).
- Validating statistical significance.
- Detecting outliers or anomalies.

## 1. The Automated EDA Protocol
Don't guess. Run the standard battery.

### Phase 1: The Shape of Water
```python
def check_health(df):
    print(f"Shape: {df.shape}")
    print(f"Types:\n{df.dtypes}")
    print(f"Missing %:\n{df.isnull().mean() * 100}")
    print(f"Duplicates: {df.duplicated().sum()}")
```

### Phase 2: Univariate Analysis (One Variable)
- **Numerical:** Histogram + Boxplot (Check for outliers).
- **Categorical:** Bar chart (Check for balance).
- **Protocol:** If skew > 1.0, consider Log Transform `np.log1p()`.

### Phase 3: Bivariate Analysis (Relationships)
- **Num vs Num:** Scatterplot / Correlation Matrix.
- **Num vs Cat:** Boxplot (Side-by-side).
- **Cat vs Cat:** Heatmap (Crosstab).

## 2. Statistical Rigor
Don't say "A is better than B" without a test.

| Scenario | Test |
|:---|:---|
| Compare 2 Means | T-Test |
| Compare >2 Means | ANOVA |
| Compare Categories | Chi-Square |
| Correlation | Pearson/Spearman |

## 3. Outlier Detection
1.  **IQR Method:** `< Q1 - 1.5*IQR` or `> Q3 + 1.5*IQR`.
2.  **Z-Score:** `> 3` standard deviations.
3.  **Isolation Forest:** For high-dimensional data (AI approach).

## 4. Insight Generation Framework
**"The What, So What, Now What"**

1.  **What:** "Churn increased to 5% in May."
2.  **So What:** "This coincides with the price hike. High-value cohorts were unaffected."
3.  **Now What:** "Segment retention offers to low-value cohorts only."

## 5. Visualization Rules
- **No Pie Charts:** Humans can't compare angles. Use Bar Charts.
- **Color:** Use color to highlight data, not for decoration.
- **Titles:** Title should be the insight ("Sales dropped in Q3"), not the metric ("Sales over Time").


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Professional Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
