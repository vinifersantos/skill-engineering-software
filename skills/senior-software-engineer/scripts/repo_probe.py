#!/usr/bin/env python3
"""Read-only repository inventory for the Harness Engineering skill.

Only checks the presence of known files/directories and counts Git status entries.
Never reads file bodies, credentials or contents of environment files, never
installs dependencies, and never changes the workspace.

Usage: python repo_probe.py --root /path/to/repository
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys

MANIFESTS = (
    "package.json", "pnpm-lock.yaml", "yarn.lock", "package-lock.json",
    "bun.lock", "bun.lockb", "pyproject.toml", "requirements.txt",
    "Pipfile", "poetry.lock", "uv.lock", "go.mod", "Cargo.toml",
    "pom.xml", "build.gradle", "build.gradle.kts", "gradlew", "mvnw",
    "Gemfile", "composer.json", "Dockerfile", "compose.yaml",
    "docker-compose.yml", "terraform.tf", "tsconfig.json",
)
DOCS = ("README.md", "README", "AGENTS.md", "CLAUDE.md", "PROJECT_MEMORY.md",
        "CONTRIBUTING.md", "ARCHITECTURE.md", "SECURITY.md")
QUALITY = ("pytest.ini", "tox.ini", "ruff.toml", ".ruff.toml", "mypy.ini",
           "eslint.config.js", "eslint.config.mjs", ".eslintrc", "jest.config.js",
           "vitest.config.ts", "playwright.config.ts", ".pre-commit-config.yaml")
DIRECTORIES = ("src", "app", "tests", "test", "spec", "docs", "migrations",
               "infra", "infrastructure", "terraform", ".github/workflows",
               ".gitlab", "prisma", "supabase")


def _git(root: Path, *args: str) -> str | None:
    if not shutil.which("git"):
        return None
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0")
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=False, text=True, stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL, timeout=5, env=env,
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


def inventory(root: Path) -> dict:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"Diretorio inexistente ou invalido: {root}")

    git_root = _git(root, "rev-parse", "--show-toplevel")
    is_repo = git_root is not None
    branch = _git(root, "symbolic-ref", "--quiet", "--short", "HEAD") if is_repo else None
    status = _git(root, "status", "--porcelain=v1", "--untracked-files=normal") if is_repo else None

    result = {
        "root": str(root),
        "read_only": True,
        "git": {
            "is_repository": is_repo,
            "branch": branch,
            "has_uncommitted_changes": bool(status) if status is not None else None,
            "changed_entry_count": len(status.splitlines()) if status is not None and status else (0 if status == "" else None),
        },
        "signals": {
            "manifests": [name for name in MANIFESTS if (root / name).is_file()],
            "documentation": [name for name in DOCS if (root / name).is_file()],
            "quality_config": [name for name in QUALITY if (root / name).is_file()],
            "directories": [name for name in DIRECTORIES if (root / name).is_dir()],
            "has_dotenv_at_root": any((root / name).is_file() for name in (".env", ".env.local", ".env.production")),
        },
        "notes": [
            "Sinais de arquivos nao comprovam que uma ferramenta ou um teste esteja funcional.",
            "Nenhum codigo, configuracao sensivel ou valor de ambiente foi lido.",
            "Revisar instrucoes do projeto, comportamento e scripts antes de executar comandos.",
        ],
    }
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Inventario read-only para agentes de programacao")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Diretorio raiz do projeto")
    args = parser.parse_args(argv)
    try:
        print(json.dumps(inventory(args.root), ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
