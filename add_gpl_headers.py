#!/usr/bin/env python3
"""Script to add GPL v3 headers to Python files."""

GPL_HEADER = '''# Notion Scriba - AI-powered bilingual documentation generator
# Copyright (C) 2025 Davide Baldoni
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''

import os
from pathlib import Path

def add_header_to_file(filepath):
    """Add GPL header to a Python file if not already present."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if GPL header already present
    if 'GNU General Public License' in content:
        print(f"⏭️  Skipping {filepath} (header already present)")
        return False
    
    # Add header after shebang if present, otherwise at top
    lines = content.split('\n')
    insert_pos = 0
    
    if lines and lines[0].startswith('#!'):
        insert_pos = 1
    
    new_lines = lines[:insert_pos] + [GPL_HEADER] + lines[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print(f"✅ Added GPL header to {filepath}")
    return True

def main():
    src_dir = Path('src/notion_scriba')
    py_files = list(src_dir.rglob('*.py'))
    
    updated = 0
    for py_file in py_files:
        if add_header_to_file(py_file):
            updated += 1
    
    print(f"\n🎉 Updated {updated}/{len(py_files)} files")

if __name__ == '__main__':
    main()
