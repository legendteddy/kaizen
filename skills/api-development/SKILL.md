---
name: api-development
description: Skill for api-development tasks and workflows.
---

# Skill: API Development (v1.0)

> REST API design and implementation best practices

## Purpose
Ensure APIs follow professional standards and modern patterns.

## Activation Trigger
- Building REST APIs
- API design review
- Backend development

---

## REST Principles

### Resource Naming
```
✅ Good:
GET  /users           # List users
GET  /users/123       # Get user 123
POST /users           # Create user
PUT  /users/123       # Update user 123
DELETE /users/123     # Delete user 123

❌ Bad:
GET /getUsers
POST /createUser
GET /user/delete/123
```

### HTTP Status Codes
| Code | Meaning | Use Case |
|:---:|:---|:---|
| 200 | OK | Successful GET, PUT |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Missing/invalid auth |
| 403 | Forbidden | No permission |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Unexpected error |

---

## Request/Response Patterns

### Pagination
```json
GET /users?page=2&limit=20

{
  "data": [...],
  "pagination": {
    "page": 2,
    "limit": 20,
    "total": 150,
    "pages": 8
  }
}
```

### Error Response
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Email is required",
    "field": "email"
  }
}
```

### Filtering
```
GET /orders?status=pending&created_after=2026-01-01
```

---

## FastAPI Example

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

class UserResponse(User):
    id: int

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    user = await db.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: User):
    return await db.create_user(user)
```

---

## Security Best Practices

| Practice | Description |
|:---|:---|
| Use HTTPS | Encrypt all traffic |
| Validate input | Never trust client data |
| Rate limiting | Prevent abuse |
| Authentication | JWT, API keys, OAuth |
| CORS | Configure allowed origins |



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
