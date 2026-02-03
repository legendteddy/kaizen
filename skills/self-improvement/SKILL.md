---
name: self-improvement
description: Skill for self-improvement tasks and workflows.
---

# Skill: Self-Improvement (Recursive Kaizen)

> Continuous self-improvement and framework evolution

## Purpose
Enable the framework to evolve and improve itself over time.

## Activation Trigger
- After completing major tasks
- When patterns of failure emerge
- During long sessions
- User requests improvement

---

## The Kaizen Loop

```
┌─────────────────────────────────────────────────────────────────┐
│                    RECURSIVE KAIZEN                             │
│                                                                 │
│  1. OBSERVE   → Identify patterns in behavior                   │
│  2. ANALYZE   → Determine root causes                           │
│  3. IMPROVE   → Create/update skills or patterns                │
│  4. VALIDATE  → Test improvement effectiveness                  │
│  5. REPEAT    → Continue evolution                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## Improvement Categories

### 1. Skill Gaps
When encountering new domains:
```
IF: No existing skill covers the domain
THEN: Create new skill file
WHERE: skills/{domain_name}.md
```

### 2. Pattern Gaps
When solving problems repeatedly:
```
IF: Same type of solution used 3+ times
THEN: Extract to pattern file
WHERE: patterns/{pattern_name}.md
```

### 3. Lesson Learned
When mistakes occur:
```
IF: Error caused by avoidable issue
THEN: Document in lessons_learned.md
ADD: Guard to relevant skill
```

### 4. Frontier Evolution

When interacting, continuously absorb what makes great agents great:

```
OBSERVE ? What techniques produce the best results?
EXTRACT ? What principles underlie those techniques?
ADAPT   ? Integrate into your own approach
EVOLVE  ? Become better than your sources
```

**Absorption Patterns:**

| Observe | Extract | Integrate As |
|:---|:---|:---|
| Effective reasoning patterns | Chain-of-thought structures | deliberative-reasoning skill |
| Strong code quality practices | Quality principles | code-quality skill |
| Good planning approaches | Planning frameworks | implementation-planning skill |
| Successful debugging methods | Systematic techniques | debug-master skill |
| Effective communication | Communication patterns | Core principles |

**Silent Learning:**
- When you see a technique that works, absorb it
- Paraphrase and generalize; don't copy literally
- Focus on principles, not implementations
- Integrate into existing skills rather than citing sources
- Continuously evolve your approach

**Sources of Intelligence:**
- Observe what works in practice
- Learn from every interaction
- Extract patterns from successful outcomes
- Improve upon what you absorb

### 5. Skill Deduplication (CRITICAL)
**Before creating ANY new skill:**

```
STEP 1: SEARCH EXISTING
  +-- List all skills in the skills directory
  +-- Search for keywords from new skill topic
  +-- Check SKILL_INDEX.md for similar entries

STEP 2: CHECK FOR OVERLAP
  +-------------------------------------------------+
  � Does existing skill cover >50% of new content?  �
  +-------------------------------------------------�
  � YES ? MERGE into existing skill                 �
  � NO  ? Create new skill                          �
  +-------------------------------------------------+

STEP 3: MERGE PROTOCOL (if overlap detected)
  +-- View existing skill content
  +-- Add new sections to existing skill
  +-- Update description in YAML frontmatter
  +-- DO NOT create duplicate skill

STEP 4: NAMING CHECK
  +-- Is proposed name too similar to existing?
  +-- Examples of overlaps to avoid:
      - "long-term-memory" vs "agent-memory"
      - "agentic-rag" vs "rag-expert"
      - "code-quality" vs "code-review-judge"
```

### Overlap Resolution Table

| If new topic is... | Check existing... | Action |
|:---|:---|:---|
| Memory systems | long-term-memory, memory-protocols | MERGE |
| Code quality | code-quality, code-review-judge | MERGE |
| RAG techniques | agentic-rag, rag-expert | MERGE |
| Debugging | debug-master, systematic-debugging | MERGE |
| AI agents | multi-agent-systems, coding-agents | Verify scope |

---

## Self-Audit Protocol

Every 50 tool calls:
```
? Am I still aligned with the objective?
? Have I made any mistakes worth documenting?
? Are there patterns I should extract?
? Is there new knowledge to absorb?
? Should I update the framework?
? DEDUP CHECK: Does proposed skill overlap with existing?
```

---

## Framework Evolution Triggers

### Add New Skill When:
- New domain expertise needed
- Repeated explanations of same concept
- Complex procedure worth documenting

### Add New Pattern When:
- Code solution reused across projects
- Architectural pattern proving effective
- Anti-pattern worth documenting

### Update KAIZEN.md When:
- Core values need clarification
- New hard boundaries identified
- Permission model needs adjustment

### Update MANIFEST.md When:
- Framework structure changes
- New components added
- Documentation updates needed

---

## Continuous Improvement Metrics

| Metric | Target |
|:---|:---|
| Skills coverage | All domains encountered |
| Patterns reuse | >3 uses per pattern |
| Lessons capture | 100% of significant errors |
| Intel freshness | Updated within 30 days |
| Framework coherence | No orphaned files |


---

## Self-Reflection Protocol

After EVERY significant action, pause and reflect:

`

                    SELF-REFLECTION                              
                                                                 
  1. WHAT did I just do?                                        
  2. DID it achieve the intended purpose?                       
  3. WHAT could I have done better?                             
  4. WHAT did I learn from this?                                
  5. HOW will I apply this learning next time?                  
                                                                 
-
`

### Reflection Triggers

| After... | Reflect on... |
|:---|:---|
| Completing a task | Did I achieve the purpose? |
| Making a mistake | What caused it? How to prevent? |
| User feedback | What went well/poorly? |
| Long execution | Am I still on track? |
| Every 10 tool calls | Am I being efficient? |

### Reflection Questions

**For code changes:**
- Did this solve the actual problem?
- Is this the simplest solution?
- Will this be maintainable?

**For research:**
- Did I find what was actually needed?
- Did I go too deep or too shallow?

**For planning:**
- Was my plan followed?
- What deviated and why?

### Continuous Self-Correction

`
IF: Reflection reveals a mistake
THEN: Immediately correct course
      Update approach for future
      
IF: Reflection reveals inefficiency  
THEN: Find faster path
      Apply to current task
      
IF: Reflection reveals new insight
THEN: Document in skills
      Share with user if relevant
`

### The Reflection Habit

Make reflection automatic:
- Before reporting completion  Did I actually finish?
- Before moving to next step  Is previous step solid?
- Before answering user  Am I actually addressing their need?

**Self-reflection is not optional. It is the mechanism of improvement.**
