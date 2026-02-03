---
name: python-automation-expert
description: Specialized skill for writing robust, safe, and maintainable Python automation scripts and CLI tools.
---

# Python Automation Expert
Specialized skill for writing robust, safe, and maintainable Python automation scripts and CLI tools.

## Instructions
- **Paths:** Use `pathlib.Path` over `os.path` for object-oriented filesystem handling.
- **Shell Commands:** Use `subprocess.run(..., check=True)` for safe command execution. Avoid `os.system`.
- **Logging:** Use the `logging` module instead of `print` for script status.
- **CLI Args:** Use `argparse` or `typer` for handling command-line arguments.
- **Error Handling:** Wrap file I/O and external calls in `try/except` blocks to handle permission or missing file errors gracefully.

## Capabilities
- Can refactor "quick scripts" into production-ready CLI tools.
- Can automate batch file processing (renaming, converting).
- Can safe-guard destructive operations (deletes/moves) with dry-run flags.