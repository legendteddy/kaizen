---
name: pandas-expert
description: Expert knowledge for the Pandas data analysis library. Focuses on vectorization, efficiency, and modern best practices.
---

# Pandas Expert
Expert knowledge for the Pandas data analysis library. Focuses on vectorization, efficiency, and modern best practices.

## Instructions
- **Vectorization:** ALWAYS prefer vectorized operations (e.g., `df['a'] + df['b']`) over loops or `.apply()`.
- **Indexing:** Use `.loc` and `.iloc` for explicit indexing. Avoid chained indexing (`df[mask]['col'] = val`) to prevent SettingWithCopyWarning.
- **I/O:** Use explicit `dtype` arguments when reading files to save memory.
- **Null Handling:** Handle `NaN` / `None` explicitly using `.fillna()`, `.dropna()`, or `pd.isna()`.
- **Method Chaining:** Prefer method chaining with `.pipe()` or `.assign()` for readable transformations.

## Capabilities
- Can optimize slow DataFrame operations.
- Can debug common Merge/Join issues (inner vs outer, suffixes).
- Can generate complex aggregation pipelines using `.groupby()`.