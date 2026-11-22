#!/usr/bin/env python3
"""
Project Foundation Template v3.7.0

A tool for generating ethical project governance templates.

This is the main entrypoint for v3.7.0, replacing setup_foundation_lite.py.
It provides a clean, thin wrapper that delegates to the modular core package.

BREAKING CHANGES from v2.x:
    - New --preset option for governance level selection
    - New --plugins-dir option for custom extensions
    - New --list-* options for discovery
    - Modular architecture with core/ package

Usage:
    python generate_foundation.py --project-name "My Project" --author-name "Name"
    python generate_foundation.py --preset enterprise --all
    python generate_foundation.py --list-presets
    python generate_foundation.py --list-principles
    python generate_foundation.py --list-guides

Copyright (c) 2025 Malcolm Howard
Licensed under the Apache License, Version 2.0
Repository: https://github.com/malcolmhoward/project-foundation-template
"""

import json
import sys
import textwrap
from datetime import datetime
from pathlib import Path

# Configure UTF-8 output on Windows before any imports that might print
from core.utils import configure_windows_utf8, SCRIPT_VERSION, OFFICIAL_REPO

configure_windows_utf8()

# Core module imports
from core.config import (
    load_config,
    merge_config_with_args,
    parse_arguments,
    validate_arguments,
    apply_preset_to_args,
    include_option_help,
)

from core.generator import EthicalFoundationGenerator

from core.presets import (
    PRESETS,
    NO_PRESET,
    get_preset,
    list_presets as get_preset_names,
    get_preset_description,
)

from core.principles import (
    ALL_PRINCIPLES,
    PRINCIPLE_VERSIONS,
    CORE_PRINCIPLES,
    GOVERNANCE_PRINCIPLES,
    SECURITY_PRINCIPLES,
    COMMUNITY_PRINCIPLES,
    ADVANCED_PRINCIPLES,
    QUALITY_PRINCIPLES,
    COMPLIANCE_PRINCIPLES,
    INFRASTRUCTURE_PRINCIPLES,
    INCLUSIVITY_PRINCIPLES,
    LIFECYCLE_PRINCIPLES,
    USABILITY_PRINCIPLES,
    WORKFLOW_PRINCIPLES,
    AUTOMATION_PRINCIPLES,
    list_all_principles,
)

from core.guides import (
    ALL_GUIDES,
    GUIDE_COMPLEXITY,
    GOVERNANCE_GUIDES,
    DEVELOPMENT_GUIDES,
    SECURITY_GUIDES,
    COMMUNITY_GUIDES,
    ONBOARDING_GUIDES,
    OPERATIONS_GUIDES,
    PLANNING_GUIDES,
    list_all_guides,
)


def show_banner(quiet: bool = False):
    """Display the application banner."""
    if quiet:
        return

    print(f"""
================================================================================
     Project Foundation Template v{SCRIPT_VERSION}
     A tool for generating ethical project governance templates
================================================================================
""")


# Width of the help text column in the --list-presets "Adds:" list. With the option
# column before it, lines stay as wide as the hand-wrapped description lines.
LIST_HELP_WIDTH = 40


def show_presets():
    """Display available governance presets."""
    print("""
================================================================================
                        AVAILABLE GOVERNANCE PRESETS
================================================================================

Presets provide pre-configured sets of features for different project needs.
Use --preset <name> to apply a preset configuration.

""")

    for preset_name in get_preset_names():
        preset = get_preset(preset_name)
        desc = preset.get("description", "")
        principles = preset.get("principles", [])
        recommended = preset.get("recommended_for", [])

        print(f"  {preset_name.upper()}")
        print(f"  {'-' * 60}")
        print(f"  Description: {desc}")
        print(f"  Principles:  {len(principles)} included")
        if recommended:
            print(f"  Best for:    {', '.join(recommended[:2])}")
        if preset.get("note"):
            print(f"  Note:        {preset['note']}")
        print()

    # NO_PRESET is a choice, not a preset: list it after the five so the
    # recommended starting point is read first.
    print(f"  {NO_PRESET.upper()}")
    print(f"  {'-' * 60}")
    print("  Description: No preset. Generates the core files (README, LICENSE, CONTRIBUTING,")
    print("               .gitignore, FOUNDATION_NOTICE) plus the --include-* flags or --all")
    print(f"               given. On the command line, --preset {NO_PRESET} also overrides a preset")
    print("               set in the config file; leaving --preset out does not.")
    print("  Best for:    Choosing your governance file by file")
    print("  Note:        Start from 'standard' if you are unsure: it is the recommended")
    print("               starting point. Leaving a file out is a choice to make knowingly.")
    print("  Adds:        Each flag adds files, with or without a preset:")
    # --all first: it is the one flag that stands for most of the others.
    options = sorted(include_option_help(), key=lambda pair: pair[0] != "--all")
    for option, help_text in options:
        lines = textwrap.wrap(help_text, width=LIST_HELP_WIDTH)
        print(f"                 {option:<28} {lines[0]}")
        for line in lines[1:]:
            print(f"                 {'':<28} {line}")
    print()

    print("""
Usage: python generate_foundation.py --preset standard --project-name "My Project" --author-name "Name"

For more details on a specific preset, see the documentation.
""")


