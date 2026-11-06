#!/usr/bin/env python3
"""Install the master skill into a supported Agent Skills directory."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senior-software-engineer"


def destination_for(agent: str, scope: str, cwd: Path | None = None, home: Path | None = None) -> Path:
    cwd = (cwd or Path.cwd()).resolve()
    home = (home or Path.home()).expanduser().resolve()

    if scope == "workspace":
        folders = {
            "codex": ".agents/skills",
            "claude": ".claude/skills",
            "cursor": ".cursor/skills",
            "gemini": ".agents/skills",
            "junie": ".junie/skills",
        }
        return cwd / folders[agent]

    folders = {
        "codex": ".agents/skills",
        "claude": ".claude/skills",
        "cursor": ".cursor/skills",
        "gemini": ".agents/skills",
        "junie": ".junie/skills",
    }
    return home / folders[agent]


def install_skill(
    source: Path,
    destination_root: Path,
    replace: bool = False,
    now: datetime | None = None,
) -> tuple[Path, Path | None]:
    source = source.expanduser().resolve()
    destination_root = destination_root.expanduser().resolve()
    if not (source / "SKILL.md").is_file():
        raise FileNotFoundError(f"Master SKILL.md not found: {source / 'SKILL.md'}")
    if destination_root == source or source in destination_root.parents:
        raise ValueError("Destination cannot be inside the source skill directory")

    destination_root.mkdir(parents=True, exist_ok=True)
    target = destination_root / source.name
    backup: Path | None = None
    if target.exists():
        if not replace:
            raise FileExistsError(f"Skill already exists: {target}. Use --replace to update it safely.")
        stamp = (now or datetime.now(timezone.utc)).strftime("%Y%m%dT%H%M%SZ")
        backup = target.with_name(f"{target.name}.backup-{stamp}")
        if backup.exists():
            raise FileExistsError(f"Backup path already exists: {backup}")
        target.rename(backup)

    try:
        shutil.copytree(source, target, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"))
    except Exception:
        if backup is not None and backup.exists() and not target.exists():
            backup.rename(target)
        raise
    return target, backup


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=("codex", "claude", "cursor", "gemini", "junie"), required=True)
    parser.add_argument("--scope", choices=("user", "workspace"), default="user")
    parser.add_argument("--replace", action="store_true", help="Preserve the previous install in a timestamped backup")
    parser.add_argument("--destination-root", type=Path, help="Override the agent's default skills directory")
    args = parser.parse_args(argv)

    try:
        destination_root = args.destination_root or destination_for(args.agent, args.scope)
        target, backup = install_skill(SKILL_DIR, destination_root, replace=args.replace)
    except (OSError, ValueError) as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        return 2

    print(f"Installed {args.agent} skill: {target}")
    if backup:
        print(f"Previous version preserved at: {backup}")
    print("Verify discovery in the target agent before removing any older installation.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
