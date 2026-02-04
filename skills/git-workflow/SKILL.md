---
name: git-workflow
description: Professional version control standards (Branching, Commit Hygiene, Worktrees).
---

# Protocol: Git Workflow

> "History is written by the victors (who squash their commits)."

## Activation Trigger
- Committing code.
- Managing branches.
- Resolving conflicts.

## Protocols

### 1. First Principle: Atomic Commits
One commit = One logical change. Tests must pass at every commit point.

### 2. Branching Strategy
- `feat/feature-name`
- `fix/bug-name`
- `chore/maintenance`
- `refactor/code-cleanup`

### 3. Commit Message Hygiene (Conventional Commits)
`type(scope): imperative description`
Example: `feat(auth): add google sso login`

## Code Patterns

### Git Worktrees (Advanced)
Stop switching branches. Clone locally.
```bash
git worktree add ../hotfix-folder fix/critical-bug
# Protocol: Works in parallel directory
git worktree remove ../hotfix-folder
```

### The "Oh Shit" Fix (Reset Soft)
Undo the commit, keep the changes in staging.
```bash
git reset --soft HEAD~1
```

## Safety Guardrails
- **No Force Push**: Check `git push --force-with-lease` if you absolutely must.
- **No Secrets**: Check `git diff` for API keys before every commit.
- **Clean History**: Squash "wip" commits before merging to main.
- **CI Green**: Never merge broken tests.
- **Lock Files**: Always commit `package-lock.json` / `poetry.lock`.
