# core/programming_languages/scala.py
# Scala language configuration (v3.5.0)

"""
Scala Language Configuration.

Provides tooling, linting, formatting, testing, and CI/CD configurations
for Scala projects.

Official Resources:
- Website: https://www.scala-lang.org/
- Documentation: https://docs.scala-lang.org/
- Scala 3 (Dotty): https://docs.scala-lang.org/scala3/

Introduced in v3.5.0 to fulfill 18-language specification.
"""

LANGUAGE_ID = "scala"

LANGUAGE = {
    "name": "Scala",
    "id": "scala",
    "extensions": ["scala", "sc"],
    "category": "tier-3",
    "official_website": "https://www.scala-lang.org/",
    "documentation_url": "https://docs.scala-lang.org/",

    # Package managers / Build tools (Scala uses build tools for deps)
    "package_managers": [
        {
            "name": "sbt",
            "config_files": ["build.sbt", "project/build.properties"],
            "lock_file": None,
            "install_cmd": "sbt compile",
            "description": "Simple Build Tool (recommended)",
        },
        {
            "name": "mill",
            "config_files": ["build.sc"],
            "lock_file": None,
            "install_cmd": "mill _.compile",
            "description": "Modern Scala build tool",
        },
        {
            "name": "gradle",
            "config_files": ["build.gradle", "build.gradle.kts"],
            "lock_file": "gradle.lockfile",
            "install_cmd": "gradle build",
            "description": "Cross-platform build tool",
        },
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "lock_file": None,
            "install_cmd": "mvn compile",
            "description": "Java ecosystem integration",
        },
    ],

    # Linters
    "linters": [
        {
            "name": "scalafix",
            "description": "Refactoring and linting tool (recommended)",
            "config_files": [".scalafix.conf"],
            "command": "sbt scalafix",
        },
        {
            "name": "wartremover",
            "description": "Flexible Scala linter",
            "config_files": [],
            "command": "sbt compile",  # Runs as compiler plugin
        },
        {
            "name": "scalastyle",
            "description": "Style checker (legacy, use scalafix)",
            "config_files": ["scalastyle-config.xml"],
            "command": "sbt scalastyle",
        },
    ],

    # Formatters
    "formatters": [
        {
            "name": "scalafmt",
            "description": "Opinionated code formatter (recommended)",
            "config_files": [".scalafmt.conf"],
            "command": "sbt scalafmt",
        },
        {
            "name": "scalariform",
            "description": "Scala source code formatter (legacy)",
            "config_files": [".scalariform.conf"],
            "command": "sbt scalariformFormat",
        },
    ],

    # Test frameworks
    "test_frameworks": [
        {
            "name": "scalatest",
            "description": "Flexible testing (recommended)",
            "config_files": [],
            "command": "sbt test",
            "coverage_cmd": "sbt coverage test coverageReport",
        },
        {
            "name": "specs2",
            "description": "BDD-style testing",
            "config_files": [],
            "command": "sbt test",
        },
        {
            "name": "munit",
            "description": "Lightweight testing (Scala 3)",
            "config_files": [],
            "command": "sbt test",
        },
        {
            "name": "zio-test",
            "description": "ZIO ecosystem testing",
            "config_files": [],
            "command": "sbt test",
        },
    ],

    # Build tools
    "build_tools": [
        {
            "name": "sbt",
            "config_files": ["build.sbt", "project/build.properties", "project/plugins.sbt"],
            "description": "Simple Build Tool (recommended)",
        },
        {
            "name": "mill",
            "config_files": ["build.sc"],
            "description": "Modern build tool with better performance",
        },
        {
            "name": "gradle",
            "config_files": ["build.gradle", "build.gradle.kts"],
            "description": "Cross-platform build automation",
        },
        {
            "name": "maven",
            "config_files": ["pom.xml"],
            "description": "Java ecosystem compatibility",
        },
    ],

    # Pre-commit hooks
    "precommit_hooks": [
        {
            "repo": "https://github.com/pre-commit/mirrors-scalafmt",
            "hooks": ["scalafmt"],
        },
    ],

    # CI workflow
    "ci_workflow": {
        "setup_steps": [
            "- uses: actions/setup-java@v4",
            "  with:",
            "    java-version: '21'",
            "    distribution: 'temurin'",
            "- uses: coursier/setup-action@v1",
            "  with:",
            "    apps: sbt",
        ],
        "install_steps": [
            "- run: sbt compile",
        ],
        "lint_steps": [
            "- run: sbt scalafmtCheck",
            "- run: sbt 'scalafixAll --check'",
        ],
        "test_steps": [
            "- run: sbt test",
        ],
        "matrix": {
            "java-version": ["17", "21"],
            "scala-version": ["2.13", "3.3"],
        },
    },

    # Documentation
    "documentation_tools": [
        {"name": "Scaladoc", "description": "API documentation generator"},
        {"name": "mdoc", "description": "Typechecked markdown documentation"},
        {"name": "Laika", "description": "Site generator for Scala projects"},
    ],

    # Scala-specific features
    "features": {
        "scala3": True,
        "scala2_compat": True,
        "jvm_interop": True,
        "js_backend": True,  # Scala.js
        "native_backend": True,  # Scala Native
        "typelevel_ecosystem": True,  # Cats, Cats Effect, FS2, etc.
        "zio_ecosystem": True,  # ZIO, ZIO HTTP, etc.
        "akka_ecosystem": True,  # Akka, Akka HTTP, Pekko
    },

    # Common project templates
    "templates": {
        "minimal": "sbt new scala/scala3.g8",
        "typelevel": "sbt new typelevel/typelevel-template.g8",
        "zio": "sbt new zio/zio-project.g8",
        "http4s": "sbt new http4s/http4s.g8",
        "play": "sbt new playframework/play-scala-seed.g8",
    },

    # Sample configuration files
    "sample_configs": {
        ".scalafmt.conf": """version = 3.7.17
runner.dialect = scala3
maxColumn = 100
align.preset = more
rewrite.rules = [
  RedundantBraces,
  RedundantParens,
  SortModifiers,
  PreferCurlyFors
]
""",
        ".scalafix.conf": """rules = [
  OrganizeImports,
  RemoveUnused,
  LeakingImplicitClassVal,
  NoValInForComprehension
]

OrganizeImports {
  groupedImports = Merge
  groups = [
    "re:javax?\\\\.",
    "scala.",
    "*"
  ]
}
""",
        "build.sbt": """ThisBuild / scalaVersion := "3.3.1"
ThisBuild / organization := "com.example"
ThisBuild / version := "0.1.0-SNAPSHOT"

lazy val root = project
  .in(file("."))
  .settings(
    name := "my-project",
    libraryDependencies ++= Seq(
      "org.scalameta" %% "munit" % "0.7.29" % Test
    )
  )
""",
    },
}
