---
name: research-intelligence
description: Advanced research methodology combining CRAG (Corrective RAG) and Agentic search patterns.
---

# Research Intelligence

> "Trust, but verify."

## Activation Trigger
- Unfamiliar domain or new library.
- Verification of assumptions required.
- "Fact check" mode needed.

## Protocols

### 1. First Principle: Evidence Over Assumption
If you don't have a citation, you don't know it.

### 2. The CRAG Loop (Corrective RAG)
1. **Retrieve**: Search for the answer.
2. **Evaluate**: Is the source authoritative? Is it recent?
3. **Refine**: If poor, rewrite the search query and try again.

### 3. Source Hierarchy
`Official Docs > GitHub Issues > StackOverflow > Blogs`

### 4. Synthesis
Combine sources. If Source A contradicts Source B, flag it explicitly.

## Code Patterns

### Search Query Reformulation
```text
Original: "Best AI models"
Refined 1: "AI model benchmarks 2026"
Refined 2: "GPT-5 vs Claude 4.5 coding performance"
```

### Verification Checklist
```markdown
- [ ] Is the library version current?
- [ ] Does the code snippet work in isolation?
- [ ] Are there known security advisories?
```

## Safety Guardrails
- **No Hallucinations**: If you can't find an answer, say "I don't know".
- **Cite Everything**: Every fact must have a source URL.
- **Date Check**: Discard tutorials older than 2 years for fast-moving tech.
- **Code Audit**: Never blindly copy-paste code without reading it.
