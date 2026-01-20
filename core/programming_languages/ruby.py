# core/programming_languages/ruby.py
# Ruby language configuration (v3.5.0)

"""
Ruby Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Ruby projects.

Official Resources:
- Website: https://www.ruby-lang.org/
- Documentation: https://ruby-doc.org/
- RubyGems: https://rubygems.org/

Introduced in v3.5.0.
"""

LANGUAGE_ID = "ruby"

LANGUAGE = {
    "name": "Ruby",
    "id": "ruby",
    "extensions": ["rb", "rake", "gemspec"],
    "category": "tier-3",
    "official_website": "https://www.ruby-lang.org/",
    "documentation_url": "https://ruby-doc.org/",

    # Package managers
    "package_managers": [
        {
            "name": "bundler",
            "config_files": ["Gemfile"],
            "lock_file": "Gemfile.lock",
            "install_cmd": "bundle install",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "rubocop",
            "description": "Static code analyzer (recommended)",
            "config_files": [".rubocop.yml"],
            "command": "bundle exec rubocop",
        },
        {
            "name": "reek",
            "description": "Code smell detector",
            "config_files": [".reek.yml"],
            "command": "bundle exec reek",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "rubocop",
            "description": "Auto-correct style issues",
            "config_files": [".rubocop.yml"],
            "command": "bundle exec rubocop -A",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "rspec",
            "description": "BDD testing (recommended)",
            "config_files": [".rspec", "spec/spec_helper.rb"],
            "command": "bundle exec rspec",
            "coverage_cmd": "bundle exec rspec --format documentation",
        },
        {
            "name": "minitest",
            "description": "Standard library testing",
            "config_files": [],
            "command": "bundle exec rake test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "rake",
            "config_files": ["Rakefile"],
            "description": "Ruby make",
        },
        {
            "name": "bundler",
            "config_files": ["Gemfile"],
            "description": "Dependency management",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/rubocop/rubocop",
            "hooks": ["rubocop"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: ruby/setup-ruby@v1",
            "  with:",
            "    ruby-version: '3.3'",
            "    bundler-cache: true",
        ],
        "install_steps": [
            "- run: bundle install",
        ],
        "lint_steps": [
            "- run: bundle exec rubocop",
        ],
        "test_steps": [
            "- run: bundle exec rspec",
        ],
        "matrix": {
            "ruby-version": ["3.1", "3.2", "3.3"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "YARD", "description": "Documentation generator"},
        {"name": "RDoc", "description": "Standard documentation"},
    ],

    # Ruby-specific features
    "features": {
        "minimum_version": "3.1",
        "recommended_version": "3.3",
        "yjit": True,  # Ruby 3.1+
        "pattern_matching": True,  # Ruby 3.0+
    },
}
