# Version Control Setup Guide

## Overview

This guide provides step-by-step instructions for setting up and implementing the version control system for the Green AI Solutions project. It covers the installation of necessary tools, configuration of version tracking, and adoption of version control practices.

## Prerequisites

- Git installed on your system
- Python 3.6 or higher
- Access to the Green AI Solutions repositories

## Installation Steps

### 1. Clone the Repository

First, clone the project repository:

```bash
git clone https://github.com/green-ai-solutions/green-ai-solutions-docs.git
cd green-ai-solutions-docs
```

### 2. Install Version Control Tools

The project includes several tools to help maintain version control:

```bash
# Make the Python script executable
chmod +x Green_AI_Solutions/Documentation/Tools/version_update.py

# Make the shell script executable
chmod +x Green_AI_Solutions/Documentation/Tools/version_check.sh

# Install the pre-commit hook (optional but recommended)
cp Green_AI_Solutions/Documentation/Tools/pre-commit-hook .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 3. Set Up Git Configuration

Configure Git to work optimally with the version control system:

```bash
# Set your user information
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Configure Git to use the built-in mergetool
git config --global merge.tool vimdiff
git config --global diff.algorithm patience

# Set up some helpful aliases
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.lg "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --date=relative"
```

## Using the Version Control Tools

### Version Update Utility

The version update utility (`version_update.py`) helps maintain consistent version information in documents:

```bash
# Update a document's version
python3 Green_AI_Solutions/Documentation/Tools/version_update.py update path/to/document.md 1.1.0 "Added new section on compliance"

# Check a document's version information
python3 Green_AI_Solutions/Documentation/Tools/version_update.py check path/to/document.md

# Generate a report of all versioned documents
python3 Green_AI_Solutions/Documentation/Tools/version_update.py report ./Green_AI_Solutions
```

### Version Check Script

The version check script (`version_check.sh`) scans files for proper version information:

```bash
# Check all files in a directory
./Green_AI_Solutions/Documentation/Tools/version_check.sh ./Green_AI_Solutions

# Check specific files or directories
./Green_AI_Solutions/Documentation/Tools/version_check.sh ./Green_AI_Solutions/Documentation
```

### Pre-Commit Hook

The pre-commit hook automatically checks for version information before each commit. If you've installed it, it will run automatically when you commit changes.

To bypass the hook in exceptional cases:

```bash
git commit --no-verify -m "Your commit message"
```

Note: Bypassing the hook is discouraged as it may lead to inconsistent version tracking.

## Document Versioning Workflow

### Creating a New Document

1. Start with the document template:
   ```bash
   cp Green_AI_Solutions/Documentation/document_template.md path/to/new-document.md
   ```

2. Fill in the document contents and metadata section

3. Set the initial version to 1.0.0

4. Add the document to the document registry

5. Commit the new document:
   ```bash
   git add path/to/new-document.md Green_AI_Solutions/Documentation/document_registry.md
   git commit -m "docs: Add new document on [topic]"
   ```

### Updating an Existing Document

1. Make your changes to the document

2. Update the version information using the version update utility:
   ```bash
   python3 Green_AI_Solutions/Documentation/Tools/version_update.py update path/to/document.md 1.1.0 "Updated section on [topic]"
   ```

3. Update the document registry if necessary

4. Commit your changes:
   ```bash
   git add path/to/document.md Green_AI_Solutions/Documentation/document_registry.md
   git commit -m "docs: Update document on [topic] to version 1.1.0"
   ```

## Best Practices

### Version Numbers

Follow semantic versioning principles:

- **Major version (1.0.0 → 2.0.0)**: Significant restructuring or content changes
- **Minor version (1.0.0 → 1.1.0)**: Additions or notable changes to existing content
- **Patch version (1.1.0 → 1.1.1)**: Small corrections or clarifications

### Commit Messages

Follow the conventional commits format:

- `docs: Add new marketing strategy document`
- `docs: Update HR automation architecture to v1.2.0`
- `docs: Fix typos in compliance framework`

### Document Registry

Keep the document registry updated with all changes:

- Add new documents to the registry
- Update version information when documents change
- Update document status when appropriate

### Regular Maintenance

Schedule regular documentation maintenance:

- Run the version report monthly to identify outdated documents
- Review the document registry quarterly for accuracy
- Update document status based on project evolution

## Troubleshooting

### Common Issues

#### Pre-commit Hook Failing

If the pre-commit hook fails:

1. Check the error messages to identify missing information
2. Add the required version information, date, or changelog
3. Commit again

If you believe the failure is a false positive:
- Use `git commit --no-verify` to bypass the hook (use sparingly)

#### Version Update Tool Errors

If the version update tool fails to update a document:

1. Check if the document follows the expected format
2. Try manually adding the version information
3. Ensure you have write permissions for the file

#### Missing Document in Registry

If a document is missing from the registry:

1. Add the document to the appropriate section of the registry
2. Include all required metadata (version, date, status, owner)
3. Commit the updated registry

## Advanced Configuration

### Customizing the Pre-commit Hook

You can customize the pre-commit hook to suit your needs:

1. Edit `.git/hooks/pre-commit`
2. Modify the file patterns or checks
3. Adjust the strictness of the validation

### Integrating with CI/CD

For automated checking in CI/CD pipelines:

1. Add the version check script to your CI workflow
2. Configure it to run on pull requests
3. Set appropriate failure conditions

## Related Documents

- [Version Control Guidelines](version_control_guidelines.md)
- [Document Management Workflow](document_management_workflow.md)
- [File Naming Conventions](file_naming_conventions.md)
- [Document Registry](document_registry.md)
- [Git Repository Setup](git_repository_setup.md)

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-05-06 | Documentation Team | Initial guide creation |

---

**Document Metadata**
- **Title**: Version Control Setup Guide
- **Version**: 1.0.0
- **Last Updated**: 2025-05-06
- **Owner**: Documentation Team
- **Status**: Approved