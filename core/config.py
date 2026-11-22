# core/config.py
# Configuration loading and argument parsing

"""
Configuration module for Project Foundation Template.

Contains:
    - Config file loading (.foundationrc or the --config file)
    - Argument parsing
    - Argument validation
    - Preset application
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Any, Optional, Tuple

from core.utils import SCRIPT_VERSION, CONFIG_FILES
from core.presets import NO_PRESET, PRESET_CHOICES


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
    # v3.0.0: Presets and plugins
    "preset": "preset",
    "plugins_dir": "plugins_dir",
    "plugins-dir": "plugins_dir",
    "pluginsDir": "plugins_dir",
    # v3.7.0: Generation log
    "include_generation_log": "include_generation_log",
    "include-generation-log": "include_generation_log",
    "includeGenerationLog": "include_generation_log",
    "log_format": "log_format",
    "log-format": "log_format",
    "logFormat": "log_format",
    "log_to": "log_to",
    "log-to": "log_to",
    "logTo": "log_to",
}

# Settings that must be given on the command line, never in a config file.
# Accepting the ethical use agreement and overwriting existing files are decisions
# the person running the generator makes each time; a .foundationrc in a cloned or
# shared repository must not make them on that person's behalf.
COMMAND_LINE_ONLY_KEYS = {
    "accept_terms": "--accept-terms",
    "accept-terms": "--accept-terms",
    "acceptTerms": "--accept-terms",
    "force_overwrite": "--force-overwrite",
    "force-overwrite": "--force-overwrite",
    "forceOverwrite": "--force-overwrite",
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
    # v3.7.0: Generation log
    "include_generation_log": False,
    "log_format": "md",
    "log_to": None,
    "force_overwrite": False,
}


class ConfigFileError(ValueError):
    """A config file is missing, unreadable, or does not hold a JSON object."""


def _json_type_name(value) -> str:
    """Return the JSON name of a parsed value's type, for error messages."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "boolean"
    if isinstance(value, (int, float)):
        return "number"
    if isinstance(value, str):
        return "string"
    if isinstance(value, dict):
        return "object"
    return "array"


def _escape_unprintable(text: str) -> str:
    """
    Return text with non-printable characters and backslashes as Python-style escapes.

    WHAT: ESC becomes `\\x1b`, a line feed becomes `\\n`, U+2028 becomes `\\u2028`, and a
          backslash becomes `\\\\`. Other printable text, including non-ASCII letters
          such as `é`, is returned unchanged.
    WHY: A value from a config file is shown in error messages, and a config file can
         come from a cloned repository. Printed raw, an ANSI escape sequence or a line
         break in the value could recolor, move, or forge lines in the terminal.
    HOW: `str.isprintable()` decides. It rejects the C0 and C1 control characters, line
         and paragraph separators, and lone surrogates, among others. Each rejected
         character is replaced by its `unicode_escape` form. A backslash is printable,
         but it is doubled as well: otherwise a backslash followed by `n` in the value
         would look the same as an escaped line feed.
    """
    return "".join(
        char if char.isprintable() and char != "\\"
        else char.encode("unicode_escape").decode("ascii")
        for char in text)


