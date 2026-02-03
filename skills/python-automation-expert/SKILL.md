---
name: python-automation-expert
description: Skill for writing robust, safe, and maintainable Python automation scripts and CLI tools.
---

# Skill: Python Automation Expert (v1.0)

## Purpose
Write "Set and Forget" scripts. Automation code must be more robust than application code because it often runs unmonitored.

## Activation Trigger
- "Write a script to..."
- "Automate this..."
- "Scrape this website..."
- "Organize these files..."

---

## Protocol: The "Robutness" Checklist

### 1. Logging (Not Print)
**Rule:** Never use `print()`. Use `logging`.
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Usage
logger.info("Starting job...")
```

### 2. Argument Parsing
**Rule:** Use `argparse` or `typer`. Never hardcode paths.
```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True, help="Input directory")
parser.add_argument("--dry-run", action="store_true", help="Simulate only")
args = parser.parse_args()
```

### 3. Error Handling (Graceful Exit)
**Rule:** Catch expected errors and exit with code 1.
```python
import sys

try:
    process_files(args.input)
except FileNotFoundError:
    logger.error("Directory not found.")
    sys.exit(1)
```

### 4. Dry Run Mode
**Rule:** Every destructive script MUST have a `--dry-run` flag.
```python
if args.dry_run:
    logger.info(f"[DRY RUN] Would delete: {file_path}")
else:
    os.remove(file_path)
```

---

## Template: Safe File Processor

```python
from pathlib import Path

def scan_and_process(directory: Path):
    for file in directory.glob("**/*.txt"):
        if file.name.startswith("."): 
            continue # Skip hidden
        
        logger.info(f"Processing {file.name}")
        # ... logic ...
```
