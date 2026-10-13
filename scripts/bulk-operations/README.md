# Bulk Operations Scripts

Reusable scripts for bulk operations on GitHub issues, PRs, and other repository artifacts.

## Pattern: Bulk Issue/PR Updates

When you need to update many GitHub issues or PRs with similar content:

### 1. Define the Template

```bash
new_section="
---
## Your Section Title

Content here...
---"
```

### 2. Get Current Content

```bash
current_body=$(gh issue view $issue_num --json body -q '.body')
```

### 3. Clean Existing Section (if replacing)

```bash
# Remove from marker to end of file
cleaned_body=$(echo "$current_body" | awk '/^## Your Section Title/{found=1} !found')
```

### 4. Append New Section

```bash
new_body="${cleaned_body}${new_section}"
```

### 5. Update the Issue/PR

```bash
gh issue edit $issue_num --body "$new_body"
# or
gh pr edit $pr_num --body "$new_body"
```

## Available Scripts & Patterns

| File | Purpose |
|------|---------|
| `update-github-issues.sh` | Template for bulk issue updates with version-specific content |
| `safe-pr-chain-rebase.md` | Pattern for safely rebasing dependent branch chains without content loss |

## Best Practices

1. **Test on one issue first** before running bulk operations
2. **Use dry-run mode** when available (add `echo` before actual commands)
3. **Log progress** so you can resume if interrupted
4. **Handle rate limits** - GitHub API has rate limits, add delays if needed
5. **Verify results** - spot-check a few items after bulk update

## Context Health Note

For complex bulk operations during long Claude sessions:

1. **Use sub-agents** for execution (fresh context, no accumulated blind spots)
2. **Keep root session as orchestrator** (high-level goals, synthesis)
3. **Document the mapping** (e.g., which issues belong to which version)
4. **Verify before and after** (check a sample pre/post update)
