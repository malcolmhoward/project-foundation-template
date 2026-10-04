# Safe PR Chain Rebase Pattern

A pattern for safely rebasing a chain of dependent branches while preserving unique content in each branch.

## Problem Statement

When rebasing a chain of branches (e.g., v2.7.0 → v2.8.0 → ... → v3.7.0), naive conflict resolution using `git checkout <parent> -- <file>` can **silently discard unique content** from child branches.

**Example regression**: A governance definition added in v3.1.0's README was lost when rebasing v3.2.0+ because conflicts were resolved by taking the parent's version without checking what the child branch uniquely contributed.

## The Pattern: Orchestrator + Sub-agents

```
Root Session (Orchestrator):
├── Define goal: "Rebase chain with [specific changes]"
├── Launch Sub-agent 1: "Catalog unique content per branch"
├── Launch Sub-agent 2: "Execute rebase with preservation checklist"
├── Launch Sub-agent 3: "Verify no regressions post-rebase"
└── Synthesize results and report
```

### Why This Works

| Problem | Solution |
|---------|----------|
| Context rot during long sessions | Fresh context per sub-agent |
| Accumulated blind spots | Each agent focuses on one task |
| Lost awareness of branch-specific content | Explicit cataloging before changes |
| Silent regressions | Dedicated verification step |

---

## Phase 1: Catalog Unique Content

**Sub-agent prompt:**
```
Catalog the unique content in each branch of the PR chain.

For each branch from [start] to [end]:
1. Check out the branch
2. Compare against its parent: `git diff <parent-branch>...<branch> --stat`
3. For key files (README, CHANGELOG, etc.), extract UNIQUE additions
4. Document: "Branch X adds: [specific content]"

Output: A preservation checklist showing what each branch uniquely contributes.
```

**Example output:**
```markdown
## Branch Content Catalog

### feat/v3.1.0-accessibility
Parent: feat/v3.0.0-entrypoint
Unique additions:
- README.md: Governance definition blockquote (lines 5-6)
- README.md: GLOSSARY.md link in docs table
- New files: core/principles/glossary.py, core/principles/maintainers.py

### feat/v3.2.0-documentation
Parent: feat/v3.1.0-accessibility
Unique additions:
- README.md: v3.2.0 version history entry
- New files: core/guides/developer_handbook.py, etc.

[...continue for all branches...]
```

---

## Phase 2: Execute Rebase with Preservation

**Sub-agent prompt:**
```
Execute the rebase chain while preserving unique content.

You have a preservation checklist from Phase 1. For each branch:

1. Check out branch: `git checkout <branch>`
2. Start rebase: `git rebase <parent>`
3. For EACH conflict:
   a. Check the preservation checklist - does this file have unique content?
   b. If YES: Manually merge, preserving the unique content
   c. If NO: Safe to take parent version
4. After rebase, verify unique content still exists
5. Amend commit if needed to include any required updates
6. Document any issues encountered

CRITICAL: Never blindly run `git checkout <parent> -- <file>` without
checking the preservation checklist first.
```

**Conflict Resolution Decision Tree:**
```
Conflict in <file>?
├── Is <file> in preservation checklist for this branch?
│   ├── YES → Manual merge required
│   │         1. Open both versions
│   │         2. Identify unique content from child
│   │         3. Merge parent changes + child unique content
│   │         4. Verify result contains both
│   └── NO → Safe to take parent version
│             `git checkout <parent> -- <file>`
└── Continue to next conflict
```

---

## Phase 3: Verify No Regressions

**Sub-agent prompt:**
```
Verify the rebase preserved all unique content.

Using the preservation checklist from Phase 1:

1. For each branch, verify its unique content still exists:
   - Check specific lines/sections documented in checklist
   - Use `grep` or `git show` to confirm content presence

2. Run any existing tests: `pytest` or equivalent

3. Compare final branch against original (pre-rebase):
   - `git diff <original-commit>..<rebased-commit>`
   - Flag any unexpected removals

4. Spot-check key files manually

Output: Regression report listing any missing content or unexpected changes.
```

---

## Quick Reference: Safe Rebase Commands

```bash
# Before starting - save original commit hashes
git log --oneline feat/v3.1.0..feat/v3.7.0 > /tmp/original-commits.txt

# During rebase - check what's unique to current branch
git diff <parent>...HEAD -- <conflicted-file>

# After conflict - verify unique content preserved
git show HEAD:<file> | grep "expected unique content"

# After all rebases - compare to original
git diff <original-v3.7.0-hash>..HEAD --stat
```

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It's Dangerous | Alternative |
|--------------|-------------------|-------------|
| `git checkout <parent> -- .` | Discards ALL child changes | Resolve file-by-file |
| Resolving conflicts without checklist | May discard unique content | Always check preservation list |
| Skipping verification phase | Regressions go unnoticed | Always verify post-rebase |
| Single long session for complex rebase | Context rot causes oversights | Use sub-agents with fresh context |

---

## Template: Rebase Session Plan

```markdown
# Rebase Plan: [Description]

## Goal
[What changes need to be propagated through the chain]

## Branch Chain
- [ ] feat/v2.7.0 (base)
- [ ] feat/v2.8.0
- [ ] ...
- [ ] feat/v3.7.0 (head)

## Phase 1: Catalog (Sub-agent)
- [ ] Document unique content per branch
- [ ] Create preservation checklist

## Phase 2: Execute (Sub-agent)
- [ ] Rebase each branch
- [ ] Resolve conflicts per checklist
- [ ] Verify after each branch

## Phase 3: Verify (Sub-agent)
- [ ] Run regression checks
- [ ] Compare against originals
- [ ] Document any issues

## Phase 4: Push (Root)
- [ ] Review sub-agent reports
- [ ] Force push all branches
- [ ] Update PRs if needed
```

---

## Related Patterns

- [Bulk GitHub Issue Updates](./update-github-issues.sh) - For updating many issues
- [Context Health Strategy](./README.md) - Orchestrator + sub-agent pattern

---

*This pattern was developed after experiencing content loss during a rebase cascade in January 2026. The governance definition added in v3.1.0 was accidentally removed when conflicts were resolved by taking parent versions without checking for unique child content.*
