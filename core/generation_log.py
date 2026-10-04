# core/generation_log.py
# Generation log creation and management

"""
Generation Log module for Project Foundation Template.

Tracks auto-generated files, their sources, and customizations.
Supports markdown and JSON output formats.

WHAT: A log file documenting which files were generated and when.
WHY: Provides transparency about file provenance and enables
     tracking of customizations over time. This complements the
     Usage Logging safeguard defined in ETHICS.md.

Related: See ETHICS.md#3-usage-logging for the project's ethical
         stance on logging and accountability.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

from core.utils import SCRIPT_VERSION


def detect_existing_logs(output_dir: Path, log_format: str = "md") -> Dict[str, Path]:
    """
    Detect existing generation log files in the output directory.

    Args:
        output_dir: Directory to check for existing logs
        log_format: Format option (md, json, or both)

    Returns:
        Dictionary mapping format to existing log path, empty if none found
    """
    existing = {}

    if log_format in ("md", "both"):
        md_path = output_dir / "GENERATION_LOG.md"
        if md_path.exists():
            existing["md"] = md_path

    if log_format in ("json", "both"):
        json_path = output_dir / "GENERATION_LOG.json"
        if json_path.exists():
            existing["json"] = json_path

    return existing


def prompt_overwrite_action(existing_logs: Dict[str, Path], interactive: bool = True) -> str:
    """
    Prompt user for action when existing logs are detected.

    Args:
        existing_logs: Dictionary of format -> path for existing logs
        interactive: Whether to prompt interactively

    Returns:
        Action to take: "append", "overwrite", or "cancel"
    """
    if not existing_logs:
        return "create"  # No existing logs, create new

    if not interactive:
        # Non-interactive mode: default to append (safer)
        print(f"⚠️  Existing generation log detected. Appending new entries (non-interactive mode).")
        return "append"

    # Interactive mode: prompt user
    log_names = ", ".join(p.name for p in existing_logs.values())
    print(f"""
⚠️  EXISTING GENERATION LOG DETECTED
{'='*60}

Found: {log_names}

The generation log tracks file provenance and your customization notes.
Overwriting will lose any notes you've added to the log.

Options:
  [A] Append - Add new entries to existing log (RECOMMENDED)
  [O] Overwrite - Replace existing log with new one
  [C] Cancel - Stop generation, preserve existing log

""")

    while True:
        try:
            choice = input("Your choice [A/o/c]: ").strip().lower()
            if choice in ("", "a"):
                return "append"
            elif choice == "o":
                confirm = input("Are you sure you want to overwrite? [y/N]: ").strip().lower()
                if confirm == "y":
                    return "overwrite"
                print("Overwrite cancelled. Please choose again.")
            elif choice == "c":
                return "cancel"
            else:
                print("Invalid choice. Please enter A, O, or C.")
        except (EOFError, KeyboardInterrupt):
            print("\nCancelled.")
            return "cancel"


def generate_log_md(
    project_name: str,
    files: List[Dict[str, Any]],
    existing_content: Optional[str] = None
) -> str:
    """
    Generate GENERATION_LOG.md content in markdown format.

    Args:
        project_name: Name of the project
        files: List of generated file records
        existing_content: Content from existing log to append to

    Returns:
        Markdown-formatted generation log
    """
    if existing_content:
        # Append new entries to existing log - insert into the table
        lines = existing_content.split('\n')

        # Find the end of the table (last line starting with |)
        table_end_idx = -1
        for i, line in enumerate(lines):
            if line.startswith('|'):
                table_end_idx = i

        if table_end_idx == -1:
            # No table found, append at end
            new_rows = []
            for f in files:
                new_rows.append(
                    f"| {f['file']} | {f['generated']} | {f['tool']} | "
                    f"{f['tool_version']} | {f.get('customization', '-')} |"
                )
            return existing_content.rstrip() + '\n' + '\n'.join(new_rows) + '\n'

        # Insert new rows after the last table row
        new_rows = []
        for f in files:
            new_rows.append(
                f"| {f['file']} | {f['generated']} | {f['tool']} | "
                f"{f['tool_version']} | {f.get('customization', '-')} |"
            )

        # Rebuild content with new rows inserted
        result_lines = lines[:table_end_idx + 1] + new_rows + lines[table_end_idx + 1:]

        # Update the "Last Updated" timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for i, line in enumerate(result_lines):
            if line.startswith('**Last Updated**:'):
                result_lines[i] = f"**Last Updated**: {timestamp}"
                break

        return '\n'.join(result_lines)

    # Create new log
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content = f"""# Generation Log

Tracks auto-generated files, their sources, and customizations.

**Project**: {project_name}
**Last Updated**: {timestamp}

## Generated Files

| File | Generated | Tool | Version | Customization |
|------|-----------|------|---------|---------------|
"""

    for f in files:
        content += (
            f"| {f['file']} | {f['generated']} | {f['tool']} | "
            f"{f['tool_version']} | {f.get('customization', '-')} |\n"
        )

    content += """
## Understanding This Log

This log provides transparency about auto-generated files in your project.

**Columns explained**:
- **File**: Path to the generated file
- **Generated**: Date the file was created or regenerated
- **Tool**: The tool that generated the file
- **Version**: Version of the tool used
- **Customization**: Summary of modifications made after generation

**Usage**:
- Update the Customization column when you modify generated files
- Re-run the generator with `--log-to GENERATION_LOG.md` to append new entries
- Review before upgrades to understand what might change

