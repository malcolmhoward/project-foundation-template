#!/usr/bin/env bash
# update-github-issues.sh
# Bulk update GitHub issues with templated content
#
# Usage:
#   ./update-github-issues.sh --repo OWNER/NAME            # dry run: show proposed changes
#   ./update-github-issues.sh --repo OWNER/NAME --apply    # edit the issues
#
# This script demonstrates a pattern for bulk-updating GitHub issues with
# version-specific or category-specific content, here a retroactive ethical
# review section.
#
# WHAT: appends (or replaces) a section in each listed issue's body.
# WHY:  editing many issues by hand is slow and inconsistent.
# HOW:  copy this script, edit the update blocks at the bottom for your issues,
#       run it without --apply, read every proposed body, then run with --apply.
#
# Safeguards:
#   - Dry run by default: nothing is edited without --apply.
#   - The repository must be named explicitly with --repo.
#   - The review outcome is never filled in for you: each block's outcome
#     starts as a [REPLACE: ...] placeholder, and --apply refuses to run while
#     any placeholder remains. Record only the result of a review you did.
#
# Prerequisites:
#   - GitHub CLI (gh) installed and authenticated
#   - Permission to edit issues in the repository

set -euo pipefail

REPO=""
APPLY=0

while [ $# -gt 0 ]; do
    case "$1" in
        --repo)
            if [ $# -lt 2 ] || [ "${2#-}" != "$2" ]; then
                echo "--repo needs a value: --repo OWNER/NAME" >&2
                exit 2
            fi
            REPO="$2"; shift 2 ;;
        --apply) APPLY=1; shift ;;
        -h|--help) awk 'NR == 1 { next } /^#/ { sub(/^# ?/, ""); print; next } { exit }' "$0"; exit 0 ;;
        *) echo "Unknown option: $1" >&2; exit 2 ;;
    esac
done

if [ -z "$REPO" ]; then
    echo "Name the repository explicitly: --repo OWNER/NAME" >&2
    exit 2
fi
case "$REPO" in
    */*) ;;
    *) echo "--repo must be OWNER/NAME, not: $REPO" >&2; exit 2 ;;
esac

PREVIEW_DIR=$(mktemp -d)
FAILED=0
PREPARED=()

# Function to update a single issue with templated content
update_issue() {
    local issue_num=$1
    local version=$2
    local outcome="$3"
    local risks="$4"
    local residual="$5"
    local mitigations="$6"
    local anchor=$7

    echo "Issue #$issue_num (${version})"

    local current_body
    current_body=$(gh issue view "$issue_num" --repo "$REPO" --json body -q '.body')

    # Remove an existing section, from "## Retroactive Ethical Review" to the end
    local cleaned_body
    cleaned_body=$(printf '%s\n' "$current_body" | awk '/^## Retroactive Ethical Review/{found=1} !found' | sed '$ { /^---$/d }')

    local new_section="
---

## Retroactive Ethical Review (Updated $(date +%Y-%m-%d))

### Summary
- **Principle Zero**: ${outcome}
- **Identified Risks**: ${risks}
- **Accepted Residual Risks**: ${residual}
- **Mitigations**: ${mitigations}

**Full Review**: [docs/ethical-review/historical-audits.md#${anchor}](https://github.com/${REPO}/blob/main/docs/ethical-review/historical-audits.md#${anchor})

---"

    local new_body="${cleaned_body}${new_section}"
    local preview="$PREVIEW_DIR/issue-$issue_num.md"
    printf '%s\n' "$new_body" > "$preview"

    if printf '%s' "$new_section" | grep -q '\[REPLACE:'; then
        echo "  Contains [REPLACE: ...] placeholders: fill them in from your review first."
        FAILED=1
    fi
    echo "  Proposed body: $preview"
    PREPARED+=("$issue_num")
}

# Nothing is edited until every body has been prepared and checked
apply_updates() {
    local issue_num
    [ "${#PREPARED[@]}" -gt 0 ] || return 0
    local done_list=""
    for issue_num in "${PREPARED[@]}"; do
        if ! gh issue edit "$issue_num" --repo "$REPO" --body-file "$PREVIEW_DIR/issue-$issue_num.md"; then
            # Say exactly where it stopped, so the run can be resumed
            echo "Editing issue #$issue_num failed." >&2
            echo "Already updated:${done_list:- none}" >&2
            echo "Not updated: everything from #$issue_num on (bodies in $PREVIEW_DIR)" >&2
            exit 1
        fi
        echo "Updated issue #$issue_num"
        done_list="$done_list #$issue_num"
    done
}

# ---------------------------------------------------------------------------
# Update blocks: edit these for your issues. Each outcome must be the result
# of a review you carried out, not a default.
# ---------------------------------------------------------------------------

echo "=== Bulk issue update for $REPO ($([ "$APPLY" -eq 1 ] && echo "applying" || echo "dry run")) ==="

# Example: one block per issue (or loop over a list), with that issue's review
update_issue 1 "v2.1.0" \
    "[REPLACE: result of your Principle Zero review, e.g. Passes, with the reason]" \
    "[REPLACE: risks identified]" \
    "[REPLACE: risks accepted, and why]" \
    "[REPLACE: mitigations in place]" \
    "[REPLACE: anchor in historical-audits.md]"

echo ""
if [ "$FAILED" -ne 0 ]; then
    echo "No issues were edited: fill in every [REPLACE: ...] placeholder, then run again." >&2
    exit 1
fi
if [ "$APPLY" -eq 1 ]; then
    apply_updates
else
    echo "Dry run: no issues were edited. Review the proposed bodies in $PREVIEW_DIR, then run with --apply."
fi
