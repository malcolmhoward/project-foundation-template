#!/bin/bash
# update-github-issues.sh
# Bulk update GitHub issues with templated content
#
# Usage: ./update-github-issues.sh
#
# This script demonstrates a pattern for bulk-updating GitHub issues
# with version-specific or category-specific content.
#
# Prerequisites:
#   - GitHub CLI (gh) installed and authenticated
#   - Appropriate repository permissions

set -e

# Configuration
REPO_OWNER="malcolmhoward"
REPO_NAME="project-foundation-template"

# Function to update a single issue with templated content
update_issue() {
    local issue_num=$1
    local version=$2
    local risks="$3"
    local residual="$4"
    local mitigations="$5"
    local anchor=$6

    echo "Processing issue #$issue_num (${version})..."

    # Get current issue body
    current_body=$(gh issue view $issue_num --json body -q '.body')

    # Remove existing section if present (adjust pattern as needed)
    # This uses awk to remove everything from "## Retroactive Ethical Review" to end
    cleaned_body=$(echo "$current_body" | awk '/^## Retroactive Ethical Review/{found=1} !found' | sed '$ { /^---$/d }')

    # Create new section (customize template as needed)
    new_section="
---

## Retroactive Ethical Review (Updated $(date +%Y-%m-%d))

This ethical review was conducted retroactively as part of implementing
PFT's Ethical Safeguards Process (see PR #76).

### Summary
- **Principle Zero**: ✅ Passes (risks identified and mitigated)
- **Educational Value**: ✅ Maintained
- **Identified Risks**: ${risks}
- **Accepted Residual Risks**: ${residual}
- **Mitigations**: ${mitigations}

**Full Review**: [docs/ethical-review/historical-audits.md#${anchor}](https://github.com/${REPO_OWNER}/${REPO_NAME}/blob/main/docs/ethical-review/historical-audits.md#${anchor})

---"

    new_body="${cleaned_body}${new_section}"

    # Update the issue
    gh issue edit $issue_num --body "$new_body" > /dev/null 2>&1
    echo "  Updated with ${version} content"
}

# Example: Update issues by version category
# Customize these sections based on your needs

echo "=== Starting bulk issue update ==="
echo ""

# v2.1.0 - Foundation Phase (Issues 1-6)
echo "--- v2.1.0 Foundation Phase ---"
for i in 1 2 3 4 5 6; do
    update_issue $i "v2.1.0" \
        "None identified (foundation phase)" \
        "None" \
        "N/A" \
        "foundation-v210"
done

# v2.2.0 - Core Infrastructure (Issues 7-10)
echo "--- v2.2.0 Core Infrastructure ---"
for i in 7 8 9 10; do
    update_issue $i "v2.2.0" \
        "Non-interactive mode could enable mass generation; easier automation lowers barrier for repo pollution" \
        "Automation misuse possible but benefits outweigh risks" \
        "Ethical agreement required, usage logging, template warnings, version expiration" \
        "v220---core-infrastructure-improvements"
done

# Add more version blocks as needed...

echo ""
echo "=== Bulk update complete ==="
