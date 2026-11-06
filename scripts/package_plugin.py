#!/usr/bin/env python3
"""Build a deterministic cross-host plugin ZIP with Agent, Antigravity and Claude manifests."""
from __future__ import annotations

import argparse
import json
import re
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senior-software-engineer"
PLUGIN_MANIFESTS = (
    ROOT / "plugin.json",
    ROOT / ".antigravity-plugin" / "plugin.json",
    ROOT / ".claude-plugin" / "plugin.json",
)
VERSION_RE = re.compile(r"^Version:\s*(\d+\.\d+\.\d+)\s*$", re.MULTILINE)
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def get_version() -> str:
    content = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    match = VERSION_RE.search(content)
    if not match:
        raise ValueError("Could not find Version: X.Y.Z in the master SKILL.md")
    version = match.group(1)
    for manifest_path in PLUGIN_MANIFESTS:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        if manifest.get("version") != version:
            raise ValueError(f"{manifest_path.relative_to(ROOT)} version does not match SKILL.md")
    return version


def build_package(output_file: Path) -> Path:
    if not (SKILL_DIR / "SKILL.md").is_file():
        raise FileNotFoundError("Master SKILL.md is missing")
    if any(not path.is_file() for path in PLUGIN_MANIFESTS):
        raise FileNotFoundError("A host plugin manifest is missing")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        files = [*PLUGIN_MANIFESTS, *[p for p in SKILL_DIR.rglob("*") if p.is_file()]]
        for path in sorted(files):
            if "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                continue
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"senior-software-engineer/{relative}", date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (stat.S_IFREG | (path.stat().st_mode & 0o777)) << 16
            archive.writestr(info, path.read_bytes())
    return output_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=ROOT / "dist")
    parser.add_argument("--version-only", action="store_true")
    args = parser.parse_args()
    version = get_version()
    if args.version_only:
        print(version)
        return 0
    output = args.output_dir / f"senior-software-engineer-plugin-v{version}.zip"
    build_package(output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
