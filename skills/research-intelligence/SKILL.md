---
name: research-intelligence
description: Advanced research methodology combining CRAG (Corrective Retrieval-Augmented Generation), agentic RAG patterns, and proactive web research for accurate, up-to-date solutions.
---

# Research Intelligence

> Advanced research methodology for accurate, verified information retrieval.

## When to Research

**Proactive Triggers:**
- Unfamiliar libraries or APIs not in codebase
- Specific errors (search error message + "solution")
- Version-sensitive libraries (check latest stable API)
- Multiple approaches possible (search "best practices")
- User asks about external tools, docs, or world knowledge

**Always Search First:**
If in doubt about any technical detail → Research before proposing a plan.

---

## Evolution: Research Methodology

```
Traditional Search:
Query → Search → Use First Result → Done

Corrective RAG (CRAG):
Query → Retrieve → Evaluate → 
  ↳ If poor: Refine query
  ↳ If good: Cross-check
  ↳ If wrong: Deep search fallback
→ Synthesize → Verify

Agentic RAG (2026):
Query → Plan → Retrieve → Evaluate →
  ↳ Reformulate query iteratively
  ↳ Route to different sources
  ↳ Self-reflect on relevance
→ Synthesize → Verify → Generate
```

---

## The CRAG Decision Tree

### 1. Initial Retrieval
**Action:** Execute `websearch` or `webfetch`.

### 2. Quality Evaluation (The Gate)
**Check:** Does the result directly answer the query or provide factual ground?

**CASE: ✅ Correct & High Confidence**
- Action: Proceed to synthesis
- Cross-check against second source
- Cite the source

**CASE: ⚠️ Ambiguous / Low Confidence**
- Action: Proactive Search Refinement
- Step: Rewrite query with specific technical terms
- Tools: `websearch` with `site:` filter (stackoverflow.com, docs, reddit)

**CASE: ❌ Incorrect / Irrelevant**
- Action: Deep Search Fallback
- Step: Search broader context/parent topics first
- Fallback: Search competitor/alternative solutions to confirm topic exists

---

## Agentic RAG Techniques

### 1. Iterative Retrieval
```
LOOP until satisfied:
  1. Retrieve documents
  2. Evaluate relevance
  3. If insufficient: reformulate query
  4. If good: synthesize
  5. Verify against sources
```

### 2. Query Reformulation
```
Original: "Best AI models"
Reformulated:
  - "AI model benchmarks 2026"
  - "frontier LLM comparison"
  - "GPT-5 vs Claude 4.5 performance"
```

### 3. Source Routing
Route queries to relevant sources based on type:

| Query Type | Best Sources |
|:---|:---|
| Technical docs | Official documentation, GitHub repos |
| Code examples | Stack Overflow, GitHub issues |
| News/updates | RSS feeds, tech blogs |
| Research | arXiv, papers, conferences |
| Community | Reddit, Discord, forums |

### 4. Self-Reflection Checklist
After retrieval, verify:
- [ ] Is this relevant to the query?
- [ ] Is this recent/current enough?
- [ ] Do I need more sources?
- [ ] Are there contradictions with other sources?
- [ ] Does this align with existing project context?

---

## Synthesis Rules

### 1. Don't Guess
If content is missing key parameters (API version, config syntax):
- **FETCH AGAIN** with specific question
- Don't fill gaps with assumptions

### 2. Cross-Check
If result contradicts `KAIZEN.md` or project context:
- Verify with second source
- Flag contradiction to user

### 3. Summarize & Collapse
Once high-confidence information found:
- Summarize findings concisely
- Discard "search noise" to preserve context
- Cite sources briefly (e.g., "Based on FastAPI v0.115 docs...")

### 4. Verify Syntax
Always verify syntax of third-party tools:
- Fetch latest `--help` output
- Check official examples
- Test commands if possible

---

## Tool Priorities

1. **`websearch`** — Broad discovery, find relevant sources
2. **`webfetch`** — Deep extraction, read full documentation
3. **`codesearch`** — Find code examples and patterns

---

## Capabilities

- Find and summarize technical documentation
- Extract code examples from GitHub issues and blogs
- Monitor for latest security patches or library updates
- Generate compliant solutions from `git diff` analysis
- Cross-reference multiple sources for verification
- Reformulate queries for better results

---

## For Sovereign Framework

Research Intelligence enables:
1. **Skill discovery**: Find relevant skills in the directory
2. **Context loading**: Dynamically retrieve relevant files
3. **Fact verification**: Cross-reference multiple sources
4. **Documentation**: Cite sources for all external knowledge
5. **Stay current**: Always use latest API versions and best practices

---

## Related Skills

- `docs-fetcher` → Deep documentation retrieval
- `decision-router` → When to research vs implement directly
- `verification` → Validate research findings before use
