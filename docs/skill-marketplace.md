# Skill Marketplace (Phase 18 Prep)

This repo is the Kaizen Skills Library. The Sovereign Engine/Dashboard can optionally expose an install UI, but the baseline capability is local-first:

- Package a skill as a single `.kaizen` file (ZIP)
- Install it into `skills/` with a safe extractor

## Why `.kaizen`

It is:
- Simple to build and inspect (ZIP + JSON)
- Works offline
- Safer than “copy this folder” workflows (path traversal checks, backups)

## Tooling

See:
- `tools/kaizen_market.py` (pack/install/inspect)
- `skills/skill-marketplace/SKILL.md`

## Manifest (Optional): `kaizen.json`

Example:
```json
{
  "name": "backup-docs",
  "version": "0.1.0",
  "description": "Back up Documents to D:",
  "author": "you",
  "created_at": "2026-02-06T21:00:00",
  "format": "kaizen-skill-zip-v1"
}
```

## Layout

Preferred:
```
kaizen.json
backup-docs/
  SKILL.md
  scripts/
    backup.py
```

Legacy (supported):
```
kaizen.json
SKILL.md
scripts/...
```

