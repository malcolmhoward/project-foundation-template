# core/presets/__init__.py
# Preset configurations for different governance levels

"""
Presets module for Project Foundation Template.

Provides 5 governance presets with different levels of features:
    - minimal: Core essentials only (5 principles)
    - light: Basic governance (8 principles)
    - standard: Recommended default (10 principles)
    - strict: Comprehensive governance (12 principles)
    - enterprise: Full governance suite (all principles)

Each preset defines which features and principles are included.
"""

from .minimal import MINIMAL_PRESET
from .light import LIGHT_PRESET
from .standard import STANDARD_PRESET
from .strict import STRICT_PRESET
from .enterprise import ENTERPRISE_PRESET

# Mapping of preset names to configurations
PRESETS = {
    "minimal": MINIMAL_PRESET,
    "light": LIGHT_PRESET,
    "standard": STANDARD_PRESET,
    "strict": STRICT_PRESET,
    "enterprise": ENTERPRISE_PRESET,
}

# Default preset
DEFAULT_PRESET = "standard"


def get_preset(name: str) -> dict:
    """Get a preset configuration by name.

    Args:
        name: Preset name (minimal, light, standard, strict, enterprise)

    Returns:
        Preset configuration dict, or empty dict if not found
    """
    return PRESETS.get(name.lower(), {})


def list_presets() -> list:
    """List all available preset names.

    Returns:
        List of preset names
    """
    return list(PRESETS.keys())


def get_preset_description(name: str) -> str:
    """Get a human-readable description of a preset.

    Args:
        name: Preset name

    Returns:
        Description string
    """
    preset = get_preset(name)
    if not preset:
        return ""
    return preset.get("description", "")


__all__ = [
    "PRESETS",
    "DEFAULT_PRESET",
    "MINIMAL_PRESET",
    "LIGHT_PRESET",
    "STANDARD_PRESET",
    "STRICT_PRESET",
    "ENTERPRISE_PRESET",
    "get_preset",
    "list_presets",
    "get_preset_description",
]
