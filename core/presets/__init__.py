# core/presets/__init__.py
# Preset configurations for different governance levels

"""
Presets module for Project Foundation Template.

Provides 5 governance presets with different levels of features:
    - minimal: Core essentials only (3 principles)
    - light: Basic governance (6 principles)
    - standard: Recommended starting point (9 principles)
    - strict: Comprehensive governance (12 principles)
    - enterprise: Full governance suite (all 30 principles)

Each preset defines which features and principles are included.

The --preset option also accepts NO_PRESET ("none"). It is not a preset: it applies
nothing, so only the core files and the --include-* flags or --all given are
generated. On the command line it also overrides a "preset" set in the config file,
which leaving --preset out does not. It is a named choice so that the custom route
shows up in --help and --list-presets.
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

# Recommended preset. The generator does not apply it automatically: with no
# --preset, only the core files and the --include-* flags given are generated.
DEFAULT_PRESET = "standard"

# The --preset choice that applies no preset. Given on the command line, it also
# overrides a "preset" set in the config file; leaving --preset out does not.
# It is deliberately not a key of PRESETS: get_preset() returns {} for it, and
# list_presets() names only the five real presets.
NO_PRESET = "none"

# Every value --preset and the "preset" config key accept, in lowercase. Both
# accept any letter case (`--preset NONE`, `"preset": "Standard"`) and lowercase
# the value before checking it against this list. The config key also has
# surrounding spaces stripped; --preset does not.
PRESET_CHOICES = list(PRESETS) + [NO_PRESET]


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
        List of preset names (not NO_PRESET, which applies no preset)
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
    "NO_PRESET",
    "PRESET_CHOICES",
    "MINIMAL_PRESET",
    "LIGHT_PRESET",
    "STANDARD_PRESET",
    "STRICT_PRESET",
    "ENTERPRISE_PRESET",
    "get_preset",
    "list_presets",
    "get_preset_description",
]
