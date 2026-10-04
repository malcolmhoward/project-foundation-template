# core/programming_languages/lua.py
# Lua language configuration (v3.5.0)

"""
Lua Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Lua projects.

Official Resources:
- Website: https://www.lua.org/
- Documentation: https://www.lua.org/docs.html
- LuaRocks: https://luarocks.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "lua"

LANGUAGE = {
    "name": "Lua",
    "id": "lua",
    "extensions": ["lua"],
    "category": "specialized",
    "official_website": "https://www.lua.org/",
    "documentation_url": "https://www.lua.org/docs.html",

    # Package managers
    "package_managers": [
        {
            "name": "luarocks",
            "config_files": ["*.rockspec"],
            "lock_file": None,
            "install_cmd": "luarocks install --deps-only *.rockspec",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "luacheck",
            "description": "Static analyzer (recommended)",
            "config_files": [".luacheckrc"],
            "command": "luacheck .",
        },
        {
            "name": "selene",
            "description": "Modern Lua linter",
            "config_files": ["selene.toml"],
            "command": "selene .",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "stylua",
            "description": "Opinionated formatter (recommended)",
            "config_files": ["stylua.toml", ".stylua.toml"],
            "command": "stylua .",
        },
        {
            "name": "lua-format",
            "description": "Configurable formatter",
            "config_files": [".lua-format"],
            "command": "lua-format -i *.lua",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "busted",
            "description": "BDD testing framework (recommended)",
            "config_files": [".busted"],
            "command": "busted",
        },
        {
            "name": "luaunit",
            "description": "xUnit-style testing",
            "config_files": [],
            "command": "lua test.lua",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "luarocks",
            "config_files": ["*.rockspec"],
            "description": "Package manager and build system",
        },
        {
            "name": "make",
            "config_files": ["Makefile"],
            "description": "Traditional build tool",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/JohnnyMorganz/StyLua",
            "hooks": ["stylua"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: leafo/gh-actions-lua@v10",
            "  with:",
            "    luaVersion: '5.4'",
            "- uses: leafo/gh-actions-luarocks@v4",
        ],
        "install_steps": [
            "- run: luarocks install busted",
        ],
        "lint_steps": [
            "- run: luarocks install luacheck && luacheck .",
        ],
        "test_steps": [
            "- run: busted",
        ],
        "matrix": {
            "lua-version": ["5.3", "5.4", "luajit"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "LDoc", "description": "Lua documentation generator"},
    ],

    # Lua-specific features
    "features": {
        "versions": ["5.1", "5.2", "5.3", "5.4"],
        "luajit": True,
        "coroutines": True,
        "metatables": True,
    },
}
