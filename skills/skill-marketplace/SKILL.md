---
name: skill-marketplace
description: Local-first packaging and installation of Kaizen skills using the `.kaizen` zip format.
version: 0.0.1
---

# Skill Marketplace (Local-First)

This skill defines the `.kaizen` package format and provides a local installer so you can ship skills as a single file and install them into `skills/`.

## Package Format: `.kaizen`

A `.kaizen` file is a ZIP archive that contains:
- `kaizen.json` (optional manifest at zip root)
- Either:
  - `<skill-name>/SKILL.md` (recommended) plus any other files under `<skill-name>/...`
  - `SKILL.md` at zip root (legacy; will install into `skills/<name>/SKILL.md`)

## CLI Tool

Tool: `tools/kaizen_market.py`

### Inspect a package
```bash
python tools/kaizen_market.py inspect path/to/something.kaizen
```

### Pack a skill directory
```bash
python tools/kaizen_market.py pack skills/my-skill --out dist/my-skill.kaizen
```

### Install a package
Run from repo root:
```bash
python tools/kaizen_market.py install dist/my-skill.kaizen
```

Notes:
- If the target folder already exists, it is moved to a timestamped backup `*.bak-YYYYMMDD-HHMMSS`.
- An install receipt is written to `skills/<skill>/.kaizen-install.json`.

