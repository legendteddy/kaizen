---
name: fastapi-expert
description: Building high-performance, async web APIs with FastAPI and Pydantic.
---

# FastAPI Expert

> "Validation is not an option. It's the law."

## Activation Trigger
- "Create an API"
- "Backend development"
- "FastAPI" mentioned.

## Protocols

### 1. First Principle: Type-Safe Contracts
The Pydantic model IS the documentation.

### 2. The Stack
- **Web**: FastAPI + Uvicorn
- **Data**: SQLAlchemy (Async) + Pydantic v2
- **Migrations**: Alembic

### 3. Dependency Injection
Use `Depends()` for everything (DB, Auth, Config). Testing becomes trivial.

## Code Patterns

### Response Model Separation
```python
class UserCreate(BaseModel):
    password: str # In request

class UserResponse(BaseModel):
    id: int       # In response
    # password excluded
```

### Async Database Session (SQLAlchemy 2.0)
```python
@asynccontextmanager
async def get_db():
    async with SessionLocal() as session:
        yield session
```

## Safety Guardrails
- **No Secrets in Code**: Environment variables only.
- **SQL Injection**: Always use ORM methods or parameterized queries.
- **Input Validation**: Never trust user input. Pydantic handles this.
- **Status Codes**: Return standard HTTP codes (201 Created, 404 Not Found), not 200 OK for everything.
- **Async Hygiene**: Do not use blocking IO (e.g. `requests`) inside async routes.
## Related Skills
- [Software Architecture](../software-architecture/SKILL.md): For service layer and repository patterns.
- [Database Operations](../database-operations/SKILL.md): For SQL optimization.
- [Security Boundaries](../safety-boundaries/SKILL.md): For API hardening.
