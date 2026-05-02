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
from datetime import datetime
from pathlib import Path

# Configure UTF-8 output on Windows before any imports that might print
from core.utils import configure_windows_utf8, SCRIPT_VERSION, OFFICIAL_REPO

configure_windows_utf8()

# Core module imports
from core.config import (
    load_config_file,
    merge_config_with_args,
    parse_arguments,
    validate_arguments,
    apply_preset_to_args,
)

from core.generator import EthicalFoundationGenerator

from core.presets import (
    PRESETS,
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
    ADVANCED_PRINCIPLES,
    COMMUNITY_PRINCIPLES,
    list_all_principles,
)

from core.guides import (
    ALL_GUIDES,
    GUIDE_COMPLEXITY,
    GOVERNANCE_GUIDES,
    DEVELOPMENT_GUIDES,
    SECURITY_GUIDES,
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
    ]

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
  - --preset <name>           Apply a preset configuration
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
    ]

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

Guides are included based on selected principles and presets.
For full guide content, see the docs/ directory after generation.
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
        Exit code (0 for success, 1 for failure)
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

    # Load config file if specified
    config_path = getattr(args, "config_path", None)
    config = load_config_file(config_path)

    # Merge config with arguments (CLI takes precedence)
    if config:
        args = merge_config_with_args(args, config)

    # Apply preset if specified
    preset_name = getattr(args, "preset", None)
    if preset_name:
        preset_config = get_preset(preset_name)
        if preset_config:
            args = apply_preset_to_args(args, preset_config)
            if not getattr(args, "quiet", False):
                print(f"Applied preset: {preset_name}")
        else:
            print(f"Warning: Unknown preset '{preset_name}', ignoring.")

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
