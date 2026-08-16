import re

with open('/home/ubuntu/agency-skills/README.md', 'r') as f:
    lines = f.readlines()

current_section = None
counts = {}

for line in lines:
    match = re.search(r'<h3 style="display:inline">(.*?)</h3>', line)
    if match:
        current_section = match.group(1)
        counts[current_section] = 0
    elif current_section and line.startswith('- ['):
        counts[current_section] += 1

for section, count in counts.items():
    print(f"{section}: {count}")
