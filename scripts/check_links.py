#!/usr/bin/env python3
"""
Automated Link Checker for EDGE | AGENCY Skills
Extracts all markdown links from README.md and category files,
verifies them concurrently, and reports broken links.
"""

import os
import re
import sys
from pathlib import Path
import concurrent.futures
import requests

# GitHub API requests are rate-limited without a token, so we use HEAD requests with a User-Agent
HEADERS = {
    "User-Agent": "EdgeAgency-LinkChecker/1.0 (Autonomous Agent)"
}

def extract_links_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    # Match markdown links: [text](url)
    links = re.findall(r'\[([^\]]+)\]\((https?://[^\)]+)\)', content)
    return [url for text, url in links]

def verify_link(url):
    # Skip anchors or mailto
    if '#' in url and not url.startswith('http'):
        return True, url, 200
    try:
        # Use GET with stream=True or HEAD
        response = requests.head(url, headers=HEADERS, timeout=10, allow_redirects=True)
        if response.status_code >= 400:
            # Fallback to GET for servers blocking HEAD
            response = requests.get(url, headers=HEADERS, timeout=10, stream=True)
        return response.status_code < 400, url, response.status_code
    except Exception as e:
        return False, url, str(e)

def main():
    root_dir = Path(__file__).resolve().parents[1]
    all_links = set()
    
    # Check README.md
    readme_path = root_dir / 'README.md'
    if readme_path.exists():
        all_links.update(extract_links_from_file(readme_path))

    # Check categories/
    cat_dir = root_dir / 'categories'
    if cat_dir.exists():
        for path in cat_dir.glob('*.md'):
            all_links.update(extract_links_from_file(path))
                
    print(f"Extracted {len(all_links)} unique URLs to verify.")
    
    broken_links = []
    # Verify concurrently with max 20 workers
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(verify_link, url): url for url in all_links}
        for future in concurrent.futures.as_completed(future_to_url):
            success, url, status = future.result()
            if not success:
                print(f"[BROKEN] {url} -> Status/Error: {status}")
                broken_links.append((url, status))
            else:
                print(f"[OK] {url}")
                
    if broken_links:
        print(f"\nFound {len(broken_links)} broken links!")
        sys.exit(1)
    else:
        print("\nAll links verified successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
