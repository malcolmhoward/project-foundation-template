# core/guides/contributor_handbook.py
# Contributor Handbook Guide (v3.2.0)

"""
Contributor Handbook Guide.

A comprehensive guide for open source contributors,
covering how to contribute effectively to the project.

Introduced in v3.2.0.
"""

GUIDE_ID = "contributor-handbook"

GUIDE = {
    "title": "Contributor Handbook",
    "purpose": "Guide open source contributors through the contribution process",
    "audience": "Open source contributors",
    "complexity": "beginner",
}

RELATED_PRINCIPLES = ["contributing", "code-of-conduct", "issue-templates", "pr-template"]

CONTENT = """
# Contributor Handbook

## Welcome Contributors!

Thank you for your interest in contributing! This handbook will guide you
through everything you need to know to make meaningful contributions.

## Ways to Contribute

### Code Contributions

- **Bug fixes** - Help squash bugs
- **New features** - Implement requested features
- **Performance** - Optimize existing code
- **Tests** - Improve test coverage
- **Refactoring** - Clean up technical debt

### Non-Code Contributions

- **Documentation** - Improve guides and API docs
- **Bug reports** - Report issues you find
- **Feature requests** - Suggest improvements
- **Code review** - Review pull requests
- **Community support** - Help others in discussions

## Getting Started

### 1. Find Something to Work On

**Good first issues:**
```
Labels to look for:
- "good first issue" - Beginner-friendly
- "help wanted" - Actively seeking help
- "documentation" - Docs improvements
- "bug" - Known bugs to fix
```

**Where to find issues:**
- GitHub Issues tab
- Project roadmap
- Discussion forums

### 2. Claim an Issue

Before starting work:
1. Check if anyone is already working on it
2. Comment that you'd like to work on it
3. Ask questions if requirements are unclear
4. Wait for maintainer acknowledgment (optional but recommended)

**Example comment:**
```
Hi! I'd like to work on this issue. I plan to:
1. Reproduce the bug locally
2. Add a failing test
3. Implement the fix
4. Update documentation if needed

Is this approach okay? Any tips?
```

### 3. Set Up Your Development Environment

```bash
# Fork the repository on GitHub

# Clone your fork
git clone https://github.com/YOUR-USERNAME/project.git
cd project

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL-OWNER/project.git

# Install dependencies
npm install  # or pip install -r requirements.txt

# Verify setup
npm test
```

### 4. Create a Branch

```bash
# Get latest changes
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

**Branch naming:**
- `feature/add-user-auth`
- `fix/login-validation`
- `docs/update-api-guide`

## Making Changes

### Code Style

Follow the project's coding standards:
- Check for `.editorconfig` or linting config
- Run linter before committing
- Match existing code style

```bash
# Run linter
npm run lint

# Auto-fix issues
npm run lint:fix
```

### Testing

**Write tests for your changes:**
```bash
# Run all tests
npm test

# Run specific test
npm test -- --grep "your test"

# Check coverage
npm run test:coverage
```

**Test requirements:**
- New features need tests
- Bug fixes need regression tests
- Maintain or improve coverage

### Documentation

Update docs when you:
- Add new features
- Change existing behavior
- Add new configuration options
- Modify API endpoints

### Commit Your Changes

**Commit message format:**
```
type(scope): brief description

Longer description if needed. Explain what and why,
not how (the code shows how).

Fixes #123
```

**Types:** feat, fix, docs, style, refactor, test, chore

**Examples:**
```bash
# Good
git commit -m "feat(auth): add password reset functionality"
git commit -m "fix(api): handle null user in response"
git commit -m "docs: update API authentication guide"

# Bad
git commit -m "fixed stuff"
git commit -m "WIP"
```

## Submitting Your Contribution

### Create a Pull Request

1. **Push your branch:**
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Open PR on GitHub:**
   - Go to your fork on GitHub
   - Click "Compare & pull request"
   - Fill out the PR template

### PR Description Template

```markdown
## Summary
Brief description of changes

## Changes Made
- Added X functionality
- Fixed Y bug
- Updated Z documentation

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Related Issues
Fixes #123

## Screenshots (if applicable)
[Add screenshots for UI changes]
```

### PR Best Practices

**Keep PRs small:**
- Easier to review
- Faster to merge
- Lower risk of conflicts
- Aim for < 400 lines changed

**One PR, one purpose:**
- Don't mix features
- Separate refactoring from features
- Split large changes into smaller PRs

**Make it reviewable:**
- Clear description
- Meaningful commit messages
- Comment complex code
- Respond to feedback promptly

## Code Review Process

### What Reviewers Look For

1. **Correctness** - Does it work?
2. **Design** - Is the approach sound?
3. **Tests** - Are changes tested?
4. **Style** - Does it match conventions?
5. **Documentation** - Is it documented?

### Responding to Feedback

**Be receptive:**
- Feedback improves code quality
- Ask for clarification if needed
- Don't take it personally

**Address all comments:**
```
# If you made the change
Done in abc1234

# If you disagree
I chose this approach because... What do you think?

# If clarification needed
Could you elaborate on what you mean by...?
```

### After Approval

Once approved:
1. Squash commits if requested
2. Maintainer will merge
3. Delete your branch
4. Celebrate!

## Communication

### Asking Questions

**Good question:**
```
I'm working on #123 and I'm unsure about X.
I've tried approaches A and B.
A doesn't work because...
B has this tradeoff...
Which would you recommend?
```

**Where to ask:**
- Issue comments - Specific issues
- Discussions - General questions
- Chat (if available) - Quick questions

### Providing Status Updates

If you're working on something for a while:
```
Update: I've completed X and Y.
Still working on Z.
Expected to have PR ready by [date].
```

### When You Can't Continue

It's okay! Just communicate:
```
Hi, I won't be able to continue with this issue due to [reason].
Feel free to assign to someone else.
[Optional: Here's what I've done so far...]
```

## Common Pitfalls

### Avoid These Mistakes

1. **Not reading CONTRIBUTING.md first**
2. **Working on claimed issues**
3. **Making large changes without discussion**
4. **Ignoring review feedback**
5. **Not testing locally**
6. **Poor commit messages**

### Solutions

1. **Read all contributor docs**
2. **Check issue assignments**
3. **Discuss in issue before starting**
4. **Address all feedback**
5. **Run full test suite**
6. **Follow commit conventions**

## Recognition

### How Contributors Are Recognized

- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- GitHub contributor badge
- Community appreciation posts

### Growing Your Role

Regular contributors may be invited to:
- Join maintainer team
- Review pull requests
- Participate in roadmap planning
- Mentor new contributors

## Resources

### Project Resources

- **README.md** - Project overview
- **CONTRIBUTING.md** - Contribution guidelines
- **CODE_OF_CONDUCT.md** - Community standards
- **docs/** - Full documentation

### Learning Resources

- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [First Timers Only](https://www.firsttimersonly.com/)
- [GitHub Skills](https://skills.github.com/)

## Getting Help

If you're stuck:
1. Re-read relevant documentation
2. Search existing issues
3. Ask in discussions
4. Reach out to maintainers

**Remember:** There are no stupid questions. We were all beginners once!

---

*Thank you for contributing! Every contribution, no matter how small, makes a difference.*
"""
