# core/config.py
# Configuration loading and argument parsing

"""
Configuration module for Project Foundation Template.

Contains:
    - Config file loading (.foundationrc)
    - Argument parsing
    - Argument validation
    - Preset application
"""

import argparse
import json
from pathlib import Path
from typing import Dict, Any, Tuple

from core.utils import SCRIPT_VERSION, CONFIG_FILES


# Map config keys to argument names (supports multiple naming conventions)
CONFIG_KEY_MAPPING = {
    "project_name": "project_name",
    "project-name": "project_name",
    "projectName": "project_name",
    "author_name": "author_name",
    "author-name": "author_name",
    "authorName": "author_name",
    "license": "license",
    "output_dir": "output_dir",
    "output-dir": "output_dir",
    "outputDir": "output_dir",
    "include_coc": "include_coc",
    "include-coc": "include_coc",
    "includeCoc": "include_coc",
    "include_security": "include_security",
    "include-security": "include_security",
    "includeSecurity": "include_security",
    # v2.3.0: Community governance templates
    "include_github_templates": "include_github_templates",
    "include-github-templates": "include_github_templates",
    "includeGithubTemplates": "include_github_templates",
    "include_changelog": "include_changelog",
    "include-changelog": "include_changelog",
    "includeChangelog": "include_changelog",
    "include_all": "include_all",
    "include-all": "include_all",
    "includeAll": "include_all",
    # v2.4.0: Security features
    "include_enhanced_security": "include_enhanced_security",
    "include-enhanced-security": "include_enhanced_security",
    "includeEnhancedSecurity": "include_enhanced_security",
    "include_secrets_detection": "include_secrets_detection",
    "include-secrets-detection": "include_secrets_detection",
    "includeSecretsDetection": "include_secrets_detection",
    # v2.5.0: Advanced governance
    "include_adr": "include_adr",
    "include-adr": "include_adr",
    "includeAdr": "include_adr",
    "include_ci": "include_ci",
    "include-ci": "include_ci",
    "includeCi": "include_ci",
    # v2.2.0: Non-interactive mode
    "verbose": "verbose",
    "non_interactive": "non_interactive",
    "non-interactive": "non_interactive",
    "nonInteractive": "non_interactive",
    "accept_terms": "accept_terms",
    "accept-terms": "accept_terms",
    "acceptTerms": "accept_terms",
    # v3.0.0: Presets and plugins
    "preset": "preset",
    "plugins_dir": "plugins_dir",
    "plugins-dir": "plugins_dir",
    "pluginsDir": "plugins_dir",
}

# Default values for arguments
DEFAULT_VALUES = {
    "project_name": None,
    "author_name": None,
    "license": "mit",
    "output_dir": ".",
    "include_coc": False,
    "include_security": False,
    # v2.3.0
    "include_github_templates": False,
    "include_changelog": False,
    "include_all": False,
    # v2.4.0
    "include_enhanced_security": False,
    "include_secrets_detection": False,
    # v2.5.0
    "include_adr": False,
    "include_ci": False,
    # v2.2.0
    "verbose": False,
    "non_interactive": False,
    "accept_terms": False,
    # v3.0.0
    "preset": None,
    "plugins_dir": None,
    "list_principles": False,
    "list_guides": False,
    "list_presets": False,
}


