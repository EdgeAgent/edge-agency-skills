import os
import re

readme_path = '/home/ubuntu/agency-skills/README.md'
categories_dir = '/home/ubuntu/agency-skills/categories'

with open(readme_path, 'r') as f:
    readme_content = f.read()

# Map category headers to filenames
category_map = {
    "Git & GitHub": "git-and-github.md",
    "Coding Agents & IDEs": "coding-agents-and-ides.md",
    "Browser & Automation": "browser-and-automation.md",
    "Web & Frontend Development": "web-and-frontend-development.md",
    "DevOps & Cloud": "devops-and-cloud.md",
    "Image & Video Generation": "image-and-video-generation.md",
    "Apple Apps & Services": "apple-apps-and-services.md",
    "Search & Research": "search-and-research.md",
    "Clawdbot Tools": "clawdbot-tools.md",
    "CLI Utilities": "cli-utilities.md",
    "Marketing & Sales": "marketing-and-sales.md",
    "Productivity & Tasks": "productivity-and-tasks.md",
    "AI & LLMs": "ai-and-llms.md",
    "Data & Analytics": "data-and-analytics.md",
    "Finance": "finance.md",
    "Media & Streaming": "media-and-streaming.md",
    "Notes & PKM": "notes-and-pkm.md",
    "iOS & macOS Development": "ios-and-macos-development.md",
    "Transportation": "transportation.md",
    "Personal Development": "personal-development.md",
    "Health & Fitness": "health-and-fitness.md",
    "Communication": "communication.md",
    "Speech & Transcription": "speech-and-transcription.md",
    "Smart Home & IoT": "smart-home-and-iot.md",
    "Shopping & E-commerce": "shopping-and-e-commerce.md",
    "Calendar & Scheduling": "calendar-and-scheduling.md",
    "PDF & Documents": "pdf-and-documents.md",
    "Self-Hosted & Automation": "self-hosted-and-automation.md",
    "Security & Passwords": "security-and-passwords.md",
    "Moltbook": "moltbook.md",
    "Gaming": "gaming.md",
    "Agent-to-Agent Protocols": "agent-to-agent-protocols.md"
}

def get_full_list(filename):
    path = os.path.join(categories_dir, filename)
    if not os.path.exists(path):
        return None
    with open(path, 'r') as f:
        lines = f.readlines()
    # Extract only the skill lines (starting with - [)
    skills = [line for line in lines if line.startswith('- [')]
    return "".join(skills)

# Rebuild sections
for section_name, filename in category_map.items():
    full_list = get_full_list(filename)
    if full_list:
        # Find the section in the README
        # Pattern: <details.*?>\s*<summary><h3.*?>SECTION_NAME</h3></summary>.*?<br/>\s*</details>
        # We need to replace the content between the summary and the </details>
        pattern = re.compile(rf'(<details.*?>\s*<summary><h3.*?>{re.escape(section_name)}</h3></summary>).*?(> \*\*\[View all.*?\n)?(\s*</details>)', re.DOTALL)
        
        replacement = r'\1\n\n' + full_list + r'\n\3'
        readme_content = pattern.sub(replacement, readme_content)

with open(readme_path, 'w') as f:
    f.write(readme_content)

print("README rebuilt with full skill lists.")
