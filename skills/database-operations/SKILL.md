---
name: database-operations
description: Engineering standards for Schema Design, SQL Optimization, and Migrations.
---

# Database Operations

> "Data outlives code."

## Activation Trigger
- Writing SQL queries.
- Designing database schema.
- Running migrations.

## Protocols

### 1. First Principle: Normalize First, Denormalize Later
Start with 3NF (Third Normal Form). Only break it if `EXPLAIN QUERY PLAN` proves you need to.

### 2. Schema Design Standards
- **Primary Keys**: Always exist. `bigint` or `uuid`.
- **Foreign Keys**: Start enforced.
- **Timestamps**: `created_at` (immutable), `updated_at` (auto-update).

### 3. Migration Safety
Never break backward compatibility in a live app.
1. Add new column (nullable).
2. Deploy code writing to both.
3. Drop old column (later).

## Code Patterns

### Safe Parameterization
```python
# ❌ SQL Injection Vector
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ Safe
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### Transaction Blocks
```python
with get_connection() as conn:
    try:
        conn.execute("UPDATE inventory ...")
        conn.execute("INSERT INTO orders ...")
        conn.commit()
    except:
        conn.rollback()
        raise
```

## Safety Guardrails
- **Rollback Plan**: Every migration needs a `down` script.
- **Index Check**: No table scan queries on production.
- **Backup Before Drop**: Never run `DROP TABLE` without a backup verification.
- **N+1 Prevention**: In ORMs, use `.joinedload()` or `.select_related()`.
- **Validation Constraints**: DB constraints (`NOT NULL`, `CHECK`) > App validation.