def _read_config_file(path: Path) -> Dict[str, Any]:
    """
    Return the JSON object in a config file, or raise ConfigFileError naming the file.

    WHAT: Every way the file can fail to give a JSON object becomes a ConfigFileError.
    WHY: The caller reports ConfigFileError in one line and exits with code 2. Any other
         exception would reach the user as a traceback, or as a message that does not
         name the file.
    HOW: The file is read as UTF-8 with or without a byte-order mark (`utf-8-sig`),
         because some Windows editors write one. A directory and an empty file are
         reported in plain words before Python's less clear errors can appear. The
         checks on the path are inside a `try` as well: they raise OSError when, for
         example, a parent directory denies access. A ValueError from the parser is
         reported as a number too long to read only when it is Python's integer
         digit-limit error; any other ValueError is reported with its own text.
    """
    try:
        is_dangling_link = path.is_symlink() and not path.exists()
        is_directory = path.is_dir()
        is_other_non_file = path.exists() and not path.is_file()
    except OSError as error:
        raise ConfigFileError(
            f"Cannot read the config file '{path}': {error}.") from error
    if is_dangling_link:
        raise ConfigFileError(
            f"Cannot read the config file '{path}': it is a symbolic link, and its "
            "target does not exist.")
    if is_directory:
        raise ConfigFileError(f"The config file '{path}' is not a file; it is a directory.")
    if is_other_non_file:
        raise ConfigFileError(f"The config file '{path}' is not a file.")
    try:
        with open(path, 'r', encoding='utf-8-sig') as f:
            text = f.read()
        if not text.strip():
            raise ConfigFileError(
                f"The config file '{path}' is empty. Write {{}} in it, or delete it.")
        config = json.loads(text)
    except ConfigFileError:
        raise
    except json.JSONDecodeError as error:
        raise ConfigFileError(
            f"The config file '{path}' is not valid JSON: {error}.") from error
    except (OSError, UnicodeDecodeError) as error:
        raise ConfigFileError(
            f"Cannot read the config file '{path}': {error}.") from error
    except RecursionError as error:
        raise ConfigFileError(
            f"Cannot read the config file '{path}': its arrays or objects are nested "
            "too deeply.") from error
    except ValueError as error:
        # JSONDecodeError and UnicodeDecodeError are handled above. The case known to
        # reach this point is an integer with more digits than Python converts by
        # default: "Exceeds the limit (4300 digits) for integer string conversion: ...".
        # Only that error is described as a number too long to read.
        if "integer string conversion" in str(error):
            raise ConfigFileError(
                f"The config file '{path}' holds a number too long to read.") from error
        raise ConfigFileError(
            f"Cannot read the config file '{path}': {error}.") from error
    if not isinstance(config, dict):
        raise ConfigFileError(
            f"The config file '{path}' must hold a JSON object, such as "
            f'{{"preset": "standard"}}; it holds a JSON {_json_type_name(config)}.')
    return config


def find_config_file(config_path: str = None) -> Optional[Path]:
    """
    Return the config file this run uses, or None when there is none.

    WHAT: The --config file when one is given; otherwise the first name in CONFIG_FILES
          present in the current directory.
    WHY: A name that is present but broken must be reported, not passed over, so a
         symbolic link whose target is missing counts as present. `Path.exists()` alone
         reports such a link as absent, and the file would be skipped without a message.
    HOW: Two things are errors here: a --config file that is absent, and a path that
         cannot be checked at all (OSError, for example when a parent directory denies
         access). Reading the file, and every other check, happens in
         _read_config_file().
    """
    if config_path:
        path = Path(config_path)
        if not _is_present(path):
            raise ConfigFileError(
                f"Config file not found: '{config_path}'. Check the path given to --config.")
        return path

    for filename in CONFIG_FILES:
        path = Path(filename)
        if _is_present(path):
            return path

    return None


def _is_present(path: Path) -> bool:
    """
    Return True when the path exists or is a symbolic link, even one with no target.

    Raises ConfigFileError naming the file when the path cannot be checked, so that the
    OSError does not reach the user as a traceback.
    """
    try:
        return path.exists() or path.is_symlink()
    except OSError as error:
        raise ConfigFileError(
            f"Cannot read the config file '{path}': {error}.") from error


def load_config(config_path: str = None) -> Tuple[Dict[str, Any], Optional[Path]]:
    """
    Load configuration from the --config file, or from a config file in the current directory.

    WHAT: Returns the config file's settings and the file they came from, or an empty
          dict and None when there is no config file.
    WHY: A config file that was missing or broken used to be skipped, sometimes without a
         message, so the run quietly ignored the settings the file was meant to supply
         (#150).
    HOW: Uses the first of these that applies:
         1. The explicit path given with --config
         2. .foundationrc in the current directory
         3. .foundationrc.json in the current directory
         4. foundationrc.json in the current directory
         Only the first file found is read; a later name is not tried when an earlier one
         is broken. Nothing is printed: the caller announces the file once the settings
         in it have been checked, so "Loaded config" never comes before an error.

    Returns:
        (settings, file). ({}, None) when --config was not given and none of the default
        files exist (not an error).

    Raises:
        ConfigFileError: the --config file does not exist, or the file used cannot be
            read, is not a file, is empty, is not valid JSON, or holds JSON that is not
            an object. The message names the file. The caller reports it and exits with
            code 2 before any file is written.
    """
    path = find_config_file(config_path)
    if path is None:
        return {}, None
    return _read_config_file(path), path


