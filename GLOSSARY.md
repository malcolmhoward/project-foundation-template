# Glossary

This glossary defines terms used throughout Project Foundation Template (PFT) and related software development concepts.

---

## PFT-Specific Terms

### Governance
The policies, processes, and documentation that guide project development, maintenance, and contributions. This includes contribution guidelines, security policies, codes of conduct, and architectural decision records.

### Governance Theater
The appearance of having proper governance without the substance—adopting templates without understanding or customizing them. PFT is designed to prevent this through education-first principles.

### Guide (Implementation Guide)
Documentation in PFT explaining HOW to apply a principle. Guides provide practical, actionable instructions for implementing governance concepts.

### Preset
A predefined collection of governance principles bundled for common use cases. PFT includes presets: minimal, light, standard, strict, and enterprise.

### Principle (Governance Principle)
A governance concept in PFT that defines WHAT must be done, WHY it matters, and the RISK of not having it. Principles are the building blocks of governance.

### Principle Zero
PFT's foundational ethical principle: "Do No Harm, Allow No Harm." All decisions in PFT flow from this principle, inspired by GAIA from [Horizon Zero Dawn®](https://www.playstation.com/games/horizon-zero-dawn/).

> *Horizon Zero Dawn is a registered trademark of Sony Interactive Entertainment ([Trademark Notice](https://sonyinteractive.com/en/copyright-and-trademark-notice/)). This project is not affiliated with or endorsed by Sony Interactive Entertainment or Guerrilla Games.*

### Programming Language Configuration
Language-specific settings in PFT (v3.5.0+) that define tooling, linting, formatting, testing, and CI/CD configurations for a programming language.

---

## Testing Methodologies

### ATDD (Acceptance Test-Driven Development)
A development approach where acceptance tests are written before implementation. Tests are derived from user stories and acceptance criteria, ensuring the software meets business requirements.

### BDD (Behavior-Driven Development)
An extension of TDD that uses natural language constructs (Given-When-Then) to describe software behavior. BDD bridges communication between technical and non-technical stakeholders. See also: Gherkin.

### E2E (End-to-End) Testing
Testing that validates complete user workflows from start to finish, simulating real user interactions.

### Gherkin
A domain-specific language used in BDD frameworks like Cucumber. Uses keywords like Given, When, Then, And, But to structure test scenarios in plain English.

### Integration Testing
Testing that verifies different components or systems work together correctly.

### Load Testing
Performance testing that evaluates system behavior under expected and peak load conditions. Measures response times, throughput, and resource utilization.

### Stress Testing
Testing that evaluates system behavior beyond normal capacity to identify breaking points and recovery characteristics.

### TDD (Test-Driven Development)
A development approach where tests are written before the code they test, driving the design of the implementation.

### Unit Test
A test that verifies a single unit of code (function, method, class) works correctly in isolation.

---

## Version Control & Collaboration

### ADR (Architecture Decision Record)
A document that captures an important architectural decision along with its context and consequences. ADRs help preserve the "why" behind technical choices.

### Branch
A parallel version of the codebase in Git. Branches allow developers to work on features independently before merging changes.

### CI/CD (Continuous Integration / Continuous Deployment)
- **CI**: The practice of frequently merging code changes into a shared repository, with automated testing to catch issues early.
- **CD**: Automated preparation of code for release (Continuous Delivery) or automated release to production (Continuous Deployment).

### Commit
A snapshot of changes in Git. Each commit has a unique identifier (SHA) and records what changed, when, and by whom.

### Conventional Commits
A specification for adding human and machine-readable meaning to commit messages. Format: `type(scope): description`.

### Fork
A personal copy of another user's repository on GitHub. Forks allow you to experiment without affecting the original project.

### PR (Pull Request)
A request to merge code changes from one branch to another. PRs enable code review and discussion before changes are integrated.

### SemVer (Semantic Versioning)
A versioning scheme using MAJOR.MINOR.PATCH numbers to convey the nature of changes (breaking, feature, fix).

---

## Accessibility & Internationalization

### a11y (Accessibility)
Making software usable by people with disabilities. The term "a11y" is a numeronym where 11 represents the number of letters between 'a' and 'y'.

### i18n (Internationalization)
Designing software for multiple languages and regions. The term "i18n" is a numeronym where 18 represents the number of letters between 'i' and 'n'.

### l10n (Localization)
Adapting software for a specific region or language, including translating text and formatting dates, numbers, and currencies.

---

## Development Tools

### Formatter
A tool that automatically formats code according to style rules (e.g., Prettier, Black, gofmt).

### Linter
A tool that analyzes code for potential errors, bugs, and style violations (e.g., ESLint, Pylint, Clippy).

### Package Manager
A tool for installing, updating, and managing software dependencies (e.g., npm, pip, cargo).

### Pre-commit Hook
A script that runs automatically before each commit is finalized, acting as a first line of defense against common issues.

---

## Additional Terms

For a comprehensive glossary of general software development terms, see the full glossary guide in `core/guides/glossary.py`.

---

*Missing a term? Suggest additions in the [project issues](https://github.com/malcolmhoward/project-foundation-template/issues)!*