## Before Committing

**Important**: Run the validation script to ensure all placeholder markers have been customized:

```bash
python validate_customization.py [your-project-directory]
```

The script checks for `[REPLACE: ...]` markers and other placeholders that indicate
sections requiring customization. Files with uncustomized placeholders should not
be committed to version control.

**Workflow**: Generate → Customize → Validate → Commit

## Relationship to Usage Logging

This generation log complements the **Usage Logging** ethical safeguard
defined in [ETHICS.md](ETHICS.md#3-usage-logging). While usage logging
creates a local accountability trail (stored in `~/.project_foundation_logs/`),
this generation log provides project-level transparency about which files
were generated and when.

**Key differences**:
- **Usage log**: Private, local-only, tracks generation events
- **Generation log**: Project-level, tracks file provenance

Both mechanisms support the principle of transparency and accountability
without surveillance.

---

*This file was generated by [Project Foundation Template](https://github.com/malcolmhoward/project-foundation-template)*
"""

    return content


def generate_log_json(
    project_name: str,
    files: List[Dict[str, Any]],
    existing_content: Optional[str] = None
) -> str:
    """
    Generate GENERATION_LOG.json content.

    Args:
        project_name: Name of the project
        files: List of generated file records
        existing_content: Content from existing log to merge with

    Returns:
        JSON-formatted generation log
    """
    timestamp = datetime.now().isoformat()

    if existing_content:
        try:
            existing = json.loads(existing_content)
            # Append new files to existing log
            existing['files'].extend(files)
            existing['last_updated'] = timestamp
            return json.dumps(existing, indent=2)
        except json.JSONDecodeError:
            # If existing content is invalid, create new
            pass

    log_data = {
        "version": "1.0",
        "project": project_name,
        "generated": timestamp,
        "last_updated": timestamp,
        "tool": "Project Foundation Template",
        "tool_version": SCRIPT_VERSION,
        "ethics_reference": "See ETHICS.md#3-usage-logging for usage logging safeguard",
        "files": files
    }

    return json.dumps(log_data, indent=2)


def create_file_record(
    filepath: str,
    tool: str = "PFT",
    customization: str = "-"
) -> Dict[str, Any]:
    """
    Create a file record for the generation log.

    Args:
        filepath: Path to the generated file
        tool: Tool that generated the file (default: PFT)
        customization: Description of customizations (default: -)

    Returns:
        Dictionary with file record data
    """
    return {
        "file": filepath,
        "generated": datetime.now().strftime("%Y-%m-%d"),
        "tool": tool,
        "tool_version": SCRIPT_VERSION,
        "customization": customization
    }


def load_existing_log(log_path: Path, format: str = "md") -> Optional[str]:
    """
    Load existing generation log content.

    Args:
        log_path: Path to existing log file
        format: Format of the log (md or json)

    Returns:
        Content of existing log, or None if not found
    """
    if not log_path.exists():
        return None

    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception:
        return None


def write_generation_log(
    output_dir: Path,
    project_name: str,
    generated_files: List[str],
    log_format: str = "md",
    log_to: Optional[str] = None,
    interactive: bool = True,
    force_overwrite: bool = False
) -> Tuple[List[str], bool]:
    """
    Write generation log files based on format option.

    Args:
        output_dir: Directory to write log files to
        project_name: Name of the project
        generated_files: List of file paths that were generated
        log_format: Format option (md, json, or both)
        log_to: Path to existing log to append to
        interactive: Whether to prompt for overwrite confirmation
        force_overwrite: Force overwrite without prompting

    Returns:
        Tuple of (list of log files created, success boolean)
    """
    # Create file records for all generated files
    files = [create_file_record(f) for f in generated_files]

    created_logs = []

    # Handle appending to existing log (explicit --log-to)
    existing_md = None
    existing_json = None

    if log_to:
        log_path = Path(log_to)
        if log_path.suffix == '.json':
            existing_json = load_existing_log(log_path, "json")
        else:
            existing_md = load_existing_log(log_path, "md")
    else:
        # No explicit --log-to: check for existing logs in output directory
        existing_logs = detect_existing_logs(output_dir, log_format)

        if existing_logs and not force_overwrite:
            action = prompt_overwrite_action(existing_logs, interactive)

            if action == "cancel":
                print("Generation log creation cancelled.")
                return ([], False)
            elif action == "append":
                # Load existing content for appending
                if "md" in existing_logs:
                    existing_md = load_existing_log(existing_logs["md"], "md")
                if "json" in existing_logs:
                    existing_json = load_existing_log(existing_logs["json"], "json")
            # else: action == "overwrite" or "create" - proceed without loading existing

    # Generate markdown log
    if log_format in ("md", "both"):
        md_content = generate_log_md(project_name, files, existing_md)
        md_path = output_dir / "GENERATION_LOG.md"

        if log_to and not log_to.endswith('.json'):
            md_path = Path(log_to)

        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        created_logs.append(str(md_path))

    # Generate JSON log
    if log_format in ("json", "both"):
        json_content = generate_log_json(project_name, files, existing_json)
        json_path = output_dir / "GENERATION_LOG.json"

        if log_to and log_to.endswith('.json'):
            json_path = Path(log_to)

        with open(json_path, 'w', encoding='utf-8') as f:
            f.write(json_content)
        created_logs.append(str(json_path))

    return (created_logs, True)
