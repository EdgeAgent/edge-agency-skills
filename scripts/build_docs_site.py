#!/usr/bin/env python3
"""Build the EDGE | AGENCY Skills static GitHub Pages site from category markdown."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = ROOT / "categories"
DOCS = ROOT / "docs"
DATA = DOCS / "data"
ASSETS = DOCS / "assets"

ENTRY_RE = re.compile(
    r"-\s*\[([^\]]+)\]\((https?://[^)]+)\)\s*-\s*(.*?)(?=\s+-\s*\[|\Z)",
    re.S,
)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read_skills() -> list[dict]:
    rows: list[dict] = []
    for path in sorted(CATEGORIES.glob("*.md")):
        raw = path.read_text(encoding="utf-8")
        title_match = re.search(r"^#\s+(.+)$", raw, re.M)
        category = title_match.group(1).strip() if title_match else path.stem.replace("-", " ").title()
        for index, match in enumerate(ENTRY_RE.finditer(raw), start=1):
            name, url, description = match.groups()
            rows.append({
                "name": clean(name),
                "url": url.strip(),
                "description": clean(description),
                "category": category,
                "categorySlug": path.stem,
                "index": index,
            })
    return rows


def main() -> None:
    skills = read_skills()
    categories: dict[str, int] = {}
    for skill in skills:
        categories[skill["category"]] = categories.get(skill["category"], 0) + 1
    payload = {
        "generatedAt": "2026-08-16",
        "total": len(skills),
        "categories": [{"name": name, "count": count} for name, count in sorted(categories.items())],
        "skills": skills,
    }
    DATA.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    (DATA / "skills.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")

    # Reuse the repository's existing branded assets for the Pages deployment.
    source_assets = ROOT / "assets"
    for filename in ("skills-banner.png", "skill_distribution.png"):
        source = source_assets / filename
        target = ASSETS / filename
        if source.exists():
            target.write_bytes(source.read_bytes())

    print(f"Built docs/data/skills.json with {len(skills)} skill entries across {len(categories)} categories.")


if __name__ == "__main__":
    main()
