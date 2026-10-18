# core/internationalization/__init__.py
# Internationalization infrastructure (v3.6.0)

"""
Internationalization (i18n) Infrastructure.

Provides locale configurations, RTL support, and translation template
generation for multi-language projects.

Note on terminology: This module uses standard ISO 639-1 language codes and
follows industry conventions for locale naming. For languages with multiple
spoken varieties (e.g., Chinese, Arabic), the locale represents the standard
written form used in software localization. See individual locale modules
for detailed notes on written vs. spoken language distinctions.

Note: This module handles spoken/written language internationalization.
For programming language support, see core/programming_languages.

Introduced in v3.6.0.
"""

from typing import Dict, List, Any
import json

from core.utils import SCRIPT_VERSION

# Import all locale configurations
from . import english
from . import spanish
from . import french
from . import german
from . import portuguese
from . import chinese
from . import japanese
from . import korean
from . import arabic
from . import hindi

# Locale module registry
LOCALE_MODULES = {
    "en": english,
    "es": spanish,
    "fr": french,
    "de": german,
    "pt": portuguese,
    "zh": chinese,
    "ja": japanese,
    "ko": korean,
    "ar": arabic,
    "hi": hindi,
}

# All locale configurations
ALL_LOCALES: Dict[str, Dict[str, Any]] = {
    locale_id: module.LOCALE
    for locale_id, module in LOCALE_MODULES.items()
}

# Locale categories
WESTERN_EUROPEAN_LOCALES = ["en", "es", "fr", "de", "pt"]
EAST_ASIAN_LOCALES = ["zh", "ja", "ko"]
RTL_LOCALES = ["ar"]  # Right-to-left languages
INDIC_LOCALES = ["hi"]

# Text direction constants
LTR = "ltr"  # Left-to-right
RTL = "rtl"  # Right-to-left


def get_locale(locale_id: str) -> Dict[str, Any]:
    """Get locale configuration by ID."""
    if locale_id not in ALL_LOCALES:
        raise ValueError(f"Unknown locale: {locale_id}")
    return ALL_LOCALES[locale_id]


def is_rtl(locale_id: str) -> bool:
    """Check if a locale uses right-to-left text direction."""
    return locale_id in RTL_LOCALES


def get_text_direction(locale_id: str) -> str:
    """Get text direction for a locale."""
    return RTL if is_rtl(locale_id) else LTR


def get_locales_by_region(region: str) -> List[str]:
    """Get locales by region category."""
    region_map = {
        "western_european": WESTERN_EUROPEAN_LOCALES,
        "east_asian": EAST_ASIAN_LOCALES,
        "rtl": RTL_LOCALES,
        "indic": INDIC_LOCALES,
    }
    return region_map.get(region.lower(), [])


def get_locale_metadata(locale_id: str) -> Dict[str, Any]:
    """Get metadata for a locale."""
    locale = get_locale(locale_id)
    return {
        "id": locale["id"],
        "name": locale["name"],
        "native_name": locale["native_name"],
        "direction": locale["direction"],
        "script": locale.get("script", "Latin"),
    }


def get_all_locale_metadata() -> List[Dict[str, Any]]:
    """Get metadata for all supported locales."""
    return [get_locale_metadata(locale_id) for locale_id in ALL_LOCALES]


def get_date_format(locale_id: str) -> str:
    """Get date format for a locale."""
    locale = get_locale(locale_id)
    return locale.get("formats", {}).get("date", "YYYY-MM-DD")


def get_number_format(locale_id: str) -> Dict[str, str]:
    """Get number format settings for a locale."""
    locale = get_locale(locale_id)
    return locale.get("formats", {}).get("number", {
        "decimal": ".",
        "thousands": ",",
    })


# Translation template generation
def generate_translation_template(
    locale_id: str,
    format: str = "json",
    include_metadata: bool = True
) -> str:
    """Generate a translation template for a locale."""
    locale = get_locale(locale_id)
    translations = locale.get("translations", {})

    template: Dict[str, Any] = {}

    if include_metadata:
        template["_metadata"] = {
            "locale": locale_id,
            "name": locale["name"],
            "direction": locale["direction"],
            "generated_by": f"Project Foundation Template v{SCRIPT_VERSION}",
        }

    template["common"] = translations.get("common", {
        "yes": "",
        "no": "",
        "ok": "",
        "cancel": "",
        "save": "",
        "delete": "",
        "edit": "",
        "close": "",
        "loading": "",
        "error": "",
        "success": "",
        "warning": "",
    })

    template["governance"] = translations.get("governance", {
        "readme": "",
        "contributing": "",
        "license": "",
        "code_of_conduct": "",
        "security_policy": "",
        "changelog": "",
    })

    template["errors"] = translations.get("errors", {
        "not_found": "",
        "unauthorized": "",
        "validation_failed": "",
        "server_error": "",
    })

    if format.lower() == "yaml":
        return _dict_to_yaml(template)
    return json.dumps(template, indent=2, ensure_ascii=False)


def _yaml_scalar(value: Any) -> str:
    """Write a value as a YAML scalar that loads back unchanged.

    Strings are always double-quoted, JSON style (a valid YAML double-quoted scalar),
    so values such as `yes`, `no`, `*anchor`, `@user` and `a: b` stay strings and
    quotes and backslashes are escaped.
    """
    if isinstance(value, str):
        quoted = json.dumps(value, ensure_ascii=False)
        # JSON leaves these unescaped, but YAML reads U+0085, U+2028 and U+2029 as line
        # breaks and rejects U+007F, so escape them too
        for char in ("\x7f", "\x85", " ", " "):
            quoted = quoted.replace(char, f"\\u{ord(char):04x}")
        return quoted
    return json.dumps(value)  # true/false, null and numbers are the same in YAML


# Words YAML 1.1 loaders (such as PyYAML) read as booleans or null, not strings
_YAML_RESERVED_WORDS = {"y", "n", "yes", "no", "on", "off", "true", "false", "null", "~"}


def _yaml_key(key: Any) -> str:
    """Write a mapping key, quoting it unless it is a plain identifier."""
    key = str(key)
    if (key and (key[0].isalpha() or key[0] == "_")
            and all(c.isalnum() or c == "_" for c in key)
            and key.lower() not in _YAML_RESERVED_WORDS):
        return key
    return _yaml_scalar(key)


def _dict_to_yaml(d: Dict, indent: int = 0) -> str:
    """Convert a dictionary to YAML format."""
    lines = []
    prefix = "  " * indent

    for key, value in d.items():
        if isinstance(value, dict) and value:
            lines.append(f"{prefix}{_yaml_key(key)}:")
            lines.append(_dict_to_yaml(value, indent + 1))
        elif isinstance(value, dict):
            lines.append(f"{prefix}{_yaml_key(key)}: {{}}")
        else:
            lines.append(f"{prefix}{_yaml_key(key)}: {_yaml_scalar(value)}")

    return "\n".join(lines)


def get_supported_locales_table() -> str:
    """Generate a markdown table of supported locales."""
    lines = [
        "| Code | Language | Native Name | Direction | Script |",
        "|------|----------|-------------|-----------|--------|",
    ]

    for locale_id, locale in ALL_LOCALES.items():
        direction = "RTL" if locale["direction"] == RTL else "LTR"
        script = locale.get("script", "Latin")
        lines.append(
            f"| {locale_id} | {locale['name']} | {locale['native_name']} | "
            f"{direction} | {script} |"
        )

    return "\n".join(lines)
