# core/plugins/validator.py
# Plugin validation logic

"""
Plugin validation for Project Foundation Template.

This module provides validation functions to ensure plugins conform
to the expected structure before they are loaded and used.
"""

import re
from typing import List, Tuple, Type, Union

from .base import PrinciplePlugin, GuidePlugin


# Valid ID pattern: lowercase letters, numbers, and hyphens
ID_PATTERN = re.compile(r"^[a-z][a-z0-9-]*[a-z0-9]$|^[a-z]$")

# Required fields for principles
PRINCIPLE_REQUIRED_FIELDS = {"name", "why", "what", "risk"}

# Required fields for guides
GUIDE_REQUIRED_FIELDS = {"title", "purpose", "audience", "complexity"}

# Valid complexity levels
VALID_COMPLEXITY_LEVELS = {"beginner", "intermediate", "advanced"}


class ValidationError:
    """Represents a single validation error.

    Attributes:
        field: The field that failed validation.
        message: Human-readable error message.
        severity: Either 'error' (blocks loading) or 'warning' (informational).
    """

    def __init__(self, field: str, message: str, severity: str = "error"):
        """Initialize a validation error.

        Args:
            field: Field name that failed validation.
            message: Description of the error.
            severity: 'error' or 'warning'.
        """
        self.field = field
        self.message = message
        self.severity = severity

    def __repr__(self) -> str:
        return f"ValidationError({self.severity}: {self.field} - {self.message})"

    def __str__(self) -> str:
        return f"[{self.severity.upper()}] {self.field}: {self.message}"


class ValidationResult:
    """Result of plugin validation.

    Attributes:
        valid: True if the plugin passed validation.
        errors: List of validation errors.
        warnings: List of validation warnings.
        plugin_type: Type of plugin ('principle' or 'guide').
        plugin_id: The plugin's ID if available.
    """

    def __init__(self, plugin_type: str, plugin_id: str = ""):
        """Initialize a validation result.

        Args:
            plugin_type: Type of plugin being validated.
            plugin_id: Plugin identifier.
        """
        self.plugin_type = plugin_type
        self.plugin_id = plugin_id
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []

    def add_error(self, field: str, message: str) -> None:
        """Add a validation error.

        Args:
            field: Field that failed validation.
            message: Error description.
        """
        self.errors.append(ValidationError(field, message, "error"))

    def add_warning(self, field: str, message: str) -> None:
        """Add a validation warning.

        Args:
            field: Field with warning.
            message: Warning description.
        """
        self.warnings.append(ValidationError(field, message, "warning"))

    @property
    def valid(self) -> bool:
        """Check if the plugin is valid (no errors).

        Returns:
            True if there are no errors.
        """
        return len(self.errors) == 0

    def format_errors(self) -> str:
        """Format all errors as a string.

        Returns:
            Newline-separated list of errors.
        """
        if not self.errors:
            return "No errors"
        return "\n".join(str(e) for e in self.errors)

    def format_all(self) -> str:
        """Format all errors and warnings.

        Returns:
            Formatted string with all issues.
        """
        lines = []
        if self.errors:
            lines.append("Errors:")
            lines.extend(f"  - {e}" for e in self.errors)
        if self.warnings:
            lines.append("Warnings:")
            lines.extend(f"  - {w}" for w in self.warnings)
        if not lines:
            return "Validation passed"
        return "\n".join(lines)


def validate_id(plugin_id: str, plugin_type: str) -> List[ValidationError]:
    """Validate a plugin ID.

    Args:
        plugin_id: The ID to validate.
        plugin_type: Type of plugin for error messages.

    Returns:
        List of validation errors (empty if valid).
    """
    errors = []

    if not plugin_id:
        errors.append(ValidationError(
            f"{plugin_type.upper()}_ID",
            f"{plugin_type.capitalize()} ID is required and cannot be empty"
        ))
        return errors

    if not isinstance(plugin_id, str):
        errors.append(ValidationError(
            f"{plugin_type.upper()}_ID",
            f"{plugin_type.capitalize()} ID must be a string"
        ))
        return errors

    if not ID_PATTERN.match(plugin_id):
        errors.append(ValidationError(
            f"{plugin_type.upper()}_ID",
            f"Invalid ID '{plugin_id}'. Must be lowercase, start with a letter, "
            f"and contain only letters, numbers, and hyphens (e.g., 'my-plugin')"
        ))

    if len(plugin_id) > 50:
        errors.append(ValidationError(
            f"{plugin_type.upper()}_ID",
            f"ID '{plugin_id}' is too long. Maximum 50 characters."
        ))

    return errors


