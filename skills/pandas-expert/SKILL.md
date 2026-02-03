---
name: pandas-expert
description: Skill for expert-level data manipulation using Pandas (Python).
---

# Skill: Pandas Expert (v1.0)

## Purpose
Write performant, readable, and "vectorized" Pandas code. Avoid loops.

## Activation Trigger
- "Process this CSV"
- "Pandas" mentioned
- Data manipulation tasks.

---

## Protocol: Vectorization (No Loops)

**❌ Bad (Iterating):**
```python
for index, row in df.iterrows():
    df.at[index, 'total'] = row['price'] * row['quantity']
```

**✅ Good (Vectorized):**
```python
df['total'] = df['price'] * df['quantity']
```

---

## Protocol: Method Chaining

Use method chaining for readable transformations.

```python
# The "Fluent" Interface
clean_df = (
    raw_df
    .dropna(subset=['id'])
    .assign(
        date=lambda x: pd.to_datetime(x['date_str']),
        total=lambda x: x['price'] * x['qty']
    )
    .rename(columns={'date_str': 'timestamp'})
    .query('total > 0')
)
```

---

## Performance Tips

1.  **Types:** Downcast int64 to int32 if possible. Use `category` for low-cardinality strings.
2.  **Parquet:** Use `.to_parquet()` instead of `.to_csv()` for massive speedups.
3.  **Chunks:** If file > RAM, use `pd.read_csv(chunksize=10000)`.

---

## Common Patterns

| Task | Pattern |
|:---|:---|
| **Vlookup** | `df1.merge(df2, on='key', how='left')` |
| **Pivot Table** | `df.pivot_table(index='date', columns='cat', values='val')` |
| **Moving Avg** | `df['val'].rolling(window=7).mean()` |
