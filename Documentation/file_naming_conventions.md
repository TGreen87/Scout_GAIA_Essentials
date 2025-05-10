# File Naming Conventions

This document establishes a standardized approach to naming files and directories within the Green AI Solutions project. Following these conventions ensures consistency, improves searchability, and supports efficient document management.

## General Principles

1. **Clarity**: Names should clearly indicate file content and purpose
2. **Consistency**: Follow established patterns across similar file types
3. **Brevity**: Keep names concise while still being descriptive
4. **Searchability**: Include relevant keywords for easy searching
5. **Versioning**: Include version information for documents that evolve over time

## Basic Structure

The standard file naming pattern is:

```
[project]_[category]_[descriptor]_[version].[extension]
```

### Components

1. **Project Identifier**: Indicates the specific project or product
   - `gas` - Green AI Solutions (main project)
   - `hrassist` - HR Assistant product
   - `aiconsult` - AI Consulting service
   - `neuropulse` - Neurodivergent platform

2. **Category**: Describes the general category or type of document
   - `doc` - General documentation
   - `spec` - Technical specifications
   - `arch` - Architecture documents
   - `proc` - Process documents
   - `plan` - Plans and roadmaps
   - `strat` - Strategic documents
   - `report` - Analysis or reporting documents
   - `ui` - User interface documents

3. **Descriptor**: Specific description of the document's content
   - Use lowercase letters and hyphens for spaces
   - Be specific but concise
   - Include key identifying terms

4. **Version**: Document version in semantic versioning format
   - Use `v` prefix followed by major.minor format
   - For example: `v1.0`, `v2.3`
   - Increment appropriately based on change magnitude

## Examples

- `gas_doc_project_overview_v1.0.md`
- `hrassist_spec_api_integration_v2.1.md`
- `gas_plan_nz_expansion_v1.0.md`
- `aiconsult_proc_implementation_methodology_v1.2.md`
- `gas_strat_monetization_model_v2.0.md`

## Directory Naming

Directories should follow a similar convention but without version numbers:

```
[Project]/[Category]/[Subcategory]
```

Example directory structure:
```
Green_AI_Solutions/
├── Documentation/
│   ├── Technical/
│   ├── Business/
│   └── User/
├── Business_Strategy/
│   ├── Market_Analysis/
│   └── Monetization/
├── HR_Automation/
│   ├── System_Architecture/
│   └── Compliance/
└── AI_Consulting/
    ├── Service_Offerings/
    └── Implementation_Framework/
```

## Document Types and Extensions

Use consistent file formats and extensions:

- **Markdown (.md)**: For all documentation that doesn't require complex formatting
- **HTML (.html)**: For web content and interactive documentation
- **PDF (.pdf)**: For finalized documents requiring preservation of formatting
- **JavaScript (.js)**: For code files
- **Python (.py)**: For code files
- **CSS (.css)**: For styling code
- **PNG (.png)**: For images with transparency
- **SVG (.svg)**: For vector graphics
- **JSON (.json)**: For data files
- **YAML (.yml)**: For configuration files

## Special Cases

### Code Files

Code files should follow language-specific conventions:
- JavaScript: Use camelCase for file names (e.g., `userAuthentication.js`)
- Python: Use snake_case for file names (e.g., `user_authentication.py`)
- Include purpose in the name (e.g., `user_authentication_service.py`)

### Visual Assets

Visual assets should follow the design system naming conventions:
- See the [Design System Naming Conventions](../Design_System/naming_conventions.md) for visual assets

### Configuration Files

Configuration files should be named descriptively:
- Use standard names where applicable (e.g., `.gitignore`, `package.json`)
- For project-specific configurations, prefix with the project identifier

## Version Control Guidelines

When a document undergoes revisions:

1. **Major Version Change (v1.0, v2.0)**:
   - Significant restructuring or content changes
   - Addition of entirely new sections or concepts
   - Major shifts in approach or strategy

2. **Minor Version Change (v1.1, v1.2)**:
   - Additions to existing content
   - Clarification of existing information
   - Refinement of concepts without changing the core approach

3. **Patch Version Change (v1.1.1, v1.1.2)**:
   - Typo corrections
   - Formatting adjustments
   - Minor clarifications without adding new content

## Implementation and Transition

For existing files:
- Documents with ongoing updates should be renamed to follow the convention
- Legacy documents can maintain their current names if they are final/archival

For new files:
- All new documents must follow these naming conventions
- Include file names in the document registry

## Document Metadata

In addition to filename conventions, include these metadata elements at the beginning or end of each document:

```
Title: [Document Title]
Version: [X.Y]
Last Updated: [YYYY-MM-DD]
Owner: [Name]
Status: [Draft/Review/Approved/Deprecated/Archived]
```

## Related Documents

- [Version Control Guidelines](version_control_guidelines.md)
- [Document Registry](document_registry.md)
- [Design System Naming Conventions](../Design_System/naming_conventions.md)

---

Last Updated: May 6, 2025
Version: 1.0
Owner: Tom Green
Status: Approved