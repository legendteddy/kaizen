---
name: fastapi-expert
description: Skill for building high-performance, async web APIs with FastAPI.
---

# Skill: FastAPI Expert (v1.0)

> "Validation is not an option. It's the law."

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

## Advanced: Background Tasks
Don't block the request for email sending.

```python
from fastapi import BackgroundTasks

def send_email(email: str, message: str):
    # ... logic ...
    pass

@app.post("/send-notification/")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(send_email, email, "Subscription confirmed")
    return {"message": "Notification sent"}
```

## Scaling Up
- **Gunicorn:** Use `gunicorn -w 4 -k uvicorn.workers.UvicornWorker`.
- **Docker:** Use minimal `python:3.11-slim` images.


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
