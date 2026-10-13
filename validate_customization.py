#!/usr/bin/env python3
"""
validate_customization.py - Validate PFT-generated files are properly customized.

This script scans generated files for placeholder markers like [REPLACE:...]
that indicate sections requiring customization before committing.

Usage:
    python validate_customization.py [directory]
    python validate_customization.py --help

Examples:
    # Validate current directory
    python validate_customization.py

    # Validate specific directory
    python validate_customization.py ./my-project

    # Validate and show detailed output
    python validate_customization.py --verbose ./my-project

    # Use as pre-commit hook (exits non-zero if issues found)
    python validate_customization.py --strict

Exit Codes:
    0 - All files are properly customized (or no generated files found)
    1 - Uncustomized placeholder markers found
    2 - Error (invalid arguments, directory not found, etc.)
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, NamedTuple


# Patterns indicating uncustomized template sections
PLACEHOLDER_PATTERNS = [
    (r'\[REPLACE:.*?\]', 'Template placeholder'),
    (r'\[TODO:.*?\]', 'TODO marker'),
    (r'TEMPLATE NOTICE:', 'Template notice comment'),
    (r'<your.*?here>', 'Generic placeholder'),
]

# File extensions to scan
SCANNABLE_EXTENSIONS = {
    '.md', '.txt', '.rst',  # Documentation
    '.yml', '.yaml',         # Config files
    '.json',                 # Config files (be careful with data)
    '.py', '.js', '.ts',     # Code with potential doc comments
}

# Files to always scan regardless of extension
ALWAYS_SCAN = {
    'README', 'CONTRIBUTING', 'CHANGELOG', 'LICENSE',
    'CODE_OF_CONDUCT', 'SECURITY', 'CLAUDE',
}

# Directories to skip
SKIP_DIRECTORIES = {
    '.git', 'node_modules', '__pycache__', '.venv', 'venv',
    'build', 'dist', '.tox', '.eggs', '*.egg-info',
    'pft-output',  # Skip PFT output directories (raw templates)
}


class Finding(NamedTuple):
    """A single finding of uncustomized content."""
    file_path: str
    line_number: int
    pattern_type: str
    matched_text: str
    line_content: str


def should_scan_file(file_path: Path) -> bool:
    """Determine if a file should be scanned."""
    # Check if in skip directory
    for part in file_path.parts:
        if part in SKIP_DIRECTORIES:
            return False

    # Check extension
    if file_path.suffix.lower() in SCANNABLE_EXTENSIONS:
        return True

    # Check if it's a known file regardless of extension
    if file_path.stem.upper() in ALWAYS_SCAN:
        return True

    return False


def scan_file(file_path: Path) -> List[Finding]:
    """Scan a single file for placeholder patterns."""
    findings = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            for line_num, line in enumerate(f, start=1):
                for pattern, pattern_type in PLACEHOLDER_PATTERNS:
                    matches = re.finditer(pattern, line, re.IGNORECASE)
                    for match in matches:
                        findings.append(Finding(
                            file_path=str(file_path),
                            line_number=line_num,
                            pattern_type=pattern_type,
                            matched_text=match.group(),
                            line_content=line.strip()[:100]  # Truncate long lines
                        ))
    except (IOError, OSError) as e:
        print(f"Warning: Could not read {file_path}: {e}", file=sys.stderr)

    return findings


def scan_directory(directory: Path, verbose: bool = False) -> List[Finding]:
    """Scan a directory recursively for placeholder patterns."""
    all_findings = []
    files_scanned = 0

    for root, dirs, files in os.walk(directory):
        # Remove skip directories from dirs to prevent descending into them
        dirs[:] = [d for d in dirs if d not in SKIP_DIRECTORIES]

        for filename in files:
            file_path = Path(root) / filename
            if should_scan_file(file_path):
                if verbose:
                    print(f"Scanning: {file_path}", file=sys.stderr)
                findings = scan_file(file_path)
                all_findings.extend(findings)
                files_scanned += 1

    if verbose:
        print(f"Scanned {files_scanned} files", file=sys.stderr)

    return all_findings


def format_findings(findings: List[Finding], verbose: bool = False) -> str:
    """Format findings for display."""
    if not findings:
        return "All files are properly customized."

    lines = []
    lines.append(f"Found {len(findings)} uncustomized placeholder(s):\n")

    # Group by file
    by_file: dict = {}
    for f in findings:
        if f.file_path not in by_file:
            by_file[f.file_path] = []
        by_file[f.file_path].append(f)

    for file_path, file_findings in sorted(by_file.items()):
        lines.append(f"\n{file_path}:")
        for finding in file_findings:
            lines.append(f"  Line {finding.line_number}: {finding.matched_text}")
            if verbose:
                lines.append(f"    Type: {finding.pattern_type}")
                lines.append(f"    Context: {finding.line_content}")

    lines.append("\n" + "=" * 60)
    lines.append("ACTION REQUIRED: Customize the above placeholders before committing.")
    lines.append("Replace [REPLACE: ...] markers with your project-specific content.")
    lines.append("=" * 60)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Validate PFT-generated files are properly customized.",
        epilog=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        'directory',
        nargs='?',
        default='.',
        help='Directory to scan (default: current directory)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output including file scanning progress'
    )
    parser.add_argument(
        '-s', '--strict',
        action='store_true',
        help='Strict mode: exit with code 1 if any placeholders found'
    )
    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Quiet mode: only output if issues found'
    )
    parser.add_argument(
        '--version',
        action='version',
        version='validate_customization.py v1.0.0 (PFT v3.7.0)'
    )

    args = parser.parse_args()

    directory = Path(args.directory)
    if not directory.exists():
        print(f"Error: Directory not found: {directory}", file=sys.stderr)
        sys.exit(2)

    if not directory.is_dir():
        print(f"Error: Not a directory: {directory}", file=sys.stderr)
        sys.exit(2)

    findings = scan_directory(directory, verbose=args.verbose)

    if findings:
        print(format_findings(findings, verbose=args.verbose))
        if args.strict:
            sys.exit(1)
    elif not args.quiet:
        print("All files are properly customized.")

    sys.exit(0)


if __name__ == '__main__':
    main()
