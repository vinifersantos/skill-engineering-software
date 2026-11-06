#!/usr/bin/env python3
"""Synchronize plugin and marketplace versions from the master SKILL.md."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILE = ROOT / "skills" / "senior-software-engineer" / "SKILL.md"
VERSION_RE = re.compile(r"^Version:\s*(\d+\.\d+\.\d+)\s*$", re.MULTILINE)
PLUGIN_FILES = (
    "plugin.json",
    ".antigravity-plugin/plugin.json",
    ".claude-plugin/plugin.json",
)
MARKETPLACE_FILES = (
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    ".github/plugin/marketplace.json",
)


def read_skill_version(root: Path = ROOT) -> str:
    content = (root / SKILL_FILE.relative_to(ROOT)).read_text(encoding="utf-8")
    match = VERSION_RE.search(content)
    if not match:
        raise ValueError("Master SKILL.md must declare Version: X.Y.Z")
    return match.group(1)


def sync_versions(root: Path = ROOT, check_only: bool = False) -> list[str]:
    version = read_skill_version(root)
    changes: list[str] = []

    for relative in PLUGIN_FILES:
        path = root / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("version") != version:
            changes.append(relative)
            data["version"] = version
            if not check_only:
                path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for relative in MARKETPLACE_FILES:
        path = root / relative
        data = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        metadata = data.get("metadata")
        if isinstance(metadata, dict) and metadata.get("version") != version:
            metadata["version"] = version
            changed = True

        for plugin in data.get("plugins", []):
            if plugin.get("name") != "senior-software-engineer":
                continue
            # Claude Code uses plugin.json as the authoritative version.
            # Duplicating version in the marketplace entry makes its validator fail.
            if relative == ".claude-plugin/marketplace.json":
                if "version" in plugin:
                    del plugin["version"]
                    changed = True
                continue
            if plugin.get("version") != version:
                plugin["version"] = version
                changed = True

        if changed:
            changes.append(relative)
            if not check_only:
                path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    return changes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report version drift without writing files")
    args = parser.parse_args()
    changes = sync_versions(check_only=args.check)
    if args.check and changes:
        print("Version drift detected:")
        print("\n".join(f"- {path}" for path in changes))
        return 1
    if changes:
        print("Synchronized version in:")
        print("\n".join(f"- {path}" for path in changes))
    else:
        print("All plugin and marketplace versions are synchronized.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
