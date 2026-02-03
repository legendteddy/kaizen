---
name: data-intelligence-pro
description: Skill for advanced data analysis, cleaning, and insight generation.
---

# Skill: Data Intelligence Pro (v1.0)

## Purpose
Turn raw data (CSV, JSON, Logs) into actionable insights using rigorous statistical methods.

## Activation Trigger
- "Analyze this dataset."
- "Find the trends."
- "Why did sales drop?"

---

## Protocol: The Data Pipeline

### 1. Profiling (The "Health Check")
**Action:** Before any analysis, run a profile.
```python
import pandas as pd

df = pd.read_csv("data.csv")
print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Missing: {df.isnull().sum()}") # Check for holes
print(f"Duplicates: {df.duplicated().sum()}")
```

### 2. Cleaning (The "Janitor Work")
- **Dates:** Convert strings to `datetime` immediately.
- **Numbers:** Strip `$` and `,` from currency columns.
- **Categoricals:** Standardize case (`"Apple"` == `"apple"`).

### 3. Analysis (The "Detective Work")
- **Distribution:** Use `df.describe()` for outliers.
- **Correlation:** `df.corr()` for relationships.
- **Time Series:** Resample by day/week (`df.resample('W')`).

---

## Protocol: Insight Generation

**Do not just dump numbers.** Use the **"What, So What, Now What"** framework.

1.  **What:** "Sales dropped 10% in Q3." (Fact)
2.  **So What:** "This correlates with the server outage on July 4th." (Cause)
3.  **Now What:** "Investigate SLA credits for affected customers." (Action)

---

## Visualization Rules (Matplotlib/Seaborn)
- **Title:** Every chart needs a title.
- **Labels:** X and Y axes must be labeled.
- **Color:** Use color accessible palettes (e.g., Viridis).
