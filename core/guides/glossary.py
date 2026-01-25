# core/guides/glossary.py
# Glossary Guide (v3.0.0)

"""
Glossary Guide.

Provides definitions of common terms, abbreviations, and concepts
used throughout the project and software development.

Introduced in v3.0.0.
"""

GUIDE_ID = "glossary"

GUIDE = {
    "title": "Glossary of Terms",
    "purpose": "Understand common terms and concepts",
    "audience": "All contributors",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["readme", "contributing"]

CONTENT = """
# Glossary of Terms

## A

### ADR (Architecture Decision Record)
A document that captures an important architectural decision along with its
context and consequences. ADRs help preserve the "why" behind technical choices.

### API (Application Programming Interface)
A set of protocols and tools for building software applications. APIs define
how different software components should interact with each other.

### Artifact
Any output produced during the software development process, such as compiled
binaries, Docker images, documentation, or test reports.

### Async/Asynchronous
A programming pattern where operations can start without waiting for previous
operations to complete. Enables non-blocking execution.

## B

### Backward Compatible
A change that doesn't break existing functionality. Old code continues to work
with new versions of a library or API.

### Branch
A parallel version of the codebase in Git. Branches allow developers to work on
features independently before merging changes.

### Breaking Change
A change that causes existing code to stop working. Breaking changes require
a major version bump in semantic versioning.

### Build
The process of converting source code into executable software, including
compilation, bundling, and optimization.

## C

### CD (Continuous Delivery/Deployment)
- **Continuous Delivery:** Automated preparation of code for release
- **Continuous Deployment:** Automated release to production

### CI (Continuous Integration)
The practice of frequently merging code changes into a shared repository,
with automated testing to catch issues early.

### CLI (Command Line Interface)
A text-based interface for interacting with software using typed commands
rather than a graphical interface.

### Clone
Creating a local copy of a remote Git repository, including all history.

### Commit
A snapshot of changes in Git. Each commit has a unique identifier (SHA) and
records what changed, when, and by whom.

### Container
A lightweight, standalone package containing everything needed to run software,
including code, runtime, and dependencies. Docker is the most common container
platform.

### CRUD
Create, Read, Update, Delete - the four basic operations for persistent storage.

## D

### Dependency
External code or library that your project requires to function. Dependencies
can be direct (explicitly imported) or transitive (dependencies of dependencies).

### Deploy
The process of releasing software to an environment where it can be accessed
by users or other systems.

### Dev/Development Environment
A local setup where developers write and test code before it reaches production.

### Docker
A platform for developing, shipping, and running applications in containers.

### DRY (Don't Repeat Yourself)
A principle stating that every piece of knowledge should have a single,
unambiguous representation in a system.

## E

### Endpoint
A specific URL where an API can be accessed. Each endpoint typically represents
a specific resource or action.

### Environment Variable
A variable set outside the application code that configures behavior, such as
database URLs or API keys.

### E2E (End-to-End) Testing
Testing that validates complete user workflows from start to finish, simulating
real user interactions.

## F

### Feature Branch
A Git branch created to develop a specific feature, isolated from the main
codebase until complete.

### Fork
A personal copy of another user's repository on GitHub. Forks allow you to
experiment without affecting the original project.

### Framework
A foundational structure of code that provides generic functionality, which
developers extend to build applications (e.g., React, Django, Rails).

## G

### Git
A distributed version control system for tracking changes in source code.

### GitHub/GitLab
Web-based platforms for hosting Git repositories with additional collaboration
features like issues, pull requests, and CI/CD.

### Gitflow
A branching model that uses feature, develop, release, and hotfix branches
to manage development workflow.

## H

### Hash
A fixed-size string generated from input data. In Git, each commit has a
unique SHA-1 hash. Used for verification and identification.

### Hotfix
An urgent bug fix that bypasses the normal development process to quickly
address a critical production issue.

### HTTP (Hypertext Transfer Protocol)
The protocol used for communication on the web. RESTful APIs use HTTP methods
(GET, POST, PUT, DELETE) to perform operations.

## I

### IDE (Integrated Development Environment)
A software application providing comprehensive facilities for software
development, like VS Code, IntelliJ, or PyCharm.

### Idempotent
An operation that produces the same result regardless of how many times it's
executed. Important concept for API design.

### Integration Testing
Testing that verifies different components or systems work together correctly.

### Issue
A tracked item in a project management system representing a bug, feature
request, or task.

## J

### JSON (JavaScript Object Notation)
A lightweight data format used for storing and exchanging data. Common in
APIs and configuration files.

### JWT (JSON Web Token)
A compact, URL-safe token format used for securely transmitting information
between parties, commonly used for authentication.

## K

### Key (API Key)
A code used to identify and authenticate an application or user when making
API requests.

## L

### Lint/Linter
A tool that analyzes code for potential errors, bugs, and style violations.
Examples: ESLint (JavaScript), Pylint (Python).

### Load Balancer
A system that distributes incoming traffic across multiple servers to ensure
no single server becomes overwhelmed.

### Lock File
A file that records exact versions of all dependencies to ensure reproducible
builds (e.g., package-lock.json, poetry.lock).

## M

### Main/Master Branch
The primary branch in a Git repository, typically containing production-ready
code. "main" is now the preferred term.

### Merge
Combining changes from one Git branch into another.

### Microservice
An architectural style where an application is composed of small, independent
services that communicate over a network.

### Mock
A simulated object used in testing to replace real dependencies, allowing
isolated testing of components.

### MVP (Minimum Viable Product)
The simplest version of a product that can be released to gather user feedback.

## N

### npm (Node Package Manager)
The default package manager for Node.js, used to install and manage JavaScript
dependencies.

## O

### OAuth
An open standard for authorization that allows applications to access user
data without exposing passwords.

### ORM (Object-Relational Mapping)
A technique for converting data between incompatible type systems in
object-oriented programming languages and relational databases.

## P

### Package
A bundle of code that can be reused across projects. Distributed through
package managers like npm, pip, or cargo.

### Patch
A small update that fixes bugs without adding features or breaking changes.
The third number in semantic versioning (1.0.X).

### Pipeline
An automated sequence of steps that code goes through from commit to
deployment, typically including build, test, and deploy stages.

### PR (Pull Request)
A request to merge code changes from one branch to another. PRs enable
code review and discussion before changes are integrated.

### Production
The live environment where software is accessible to end users.

## R

### README
A document (typically README.md) that provides an overview of a project,
including installation and usage instructions.

### Refactor
Restructuring existing code without changing its external behavior to improve
readability, maintainability, or performance.

### Repository (Repo)
A storage location for a project's files and version history, managed by
a version control system like Git.

### REST (Representational State Transfer)
An architectural style for designing networked applications, commonly used
for web APIs.

### Rollback
Reverting to a previous version of deployed software, typically after
discovering issues with a new release.

## S

### Sandbox
An isolated environment for testing that doesn't affect production data
or systems.

### SDK (Software Development Kit)
A collection of tools, libraries, and documentation for building applications
for a specific platform or service.

### SemVer (Semantic Versioning)
A versioning scheme using MAJOR.MINOR.PATCH numbers to convey the nature
of changes (breaking, feature, fix).

### Sprint
A fixed time period (typically 1-4 weeks) during which specific work must
be completed in Agile development.

### SSH (Secure Shell)
A cryptographic protocol for secure communication, commonly used for
remote server access and Git operations.

### Staging
A pre-production environment that mirrors production, used for final testing
before release.

### Stub
A simplified implementation of a component used in testing, returning
predetermined responses.

## T

### TDD (Test-Driven Development)
A development approach where tests are written before the code they test,
driving the design of the implementation.

### Token
A piece of data used for authentication or authorization, such as an API
key or JWT.

### Transpile
Converting code from one language version to another (e.g., TypeScript to
JavaScript, or modern JS to older versions).

## U

### Unit Test
A test that verifies a single unit of code (function, method, class) works
correctly in isolation.

### Upstream
The original repository that a fork was created from. Also refers to the
direction of changes flowing toward the main branch.

## V

### Version Control
A system for tracking changes to files over time, allowing collaboration
and history preservation. Git is the most common.

### Virtual Environment
An isolated Python environment with its own dependencies, separate from
the system Python installation.

### VM (Virtual Machine)
Software that emulates a computer system, allowing multiple operating
systems to run on a single physical machine.

## W

### Webhook
An HTTP callback that sends data to a specified URL when an event occurs,
enabling real-time notifications between systems.

### Workflow
A defined sequence of steps or processes, often automated in CI/CD systems.

## Y

### YAML
A human-readable data serialization format commonly used for configuration
files (e.g., CI/CD pipelines, Kubernetes manifests).

## Symbols & Numbers

### 2FA (Two-Factor Authentication)
An authentication method requiring two different forms of identification,
such as a password and a code from a mobile app.

### 12-Factor App
A methodology for building software-as-a-service applications, covering
areas like configuration, dependencies, and processes.

---

## PFT-Specific Terms

These terms are specific to Project Foundation Template (PFT):

### Governance
The policies, processes, and documentation that guide how a project is developed,
maintained, and contributed to. This includes contribution guidelines, security
policies, codes of conduct, and architectural decision records.

### Governance Theater
The appearance of having proper governance without the substance - adopting
templates without understanding or customizing them. PFT is designed to prevent
this through education-first principles.

### Principle (Governance Principle)
A governance concept in PFT that defines WHAT must be done, WHY it matters, and
the RISK of not having it. Principles are the building blocks of governance.

### Guide (Implementation Guide)
Documentation in PFT explaining HOW to apply a principle. Guides provide
practical, actionable instructions for implementing governance concepts.

### Preset
A predefined collection of governance principles bundled for common use cases.
PFT includes presets: minimal, light, standard, strict, and enterprise.

### Principle Zero
PFT's foundational ethical principle: "Do No Harm, Allow No Harm." All decisions
in PFT flow from this principle, inspired by GAIA from Horizon Zero Dawn®.

> *Horizon Zero Dawn is a registered trademark of Sony Interactive Entertainment
> ([Trademark Notice](https://sonyinteractive.com/en/copyright-and-trademark-notice/)).
> This project is not affiliated with or endorsed by Sony Interactive Entertainment
> or Guerrilla Games.*

### Programming Language Configuration
Language-specific settings in PFT (v3.5.0+) that define tooling, linting,
formatting, testing, and CI/CD configurations for a programming language.

---

## Testing Methodologies

### ATDD (Acceptance Test-Driven Development)
A development approach where acceptance tests are written before implementation.
Tests are derived from user stories and acceptance criteria, ensuring the
software meets business requirements.

### BDD (Behavior-Driven Development)
An extension of TDD that uses natural language constructs (Given-When-Then)
to describe software behavior. BDD bridges communication between technical
and non-technical stakeholders. See also: Gherkin.

### Gherkin
A domain-specific language used in BDD frameworks like Cucumber. Uses keywords
like Given, When, Then, And, But to structure test scenarios in plain English.

### Load Testing
Performance testing that evaluates system behavior under expected and peak load
conditions. Measures response times, throughput, and resource utilization.

### Stress Testing
Testing that evaluates system behavior beyond normal capacity to identify
breaking points and recovery characteristics.

---

*Missing a term? Suggest additions in the project issues!*
"""
