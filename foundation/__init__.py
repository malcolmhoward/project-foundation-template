# foundation - Project Foundation Template Package
# v2.6.0 - Stabilization & Testability

"""
Project Foundation Template - Modular Package

This package provides the core functionality for generating
ethical project governance templates.

Modules:
    config: Configuration loading and argument parsing
    education: Educational content and principles
    utils: Helper utilities
    templates: Template generation subpackage

Note: The main generator class remains in setup_foundation_lite.py
for backward compatibility. It imports from these modules.
"""

from foundation.utils import (
    SCRIPT_VERSION,
    OFFICIAL_REPO,
    EXPIRATION_DATE,
    CONFIG_FILES,
    SECRETS_PATTERNS,
    configure_windows_utf8,
    check_expiration,
    get_expiration_warning,
)

from foundation.config import (
    load_config_file,
    merge_config_with_args,
    parse_arguments,
    validate_arguments,
    CONFIG_KEY_MAPPING,
    DEFAULT_VALUES,
)

from foundation.education import (
    LITE_PRINCIPLES,
    EDUCATION_CONTENT,
    ETHICAL_USE_AGREEMENT,
    get_principle,
    get_education_content,
    format_principle_display,
)

__version__ = "2.6.0-lite"
__all__ = [
    # Utils
    "SCRIPT_VERSION",
    "OFFICIAL_REPO",
    "EXPIRATION_DATE",
    "CONFIG_FILES",
    "SECRETS_PATTERNS",
    "configure_windows_utf8",
    "check_expiration",
    "get_expiration_warning",
    # Config
    "load_config_file",
    "merge_config_with_args",
    "parse_arguments",
    "validate_arguments",
    "CONFIG_KEY_MAPPING",
    "DEFAULT_VALUES",
    # Education
    "LITE_PRINCIPLES",
    "EDUCATION_CONTENT",
    "ETHICAL_USE_AGREEMENT",
    "get_principle",
    "get_education_content",
    "format_principle_display",
]
