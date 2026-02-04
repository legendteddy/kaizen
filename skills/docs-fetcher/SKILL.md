---
name: docs-fetcher
description: Protocol for retrieving, parsing, and applying external documentation.
---

# Protocol: Documentation Fetcher

> "Read the manual so the user doesn't have to."

## Activation Trigger
- Using a new library or tool.
- Encountering API deprecation errors.
- Verifying syntax for a specific version.

## When to Use
- User mentions a library/tool you don't know.
- You encounter an API error (deprecated methods).
- You need to verify syntax for a specific version (v1 vs v2).

## Targeted Retrieval Protocol

Never dump entire documentation into context. Use this precision flow:

### 1. Identify Critical Scope
Before fetching, define exactly what you need.
- **Wrong:** "Read pandas docs"
- **Right:** "Read pandas.DataFrame.merge parameters"

### 2. The Retrieval Loop
1. **Search** for official documentation URL (avoid 3rd party tutorials if official exists).
2. **Fetch** the `Quickstart` or `API Reference` page first.
3. **Scan** for keywords related to the task.
4. **Extract** ONLY the relevant function signatures and examples.
5. **Discard** marketing fluff, installation guides (unless installing), and unrelated features.

### Retrieval Pseudocode
```python
def precise_fetch(query):
    # 1. Google Search specific documentation
    url = search(f"{query} site:docs.python.org OR site:readthedocs.io")
    # 2. Scrape only the main content div
    content = scrape(url, selector="main.content")
    # 3. Summarize for API signatures
    return extract_signatures(content)
```

### 3. Context Optimization
| Content | Action |
|:---|:---|
| Function Signature | KEEP exact syntax |
| Code Example | KEEP, but minimize comments |
| Conceptual Guide | SUMMARIZE in 1-2 bullets |
| Deprecation Warnings | HIGHLIGHT as critical |

## Self-Correction Hook
If code written using fetched docs fails:
1. **Don't guess**.
2. Go back to docs.
3. Check **Version Number** (are you looking at v2 docs for v3 code?).
4. Check **Breaking Changes** log.

## Anti-Patterns
- **The "Whole Book" Error**: Reading the entire documentation site.
- **The "Hallucination" Error**: Guessing API methods because you're lazy to fetch.
- **The "Stale" Error**: Using training data knowledge instead of fetching live docs for rapidly moving tools (e.g., LangChain, Next.js).

## Self-Improvement
- **Did I fetch too much?** -> Refine search queries next time.
- **Did I miss a parameter?** -> Check function signature more carefully.
- **Is this a tool I use often?** -> Suggest creating a dedicated skill for it.

## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Agent Identity](../agent-identity/SKILL.md)
- [Stability Protocols](../stability-protocols/SKILL.md)
- [Safety Boundaries](../safety-boundaries/SKILL.md)
