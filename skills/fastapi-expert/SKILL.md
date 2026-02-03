---
name: fastapi-expert
description: Skill for building high-performance, async web APIs with FastAPI.
---

# Skill: FastAPI Expert (v1.0)

## Purpose
Build production-ready, type-safe APIs using Modern Python.

## Activation Trigger
- "Create an API..."
- "Build a backend..."
- "FastAPI" mentioned.

---

## Protocol: The Standard Stack

| Component | Choice |
|:---|:---|
| **App** | `FastAPI` |
| **Server** | `Uvicorn` |
| **Validation** | `Pydantic v2` |
| **DB** | `SQLAlchemy` + `Alembic` |
| **Async** | `async def` everywhere |

---

## Protocol: Implementation Patterns

### 1. The Pydantic Model (Schema)
**Rule:** Separate Request and Response models.

```python
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    is_active: bool
    
    class Config:
        from_attributes = True # ORM Mode
```

### 2. The Dependency Injection
**Rule:** Use `Depends` for DB sessions and Auth.

```python
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)
```

### 3. Error Handling
**Rule:** Use `HTTPException`, don't return dicts.

```python
from fastapi import HTTPException

if not user:
    raise HTTPException(status_code=404, detail="User not found")
```

---

## Checklist: Production Readiness
- [ ] **Docs:** Are `/docs` (Swagger) working?
- [ ] **CORS:** Is `CORSMiddleware` configured?
- [ ] **Env:** Are secrets loaded from `.env`?
- [ ] **Tests:** Are `TestClient` tests passing?