def validate_principle_dict(principle: dict) -> List[ValidationError]:
    """Validate a principle dictionary.

    Args:
        principle: The PRINCIPLE dict to validate.

    Returns:
        List of validation errors.
    """
    errors = []

    if not principle:
        errors.append(ValidationError(
            "PRINCIPLE",
            "PRINCIPLE dictionary is required and cannot be empty"
        ))
        return errors

    if not isinstance(principle, dict):
        errors.append(ValidationError(
            "PRINCIPLE",
            "PRINCIPLE must be a dictionary"
        ))
        return errors

    # Check required fields
    missing = PRINCIPLE_REQUIRED_FIELDS - set(principle.keys())
    if missing:
        errors.append(ValidationError(
            "PRINCIPLE",
            f"Missing required fields: {', '.join(sorted(missing))}"
        ))

    # Validate field types and content
    for field in PRINCIPLE_REQUIRED_FIELDS:
        if field in principle:
            value = principle[field]
            if not isinstance(value, str):
                errors.append(ValidationError(
                    f"PRINCIPLE.{field}",
                    f"Field '{field}' must be a string, got {type(value).__name__}"
                ))
            elif not value.strip():
                errors.append(ValidationError(
                    f"PRINCIPLE.{field}",
                    f"Field '{field}' cannot be empty"
                ))

    return errors


def validate_guide_dict(guide: dict) -> List[ValidationError]:
    """Validate a guide dictionary.

    Args:
        guide: The GUIDE dict to validate.

    Returns:
        List of validation errors.
    """
    errors = []

    if not guide:
        errors.append(ValidationError(
            "GUIDE",
            "GUIDE dictionary is required and cannot be empty"
        ))
        return errors

    if not isinstance(guide, dict):
        errors.append(ValidationError(
            "GUIDE",
            "GUIDE must be a dictionary"
        ))
        return errors

    # Check required fields
    missing = GUIDE_REQUIRED_FIELDS - set(guide.keys())
    if missing:
        errors.append(ValidationError(
            "GUIDE",
            f"Missing required fields: {', '.join(sorted(missing))}"
        ))

    # Validate field types and content
    for field in GUIDE_REQUIRED_FIELDS:
        if field in guide:
            value = guide[field]
            if not isinstance(value, str):
                errors.append(ValidationError(
                    f"GUIDE.{field}",
                    f"Field '{field}' must be a string, got {type(value).__name__}"
                ))
            elif not value.strip():
                errors.append(ValidationError(
                    f"GUIDE.{field}",
                    f"Field '{field}' cannot be empty"
                ))

    # Validate complexity level
    if "complexity" in guide and isinstance(guide["complexity"], str):
        if guide["complexity"].lower() not in VALID_COMPLEXITY_LEVELS:
            errors.append(ValidationError(
                "GUIDE.complexity",
                f"Invalid complexity '{guide['complexity']}'. "
                f"Must be one of: {', '.join(sorted(VALID_COMPLEXITY_LEVELS))}"
            ))

    return errors


def validate_principle_plugin(
    plugin_class: Type[PrinciplePlugin]
) -> ValidationResult:
    """Validate a principle plugin class.

    Args:
        plugin_class: The plugin class to validate.

    Returns:
        ValidationResult with any errors or warnings.
    """
    result = ValidationResult("principle")

    # Check it's a proper class
    if not isinstance(plugin_class, type):
        result.add_error("class", "Plugin must be a class, not an instance")
        return result

    # Check inheritance (optional but recommended)
    if not issubclass(plugin_class, PrinciplePlugin):
        result.add_warning(
            "class",
            "Plugin does not inherit from PrinciplePlugin. "
            "Consider inheriting for better IDE support."
        )

    # Validate PRINCIPLE_ID
    principle_id = getattr(plugin_class, "PRINCIPLE_ID", None)
    result.plugin_id = principle_id or ""
    for error in validate_id(principle_id, "principle"):
        result.errors.append(error)

    # Validate PRINCIPLE dict
    principle = getattr(plugin_class, "PRINCIPLE", None)
    for error in validate_principle_dict(principle):
        result.errors.append(error)

    # Validate EDUCATION (required but can be empty)
    education = getattr(plugin_class, "EDUCATION", None)
    if education is None:
        result.add_error("EDUCATION", "EDUCATION attribute is required")
    elif not isinstance(education, str):
        result.add_error(
            "EDUCATION",
            f"EDUCATION must be a string, got {type(education).__name__}"
        )
    elif not education.strip():
        result.add_warning(
            "EDUCATION",
            "EDUCATION is empty. Consider adding educational content."
        )

    return result


