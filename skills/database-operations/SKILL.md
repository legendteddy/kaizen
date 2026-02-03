---
name: database-operations
description: Comprehensive database engineering covering schema design, SQL optimization, SQLite patterns, data integrity, and migration strategies.
---

# Database Operations

> SQL and database best practices for data operations, schema design, and optimization.

## Purpose
Ensure proper database design, queries, and data handling with focus on data integrity and performance.

## Core Competencies
1. **Schema Design**: 3rd Normal Form (3NF) by default. Use foreign keys strictly.
2. **Query Optimization**: Analyze `EXPLAIN QUERY PLAN` for slow queries. Add indexes judiciously.
3. **Migrations**: Never break existing data. Always provide up/down migration scripts.
4. **SQLite Mastery**: Use specific SQLite features (WAL mode, JSON1) effectively.

## Activation Trigger
- Working with SQLite, PostgreSQL, or other databases
- Writing SQL queries
- Database schema design
- Query optimization needed

---

## SQLite Patterns

### Connection Management
```python
import sqlite3
from contextlib import contextmanager

@contextmanager
def get_connection(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Dict-like access
    try:
        yield conn
    finally:
        conn.close()
```

### Parameterized Queries
```python
# NEVER string concatenation (SQL injection risk)
# ❌ cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ Always use parameterized queries
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
```

### Transactions
```python
with get_connection("app.db") as conn:
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO orders ...")
        cursor.execute("UPDATE inventory ...")
        conn.commit()
    except Exception:
        conn.rollback()
        raise
```

---

## Schema Design

### Normalization
```sql
-- 1NF: Atomic values, unique rows
-- 2NF: No partial dependencies
-- 3NF: No transitive dependencies

CREATE TABLE customers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

### Indexes
```sql
-- Index frequently queried columns
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_date ON orders(order_date);

-- Composite index for multi-column queries
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);
```

---

## Query Patterns

### Pagination
```sql
SELECT * FROM items
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;  -- Page 3 (0-indexed: skip 40, take 20)
```

### Aggregation
```sql
SELECT 
    customer_id,
    COUNT(*) as order_count,
    SUM(total) as total_spent
FROM orders
GROUP BY customer_id
HAVING order_count > 5
ORDER BY total_spent DESC;
```

### JSON in SQLite
```sql
-- Store JSON
INSERT INTO settings (config) VALUES ('{"theme": "dark"}');

-- Query JSON
SELECT json_extract(config, '$.theme') FROM settings;
```

---

## Best Practices

| Practice | Description |
|:---|:---|
| Use transactions | Group related operations |
| Parameterize queries | Prevent SQL injection |
| Add indexes | For frequently queried columns |
| Use foreign keys | Maintain referential integrity |
| Backup regularly | Before migrations |
| Normalize to 3NF | Reduce redundancy |
| Analyze queries | Use EXPLAIN QUERY PLAN |

---

## Operational Workflow

1. **Analyze**: Look at current schema (`schema.sql` or existing tables)
2. **Critique**: Identify N+1 queries, missing indexes, or weak types
3. **Propose**: Write the migration SQL before changing application code
4. **Verify**: Ensure the migration runs on a copy of the database
5. **Document**: Update schema documentation after changes

---

## Data Engineering Principles

### Integrity First
- Foreign key constraints prevent orphaned records
- Check constraints ensure data validity
- NOT NULL where appropriate
- Unique constraints for identifiers

### Performance Second
- Index frequently queried columns
- Avoid SELECT * in production
- Use EXPLAIN to verify query plans
- Batch operations when possible

### Migrations Safely
- Always have rollback plan (down migration)
- Test migrations on copy of production data
- Make migrations idempotent when possible
- Never drop columns with data without backup

---

## SQLite Specifics

### WAL Mode (Write-Ahead Logging)
```sql
-- Enable for better concurrency
PRAGMA journal_mode = WAL;
```

### JSON1 Extension
```sql
-- Store and query JSON
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    data JSON
);

-- Query JSON fields
SELECT * FROM events WHERE json_extract(data, '$.type') = 'click';
```

### Text vs Numeric
```sql
-- Store dates as ISO8601 text
CREATE TABLE events (
    timestamp TEXT DEFAULT (datetime('now'))
);
```



## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Sovereign Standards?


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