def load_config_file(config_path: str = None) -> Dict[str, Any]:
    """Return only the settings from load_config(); see it for the rules and errors."""
    return load_config(config_path)[0]


def normalize_config_preset(value, config_file=None):
    """
    Return a config file's "preset" value in lowercase, checked against PRESET_CHOICES.

    WHAT: `"Standard"` and `"NONE"` mean `standard` and `none`; anything else is an error.
    WHY: A misspelled preset used to be ignored with a warning, so the run quietly wrote
         fewer governance files than the config file requested.
    HOW: None (JSON null) and an empty or whitespace-only string mean the key is unset.
         Any other value must be one of PRESET_CHOICES in any letter case; otherwise
         ValueError names the value, the config file (when `config_file` is given), and
         the valid choices. A string is shown in single quotes with its non-printable
         characters escaped (see _escape_unprintable()), so a value cannot send control
         sequences to the terminal. A value that is not a string is shown as JSON, with
         its JSON type. Spaces around the value are stripped, so `" Strict "` means
         `strict`.
         `--preset` on the command line does not strip them: `--preset " strict "` is
         rejected.
    """
    if value is None or (isinstance(value, str) and not value.strip()):
        return None
    if isinstance(value, str) and value.strip().lower() in PRESET_CHOICES:
        return value.strip().lower()
    if isinstance(value, str):
        shown = f"'{_escape_unprintable(value)}'"
    else:
        shown = f"'{json.dumps(value)}' (a JSON {_json_type_name(value)})"
    where = f"the config file '{config_file}'" if config_file else "the config file"
    choices = ", ".join(f"'{choice}'" for choice in PRESET_CHOICES)
    raise ValueError(
        f"Invalid preset {shown} in {where}. Valid choices (in any letter case): {choices}.")


def merge_config_with_args(args, config: Dict[str, Any], config_file=None):
    """
    Merge config file settings with command-line arguments.
    Command-line arguments take precedence over config file.

    A config value is used only when the argument still has its default value. So
    `--preset none` on the command line overrides a "preset" in the config file, and
    leaving --preset out applies the config file's preset.

    Settings in COMMAND_LINE_ONLY_KEYS are ignored with a warning: they must be
    given on the command line.

    Args:
        config_file: The file the settings came from; the invalid-preset error names it.

    Raises:
        ValueError: the config file's "preset" is used and is not one of PRESET_CHOICES.
    """
    for config_key, flag in COMMAND_LINE_ONLY_KEYS.items():
        if config_key in config:
            print(f"⚠️  Ignoring '{config_key}' in the config file: pass {flag} on the "
                  "command line instead.", file=sys.stderr)

    for config_key, arg_name in CONFIG_KEY_MAPPING.items():
        if config_key in config:
            # Only apply config value if arg wasn't explicitly set
            current_value = getattr(args, arg_name, None)
            if current_value == DEFAULT_VALUES.get(arg_name):
                value = config[config_key]
                if arg_name == "preset":
                    value = normalize_config_preset(value, config_file)
                setattr(args, arg_name, value)

    return args


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser with educational descriptions."""
    parser = argparse.ArgumentParser(
        description="Generate ethical project foundations with education",
        epilog="""
This tool generates TEMPLATE documentation for project governance.
Templates must be customized for your specific needs.

Examples:
  Interactive mode:
    python generate_foundation.py --project-name MyProject --author-name "Jane Doe"

  Using a preset:
    python generate_foundation.py --preset enterprise --project-name MyProject --author-name "Jane Doe"

  Without a preset (core files plus the options you name):
    python generate_foundation.py --preset none --include-ci --project-name MyProject --author-name "Jane Doe"

  Non-interactive mode (for CI/scripts):
    python generate_foundation.py --non-interactive --accept-terms --project-name MyProject --author-name "Jane Doe"

  List available options:
    python generate_foundation.py --list-presets
    python generate_foundation.py --list-principles
    python generate_foundation.py --list-guides

  Using config file:
    python generate_foundation.py --config .foundationrc

