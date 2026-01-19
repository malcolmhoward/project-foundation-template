# core - Project Foundation Template Package
# v2.8.0 - Modular Principles

"""
Project Foundation Template - Modular Package

This package provides the core functionality for generating
ethical project governance templates.

Modules:
    config: Configuration loading and argument parsing
    education: Educational content and ethical agreement
    ethics: Ethical safeguards and version advisory checks
    generator: Main EthicalFoundationGenerator class
    presets: Governance preset configurations
    principles: Individual governance principle modules
    utils: Helper utilities
    templates: Template generation subpackage
"""

from core.utils import (
    SCRIPT_VERSION,
    OFFICIAL_REPO,
    EXPIRATION_DATE,
    CONFIG_FILES,
    SECRETS_PATTERNS,
    configure_windows_utf8,
    check_expiration,
    get_expiration_warning,
)

from core.config import (
    load_config_file,
    merge_config_with_args,
    parse_arguments,
    validate_arguments,
    CONFIG_KEY_MAPPING,
    DEFAULT_VALUES,
)

from core.education import (
    LITE_PRINCIPLES,
    EDUCATION_CONTENT,
    ETHICAL_USE_AGREEMENT,
    get_principle,
    get_education_content,
    format_principle_display,
)

from core.ethics import (
    check_version_advisory,
    show_ethical_agreement,
    is_version_expired,
    get_version_status,
)

from core.generator import EthicalFoundationGenerator

from core.presets import (
    PRESETS,
    DEFAULT_PRESET,
    get_preset,
    list_presets,
    get_preset_description,
)

from core.principles import (
    ALL_PRINCIPLES,
    ALL_EDUCATION,
    CORE_PRINCIPLES,
    GOVERNANCE_PRINCIPLES,
    SECURITY_PRINCIPLES,
    ADVANCED_PRINCIPLES,
    COMMUNITY_PRINCIPLES,
    PRINCIPLE_VERSIONS,
    get_principles_by_category,
    get_principles_for_version,
    list_all_principles,
)

__version__ = "2.8.0-lite"
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
    # Ethics
    "check_version_advisory",
    "show_ethical_agreement",
    "is_version_expired",
    "get_version_status",
    # Generator
    "EthicalFoundationGenerator",
    # Presets
    "PRESETS",
    "DEFAULT_PRESET",
    "get_preset",
    "list_presets",
    "get_preset_description",
    # Principles
    "ALL_PRINCIPLES",
    "ALL_EDUCATION",
    "CORE_PRINCIPLES",
    "GOVERNANCE_PRINCIPLES",
    "SECURITY_PRINCIPLES",
    "ADVANCED_PRINCIPLES",
    "COMMUNITY_PRINCIPLES",
    "PRINCIPLE_VERSIONS",
    "get_principles_by_category",
    "get_principles_for_version",
    "list_all_principles",
]
