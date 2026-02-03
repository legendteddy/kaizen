---
name: git-workflow
description: Comprehensive Git best practices including branching, Conventional Commits, worktrees, and professional version control standards.
---

# Git Workflow

> Professional version control for clean history and team collaboration.

## Branching Strategy

```
main ─────────────────────────────────────→
       \                    /
        feature/add-auth ──→ (merge)
```

### Branch Naming
```
feature/add-user-auth
bugfix/fix-login-crash
hotfix/security-patch
refactor/cleanup-database
```

---

## Commit Messages (Conventional Commits)

### Format
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Rules:**
- **Type:** Required (feat, fix, docs, style, refactor, test, chore)
- **Scope:** Optional but encouraged for monorepos (e.g., `(frontend)`, `(core)`)
- **Description:** Imperative mood ("Add" not "Added"), max 50 characters
- **Body:** Wrap at 72 characters, explain what and why

### Types
| Type | Use For |
|:---|:---|
| feat | New feature |
| fix | Bug fix |
| docs | Documentation only |
| style | Formatting/whitespace changes |
| refactor | Code restructuring without logic change |
| test | Adding or updating tests |
| chore | Maintenance, tooling, build changes |

### Examples
```bash
# Good
feat(auth): add JWT login support

fix(api): handle null user response

docs(readme): update installation steps

# Bad (don't do these)
feat: added login support        # "Added" not imperative
fix: bug                       # Too vague
feat(auth): some changes         # No scope, vague description
```

---

## Git Worktrees

For parallel development on multiple branches:
```bash
# Create worktree for a feature
git worktree add ../feature-auth feature/add-auth

# Work in parallel directories
cd ../feature-auth
# ... make changes ...

# Remove when done
git worktree remove ../feature-auth
```

---

## Common Operations

### Undo Last Commit (keep changes)
```bash
git reset --soft HEAD~1
```

### Interactive Rebase (clean history)
```bash
git rebase -i HEAD~3
```

### Stash Changes
```bash
git stash push -m "work in progress"
git stash pop
```

---

## Pre-Push Checklist
```
□ All tests pass
□ No debug code left (console.log, debuggers)
□ Commit messages follow Conventional Commits format
□ Commits are in imperative mood
□ Branch is up to date with main
□ No secrets or credentials in commits
```

---

## Capabilities

- Generate compliant commit messages from `git diff`
- Manage complex rebase/merge conflicts
- Create standard Release Notes / Changelogs
- Enforce branch naming conventions
- Review commit history for quality
