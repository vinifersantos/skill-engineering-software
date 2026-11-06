#!/usr/bin/env python3
"""Validate the master skill, host manifests, marketplaces and local references."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "senior-software-engineer"
LINK_RE = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
REF_RE = re.compile(r"`(references/[A-Za-z0-9_.-]+\.md)`")
VERSION_RE = re.compile(r"^Version:\s*(\d+\.\d+\.\d+)\s*$", re.MULTILINE)
PLUGIN_NAME = "senior-software-engineer"
MARKETPLACE_NAME = "skill-engineering-software"


def parse_frontmatter(skill_file: Path) -> tuple[dict[str, str], str]:
    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("SKILL.md frontmatter closing delimiter was not found")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip('"').strip("'")
    return fields, text[end + 5 :]


def local_link_target(source: Path, raw_target: str) -> Path | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith("#"):
        return None
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc:
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    return (source.parent / path).resolve()


def validate_local_markdown_links(base: Path) -> list[str]:
    errors: list[str] = []
    for source in sorted(base.rglob("*.md")):
        text = source.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            raw_target = match.group(1).split()[0]
            target = local_link_target(source, raw_target)
            if target is not None and not target.exists():
                try:
                    rel_source = source.relative_to(ROOT)
                except ValueError:
                    rel_source = source
                errors.append(f"{rel_source}: broken local link -> {raw_target}")
    return errors


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: invalid or unreadable JSON: {exc}")
        return None
    if not isinstance(payload, dict):
        errors.append(f"{path.relative_to(ROOT)}: JSON root must be an object")
        return None
    return payload


def validate_skill(skill_dir: Path = SKILL_DIR) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"Missing master skill file: {skill_file}"]

    try:
        fields, body = parse_frontmatter(skill_file)
    except (OSError, ValueError) as exc:
        return [str(exc)]

    if fields.get("name") != PLUGIN_NAME:
        errors.append(f"Frontmatter name must be '{PLUGIN_NAME}'")
    description = fields.get("description", "")
    if not description or len(description) > 1024:
        errors.append("SKILL.md description must contain 1-1024 characters")
    version_match = VERSION_RE.search(body)
    if not version_match:
        errors.append("SKILL.md must declare a semantic Version: X.Y.Z")

    for match in REF_RE.finditer(body):
        rel = match.group(1)
        if not (skill_dir / rel).is_file():
            errors.append(f"SKILL.md references a missing file: {rel}")

    required_files = [
        "README.md",
        "CHANGELOG.md",
        "agents/openai.yaml",
        "assets/icon.svg",
        "scripts/repo_probe.py",
        "scripts/test_repo_probe.py",
        "references/code-first-impact-driven.md",
        "references/grill-me-mode.md",
        "references/agent-harness-orchestration.md",
        "references/database-engineering.md",
        "references/ci-cd-release-engineering.md",
        "references/debugging-rca-refactoring.md",
        "references/context-memory-tooling.md",
        "references/secret-management.md",
        "references/observability-telemetry.md",
        "references/disaster-recovery.md",
        "references/topic-coverage.md",
    ]
    for rel in required_files:
        if not (skill_dir / rel).is_file():
            errors.append(f"Missing required package file: {rel}")

    skill_files = list(skill_dir.rglob("SKILL.md"))
    if skill_files != [skill_file]:
        errors.append("The master package must contain exactly one SKILL.md entry point")

    agent_yaml = skill_dir / "agents" / "openai.yaml"
    if agent_yaml.is_file():
        yaml_text = agent_yaml.read_text(encoding="utf-8")
        for match in re.finditer(r"icon_(?:small|large):\s*(\S+)", yaml_text):
            if not (skill_dir / match.group(1)).is_file():
                errors.append(f"Agent metadata references a missing icon: {match.group(1)}")
        short_description = re.search(r"short_description:\s*(.+)", yaml_text)
        if not short_description or not 1 <= len(short_description.group(1).strip()) <= 100:
            errors.append("agents/openai.yaml short_description must contain 1-100 characters")

    errors.extend(validate_local_markdown_links(skill_dir))
    return errors


def validate_plugin_manifests() -> list[str]:
    errors: list[str] = []
    skill_version_match = VERSION_RE.search((SKILL_DIR / "SKILL.md").read_text(encoding="utf-8"))
    skill_version = skill_version_match.group(1) if skill_version_match else None

    manifest_paths = (
        ROOT / "plugin.json",
        ROOT / ".antigravity-plugin/plugin.json",
        ROOT / ".claude-plugin/plugin.json",
    )
    manifests: dict[str, dict] = {}
    for path in manifest_paths:
        manifest = load_json(path, errors)
        if not manifest:
            continue
        manifests[path.relative_to(ROOT).as_posix()] = manifest
        if manifest.get("name") != PLUGIN_NAME:
            errors.append(f"{path.relative_to(ROOT)}: plugin name mismatch")
        if skill_version and manifest.get("version") != skill_version:
            errors.append(f"{path.relative_to(ROOT)}: plugin version must match SKILL.md ({skill_version})")

    root_manifest = manifests.get("plugin.json")
    if root_manifest:
        if root_manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
            errors.append("plugin.json must declare the Agent Plugins 1.0 schema")
        interface = root_manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
        logo = interface.get("logo")
        if logo:
            logo_path = (ROOT / str(logo).removeprefix("./")).resolve()
            if not logo_path.is_file():
                errors.append(f"plugin.json references a missing OpenAI logo: {logo}")

    antigravity_manifest = manifests.get(".antigravity-plugin/plugin.json")
    if antigravity_manifest:
        if antigravity_manifest.get("$schema") != "https://antigravity.google/schemas/v1/plugin.json":
            errors.append("Antigravity manifest must declare the official plugin schema")
        logo = antigravity_manifest.get("logo")
        if logo and not (ROOT / logo).is_file():
            errors.append(f"Antigravity manifest references a missing logo: {logo}")

    claude_manifest = manifests.get(".claude-plugin/plugin.json")
    if claude_manifest:
        skills = claude_manifest.get("skills")
        if not isinstance(skills, list) or "./skills/senior-software-engineer" not in skills:
            errors.append("Claude plugin manifest must expose the master skill directory")

    marketplace_paths = (
        ROOT / ".agents/plugins/marketplace.json",
        ROOT / ".claude-plugin/marketplace.json",
        ROOT / ".github/plugin/marketplace.json",
    )
    for path in marketplace_paths:
        marketplace = load_json(path, errors)
        if not marketplace:
            continue
        if marketplace.get("name") != MARKETPLACE_NAME:
            errors.append(f"{path.relative_to(ROOT)}: marketplace name mismatch")
        metadata = marketplace.get("metadata")
        if skill_version and isinstance(metadata, dict) and metadata.get("version") != skill_version:
            errors.append(f"{path.relative_to(ROOT)}: marketplace metadata version must match SKILL.md")
        entries = marketplace.get("plugins")
        if not isinstance(entries, list) or len(entries) != 1:
            errors.append(f"{path.relative_to(ROOT)}: expected exactly one master plugin entry")
            continue
        entry = entries[0]
        if entry.get("name") != PLUGIN_NAME:
            errors.append(f"{path.relative_to(ROOT)}: marketplace plugin name mismatch")
        if path == ROOT / ".claude-plugin/marketplace.json":
            if "version" in entry:
                errors.append("Claude marketplace entry must omit version; plugin.json is authoritative")
        elif skill_version and entry.get("version") != skill_version:
            errors.append(f"{path.relative_to(ROOT)}: marketplace plugin version must match SKILL.md")

        source = entry.get("source")
        if isinstance(source, str):
            source_path = (ROOT / source).resolve()
            if not source_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: local plugin source does not exist: {source}")
        elif isinstance(source, dict) and source.get("source") == "local":
            source_path = (ROOT / str(source.get("path", ""))).resolve()
            if not source_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: local plugin source path does not exist")
        elif isinstance(source, dict) and source.get("source") == "url":
            if not str(source.get("url", "")).startswith(("https://", "ssh://", "git@")):
                errors.append(f"{path.relative_to(ROOT)}: remote plugin source requires a Git URL")
        elif isinstance(source, dict) and source.get("source") == "github":
            if not source.get("repo"):
                errors.append(f"{path.relative_to(ROOT)}: GitHub plugin source requires repo")
        else:
            errors.append(f"{path.relative_to(ROOT)}: unsupported marketplace source format")

    copilot_settings_path = ROOT / ".github/copilot/settings.json"
    copilot_settings = load_json(copilot_settings_path, errors)
    if copilot_settings:
        plugin_id = f"{PLUGIN_NAME}@{MARKETPLACE_NAME}"
        if copilot_settings.get("enabledPlugins", {}).get(plugin_id) is not True:
            errors.append("Copilot repository settings must enable the master plugin")
        if MARKETPLACE_NAME not in copilot_settings.get("extraKnownMarketplaces", {}):
            errors.append("Copilot repository settings must register the master marketplace")

    claude_settings_path = ROOT / ".claude/settings.json"
    claude_settings = load_json(claude_settings_path, errors)
    if claude_settings:
        plugin_id = f"{PLUGIN_NAME}@{MARKETPLACE_NAME}"
        if claude_settings.get("enabledPlugins", {}).get(plugin_id) is not True:
            errors.append("Claude project settings must enable the master plugin")
        if MARKETPLACE_NAME not in claude_settings.get("extraKnownMarketplaces", {}):
            errors.append("Claude project settings must register the master marketplace")

    return errors


def main() -> int:
    errors = validate_skill()
    errors.extend(validate_local_markdown_links(ROOT))
    errors.extend(validate_plugin_manifests())
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    ref_count = len(list((SKILL_DIR / "references").glob("*.md")))
    print("VALIDATION PASSED")
    print(f"Master skill: {SKILL_DIR.relative_to(ROOT) / 'SKILL.md'}")
    print(f"Internal references: {ref_count}")
    print("Agent Plugins, Antigravity, Claude, Cursor and Copilot manifests: OK")
    print("Marketplace and repository auto-install settings: OK")
    print("Local Markdown links: OK")
    print("Single skill entry point: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
