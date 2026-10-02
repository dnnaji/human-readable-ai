"""Check public file types, private identifiers, and local links. MIT licensed."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {".md", ".html", ".svg", ".py"}
SPECIAL = {".gitignore", "LICENSE", "LICENSE-CODE"}
PATTERNS = {
    "absolute home path": r"/(?:home|Users)/[^\s/]+/",
    "private conversation identifier": r"\b(?:T-)?[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b",
    "private IPv4 address": r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2}|100\.(?:6[4-9]|[7-9]\d|1[01]\d|12[0-7])(?:\.\d{1,3}){2})\b",
}


def main():
    problems = []
    files = [
        p for p in ROOT.rglob("*")
        if p.is_file() and not {".git", "__pycache__"}.intersection(p.relative_to(ROOT).parts)
    ]
    for path in files:
        relative = path.relative_to(ROOT)
        if path.is_symlink():
            problems.append(f"{relative}: symlinks are not allowed")
            continue
        if path.suffix not in ALLOWED and str(relative) not in SPECIAL:
            problems.append(f"{relative}: unexpected file type")
            continue
        text = path.read_text(encoding="utf-8")
        for label, pattern in PATTERNS.items():
            if re.search(pattern, text, re.I):
                problems.append(f"{relative}: {label}")
        links = []
        if path.suffix == ".md":
            links = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)(?:\s+[^)]*)?\)", text)
        elif path.suffix == ".html":
            links = re.findall(r'(?:href|src)=[\"\']([^\"\']+)', text)
        elif path.suffix == ".svg":
            ET.fromstring(text)
        for link in links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (path.parent / unquote(parsed.path)).resolve()
            if not target.is_relative_to(ROOT) or not target.exists():
                problems.append(f"{relative}: missing or escaping local link: {link}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"Publication structure and local-link checks passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
