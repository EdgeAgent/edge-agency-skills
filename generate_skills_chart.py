import matplotlib.pyplot as plt
import numpy as np

# Data from README
categories = [
    'Coding Agents', 'Web & Frontend', 'DevOps & Cloud', 
    'Search & Research', 'Browser Automation', 'Productivity', 
    'AI & LLMs', 'CLI Utilities', 'Git & GitHub', 'Media Gen'
]
counts = [1222, 938, 409, 350, 335, 206, 197, 186, 170, 169]

plt.style.use('seaborn-v0_8-darkgrid' if 'seaborn-v0_8-darkgrid' in plt.style.available else 'default')
fig, ax = plt.subplots(figsize=(12, 7), dpi=300)

colors = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4', '#ef4444', '#6366f1', '#14b8a6', '#f97316']
bars = ax.barh(categories[::-1], counts[::-1], color=colors[::-1])

ax.set_xlabel('Number of Verified Skills', fontsize=12, fontweight='bold')
ax.set_title('EDGE | AGENCY Skills: Capability Distribution (5,490+ Skills)', fontsize=14, fontweight='bold', pad=20)

for bar in bars:
    width = bar.get_width()
    ax.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width}', 
            va='center', ha='left', fontsize=10, fontweight='bold')

plt.tight_layout()
import os
os.makedirs('/home/ubuntu/agency-skills/assets', exist_ok=True)
plt.savefig('/home/ubuntu/agency-skills/assets/skill_distribution.png')
plt.close()
print("Skill distribution chart generated.")
