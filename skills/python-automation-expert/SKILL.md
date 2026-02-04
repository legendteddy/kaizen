---
name: python-automation-expert
description: Standards for robust, unmonitored automation scripts.
---

# Protocol: Python Automation Expert

> "If you do it twice, automate it."

## Activation Trigger
- Writing "set and forget" scripts.
- Data fetching/scraping.
- File system organization.

## Protocols

### 1. First Principle: Graceful Failure
Scripts run when you are asleep. They must fail loudly and safely.

### 2. Argument Parsing
Never hardcode paths. Use `argparse` or `typer`.

### 3. Dry Run Discipline
Destructive actions (delete, upload) MUST support `--dry-run`.

## Code Patterns

### The "Robutness" Scaffold
```python
import logging
import argparse
import sys

# Protocol: Logging, not print
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    try:
        run_job(dry_run=args.dry_run)
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
```

## Safety Guardrails
- **Dry Run Mandatory**: If it deletes file, it needs `--dry-run`.
- **Exit Codes**: Success = 0, Error = 1.
- **Pathlib**: Use `Path("foo/bar")`, not string manipulation.
- **Retries**: Network calls must have exponential backoff.
- **Limits**: Scrapers must have rate limits (sleep).
