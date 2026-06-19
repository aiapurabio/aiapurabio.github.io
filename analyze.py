import os
import re
import json

root_dir = '/Users/macbookretina/Downloads/aiapurabio-sitoweb/aiapurabio.github.io'

# 1. Find all files
assets = []
html_css_files = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    if '.git' in dirpath:
        continue
    for f in filenames:
        if f == '.DS_Store':
            continue
        full_path = os.path.join(dirpath, f)
        rel_path = os.path.relpath(full_path, root_dir)
        if f.endswith(('.html', '.css', '.js')):
            html_css_files.append((rel_path, full_path))
        if f.endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4', '.webm', '.mov', '.gif')):
            assets.append((rel_path, full_path, f))

# 2. Check for bad file names
bad_names = []
def is_bad(name):
    if ' ' in name: return True
    if any(c in name for c in ['(', ')', '[', ']', '{', '}', '\'', '"', '!', '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '?', '|', '\\', ':', ';', ',', '`', '~']): return True
    if any(ord(c) > 127 for c in name): return True # Accents
    if name != name.lower(): return True # Uppercase
    if name.count('.') > 1: return True # Double extension
    if len(name) > 60: return True # Too long
    return False

for rel_path, full_path, name in assets:
    if is_bad(name):
        bad_names.append((rel_path, name))

# 3. Extract all links from HTML/CSS
links = []
link_pattern = re.compile(r'(?:src|href|poster|url)\s*[=:]\s*[\'"]?([^\'"\s\>]+)[\'"]?', re.IGNORECASE)

for rel_path, full_path in html_css_files:
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
        found = link_pattern.findall(content)
        for link in found:
            if link.startswith('http') or link.startswith('#') or link.startswith('mailto:') or link.startswith('tel:'):
                continue
            if link.endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg', '.mp4', '.webm', '.mov', '.gif')):
                links.append((rel_path, link))

# Normalize links to absolute repository paths
normalized_links = []
for file_path, link in links:
    # Resolve relative link
    file_dir = os.path.dirname(file_path)
    if link.startswith('/'):
        norm_link = link[1:]
    else:
        norm_link = os.path.normpath(os.path.join(file_dir, link))
    normalized_links.append((file_path, link, norm_link))

# 4. Find broken links and unused assets
asset_rel_paths = {a[0] for a in assets}
referenced_assets = {nl[2] for nl in normalized_links}

broken_links = []
for file_path, original_link, norm_link in normalized_links:
    if norm_link not in asset_rel_paths:
        broken_links.append((file_path, original_link, norm_link))

unused_assets = []
for rel_path, full_path, name in assets:
    if rel_path not in referenced_assets:
        unused_assets.append(rel_path)

output = {
    'assets_count': len(assets),
    'bad_names': bad_names,
    'broken_links': broken_links,
    'unused_assets': unused_assets
}

print(json.dumps(output, indent=2))