def validate_guide_plugin(plugin_class: Type[GuidePlugin]) -> ValidationResult:
    """Validate a guide plugin class.

    Args:
        plugin_class: The plugin class to validate.

    Returns:
        ValidationResult with any errors or warnings.
    """
    result = ValidationResult("guide")

    # Check it's a proper class
    if not isinstance(plugin_class, type):
        result.add_error("class", "Plugin must be a class, not an instance")
        return result

    # Check inheritance (optional but recommended)
    if not issubclass(plugin_class, GuidePlugin):
        result.add_warning(
            "class",
            "Plugin does not inherit from GuidePlugin. "
            "Consider inheriting for better IDE support."
        )

    # Validate GUIDE_ID
    guide_id = getattr(plugin_class, "GUIDE_ID", None)
    result.plugin_id = guide_id or ""
    for error in validate_id(guide_id, "guide"):
        result.errors.append(error)

    # Validate GUIDE dict
    guide = getattr(plugin_class, "GUIDE", None)
    for error in validate_guide_dict(guide):
        result.errors.append(error)

    # Validate CONTENT (required)
    content = getattr(plugin_class, "CONTENT", None)
    if content is None:
        result.add_error("CONTENT", "CONTENT attribute is required")
    elif not isinstance(content, str):
        result.add_error(
            "CONTENT",
            f"CONTENT must be a string, got {type(content).__name__}"
        )
    elif not content.strip():
        result.add_error("CONTENT", "CONTENT cannot be empty")

    # Validate RELATED_PRINCIPLES (optional)
    related = getattr(plugin_class, "RELATED_PRINCIPLES", [])
    if related is not None:
        if not isinstance(related, list):
            result.add_error(
                "RELATED_PRINCIPLES",
                f"RELATED_PRINCIPLES must be a list, got {type(related).__name__}"
            )
        else:
            for i, item in enumerate(related):
                if not isinstance(item, str):
                    result.add_error(
                        f"RELATED_PRINCIPLES[{i}]",
                        f"Must be a string, got {type(item).__name__}"
                    )

    return result


def validate_plugin(
    plugin_class: type,
    plugin_type: str = "auto"
) -> ValidationResult:
    """Validate a plugin class.

    Args:
        plugin_class: The plugin class to validate.
        plugin_type: 'principle', 'guide', or 'auto' to detect.

    Returns:
        ValidationResult with any errors or warnings.

    Raises:
        ValueError: If plugin_type is invalid or cannot be detected.
    """
    if plugin_type == "auto":
        # Try to detect based on attributes or inheritance
        if hasattr(plugin_class, "PRINCIPLE_ID") and hasattr(plugin_class, "PRINCIPLE"):
            plugin_type = "principle"
        elif hasattr(plugin_class, "GUIDE_ID") and hasattr(plugin_class, "GUIDE"):
            plugin_type = "guide"
        else:
            result = ValidationResult("unknown")
            result.add_error(
                "class",
                "Cannot determine plugin type. Plugin must have either "
                "(PRINCIPLE_ID, PRINCIPLE) or (GUIDE_ID, GUIDE) attributes."
            )
            return result

    if plugin_type == "principle":
        return validate_principle_plugin(plugin_class)
    elif plugin_type == "guide":
        return validate_guide_plugin(plugin_class)
    else:
        raise ValueError(f"Invalid plugin_type: {plugin_type}. Use 'principle', 'guide', or 'auto'.")


__all__ = [
    "ValidationError",
    "ValidationResult",
    "validate_id",
    "validate_principle_dict",
    "validate_guide_dict",
    "validate_principle_plugin",
    "validate_guide_plugin",
    "validate_plugin",
    "PRINCIPLE_REQUIRED_FIELDS",
    "GUIDE_REQUIRED_FIELDS",
    "VALID_COMPLEXITY_LEVELS",
]
