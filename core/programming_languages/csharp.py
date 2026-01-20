# core/programming_languages/csharp.py
# C# language configuration (v3.5.0)

"""
C# Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for C# projects.

Official Resources:
- Website: https://dotnet.microsoft.com/
- Documentation: https://learn.microsoft.com/en-us/dotnet/csharp/
- NuGet: https://www.nuget.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "csharp"

LANGUAGE = {
    "name": "C#",
    "id": "csharp",
    "extensions": ["cs", "csx"],
    "category": "tier-2",
    "official_website": "https://dotnet.microsoft.com/",
    "documentation_url": "https://learn.microsoft.com/en-us/dotnet/csharp/",

    # Package managers
    "package_managers": [
        {
            "name": "nuget",
            "config_files": ["*.csproj", "nuget.config"],
            "lock_file": "packages.lock.json",
            "install_cmd": "dotnet restore",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "dotnet format",
            "description": "Built-in analyzer",
            "config_files": [".editorconfig"],
            "command": "dotnet format --verify-no-changes",
        },
        {
            "name": "roslyn analyzers",
            "description": "Code analysis",
            "config_files": [".editorconfig"],
            "command": "dotnet build /p:TreatWarningsAsErrors=true",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "dotnet format",
            "description": "Built-in formatter (recommended)",
            "config_files": [".editorconfig"],
            "command": "dotnet format",
        },
        {
            "name": "csharpier",
            "description": "Opinionated formatter",
            "config_files": [".csharpierrc"],
            "command": "dotnet csharpier .",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "xunit",
            "description": "Unit testing (recommended)",
            "config_files": [],
            "command": "dotnet test",
            "coverage_cmd": "dotnet test --collect:'XPlat Code Coverage'",
        },
        {
            "name": "nunit",
            "description": "Alternative testing framework",
            "config_files": [],
            "command": "dotnet test",
        },
        {
            "name": "mstest",
            "description": "Microsoft testing framework",
            "config_files": [],
            "command": "dotnet test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "dotnet cli",
            "config_files": ["*.csproj", "*.sln"],
            "description": "Built-in build system",
        },
        {
            "name": "msbuild",
            "config_files": ["*.csproj", "*.sln"],
            "description": "Full build system",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/dotnet/format",
            "hooks": ["dotnet-format"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-dotnet@v4",
            "  with:",
            "    dotnet-version: '8.0.x'",
        ],
        "install_steps": [
            "- run: dotnet restore",
        ],
        "lint_steps": [
            "- run: dotnet format --verify-no-changes",
        ],
        "test_steps": [
            "- run: dotnet test --no-restore",
        ],
        "matrix": {
            "dotnet-version": ["6.0.x", "8.0.x"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "DocFX", "description": "Documentation generator"},
        {"name": "XML comments", "description": "In-code documentation"},
    ],

    # C#-specific features
    "features": {
        "lts_versions": [".NET 6", ".NET 8"],
        "nullable": True,
        "records": True,
        "top_level_statements": True,
    },
}
