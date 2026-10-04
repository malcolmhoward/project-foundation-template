# core/guides/onboarding.py
# Developer Onboarding Guide (v3.0.0)

"""
Developer Onboarding Guide.

Provides a comprehensive guide for new team members to get started
with the project, tools, and development workflow.

Introduced in v3.0.0.
"""

GUIDE_ID = "onboarding"

GUIDE = {
    "title": "Developer Onboarding Guide",
    "purpose": "Get new developers up and running quickly",
    "audience": "New team members",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["readme", "contributing"]

CONTENT = """
# Developer Onboarding Guide

## Welcome!

This guide will help you get set up and productive as quickly as possible.
Follow these steps in order for the smoothest onboarding experience.

## Day 1: Environment Setup

### 1. Access and Accounts

**Request access to:**
- [ ] GitHub organization
- [ ] Team communication (Slack/Discord/Teams)
- [ ] Project management tool (Jira/Linear/etc.)
- [ ] Cloud platform (AWS/GCP/Azure)
- [ ] Monitoring and logging systems
- [ ] Documentation wiki

**Set up:**
- [ ] Two-factor authentication on all accounts
- [ ] SSH keys for Git access
- [ ] Password manager

### 2. Development Machine Setup

**Install required software:**

```bash
# Version control
git --version  # Should be 2.x+

# Language runtime (project-specific)
python --version  # or
node --version    # or
go version

# Package managers
pip --version   # Python
npm --version   # Node.js

# Optional but recommended
docker --version
docker-compose --version
```

**Configure Git:**

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"

# Recommended settings
git config --global pull.rebase true
git config --global init.defaultBranch main
git config --global core.autocrlf input  # or 'true' on Windows
```

### 3. Clone and Set Up the Project

```bash
# Clone the repository
git clone git@github.com:org/project.git
cd project

# Install dependencies
pip install -r requirements.txt
# or
npm install

# Set up environment
cp .env.example .env
# Edit .env with your local settings

# Verify setup
npm test
# or
pytest
```

### 4. IDE Setup

**Recommended: VS Code**

Install extensions:
- Language-specific (Python, ESLint, etc.)
- GitLens
- EditorConfig
- Prettier (if applicable)

**Configure settings:**
```json
{
  "editor.formatOnSave": true,
  "editor.tabSize": 2,
  "files.trimTrailingWhitespace": true
}
```

## Day 2: Understanding the Codebase

### Project Structure

```
project/
├── src/                 # Application source code
│   ├── api/             # API endpoints
│   ├── models/          # Data models
│   ├── services/        # Business logic
│   └── utils/           # Helper functions
├── tests/               # Test files
├── docs/                # Documentation
├── scripts/             # Utility scripts
├── .github/             # GitHub workflows
└── config/              # Configuration files
```

### Key Files to Read

1. **README.md** - Project overview and quick start
2. **CONTRIBUTING.md** - How to contribute
3. **docs/architecture.md** - System design
4. **src/main.py** - Application entry point

### Running the Application

```bash
# Development mode
npm run dev
# or
python main.py --debug

# Access at
http://localhost:3000
```

### Running Tests

```bash
# All tests
npm test
pytest

# Specific tests
pytest tests/test_users.py
npm test -- --grep "user"

# With coverage
pytest --cov=src
npm run test:coverage
```

## Week 1: Development Workflow

### Understanding the Branching Strategy

```
main          ─────●─────●─────●─────
               \\      /    \\    /
feature/xyz     ●────●      ●──●
                          /
feature/abc              ●
```

**Branch naming:**
- `feature/description` - New features
- `fix/description` - Bug fixes
- `docs/description` - Documentation
- `refactor/description` - Code improvements

### Making Your First Contribution

1. **Pick a starter issue**
   - Look for issues labeled "good first issue"
   - Ask your mentor if unsure

2. **Create a branch**
   ```bash
   git checkout main
   git pull origin main
   git checkout -b feature/your-feature
   ```

3. **Make changes**
   - Write code
   - Add tests
   - Update documentation

4. **Commit your work**
   ```bash
   git add .
   git commit -m "feat(scope): brief description"
   ```

5. **Push and create PR**
   ```bash
   git push -u origin feature/your-feature
   # Open PR on GitHub
   ```

6. **Address review feedback**
   - Make requested changes
   - Push updates
   - Respond to comments

### Commit Message Format

```
type(scope): subject

body (optional)

footer (optional)
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Examples:**
```
feat(auth): add password reset functionality

Implements password reset flow with email verification.
Users receive a time-limited token to reset their password.

Closes #123
```

## Understanding Key Concepts

### Architecture Overview

[Include your project's specific architecture diagram or description]

**Key components:**
1. **API Layer** - Handles HTTP requests
2. **Service Layer** - Business logic
3. **Data Layer** - Database access
4. **External Services** - Third-party integrations

### Data Flow

```
Request → Router → Controller → Service → Repository → Database
                                            ↓
Response ← Controller ← Service ← Repository ← Database
```

### Important Patterns Used

- **Dependency Injection** - Components receive dependencies
- **Repository Pattern** - Abstract data access
- **Service Layer** - Encapsulate business logic

## Team Practices

### Communication

- **Daily standups** - [Time and location]
- **Team chat** - Use #team-channel for questions
- **Documentation** - Update docs as you learn

### Code Review

**As an author:**
- Keep PRs small (< 400 lines)
- Write clear descriptions
- Respond to feedback promptly

**As a reviewer:**
- Be constructive and kind
- Focus on significant issues
- Approve when satisfied

### Getting Help

1. **Check documentation** first
2. **Search existing issues** on GitHub
3. **Ask in team chat** with context
4. **Schedule a call** for complex topics

## Key Resources

### Documentation

- [Project Documentation](docs/)
- [API Reference](docs/api.md)
- [Architecture Guide](docs/architecture.md)

### Guides in This Project

- **Coding Standards** - Code style and conventions
- **Test Strategies** - Testing best practices
- **Troubleshooting** - Common issues and solutions
- **FAQ** - Frequently asked questions
- **Glossary** - Term definitions

### External Resources

- [Language Documentation]
- [Framework Documentation]
- [Company Engineering Blog]

## Onboarding Checklist

### Week 1

- [ ] Complete environment setup
- [ ] Successfully run the application locally
- [ ] Successfully run all tests
- [ ] Read key documentation
- [ ] Understand project structure
- [ ] Complete first starter issue
- [ ] Get first PR merged

### Week 2

- [ ] Understand deployment process
- [ ] Review architecture documentation
- [ ] Complete second contribution
- [ ] Shadow a code review
- [ ] Meet with key team members

### Month 1

- [ ] Comfortable with the codebase
- [ ] Completed several contributions
- [ ] Participated in code reviews
- [ ] Understand monitoring and logging
- [ ] Can debug production issues
- [ ] Contributed to documentation

## Feedback

We want to improve onboarding! Please:
- Note anything confusing
- Suggest documentation improvements
- Share what helped you learn
- Update this guide with what you wish you knew

---

*Welcome to the team! Don't hesitate to ask questions - we're here to help.*
"""
