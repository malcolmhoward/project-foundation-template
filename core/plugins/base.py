# core/plugins/base.py
# Base classes for plugin development

"""
Base classes for Project Foundation Template plugins.

This module provides the base classes that users inherit from to create
custom principles and guides that integrate with the foundation template.

Example:
    from core.plugins.base import PrinciplePlugin

    class MyPrinciple(PrinciplePlugin):
        PRINCIPLE_ID = "my-custom-principle"
        PRINCIPLE = {
            "name": "My Custom Principle",
            "why": "Because it matters",
            "what": "What this principle covers",
            "risk": "What happens without it",
        }
        EDUCATION = "Educational content here..."
"""

from abc import ABC
from typing import ClassVar


class PrinciplePlugin(ABC):
    """Base class for custom principle plugins.

    Inherit from this class to create a custom principle that can be
    loaded by the plugin system and used alongside built-in principles.

    Class Attributes:
        PRINCIPLE_ID: Unique identifier for this principle (e.g., 'my-principle').
                     Must be lowercase with hyphens, no spaces.
        PRINCIPLE: Dict containing the principle definition with keys:
                  - name: Human-readable name
                  - why: Rationale for this principle
                  - what: What this principle covers
                  - risk: Consequences of not following this principle
        EDUCATION: Educational content string explaining this principle
                  in more detail. Can include markdown formatting.

    Example:
        class SecurityBestPractices(PrinciplePlugin):
            PRINCIPLE_ID = "security-best-practices"

            PRINCIPLE = {
                "name": "Security Best Practices",
                "why": "Protects users and organization from vulnerabilities",
                "what": "Comprehensive security guidelines and checks",
                "risk": "Data breaches, reputation damage, legal liability",
            }

            EDUCATION = '''
            Security best practices include:
            - Regular dependency updates
            - Input validation
            - Secure authentication
            '''
    """

    PRINCIPLE_ID: ClassVar[str] = ""
    PRINCIPLE: ClassVar[dict] = {}
    EDUCATION: ClassVar[str] = ""

    @classmethod
    def get_id(cls) -> str:
        """Get the principle identifier.

        Returns:
            The unique principle ID string.
        """
        return cls.PRINCIPLE_ID

    @classmethod
    def get_principle(cls) -> dict:
        """Get the principle definition.

        Returns:
            Dict with name, why, what, and risk keys.
        """
        return cls.PRINCIPLE.copy()

    @classmethod
    def get_education(cls) -> str:
        """Get the educational content.

        Returns:
            Educational content string.
        """
        return cls.EDUCATION

    @classmethod
    def to_dict(cls) -> dict:
        """Convert the plugin to a dictionary representation.

        Returns:
            Dict with id, principle, and education keys.
        """
        return {
            "id": cls.PRINCIPLE_ID,
            "principle": cls.PRINCIPLE.copy(),
            "education": cls.EDUCATION,
        }


class GuidePlugin(ABC):
    """Base class for custom guide plugins.

    Inherit from this class to create a custom guide that can be
    loaded by the plugin system and used alongside built-in guides.

    Class Attributes:
        GUIDE_ID: Unique identifier for this guide (e.g., 'my-guide').
                 Must be lowercase with hyphens, no spaces.
        GUIDE: Dict containing the guide metadata with keys:
              - title: Human-readable title
              - purpose: What users will learn
              - audience: Who this guide is for
              - complexity: One of 'beginner', 'intermediate', 'advanced'
        CONTENT: The actual guide content as a string.
                Can include full markdown formatting.
        RELATED_PRINCIPLES: Optional list of related principle IDs.

    Example:
        class TestingGuide(GuidePlugin):
            GUIDE_ID = "testing-guide"

            GUIDE = {
                "title": "Testing Best Practices Guide",
                "purpose": "Learn how to write effective tests",
                "audience": "Developers",
                "complexity": "intermediate",
            }

            CONTENT = '''
            # Testing Best Practices

            ## Overview
            This guide covers testing strategies...

            ## Unit Testing
            ...
            '''

            RELATED_PRINCIPLES = ["quality-assurance", "code-standards"]
    """

    GUIDE_ID: ClassVar[str] = ""
    GUIDE: ClassVar[dict] = {}
    CONTENT: ClassVar[str] = ""
    RELATED_PRINCIPLES: ClassVar[list] = []

    @classmethod
    def get_id(cls) -> str:
        """Get the guide identifier.

        Returns:
            The unique guide ID string.
        """
        return cls.GUIDE_ID

    @classmethod
    def get_guide(cls) -> dict:
        """Get the guide metadata.

        Returns:
            Dict with title, purpose, audience, and complexity keys.
        """
        return cls.GUIDE.copy()

    @classmethod
    def get_content(cls) -> str:
        """Get the guide content.

        Returns:
            Guide content string (markdown).
        """
        return cls.CONTENT

    @classmethod
    def get_related_principles(cls) -> list:
        """Get related principle IDs.

        Returns:
            List of principle ID strings.
        """
        return cls.RELATED_PRINCIPLES.copy()

    @classmethod
    def to_dict(cls) -> dict:
        """Convert the plugin to a dictionary representation.

        Returns:
            Dict with id, guide, content, and related_principles keys.
        """
        return {
            "id": cls.GUIDE_ID,
            "guide": cls.GUIDE.copy(),
            "content": cls.CONTENT,
            "related_principles": cls.RELATED_PRINCIPLES.copy(),
        }


class PluginMetadata:
    """Metadata for a plugin module.

    This class stores information about a plugin for display and
    management purposes.

    Attributes:
        name: Human-readable plugin name.
        version: Plugin version string (e.g., '1.0.0').
        author: Plugin author name or email.
        description: Brief description of what the plugin provides.
        source_path: Path to the plugin file.
    """

    def __init__(
        self,
        name: str,
        version: str = "1.0.0",
        author: str = "",
        description: str = "",
        source_path: str = "",
    ):
        """Initialize plugin metadata.

        Args:
            name: Human-readable plugin name.
            version: Plugin version string.
            author: Plugin author name or email.
            description: Brief description of the plugin.
            source_path: Path to the plugin file.
        """
        self.name = name
        self.version = version
        self.author = author
        self.description = description
        self.source_path = source_path

    def to_dict(self) -> dict:
        """Convert metadata to dictionary.

        Returns:
            Dict with all metadata fields.
        """
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
            "source_path": self.source_path,
        }

    def __repr__(self) -> str:
        return f"PluginMetadata(name='{self.name}', version='{self.version}')"


__all__ = [
    "PrinciplePlugin",
    "GuidePlugin",
    "PluginMetadata",
]
