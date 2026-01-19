# core/guides/faq.py
# Frequently Asked Questions Guide (v3.0.0)

"""
Frequently Asked Questions Guide.

Provides answers to common questions about project setup,
development workflows, and best practices.

Introduced in v3.0.0.
"""

GUIDE_ID = "faq"

GUIDE = {
    "title": "Frequently Asked Questions",
    "purpose": "Find quick answers to common questions",
    "audience": "All contributors",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["contributing", "readme"]

CONTENT = """
# Frequently Asked Questions

## Getting Started

### How do I set up the development environment?

1. **Clone the repository:**
   ```bash
   git clone https://github.com/org/project.git
   cd project
   ```

2. **Install dependencies:**
   ```bash
   # Python
   python -m venv venv
   source venv/bin/activate  # or venv\\Scripts\\activate on Windows
   pip install -r requirements.txt

   # Node.js
   npm install
   ```

3. **Set up configuration:**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

4. **Run the application:**
   ```bash
   # Development mode
   npm run dev
   # or
   python main.py
   ```

### Where is the documentation?

- **README.md** - Project overview and quick start
- **docs/** - Detailed documentation
- **CONTRIBUTING.md** - How to contribute
- **CHANGELOG.md** - Version history

### How do I run tests?

```bash
# Run all tests
npm test
# or
pytest

# Run specific test file
pytest tests/test_users.py

# Run with coverage
pytest --cov=src

# Run in watch mode
npm test -- --watch
```

## Contributing

### How do I create a new branch?

Follow the branching naming convention:

```bash
# Feature branch
git checkout -b feature/add-user-search

# Bug fix branch
git checkout -b fix/login-validation

# Documentation
git checkout -b docs/update-readme
```

### How do I submit a pull request?

1. Create a feature branch from `main`
2. Make your changes with clear commits
3. Push your branch to origin
4. Open a pull request on GitHub
5. Fill in the PR template
6. Request review from maintainers

### What should my commit messages look like?

Follow conventional commits:

```
type(scope): brief description

Longer description if needed.

Fixes #123
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Examples:**
```
feat(auth): add OAuth2 login support
fix(api): handle null response from payment service
docs(readme): update installation instructions
```

### How long until my PR is reviewed?

- **Small PRs (< 100 lines):** 1-2 business days
- **Medium PRs (100-500 lines):** 2-5 business days
- **Large PRs (> 500 lines):** Consider breaking into smaller PRs

Expedite by:
- Writing a clear PR description
- Keeping changes focused
- Including tests
- Responding to feedback promptly

## Development

### How do I add a new dependency?

1. **Evaluate the dependency** (see Dependency Guide)
2. **Add it properly:**
   ```bash
   # Production dependency
   npm install package-name
   pip install package-name

   # Development dependency
   npm install --save-dev package-name
   pip install package-name  # Add to requirements-dev.txt
   ```
3. **Commit the lock file changes**

### How do I configure environment variables?

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit your local .env** (never commit this file)

3. **Access in code:**
   ```python
   import os
   database_url = os.getenv("DATABASE_URL")
   ```

**Common variables:**
| Variable | Purpose | Example |
|----------|---------|---------|
| DATABASE_URL | Database connection | postgres://localhost/db |
| API_KEY | External service key | sk_test_xxx |
| DEBUG | Enable debug mode | true/false |
| LOG_LEVEL | Logging verbosity | debug/info/warn |

### How do I debug a failing test?

1. **Run the specific test with verbose output:**
   ```bash
   pytest tests/test_file.py::test_name -v
   ```

2. **Add print statements or use debugger:**
   ```python
   def test_something():
       import pdb; pdb.set_trace()
       # or
       breakpoint()
   ```

3. **Check test isolation:**
   ```bash
   # Run just that test
   pytest tests/test_file.py::test_name

   # Run entire file
   pytest tests/test_file.py
   ```

### How do I update documentation?

1. **For README/CONTRIBUTING:** Edit the markdown file directly
2. **For API docs:** Update docstrings, then regenerate
3. **For guides:** Edit files in `docs/` directory

Always preview changes locally before committing.

## Deployment

### How do I deploy to staging?

Merging to `main` triggers automatic deployment to staging:

1. Get PR approved and merged to `main`
2. CI/CD pipeline runs automatically
3. Check staging environment for your changes
4. Verify functionality before production deployment

### How do I deploy to production?

Production deployments follow a controlled process:

1. **Create a release branch** (if required)
2. **Run release checklist**
3. **Create a GitHub release** with version tag
4. **Monitor deployment** for issues

See the Release Process Guide for detailed steps.

### How do I roll back a deployment?

**Automatic rollback:**
If health checks fail, deployments roll back automatically.

**Manual rollback:**
```bash
# Identify the last good version
git log --oneline

# Deploy specific version
git checkout v1.2.3
# or use deployment tool
./deploy.sh v1.2.3
```

## Troubleshooting

### The build is failing. What do I do?

1. **Read the error message** carefully
2. **Check common causes:**
   - Missing dependencies
   - Syntax errors
   - Environment variable issues
3. **Try locally:**
   ```bash
   npm run build
   ```
4. **Check CI logs** for detailed output

### My changes aren't showing up. Why?

1. **Did you save the file?**
2. **Did you restart the dev server?** (if needed)
3. **Clear caches:**
   ```bash
   npm run clean
   # or clear browser cache
   ```
4. **Check correct branch:**
   ```bash
   git branch --show-current
   ```

### I'm getting merge conflicts. How do I resolve them?

1. **Pull latest changes:**
   ```bash
   git fetch origin
   git merge origin/main
   ```

2. **Open conflicted files** and look for conflict markers:
   ```
   <<<<<<< HEAD
   your changes
   =======
   their changes
   >>>>>>> origin/main
   ```

3. **Edit to resolve** (keep what's correct)

4. **Mark resolved and commit:**
   ```bash
   git add resolved-file.py
   git commit -m "Resolve merge conflicts"
   ```

### How do I undo my last commit?

**Keep changes, undo commit:**
```bash
git reset --soft HEAD~1
```

**Discard changes entirely:**
```bash
git reset --hard HEAD~1
```

**Already pushed? Create a revert:**
```bash
git revert HEAD
git push
```

## Project-Specific

### Where do I add new features?

```
src/
├── components/    # UI components
├── services/      # Business logic
├── models/        # Data models
├── utils/         # Helper functions
└── api/           # API endpoints
```

### How do I add a new API endpoint?

1. Create route handler in `src/api/`
2. Add input validation
3. Implement business logic in service layer
4. Write tests
5. Update API documentation

### What code style do we follow?

- **Formatting:** Handled by Prettier/Black (run automatically)
- **Linting:** ESLint/Pylint rules in config files
- **Naming:** See Coding Standards Guide
- **Testing:** See Test Strategies Guide

### Who do I ask for help?

1. **Search existing issues** on GitHub
2. **Check documentation** and this FAQ
3. **Ask in team chat** (Slack/Discord)
4. **Create an issue** if it's a bug or feature request
5. **Reach out to maintainers** for urgent matters

---

*Can't find your question? Open an issue or ask in team chat!*
"""
