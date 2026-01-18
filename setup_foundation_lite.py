#!/usr/bin/env python3
"""
Project Foundation Generator - Ethical Lite Edition
Version: 2.6.0-lite
Released: 2025-09-24

This tool generates educational project foundations with built-in governance principles.
It is designed to teach best practices while creating useful templates.

IMPORTANT: This generates TEMPLATES only. They are starting points, not complete solutions.
Actual security, compliance, and governance require ongoing human judgment and expertise.

Copyright (c) 2025 Malcolm Howard

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Repository: https://github.com/malcolmhoward/project-foundation-template
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# v2.6.0: Import from modular foundation package
from core import (
    # Utils
    SCRIPT_VERSION,
    configure_windows_utf8,
    # Config
    load_config_file,
    merge_config_with_args,
    parse_arguments,
    validate_arguments,
)

# v2.6.0: Import generator class from its own module
from core.generator import EthicalFoundationGenerator

# Configure stdout for UTF-8 on Windows (handles Unicode characters in output)
configure_windows_utf8()


def main():
    """Main entry point with ethical safeguards."""
    args = parse_arguments()

    # Load config file and merge with arguments
    config = load_config_file(args.config_path)
    if config:
        args = merge_config_with_args(args, config)

    # Validate arguments
    is_valid, error_message = validate_arguments(args)
    if not is_valid:
        # Educational error message
        print(f"""
❌ MISSING REQUIRED ARGUMENTS

{error_message}

📚 HELP: How to provide required values

Option 1: Command line arguments
  python {sys.argv[0]} --project-name "MyProject" --author-name "Your Name"

Option 2: Config file (.foundationrc)
  Create a file named .foundationrc with:
  {{
    "project_name": "MyProject",
    "author_name": "Your Name"
  }}

Option 3: Both (command line overrides config)
  python {sys.argv[0]} --config .foundationrc --project-name "Override"

For CI/automation, use:
  python {sys.argv[0]} --non-interactive --accept-terms --project-name "MyProject" --author-name "Your Name"

Run with --help for all options.
""")
        return 1

    # Show banner (unless quiet mode)
    if not args.quiet:
        print(f"""
╔══════════════════════════════════════════════════════════════╗
║     Project Foundation Generator - Ethical Lite Edition      ║
║                      Version {SCRIPT_VERSION:^8}                      ║
╚══════════════════════════════════════════════════════════════╝
""")

    generator = EthicalFoundationGenerator(args)

    success = generator.run()

    # Export JSON if requested
    if args.export_json:
        result = {
            "success": success,
            "version": SCRIPT_VERSION,
            "project_name": args.project_name,
            "author_name": args.author_name,
            "output_dir": str(Path(args.output_dir).absolute()),
            "files_generated": generator.generated_files if success else [],
            "timestamp": datetime.now().isoformat()
        }
        print("\n--- JSON OUTPUT ---")
        print(json.dumps(result, indent=2))

    if success:
        return 0
    else:
        return 1


if __name__ == "__main__":
    sys.exit(main())
