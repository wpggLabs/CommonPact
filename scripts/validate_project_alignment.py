#!/usr/bin/env python3
"""Check public claims, repository identity privacy, and website metadata."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md", "FOUNDER_VISION.md", "STATUS.md", "PROTOCOL.md", "PROFILE_STANDARD.md",
    "USE_CASES_AND_USER_JOURNEYS.md", "CORE_PROFILE_MAPPING.md", "ADOPTION_AND_NETWORK_BOOTSTRAP.md",
    "ACCESSIBILITY.md", "ABUSE_AND_MODERATION.md", "KEY_MANAGEMENT_AND_RECOVERY.md",
    "DATA_PORTABILITY.md", "LEGAL_REVIEW_CHECKLIST.md", "TRANSPORT_PROFILE_STANDARD.md",
    "profiles/pactrental/README.md", "profiles/pactrental/profile-manifest.json",
    "profiles/pactrental/schemas/pactrental-profile.schema.json",
    "profiles/pactrental/test-vectors/pactrental-v0.1.json",
    "docs/index.html", "docs/styles.css", "docs/assets/commonpact-social.png",
    "docs/assets/commonpact-mark.svg", "docs/favicon.svg", "docs/sitemap.xml", "docs/robots.txt",
    "CITATION.cff", "codemeta.json",
]
TEXT_SUFFIXES = {
    ".cff", ".css", ".html", ".js", ".json", ".md", ".py", ".svg",
    ".toml", ".txt", ".xml", ".yaml", ".yml",
}
PRIVATE_NAME_TOKENS = (
    ("mi" + "raz").casefold(),
    ("meh" + "bub").casefold(),
)

failures = []
for name in REQUIRED:
    if not (ROOT / name).exists():
        failures.append(f"missing {name}")

texts = {
    name: (ROOT / name).read_text(encoding="utf-8")
    for name in ["README.md", "FOUNDER_VISION.md", "STATUS.md", "docs/index.html"]
    if (ROOT / name).exists()
}
for name, text in texts.items():
    for phrase in ["founder", "pre-implementation", "CommonPact"]:
        if phrase.lower() not in text.lower():
            failures.append(f"{name} missing required claim phrase: {phrase}")

site = texts.get("docs/index.html", "")
for marker in [
    'rel="canonical"', 'property="og:image"', 'name="twitter:card"',
    'href="favicon.svg"', 'id="journeys"', 'id="architecture"', 'id="status"',
    "The system is not built", "No mandatory platform owner",
]:
    if marker not in site:
        failures.append(f"website missing {marker}")

status = texts.get("STATUS.md", "")
for phrase in [
    "Complete founder-authored CommonPact Research RFC package",
    "No two independent CommonPact implementations",
    "PactFund",
]:
    if phrase not in status:
        failures.append(f"STATUS.md missing {phrase}")

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
        continue
    if path.suffix.casefold() not in TEXT_SUFFIXES and path.name != "CITATION.cff":
        continue
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue
    folded = content.casefold()
    for token in PRIVATE_NAME_TOKENS:
        if token in folded:
            failures.append(
                f"{path.relative_to(ROOT)} contains a private personal-name token"
            )

citation_path = ROOT / "CITATION.cff"
if citation_path.exists():
    citation = citation_path.read_text(encoding="utf-8")
    if 'name: "wpggLabs"' not in citation:
        failures.append("CITATION.cff must identify wpggLabs as the author")
    if "family-names:" in citation or "given-names:" in citation:
        failures.append("CITATION.cff must not contain personal-name author fields")

codemeta_path = ROOT / "codemeta.json"
if codemeta_path.exists():
    try:
        codemeta = json.loads(codemeta_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        failures.append(f"codemeta.json is invalid JSON: {exc}")
    else:
        author = codemeta.get("author", {})
        if author.get("@type") != "Organization" or author.get("name") != "wpggLabs":
            failures.append("codemeta.json must identify wpggLabs as an organization")

if failures:
    print("Alignment validation failed:")
    for failure in failures:
        print("-", failure)
    sys.exit(1)
print("Repository, public identity privacy, completion claims, required artifacts, and website metadata are aligned.")