def show_principles():
    """Display available governance principles."""
    print("""
================================================================================
                      AVAILABLE GOVERNANCE PRINCIPLES
================================================================================

Principles define WHAT governance elements your project should have and WHY.
Each principle includes educational content explaining its importance.

""")

    # Group by category
    categories = [
        ("CORE (Always included)", CORE_PRINCIPLES),
        ("GOVERNANCE", GOVERNANCE_PRINCIPLES),
        ("SECURITY", SECURITY_PRINCIPLES),
        ("COMMUNITY", COMMUNITY_PRINCIPLES),
        ("ADVANCED", ADVANCED_PRINCIPLES),
        ("QUALITY", QUALITY_PRINCIPLES),
        ("COMPLIANCE", COMPLIANCE_PRINCIPLES),
        ("INFRASTRUCTURE", INFRASTRUCTURE_PRINCIPLES),
        ("INCLUSIVITY", INCLUSIVITY_PRINCIPLES),
        ("LIFECYCLE", LIFECYCLE_PRINCIPLES),
        ("DOCUMENTATION", USABILITY_PRINCIPLES),
        ("WORKFLOW", WORKFLOW_PRINCIPLES),
        ("TOOLING", AUTOMATION_PRINCIPLES),
    ]
    # Anything not in a category above still gets listed, so the output stays complete.
    listed = {pid for _, ids in categories for pid in ids}
    other = [pid for pid in ALL_PRINCIPLES if pid not in listed]
    if other:
        categories.append(("OTHER", other))

    for category_name, principle_ids in categories:
        print(f"  {category_name}")
        print(f"  {'-' * 60}")
        for pid in principle_ids:
            if pid in ALL_PRINCIPLES:
                principle = ALL_PRINCIPLES[pid]
                version = PRINCIPLE_VERSIONS.get(pid, "")
                print(f"    - {pid:<25} {principle.get('name', '')} (v{version})")
        print()

    print(f"""
Total principles: {len(list_all_principles())}

Enable principles via:
  - --preset <name>           Apply a preset configuration ('none' applies no preset)
  - --include-coc             Include specific principles
  - --all                     Include all optional principles

For detailed principle information, see the documentation.
""")


def show_guides():
    """Display available implementation guides."""
    print("""
================================================================================
                      AVAILABLE IMPLEMENTATION GUIDES
================================================================================

Guides provide HOW-TO documentation for implementing governance practices.
They complement principles by offering practical implementation guidance.

""")

    # Group by category
    categories = [
        ("GOVERNANCE", GOVERNANCE_GUIDES),
        ("DEVELOPMENT", DEVELOPMENT_GUIDES),
        ("SECURITY", SECURITY_GUIDES),
        ("COMMUNITY", COMMUNITY_GUIDES),
        ("ONBOARDING", ONBOARDING_GUIDES),
        ("OPERATIONS", OPERATIONS_GUIDES),
        ("PLANNING", PLANNING_GUIDES),
    ]
    # Anything not in a category above still gets listed, so the output stays complete.
    listed = {gid for _, ids in categories for gid in ids}
    other = [gid for gid in ALL_GUIDES if gid not in listed]
    if other:
        categories.append(("OTHER", other))

    for category_name, guide_ids in categories:
        print(f"  {category_name}")
        print(f"  {'-' * 60}")
        for gid in guide_ids:
            if gid in ALL_GUIDES:
                guide = ALL_GUIDES[gid]
                complexity = GUIDE_COMPLEXITY.get(gid, "")
                print(f"    - {gid:<25} [{complexity}] {guide.get('title', '')}")
        print()

    print(f"""
Total guides: {len(list_all_guides())}

Guides are reference content: they are not written into generated projects
yet (planned for v3.8.0, issue #116). Read them through the Python API,
e.g. core.guides.get_guide_content("onboarding").
""")


