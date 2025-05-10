#!/usr/bin/env python3
"""
Version Update Utility

This script helps maintain consistent version information across project documents.
It updates version numbers, last modified dates, and maintains changelogs.

Usage:
  version_update.py update <file_path> <version> <change_description>
  version_update.py check <file_path>
  version_update.py report [<directory>]

Options:
  update    Update a file's version information
  check     Check a file's version information
  report    Generate a report of version information for all files in a directory
"""

import os
import re
import sys
import argparse
from datetime import datetime
import csv
import json

# Configuration
VERSION_PATTERNS = [
    r'Version:\s+(\d+\.\d+\.\d+)',
    r'Version (\d+\.\d+\.\d+)',
    r'v(\d+\.\d+\.\d+)',
    r'"version":\s+"(\d+\.\d+\.\d+)"',
    r'version=["\'"](\d+\.\d+\.\d+)["\']'
]

DATE_PATTERNS = [
    r'Last Updated:\s+(\d{4}-\d{2}-\d{2})',
    r'Updated:\s+(\d{4}-\d{2}-\d{2})',
    r'Date:\s+(\d{4}-\d{2}-\d{2})'
]

CHANGELOG_PATTERNS = [
    r'## Change Log\s*\n\s*\|',
    r'## Changelog\s*\n\s*\|',
    r'# Change Log\s*\n\s*\|'
]

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Version Update Utility')
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Update command
    update_parser = subparsers.add_parser('update', help='Update version information')
    update_parser.add_argument('file_path', help='Path to the file to update')
    update_parser.add_argument('version', help='New version number (X.Y.Z)')
    update_parser.add_argument('change_description', help='Description of the changes made')
    
    # Check command
    check_parser = subparsers.add_parser('check', help='Check version information')
    check_parser.add_argument('file_path', help='Path to the file to check')
    
    # Report command
    report_parser = subparsers.add_parser('report', help='Generate version report')
    report_parser.add_argument('directory', nargs='?', default='.', help='Directory to scan')
    report_parser.add_argument('--format', choices=['csv', 'json', 'text'], default='text',
                              help='Output format (default: text)')
    
    return parser.parse_args()

def extract_version(content):
    """Extract version number from file content."""
    for pattern in VERSION_PATTERNS:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None

def extract_date(content):
    """Extract last updated date from file content."""
    for pattern in DATE_PATTERNS:
        match = re.search(pattern, content)
        if match:
            return match.group(1)
    return None

def find_changelog(content):
    """Find the changelog section in the content."""
    for pattern in CHANGELOG_PATTERNS:
        match = re.search(pattern, content)
        if match:
            return match.start()
    return -1

def update_version(file_path, new_version, change_description):
    """Update version information in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    updated = False
    today = datetime.now().strftime('%Y-%m-%d')
    author = os.environ.get('USER', 'Unknown')
    
    # Update version number
    for pattern in VERSION_PATTERNS:
        content, count = re.subn(pattern, f'Version: {new_version}', content)
        if count > 0:
            updated = True
    
    # Update last modified date
    for pattern in DATE_PATTERNS:
        content, count = re.subn(pattern, f'Last Updated: {today}', content)
        if count > 0:
            updated = True
    
    # Update changelog if found
    changelog_pos = find_changelog(content)
    if changelog_pos >= 0:
        # Find the table header and insert a new row after it
        lines = content.split('\n')
        changelog_line = None
        table_header_line = None
        
        for i, line in enumerate(lines):
            if '## Change Log' in line or '## Changelog' in line or '# Change Log' in line:
                changelog_line = i
            if changelog_line is not None and '|----' in line:
                table_header_line = i
                break
        
        if table_header_line is not None:
            new_row = f"| {new_version} | {today} | {author} | {change_description} |"
            lines.insert(table_header_line + 1, new_row)
            content = '\n'.join(lines)
            updated = True
    
    if updated:
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {file_path} to version {new_version}")
            return True
        except Exception as e:
            print(f"Error writing file: {e}")
            return False
    else:
        print(f"No version pattern found in {file_path}")
        return False

def check_version(file_path):
    """Check version information in a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    version = extract_version(content)
    date = extract_date(content)
    
    print(f"File: {file_path}")
    print(f"Version: {version or 'Not found'}")
    print(f"Last Updated: {date or 'Not found'}")
    
    if version is None:
        print("WARNING: No version information found")
    if date is None:
        print("WARNING: No date information found")
    
    # Check if filename contains version
    basename = os.path.basename(file_path)
    if version and version not in basename and 'v' + version not in basename:
        print(f"WARNING: Filename does not contain version number {version}")

def scan_directory(directory):
    """Scan directory for files with version information."""
    results = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Skip certain directories and file types
            skip_dirs = ['.git', 'node_modules', '__pycache__', 'venv']
            if any(skip_dir in file_path for skip_dir in skip_dirs):
                continue
                
            # Only process certain file types
            extensions = ['.md', '.py', '.js', '.html', '.css', '.json', '.yml', '.yaml', '.txt']
            if not any(file.endswith(ext) for ext in extensions):
                continue
            
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                version = extract_version(content)
                date = extract_date(content)
                
                if version or date:
                    results.append({
                        'file_path': file_path,
                        'version': version,
                        'date': date
                    })
            except Exception:
                # Skip files that can't be read as text
                continue
    
    return results

def generate_report(directory, format_type):
    """Generate a report of version information."""
    results = scan_directory(directory)
    
    if format_type == 'csv':
        output_file = 'version_report.csv'
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['file_path', 'version', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for result in results:
                writer.writerow(result)
        print(f"Report saved to {output_file}")
    
    elif format_type == 'json':
        output_file = 'version_report.json'
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(results, jsonfile, indent=2)
        print(f"Report saved to {output_file}")
    
    else:  # text format
        print(f"Found {len(results)} files with version information in {directory}")
        print("-" * 80)
        for result in results:
            print(f"File: {result['file_path']}")
            print(f"Version: {result['version'] or 'Not found'}")
            print(f"Last Updated: {result['date'] or 'Not found'}")
            print("-" * 80)

def main():
    """Main function."""
    args = parse_args()
    
    if args.command == 'update':
        update_version(args.file_path, args.version, args.change_description)
    
    elif args.command == 'check':
        check_version(args.file_path)
    
    elif args.command == 'report':
        generate_report(args.directory, args.format)
    
    else:
        print(__doc__)

if __name__ == "__main__":
    main()