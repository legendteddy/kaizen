---
name: api-development
description: REST API design standards, status codes, and security practices.
---

# API Development

> "Your API is your product."

## Activation Trigger
- Building REST endpoints.
- Designing API contracts.
- Integrating with external services.

## Protocols

### 1. First Principle: Resources over Actions
`POST /users`, not `POST /createUser`.

### 2. Status Code Semantics
- **200**: OK.
- **201**: Created (Return Location header).
- **400**: Client Error (Validation).
- **401**: Who are you? (Auth).
- **403**: You can't do that (Permission).
- **404**: Not found.
- **500**: We messed up.

### 3. Pagination is Mandatory
Never return unbounded lists. Default `limit=20`.

## Code Patterns

### Standard Error Response
```json
{
  "error": {
    "code": "VALIDATION_FAILED",
    "message": "Email is invalid",
    "field": "email"
  }
}
```

### Filtering Syntax
```text
GET /orders?status=active&created_after=2026-01-01
```

## Safety Guardrails
- **Rate Limiting**: APIs must be protected from abuse.
- **Sanitize Input**: Validate all query params and body fields.
- **No Info Leaks**: Never return stack traces in 500 errors.
- **Authz Check**: Every endpoint must verify ownership of the resource being accessed.
- **Idempotency**: `GET`, `PUT`, `DELETE` should be safe to retry.