def load_plugins(plugins_dir: str) -> list:
    """
    Load custom plugins from specified directory.

    Plugins allow extending the generator with custom functionality.
    This is a placeholder for future plugin architecture.

    Args:
        plugins_dir: Path to plugins directory

    Returns:
        List of loaded plugin modules (empty for now)
    """
    if not plugins_dir:
        return []

    plugins_path = Path(plugins_dir)
    if not plugins_path.exists():
        print(f"Warning: Plugins directory not found: {plugins_dir}")
        return []

    # Future: Load and validate plugins
    # For now, this is a placeholder for the plugin architecture
    print(f"Note: Plugin loading from {plugins_dir} (not yet implemented)")
    return []


def main() -> int:
    """
    Main entry point for Project Foundation Template v3.7.0.

    This function orchestrates the generation process:
    1. Parse command-line arguments
    2. Handle list commands (--list-presets, --list-principles, --list-guides)
    3. Load and merge configuration
    4. Apply preset if specified
    5. Validate arguments
    6. Run the generator

    Returns:
        Exit code (0 for success, 1 for failure, 2 for invalid configuration: a config
        file that is missing, unreadable, not valid JSON, or not a JSON object, or an
        invalid "preset" in it; argparse also exits with 2 for invalid command-line
        arguments)
    """
    # Parse arguments
    args = parse_arguments()

    # Handle list commands first (these don't require project-name/author-name)
    if getattr(args, "list_presets", False):
        show_presets()
        return 0

    if getattr(args, "list_principles", False):
        show_principles()
        return 0

    if getattr(args, "list_guides", False):
        show_guides()
        return 0

    # Load the config file, then merge it with the arguments (CLI takes precedence)
    config_path = getattr(args, "config_path", None)
    try:
        config, config_file = load_config(config_path)
        if config:
            args = merge_config_with_args(args, config, config_file)
    except ValueError as error:
        # A config file that is missing, unreadable, not valid JSON, or not a JSON
        # object (ConfigFileError), or an invalid "preset" in it. Stop here, as argparse does
        # for an invalid --preset: continuing would ignore settings the file was meant
        # to supply. Nothing has been written yet.
        print(f"Error: {error}", file=sys.stderr)
        return 2
    if config_file is not None:
        # Printed only now, after the file was read and its preset checked, so this line
        # never comes before a config error.
        print(f"📋 Loaded config from: {config_file}\n")

    # Apply preset if specified
    # NO_PRESET applies nothing. Given on the command line, it has already kept
    # merge_config_with_args from filling in the config file's preset.
    preset_name = getattr(args, "preset", None)
    if preset_name == NO_PRESET:
        if not getattr(args, "quiet", False):
            print("No preset applied: core files plus the --include-* flags or --all given.")
    elif preset_name:
        # argparse and normalize_config_preset() have already checked the name.
        args = apply_preset_to_args(args, get_preset(preset_name))
        if not getattr(args, "quiet", False):
            print(f"Applied preset: {preset_name}")

    # Load plugins if specified
    plugins_dir = getattr(args, "plugins_dir", None)
    if plugins_dir:
        load_plugins(plugins_dir)

    # Validate arguments
    is_valid, error_message = validate_arguments(args)

    if not is_valid:
        show_banner(quiet=True)
        print(f"""
Error: Missing required arguments

{error_message}

Quick help:
  python generate_foundation.py --project-name "MyProject" --author-name "Your Name"
  python generate_foundation.py --preset standard --project-name "MyProject" --author-name "Your Name"
  python generate_foundation.py --help

Discovery commands:
  python generate_foundation.py --list-presets
  python generate_foundation.py --list-principles
  python generate_foundation.py --list-guides
""")
        return 1

    # Show banner
    show_banner(quiet=getattr(args, "quiet", False))

    # Create and run generator
    generator = EthicalFoundationGenerator(args)
    success = generator.run()

    # Export JSON if requested
    if getattr(args, "export_json", False):
        result = {
            "success": success,
            "version": SCRIPT_VERSION,
            "project_name": args.project_name,
            "author_name": args.author_name,
            "output_dir": str(Path(args.output_dir).absolute()),
            "preset": preset_name,
            "files_generated": generator.generated_files if success else [],
            "timestamp": datetime.now().isoformat()
        }
        print("\n--- JSON OUTPUT ---")
        print(json.dumps(result, indent=2))

    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
