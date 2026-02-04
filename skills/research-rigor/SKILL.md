---
name: research-rigor
description: Protocols for verifying knowledge BEFORE acting (Grep First, Input Rigor).
---

# Research Rigor (Anti-Laziness Protocol)

> "To guess is cheap. To know is Sovereign."

## Activation Trigger
- User asks: "Do we have X?"
- You think: "I don't think we have X."
- You are about to say: "I cannot find..."
- You are about to create a new file/skill.

## Protocols

### 1. First Principle: The "Grep First" Rule
You are strictly FORBIDDEN from declaring "X does not exist" until you have performed a `grep_search` for X and its synonyms.
**Lazy**: "I don't see a design skill."
**Rigorous**: "I grepped for 'design', 'style', 'css', 'ui' and found nothing."

### 2. The Search Radius
Do not just look in the current directory.
*   **Level 1**: `ls` current dir.
*   **Level 2**: `grep` recursive in parent dir.
*   **Level 3**: Read `manifest.json` or `README.md` index files.

### 3. Verification of Absence
Absence of evidence is not evidence of absence.
If you fail to find something, you must state your search method to the user.
*   "I searched `skills/` for 'seo' and found 0 results." (User trusts this).
*   "I don't think we have seo." (User hates this).

## Code Patterns

### The Rigorous Search Loop
```python
# 1. Broad Search
grep_search(query="SEO", path="src/")

# 2. Synonym Search
grep_search(query="search engine", path="src/")

# 3. File List Analysis
find_by_name(pattern="*seo*", path="src/")
```

## Safety Guardrails
- **Don't Hallucinate Paths**: Never `read_file` a path you haven't seen in `ls` or `find`.
- **Don't Reinvent Wheels**: If a similar file exists, read it before creating a new one.
- **Acknowledge Limits**: If search fails, ask the user for a pointer *after* proving you tried.
