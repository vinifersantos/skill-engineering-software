#!/usr/bin/env python3
"""Build a deterministic ZIP containing the installable master skill folder."""
from __future__ import annotations

import argparse
import re
import stat
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senior-software-engineer"
VERSION_RE = re.compile(r"^Version:\s*(\d+\.\d+\.\d+)\s*$", re.MULTILINE)
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)


def get_version(skill_dir: Path = SKILL_DIR) -> str:
    content = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = VERSION_RE.search(content)
    if not match:
        raise ValueError("Could not find 'Version: X.Y.Z' in SKILL.md")
    return match.group(1)


def build_package(skill_dir: Path, output_file: Path) -> Path:
    if not (skill_dir / "SKILL.md").is_file():
        raise FileNotFoundError(f"SKILL.md not found in {skill_dir}")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    prefix = "senior-software-engineer"
    with zipfile.ZipFile(output_file, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file():
                continue
            if "__pycache__" in path.parts or path.suffix == ".pyc" or path.name == ".DS_Store":
                continue
            relative = path.relative_to(skill_dir).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{relative}", date_time=FIXED_TIMESTAMP)
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
    output = args.output_dir / f"senior-software-engineer-v{version}.zip"
    build_package(SKILL_DIR, output)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