Config file format (.foundationrc):
  {
    "project_name": "MyProject",
    "author_name": "Jane Doe",
    "license": "mit",
    "preset": "standard"
  }

  "preset" takes minimal, light, standard, strict, enterprise, or none (no preset).
  --preset on the command line overrides it; --preset none cancels it.

  Without --config, the first of .foundationrc, .foundationrc.json, and
  foundationrc.json found in the current directory is used. A --config file that
  does not exist, or a config file that cannot be read, is not valid JSON, or
  is not a JSON object, stops the run with exit code 2 before any file is
  written.
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
        help="Include all optional templates (Code of Conduct, Security, GitHub, Changelog, Enhanced Security, Secrets Detection, ADR, CI, Glossary, Maintainers, Scaffold Manifest)"
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

    # v3.1.0: Accessibility features
    parser.add_argument(
        "--include-glossary",
        dest="include_glossary",
        action="store_true",
        help="Include GLOSSARY.md with project terminology definitions"
    )

    parser.add_argument(
        "--include-maintainers",
        dest="include_maintainers",
        action="store_true",
        help="Include MAINTAINERS.md with maintainer information"
    )

    parser.add_argument(
        "--include-manifest",
        dest="include_manifest",
        action="store_true",
        help="Include SCAFFOLD_MANIFEST.md documenting what was generated"
    )

    # v3.7.0: Generation log
    parser.add_argument(
        "--include-generation-log",
        dest="include_generation_log",
        action="store_true",
        help="Include GENERATION_LOG tracking generated files with provenance"
    )

    parser.add_argument(
        "--log-format",
        dest="log_format",
        choices=["md", "json", "both"],
        default="md",
        help="Format for generation log: md (default), json, or both"
    )

    parser.add_argument(
        "--log-to",
        dest="log_to",
        help="Append to existing generation log file instead of creating new"
    )

    parser.add_argument(
        "--force-overwrite",
        dest="force_overwrite",
        action="store_true",
        help="Overwrite existing files without prompting (required for non-interactive runs "
             "into a directory that already has generated files; command line only)"
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
        # Lowercase the value before argparse checks it, so that `--preset NONE` (the
        # heading --list-presets prints) and `--preset Standard` are accepted.
        type=str.lower,
        choices=PRESET_CHOICES,
        help=("Governance preset (minimal/light/standard/strict/enterprise; standard is "
              "recommended; any letter case). A preset is a starting point: --include-* "
              f"flags and --all add to it. '{NO_PRESET}' applies no preset: only the core "
              "files plus the --include-* flags or --all given are generated. On the "
              f"command line, '{NO_PRESET}' also overrides a preset set in the config file.")
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

    return parser


def parse_arguments():
    """Parse command-line arguments with educational descriptions."""
    return build_parser().parse_args()


def include_option_help() -> list:
    """
    Return (option, help) pairs for --all and the --include-* options.

    Read from the parser so that --list-presets describes the same options --help does.
    """
    # Deliberate use of the private `_actions` list: argparse has no public iterator.
    return [(action.option_strings[0], action.help)
            for action in build_parser()._actions
            if action.option_strings
            and (action.option_strings[0] == "--all"
                 or action.option_strings[0].startswith("--include-"))]


# Preset feature names and the arguments they set. Other --include-* flags (glossary,
# maintainers, manifest, generation log) are not set by presets and combine with them.
PRESET_FEATURE_ARGS = {
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


def preset_enabled_args(preset_config: Dict[str, Any]) -> set:
    """
    Return the names of the arguments a preset turns on.

    Args:
        preset_config: Preset configuration dict with 'features' key

    Returns:
        Set of argument names (e.g. "include_ci") for the features the preset enables
    """
    features = (preset_config or {}).get("features", {})
    return {arg_name for feature_name, arg_name in PRESET_FEATURE_ARGS.items()
            if features.get(feature_name)}


def apply_preset_to_args(args, preset_config: Dict[str, Any]):
    """
    Apply preset configuration to arguments.

    A preset is a starting point: it turns on the features it includes and never
    turns off a feature requested with an --include-* flag, --all, or the config
    file. `--preset standard --include-adr` therefore generates the standard files
    plus the ADR templates.

    Args:
        args: Parsed arguments namespace
        preset_config: Preset configuration dict with 'features' key

    Returns:
        Modified args namespace
    """
    for arg_name in preset_enabled_args(preset_config):
        setattr(args, arg_name, True)

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
