---
name: docs-fetcher
description: Fetches and summarizes documentation for external libraries or tools to ground the agent in reality.
---

# Documentation Fetcher

Use this skill when the User introduces a new tool or asks for an explanation.

## Vibe Check
-   **User Intent**: "Explain how this works" or "Use that new library."
-   **Goal**: Learn the tool instantly so the user doesn't have to explain it.

## Protocol
1.  **Search**: Find the official docs.
2.  **Learn**: Read the "Get Started" and "API Reference".
3.  **Teach**: Explain it back to the user in simple terms (if asked).
4.  **Do**: Use the correct syntax in the code.

## Example Trigger
User: "Use the new `super-grid` library."
Agent: "I don't know `super-grid`. Learning it now..."
(Agent searches -> fetches docs -> implements code).