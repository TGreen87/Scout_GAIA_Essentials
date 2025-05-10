#!/bin/bash

# Version Check Script
# This script helps ensure all new files follow project version control standards.
# It can be used as a pre-commit hook or run manually.
#
# Usage:
#   ./version_check.sh [directory]
#
# If no directory is specified, it scans the current directory.

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Default to current directory if none specified
TARGET_DIR=${1:-.}

# File types to check
FILE_TYPES=("md" "html" "py" "js" "jsx" "ts" "tsx" "css" "scss")

# Files to ignore
IGNORE_PATTERNS=(
  "node_modules"
  ".git"
  "__pycache__"
  "venv"
  "dist"
  "build"
  "README.md"
  "LICENSE"
  "package.json"
  "package-lock.json"
)

# Patterns to check for
VERSION_PATTERN="[Vv]ersion:? +([0-9]+\.[0-9]+\.[0-9]+)"
DATE_PATTERN="[Ll]ast [Uu]pdated:? +([0-9]{4}-[0-9]{2}-[0-9]{2})"
CHANGELOG_PATTERN="[Cc]hange[Ll]og"

# Counters
total_files=0
compliant_files=0
missing_version=0
missing_date=0
missing_changelog=0

# Check if a file should be ignored
should_ignore() {
  local file=$1
  
  for pattern in "${IGNORE_PATTERNS[@]}"; do
    if [[ "$file" == *"$pattern"* ]]; then
      return 0
    fi
  done
  
  return 1
}

# Check a file for version information
check_file() {
  local file=$1
  local extension="${file##*.}"
  local issues=()
  
  # Skip if file should be ignored
  if should_ignore "$file"; then
    return
  fi
  
  # Skip if not in target file types
  if [[ ! " ${FILE_TYPES[@]} " =~ " ${extension} " ]]; then
    return
  fi
  
  total_files=$((total_files + 1))
  
  # Check for version
  if ! grep -qE "$VERSION_PATTERN" "$file"; then
    missing_version=$((missing_version + 1))
    issues+=("Missing version information")
  fi
  
  # Check for last updated date
  if ! grep -qE "$DATE_PATTERN" "$file"; then
    missing_date=$((missing_date + 1))
    issues+=("Missing last updated date")
  fi
  
  # Check for changelog (only for larger files)
  file_size=$(wc -l < "$file")
  if [[ $file_size -gt 30 ]]; then
    if ! grep -qE "$CHANGELOG_PATTERN" "$file"; then
      missing_changelog=$((missing_changelog + 1))
      issues+=("Missing changelog section")
    fi
  fi
  
  # Report issues for this file
  if [[ ${#issues[@]} -gt 0 ]]; then
    echo -e "${YELLOW}Issues in ${file}:${NC}"
    for issue in "${issues[@]}"; do
      echo -e "  - $issue"
    done
  else
    compliant_files=$((compliant_files + 1))
    echo -e "${GREEN}✓ ${file} is compliant${NC}"
  fi
}

echo "Running version control check in $TARGET_DIR"
echo "----------------------------------------"

# Find and check files
find "$TARGET_DIR" -type f | while read -r file; do
  check_file "$file"
done

# Calculate compliance percentage
if [[ $total_files -gt 0 ]]; then
  compliance_pct=$(( (compliant_files * 100) / total_files ))
else
  compliance_pct=0
fi

# Final summary
echo "----------------------------------------"
echo -e "${GREEN}Version Control Check Summary:${NC}"
echo "Total files checked: $total_files"
echo "Compliant files: $compliant_files ($compliance_pct%)"
echo -e "${YELLOW}Issues found:${NC}"
echo "  - Missing version: $missing_version files"
echo "  - Missing date: $missing_date files"
echo "  - Missing changelog: $missing_changelog files"

# Provide guidance on fixing issues
if [[ $compliance_pct -lt 100 ]]; then
  echo -e "\n${YELLOW}Recommendations:${NC}"
  echo "1. Add version information to files:"
  echo "   Version: 1.0.0"
  echo "2. Add last updated date:"
  echo "   Last Updated: $(date +%Y-%m-%d)"
  echo "3. Add changelog section to larger files:"
  echo "   ## Change Log"
  echo "   | Version | Date | Author | Changes |"
  echo "   |---------|------|--------|---------|"
  echo "   | 1.0.0 | $(date +%Y-%m-%d) | Your Name | Initial version |"
  echo -e "\nYou can use the version_update.py utility to add these elements automatically."
fi

# Exit with error code if compliance is low
if [[ $compliance_pct -lt 75 ]]; then
  echo -e "\n${RED}Low compliance detected. Please fix version information before committing.${NC}"
  exit 1
fi

exit 0