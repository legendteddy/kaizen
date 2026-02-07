---
name: agent-cowork
description: Sovereign agentic automation pattern. Enables non-programmers to build apps and automate complex tasks via conversational AI.
---

# Protocol: Agent Cowork (Sovereign Automation)

> "Turn intent into action. No code required."

## Purpose
This skill enables Claude/Gemini agents to function as a full-stack task automation platform:
- **App Creation**: Build mini-applications via conversation
- **Task Automation**: Automate legal, finance, data, and operations workflows
- **File System Access**: Direct manipulation of local files and data
- **Plugin Architecture**: Modular extension via domain-specific tools

## Activation Trigger
- User asks to "automate," "build," or "create an app for..."
- Request involves multi-step workflows (legal docs, data pipelines, reports)
- User wants to "do what Claude Cowork does"

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    AGENT COWORK LAYER                            │
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Conversational Interface (Natural Language → Action)     │   │
│  └───────────────────────────────────────────────────────────┘   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────┐   │
│  │ MEM      │  │ COMPUTER │  │ SUBAGENT │  │ DATA           │   │
│  │ (Memory) │  │ (GUI)    │  │ (Multi)  │  │ (Analytics)    │   │
│  └──────────┘  └──────────┘  └──────────┘  └────────────────┘   │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────────────┐   │
│  │  Sovereign Memory Engine (GraphRAG + CRAG)                │   │
│  │  - Knowledge persistence                                  │   │
│  │  - Context recall                                         │   │
│  │  - Entity extraction                                      │   │
│  └───────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core Capabilities

### 1. Document Automation
| Task | Method |
|------|--------|
| Contract review | Extract clauses → Compare to templates → Flag risks |
| Due diligence | Parse docs → Build entity graph → Generate report |
| Summarization | Chunk → Embed → Synthesize with citations |

### 2. Data Pipeline
| Task | Method |
|------|--------|
| ETL | Read source → Transform (clean, join) → Write target |
| Reporting | Query data → Visualize → Generate PDF/HTML |
| Analysis | Load → EDA (data-intelligence-pro) → Insights |

### 3. Operations Automation
| Task | Method |
|------|--------|
| File organization | Scan → Classify → Move/rename |
| Batch processing | Queue → Transform → Export |
| Scheduling | Cron-like triggers → Execute workflows |

### 4. App Generation
| Task | Method |
|------|--------|
| Web dashboard | Define schema → Generate React/HTML → Deploy |
| CLI tool | Specify commands → Generate Python → Package |
| API wrapper | Parse docs → Generate client → Test |

---

## Integration Points

### Memory (Required)
```powershell
# Boot the memory engine
cd C:\Users\thoma\.gemini\sovereign-engine
.\start_engine.bat
```

### REST API
```bash
# Save context
curl -X POST http://localhost:8787/ingest -d '{"content": "..."}'

# Recall context
curl -X POST http://localhost:8787/search -d '{"query": "..."}'

# Deep reflection
curl -X POST http://localhost:8787/reflect -d '{"topic": "..."}'
```

### Terminal Interface
```powershell
# Direct CLI access
cd C:\Users\thoma\.gemini\sovereign-engine
.\link.bat
```

---

## Workflow Pattern

### The "Intent → Plan → Execute → Verify" Loop

1. **INTERPRET**: Parse user intent into atomic tasks
   ```
   "Organize my downloads folder by file type"
   → Tasks: [scan_dir, classify_files, create_folders, move_files]
   ```

2. **PLAN**: Determine tool sequence and dependencies
   ```
   Task 1: list_dir("Downloads")
   Task 2: classify by extension → group
   Task 3: mkdir for each type
   Task 4: move files
   ```

3. **EXECUTE**: Run with checkpoints
   - Save progress after each major step
   - Handle errors gracefully

4. **VERIFY**: Confirm success
   - Compare before/after state
   - Report results to user

---

## Plugin Architecture

Plugins extend Cowork capabilities. Each plugin is a skill that follows:

```yaml
# plugins/legal/PLUGIN.md
name: legal-automation
domain: legal
capabilities:
  - contract_review
  - due_diligence
  - clause_extraction
entry_point: run_legal_task(task_type, documents)
```

### Available Plugins (via Kaizen Skills)
| Domain | Skill | Capabilities |
|--------|-------|--------------|
| Memory | `mem` | GraphRAG, CRAG, persistence |
| Data | `data-intelligence-pro` | EDA, statistics, insights |
| GUI | `computer-use` | Click, type, screenshot |
| Multi-Agent | `subagent-orchestration` | Parallel execution |
| Web | `web-development` | HTML, CSS, JS apps |
| API | `fastapi-expert` | Backend services |
| **Legal** | `legal-automation` | Contract review, due diligence, clause extraction |
| **Finance** | `finance-automation` | Tax prep, bookkeeping, financial modeling |


---

## Security & Governance

| Rule | Enforcement |
|------|-------------|
| File access | Only user-approved directories |
| Network | No external calls without explicit approval |
| Deletion | Always require confirmation for destructive ops |
| Secrets | Never log or echo API keys |

---

## Example Workflows

### Legal: Contract Review
```
User: "Review this contract for non-standard clauses"
Agent:
1. Load contract.pdf → Extract text
2. Invoke legal patterns → Identify clauses
3. Compare to standard templates (from memory)
4. Generate risk report with citations
```

### Data: Sales Report
```
User: "Create a weekly sales dashboard from sales.csv"
Agent:
1. Load sales.csv → Parse with pandas
2. Run EDA (data-intelligence-pro)
3. Generate HTML dashboard with charts
4. Save to reports/ → Open in browser
```

### Ops: File Organization
```
User: "Sort my downloads by type and date"
Agent:
1. Scan Downloads/ → Classify files
2. Create folders: Images/, Docs/, Archives/, 2024/, 2025/
3. Move files → Verify counts
4. Report: "Organized 247 files into 5 categories"
```

---

## Action Checklist
- [ ] Is the Sovereign Memory Engine running?
- [ ] Did I parse user intent into atomic tasks?
- [ ] Am I using existing skills (mem, data, computer-use)?
- [ ] Did I checkpoint progress for long workflows?
- [ ] Did I verify results before reporting success?

---

## Related Skills
- [Mem (Memory)](../mem/SKILL.md)
- [Computer Use](../computer-use/SKILL.md)
- [Subagent Orchestration](../subagent-orchestration/SKILL.md)
- [Data Intelligence Pro](../data-intelligence-pro/SKILL.md)
- [Agent Architecture](../agent-architecture/SKILL.md)
