---
name: pandas-expert
description: High-performance data manipulation, vectorization patterns, and memory optimization.
---

# Pandas Expert

> "If you are looping, you are losing."

## Activation Trigger
- Manipulating large datasets (>10k rows).
- Optimizing slow data processing pipelines.
- Debugging memory issues in Python data scripts.

## 1. Vectorization Protocols

**The Golden Rule:** NEVER use `iterrows()` for math.

| Slow (Loop) | Fast (Vector) | Speedup |
|:---|:---|:---|
| `for i, r in df.iterrows()` | `df['col'] = ...` | ~1000x |
| `df.apply(lambda x: ...)` | `np.where(...)` | ~100x |
| String matching loop | `df['s'].str.contains()` | ~50x |

**Complex Logic?** Use `numpy.select()`:
```python
conditions = [
    (df['age'] < 18),
    (df['age'] >= 18) & (df['student'] == True)
]
choices = ['child', 'student']
df['status'] = np.select(conditions, choices, default='adult')
```

## 2. Memory Optimization (The Diet)
Default Pandas uses massive RAM. Shrink it.

1.  **Load Less:** `pd.read_csv(..., usecols=['id', 'val'])`
2.  **Downcast Types:**
    - `float64` -> `float32` (Half size)
    - `object` (Strings) -> `category` (Index-based, massive savings for low cardinality)
3.  **Nullable Ints:** Use `Int64` instead of `float64` for columns with NaNs.

```python
# Automatic Downcasting Code
for col in df.select_dtypes(include=['float64']):
    df[col] = pd.to_numeric(df[col], downcast='float')
```

## 3. Method Chaining (The Fluent Style)
Readable pipelines are debuggable pipelines.

```python
(
    load_data()
    .pipe(clean_names)
    .assign(
        revenue=lambda x: x.price * x.qty,
        date=lambda x: pd.to_datetime(x.timestamp)
    )
    .query("revenue > 100")
    .groupby("category")
    .agg(total_rev=("revenue", "sum"))
    .reset_index()
)
```

## 4. Polars (The 2026 Alternative)
If dataset > 10GB, abandon Pandas. Use **Polars**.
- Lazy Evaluation (`.lazy().collect()`)
- Parallel Execution (Rust backend)
- No index headaches.

## 5. Debugging Pipelines
Break the chain to inspect:
```python
.pipe(lambda df: print(df.shape) or df)  # Returns df after printing
```