def load_config_file(config_path: str = None) -> Dict[str, Any]:
    """
    Load configuration from a .foundationrc file.

    Searches for config files in order:
    1. Explicit path if provided via --config
    2. .foundationrc in current directory
    3. .foundationrc.json in current directory
    4. foundationrc.json in current directory

    Returns empty dict if no config found (not an error).
    """
    config = {}

    if config_path:
        # Explicit config path provided
        path = Path(config_path)
        if not path.exists():
            print(f"⚠️  Config file not found: {config_path}")
            print("   Continuing with command-line arguments only.\n")
            return {}
        try:
            with open(path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            print(f"📋 Loaded config from: {path}\n")
            return config
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing config file: {e}")
            print("   Config file must be valid JSON.\n")
            return {}

    # Search for default config files
    for filename in CONFIG_FILES:
        path = Path(filename)
        if path.exists():
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                print(f"📋 Loaded config from: {path}\n")
                return config
            except json.JSONDecodeError:
                continue  # Try next file

    return config


def merge_config_with_args(args, config: Dict[str, Any]):
    """
    Merge config file settings with command-line arguments.
    Command-line arguments take precedence over config file.
    """
    for config_key, arg_name in CONFIG_KEY_MAPPING.items():
        if config_key in config:
            # Only apply config value if arg wasn't explicitly set
            current_value = getattr(args, arg_name, None)
            if current_value == DEFAULT_VALUES.get(arg_name):
                setattr(args, arg_name, config[config_key])

    return args


def parse_arguments():
    """Parse command-line arguments with educational descriptions."""
    parser = argparse.ArgumentParser(
        description="Generate ethical project foundations with education",
        epilog="""
This tool generates TEMPLATE documentation for project governance.
Templates must be customized for your specific needs.

Examples:
  Interactive mode:
    python setup_foundation.py --project-name MyProject --author-name "Jane Doe"

  Using a preset:
    python setup_foundation.py --preset enterprise --project-name MyProject --author-name "Jane Doe"

  Non-interactive mode (for CI/scripts):
    python setup_foundation.py --non-interactive --accept-terms --project-name MyProject --author-name "Jane Doe"

  List available options:
    python setup_foundation.py --list-presets
    python setup_foundation.py --list-principles
    python setup_foundation.py --list-guides

  Using config file:
    python setup_foundation.py --config .foundationrc

Config file format (.foundationrc):
  {
    "project_name": "MyProject",
    "author_name": "Jane Doe",
    "license": "mit",
    "preset": "standard"
  }
""",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    # Core required arguments
    parser.add_argument(
        "--project-name",
        dest="project_name",
        help="Name of your project (required unless in config)"
    )

    parser.add_argument(
        "--author-name",
        dest="author_name",
        help="Your name or organization (required unless in config)"
    )

    # Optional arguments
    parser.add_argument(
        "--license",
        choices=["mit", "apache", "gpl"],
        default="mit",
        help="License type (default: mit)"
    )

    parser.add_argument(
        "--output-dir",
        dest="output_dir",
        default=".",
        help="Output directory (default: current directory)"
    )

    parser.add_argument(
        "--include-coc",
        dest="include_coc",
        action="store_true",
        help="Include Code of Conduct template"
    )

    parser.add_argument(
        "--include-security",
        dest="include_security",
        action="store_true",
        help="Include Security Policy template"
    )

    # v2.3.0: Community governance templates
    parser.add_argument(
        "--include-github-templates",
        dest="include_github_templates",
        action="store_true",
        help="Include GitHub issue and PR templates (.github/ folder)"
    )

    parser.add_argument(
        "--include-changelog",
        dest="include_changelog",
        action="store_true",
        help="Include CHANGELOG.md template"
    )

    parser.add_argument(
        "--all",
        dest="include_all",
        action="store_true",
        help="Include all optional templates (CoC, Security, GitHub, Changelog, Enhanced Security, Secrets Detection, ADR, CI)"
    )

    # v2.4.0: Security features
    parser.add_argument(
        "--include-enhanced-security",
        dest="include_enhanced_security",
        action="store_true",
        help="Include comprehensive SECURITY.md with vulnerability reporting process"
    )

    parser.add_argument(
        "--include-secrets-detection",
        dest="include_secrets_detection",
        action="store_true",
        help="Include pre-commit config with secrets detection hooks"
    )

    # v2.5.0: Advanced governance
    parser.add_argument(
        "--include-adr",
        dest="include_adr",
        action="store_true",
        help="Include Architecture Decision Record templates"
    )

    parser.add_argument(
        "--include-ci",
        dest="include_ci",
        action="store_true",
        help="Include GitHub Actions CI workflow"
    )

    # v2.2.0: Non-interactive mode
    parser.add_argument(
        "--non-interactive",
        dest="non_interactive",
        action="store_true",
        help="Run without prompts (for CI/scripts). Requires --accept-terms."
    )

    parser.add_argument(
        "--accept-terms",
        dest="accept_terms",
        action="store_true",
        help="Accept ethical use agreement (required for --non-interactive)"
    )

    # v2.2.0: Config file support
    parser.add_argument(
        "--config",
        dest="config_path",
        help="Path to config file (default: .foundationrc in current directory)"
    )

    # v2.2.0: JSON export
    parser.add_argument(
        "--export-json",
        dest="export_json",
        action="store_true",
        help="Output results as JSON (useful for tooling integration)"
    )

    # Output control
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show detailed output"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Minimal output (implies --non-interactive behavior for output only)"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {SCRIPT_VERSION}"
    )

    # v3.0.0: Preset support
    parser.add_argument(
        "--preset",
        choices=["minimal", "light", "standard", "strict", "enterprise"],
        help="Governance preset (minimal/light/standard/strict/enterprise). Overrides individual --include-* flags."
    )

    parser.add_argument(
        "--plugins-dir",
        dest="plugins_dir",
        help="Path to custom plugins directory for extending generator functionality"
    )

    # v3.0.0: List commands (discovery)
    parser.add_argument(
        "--list-principles",
        dest="list_principles",
        action="store_true",
        help="Show available governance principles and exit"
    )

    parser.add_argument(
        "--list-guides",
        dest="list_guides",
        action="store_true",
        help="Show available implementation guides and exit"
    )

    parser.add_argument(
        "--list-presets",
        dest="list_presets",
        action="store_true",
        help="Show available governance presets and exit"
    )

    return parser.parse_args()


def apply_preset_to_args(args, preset_config: Dict[str, Any]):
    """
    Apply preset configuration to arguments.

    Preset features override individual --include-* flags.

    Args:
        args: Parsed arguments namespace
        preset_config: Preset configuration dict with 'features' key

    Returns:
        Modified args namespace
    """
    if not preset_config or "features" not in preset_config:
        return args

    features = preset_config["features"]

    # Map preset feature names to argument names
    feature_to_arg = {
        "code_of_conduct": "include_coc",
        "security": "include_security",
        "changelog": "include_changelog",
        "issue_templates": "include_github_templates",
        "pr_template": "include_github_templates",  # Combined with issue templates
        "enhanced_security": "include_enhanced_security",
        "secrets_detection": "include_secrets_detection",
        "adr": "include_adr",
        "ci_workflow": "include_ci",
    }

    for feature_name, arg_name in feature_to_arg.items():
        if feature_name in features:
            setattr(args, arg_name, features[feature_name])

    return args


def validate_arguments(args, skip_required: bool = False) -> Tuple[bool, str]:
    """
    Validate that required arguments are provided.

    Args:
        args: Parsed arguments namespace
        skip_required: If True, skip validation of required fields
                       (used when running --list-* commands)

    Returns:
        Tuple of (is_valid, error_message)
    """
    errors = []

    # Skip validation for list commands
    if skip_required:
        return True, ""

    if not args.project_name:
        errors.append("--project-name is required (or set 'project_name' in config file)")

    if not args.author_name:
        errors.append("--author-name is required (or set 'author_name' in config file)")

    if args.non_interactive and not args.accept_terms:
        errors.append("--accept-terms is required when using --non-interactive mode")
        errors.append("  This ensures you've read and understood the ethical use agreement.")
        errors.append("  Review the agreement by running without --non-interactive first.")

    if errors:
        return False, "\n".join(errors)

    return True, ""
