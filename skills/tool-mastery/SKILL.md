---
name: tool-mastery
description: Master the available tools for file operations, code search, web research, and bash commands. Understand capabilities, limitations, and best practices.
---

# Tool Mastery

> Optimal use of available tools for maximum efficiency.

## Activation Trigger
- Selecting the right tool for a task.
- Optimizing tool usage (reducing tokens).
- Debugging tool errors.

## Available Tools

### 1. File Operations
| Tool | Purpose | Best Practice |
|:---|:---|:---|
| `read` | Read file content | Use offset/limit for large files |
| `write` | Create new files | Overwrites existing files |
| `edit` | Modify existing files | Use for targeted changes |
| `glob` | Find files by pattern | Use `**/*.ext` for recursive search |

### 2. Code Search
| Tool | Purpose | Best Practice |
|:---|:---|:---|
| `grep` | Search file contents | Use regex for patterns |
| `codesearch` | Find code examples | Use for library/framework queries |

### 3. Web & Research
| Tool | Purpose | Best Practice |
|:---|:---|:---|
| `websearch` | Search the web | Use for current info, docs, examples |
| `webfetch` | Fetch URL content | Use for documentation, articles |

### 4. System Commands
| Tool | Purpose | Best Practice |
|:---|:---|:---|
| `bash` | Execute shell commands | Use for git, npm, testing, etc. |
| `skill` | Load a skill | Use to access domain expertise |

---

## Power Patterns

### Pattern: Parallel File Reading
Read multiple independent files at once:
```javascript
// Read concurrently (no dependencies between files)
read('file1.ts')
read('file2.ts')
read('config.json')
```

### Pattern: Search Then Read
Find relevant code efficiently:
```javascript
// 1. Search for pattern
grep('functionName', 'src/')

// 2. Read only matching files
read('src/matching-file.ts')
```

### Pattern: Verify After Edit
Always verify changes:
```javascript
// 1. Make edit
edit('file.ts', oldString, newString)

// 2. Verify the change
read('file.ts')
```

### Pattern: Batch Tool Calls
Submit multiple independent tool calls together:
```javascript
// These are independent - can run in parallel
read('package.json')
glob('**/*.test.ts')
grep('function_name', 'src/')
```

---

## Tool-Specific Best Practices

### `read` - File Reading
- ✅ Use `offset` and `limit` for large files (>100 lines)
- ✅ Read specific line ranges when you know what you need
- ❌ Don't read entire files when you only need a section

### `edit` - File Modification
- ✅ Provide unique strings with sufficient context
- ✅ Make minimal, targeted changes
- ❌ Don't use if you haven't read the file first
- ❌ Don't make multiple edits to the same file in parallel

### `write` - File Creation
- ✅ Use for new files only
- ✅ Provide complete, valid content
- ⚠️ Will overwrite existing files (use with caution)

### `glob` - File Discovery
- ✅ Use `**/*.ext` for recursive searches
- ✅ Use specific patterns to limit results
- ✅ Combine with `grep` to find files containing specific content

### `grep` - Content Search
- ✅ Use regex patterns: `function\s+\w+`
- ✅ Search in specific directories: `grep('pattern', 'src/')`
- ✅ Filter by file type: `include: '*.ts'`

### `websearch` - Web Research
- ✅ Use for current documentation
- ✅ Search for specific errors: `"error message" solution`
- ✅ Find best practices: `best practices for X in Y`

### `webfetch` - URL Content
- ✅ Fetch documentation pages
- ✅ Read blog posts, articles
- ✅ Verify API examples

### `bash` - Shell Commands
- ✅ Use for git operations
- ✅ Run tests: `npm test`, `pytest`
- ✅ Check status: `git status`, `ls -la`
- ⚠️ Be careful with destructive commands

---

## Anti-Patterns

| Bad Practice | Why It's Wrong | Good Practice |
|:---|:---|:---|
| Edit files in parallel | Race conditions, conflicts | Sequential edits to same file |
| Reading without searching first | Wastes tokens | Use `grep` to find relevant sections |
| Not verifying edits | Silent failures | Always `read` after `edit` |
| Overly broad glob patterns | Too many results | Narrow with specific paths |
| Web search for codebase questions | Inefficient | Use `grep` and `read` first |
| Bash for file reading | Unnecessary | Use `read` tool directly |

---

## When to Use Which Tool

### Finding Code
1. **Know the filename?** → `read`
2. **Know part of content?** → `grep`
3. **Looking for file patterns?** → `glob`
4. **Need external examples?** → `codesearch`

### Reading Code
1. **Small file (<100 lines)?** → `read` (whole file)
2. **Large file?** → `read` with offset/limit
3. **Just need structure?** → `read` first 50 lines
4. **Multiple files?** → Parallel `read` calls

### Modifying Code
1. **New file?** → `write`
2. **Existing file, small change?** → `edit`
3. **Major refactor?** → Multiple sequential `edit` calls
4. **Always verify!** → `read` after changes

### Research
1. **Internal codebase question?** → `grep` + `read`
2. **Documentation lookup?** → `webfetch`
3. **Best practices/examples?** → `websearch`
4. **Code patterns?** → `codesearch`

---

## Tool Limitations

| Tool | Limitations |
|:---|:---|
| `read` | Max 2000 lines per call (use offset/limit) |
| `edit` | Requires unique string match |
| `glob` | Returns max ~1000 files |
| `grep` | Regex syntax may vary |
| `websearch` | May return stale results |
| `webfetch` | Some sites may block |
| `bash` | Platform-specific (Linux/Mac/Win differences) |

---

*"The right tool for the right job, used the right way."*


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
