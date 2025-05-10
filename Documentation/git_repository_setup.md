# Git Repository Setup Guide

## Overview

This guide provides instructions for setting up and using Git version control for the Green AI Solutions project. It covers repository structure, branching strategy, and workflow practices to ensure consistent version control across the team.

## Repository Structure

The Green AI Solutions project is organized into multiple repositories:

1. **green-ai-solutions-docs**: Documentation and business materials
2. **green-ai-hr-automation**: HR automation system code
3. **green-ai-website**: Company website and digital presence
4. **green-ai-consulting-tools**: AI consulting tools and resources

### Repository Setup

To set up the repositories:

```bash
# Create documentation repository
mkdir green-ai-solutions-docs
cd green-ai-solutions-docs
git init
git remote add origin https://github.com/green-ai-solutions/green-ai-solutions-docs.git

# Create initial structure
mkdir -p Business_Strategy HR_Automation AI_Consulting Website_Marketing Documentation Design_System

# Add .gitignore
cat > .gitignore << 'EOL'
# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Temporary files
*.tmp
*.log
temp/

# Build artifacts
build/
dist/
node_modules/
__pycache__/
*.py[cod]
*$py.class
EOL

# Create README
cat > README.md << 'EOL'
# Green AI Solutions Documentation

This repository contains documentation and business materials for the Green AI Solutions project.

## Repository Structure

- `Business_Strategy/`: Business strategy documents
- `HR_Automation/`: HR automation system documentation
- `AI_Consulting/`: AI consulting services documentation
- `Website_Marketing/`: Website and marketing materials
- `Documentation/`: Project documentation and guides
- `Design_System/`: Design system and visual assets

## Getting Started

See the [Documentation Guide](Documentation/documentation_guide.md) for information on contributing to this repository.
EOL

# Initial commit
git add .
git commit -m "Initial repository structure"
```

Repeat similar steps for other repositories with appropriate directory structures.

## Branching Strategy

We use a modified GitFlow branching strategy:

### Main Branches

- **main**: Production-ready code and documentation
- **develop**: Integration branch for ongoing development

### Supporting Branches

- **feature/[feature-name]**: New features or significant additions
- **bugfix/[bug-description]**: Bug fixes
- **release/[version]**: Release preparation
- **hotfix/[issue-description]**: Emergency fixes for production

### Branch Naming Conventions

- Use lowercase letters and hyphens
- Include descriptive name after the prefix
- Examples:
  - `feature/australian-compliance-module`
  - `bugfix/login-validation-error`
  - `release/v1.0.0`
  - `hotfix/critical-security-patch`

## Workflow

### Starting New Work

When starting new work:

```bash
# Ensure you have the latest develop branch
git checkout develop
git pull origin develop

# Create a new feature branch
git checkout -b feature/your-feature-name

# Make your changes...
```

### Regular Commits

Commit frequently with descriptive messages:

```bash
git add .
git commit -m "feat: Implement Australian compliance check"
```

#### Commit Message Format

Follow Conventional Commits specification:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or modifying tests
- `chore`: Changes to build process or auxiliary tools

Example: `feat(compliance): Implement Fair Work Act requirements`

### Pushing Changes

Push your branch to the remote repository:

```bash
git push origin feature/your-feature-name
```

### Pull Requests

1. Create a pull request from your feature branch to the develop branch
2. Include a descriptive title and detailed description
3. Reference any related issues or requirements
4. Request reviews from appropriate team members
5. Address feedback and make necessary changes
6. Merge pull request once approved

### Releases

When preparing a release:

```bash
# Create a release branch from develop
git checkout develop
git pull origin develop
git checkout -b release/v1.0.0

# Make any final adjustments and version updates
git commit -m "chore: Prepare v1.0.0 release"

# Merge to main and tag
git checkout main
git merge release/v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"
git push origin main --tags

# Merge back to develop
git checkout develop
git merge release/v1.0.0
git push origin develop
```

## Configuration

### User Configuration

Configure your Git user information:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Git Hooks

Consider implementing Git hooks for quality checks:

- **pre-commit**: Lint code, check formatting, run tests
- **commit-msg**: Validate commit message format
- **pre-push**: Run comprehensive tests

## GitHub Repository Settings

Configure these settings in the GitHub repository:

1. **Branch Protection**:
   - Require pull request reviews before merging
   - Require status checks to pass
   - Require branches to be up to date
   - Include administrators in restrictions

2. **Merge Button Settings**:
   - Allow merge commits
   - Allow squash merging
   - Automatically delete head branches

3. **Issue Templates**:
   - Bug report template
   - Feature request template
   - Documentation update template

## Documentation Control

For markdown and documentation files:

1. Include version number and last updated date at the bottom of each file
2. Follow the [File Naming Conventions](file_naming_conventions.md)
3. Register documents in the [Document Registry](document_registry.md)
4. Include a change log section in substantial documents

## Handling Binary Files

For binary files (images, PDFs, etc.):

1. Consider if the binary file belongs in Git or should be stored elsewhere
2. Avoid frequent changes to large binary files
3. For design assets, follow the [Design System Naming Conventions](../Design_System/naming_conventions.md)

## Git Tools and Extensions

Recommended tools for better Git workflow:

- **GitHub Desktop**: User-friendly Git client
- **GitLens**: VS Code extension for Git integration
- **Sourcetree**: Visual Git client for complex operations
- **git-flow**: Command-line tools for GitFlow workflow

## Getting Help

If you encounter issues with Git:

1. Check the [Git documentation](https://git-scm.com/doc)
2. Consult the project lead or technical support
3. Review Git training resources in the Documentation/Training directory

## Related Documents

- [Version Control Guidelines](version_control_guidelines.md)
- [File Naming Conventions](file_naming_conventions.md)
- [Document Registry](document_registry.md)
- [Code Style Guide](code_style_guide.md)

---

**Document Metadata**
- **Title**: Git Repository Setup Guide
- **Version**: 1.0.0
- **Last Updated**: 2025-05-06
- **Owner**: Technical Lead
- **Status**: Approved