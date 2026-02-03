---
name: fastapi-expert
description: Best practices for high-performance, scalable FastAPI applications.
---

# FastAPI Expert
Best practices for high-performance, scalable FastAPI applications.

## Instructions
- **Async First:** Use `async def` for all routes involving I/O (DB, API calls). Use `def` only for CPU-bound tasks.
- **Pydantic:** Use Pydantic models for ALL request/response bodies. Decouple `BaseSettings` for config.
- **Dependency Injection:** Use `Depends()` for database sessions, authentication, and service layers.
- **Structure:** Organize by domain/module (e.g., `src/users`, `src/billing`) rather than generic `controllers/models` folders.
- **Error Handling:** Raise `HTTPException` instead of returning error dicts.

## Capabilities
- Can refactor routes to be asynchronous.
- Can generate Pydantic schemas from JSON.
- Can implement standard JWT authentication flows.