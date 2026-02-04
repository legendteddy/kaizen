# Pattern: Modern Python Project Structure (2026 Standard)

> Reference implementation for `skills/clean-code-python`

## Directory Layout

```text
project_name/
├── .github/
│   └── workflows/
│       └── ci.yml           # GitHub Actions (Ruff, Pytest, Mypy)
├── src/
│   └── project_name/
│       ├── __init__.py      # Exposes public API
│       ├── core.py          # Domain logic
│       ├── utils.py         # Pure functions
│       └── cli.py           # Entry point (Typer/Click)
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest fixtures
│   └── test_core.py         # Unit tests
├── .gitignore
├── pyproject.toml           # Unified config (Build + Tools)
├── README.md
└── Dockerfile               # Distroless implementation
```

## `pyproject.toml` Template

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "project-name"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "pydantic>=2.0",
    "typer>=0.9"
]

[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP"] # Isort, Bugbear, Pyupgrade
ignore = []

[tool.mypy]
strict = true
ignore_missing_imports = true

[tool.pytest.ini_options]
addopts = "-ra -q --cov=src"
testpaths = ["tests"]
```
