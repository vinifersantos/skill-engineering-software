from __future__ import annotations

import json
import tempfile
import unittest
import zipfile
from pathlib import Path

from install_skill import destination_for, install_skill
from package_plugin import build_package as build_plugin_package, get_version as get_plugin_version
from package_skill import build_package as build_skill_package, get_version as get_skill_version
from validate_repository import parse_frontmatter, validate_local_markdown_links
from sync_version import sync_versions


class RepositoryToolTests(unittest.TestCase):
    def test_frontmatter_parser_reads_name_and_description(self):
        with tempfile.TemporaryDirectory() as tmp:
            file = Path(tmp) / "SKILL.md"
            file.write_text('---\nname: example\ndescription: "Example skill"\n---\n\n# Body\n', encoding="utf-8")
            fields, body = parse_frontmatter(file)
            self.assertEqual(fields["name"], "example")
            self.assertEqual(fields["description"], "Example skill")
            self.assertIn("# Body", body)

    def test_link_validator_detects_missing_local_target(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "index.md").write_text("[Missing](missing.md)\n", encoding="utf-8")
            errors = validate_local_markdown_links(root)
            self.assertEqual(len(errors), 1)
            self.assertIn("missing.md", errors[0])

    def test_skill_package_contains_one_entry_point(self):
        root = Path(__file__).resolve().parents[1]
        skill = root / "skills" / "senior-software-engineer"
        version = get_skill_version(skill)
        with tempfile.TemporaryDirectory() as tmp:
            output = build_skill_package(skill, Path(tmp) / "skill.zip")
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
            self.assertIn("senior-software-engineer/SKILL.md", names)
            self.assertIn("senior-software-engineer/references/code-first-impact-driven.md", names)
            self.assertFalse(any(name.endswith("/SKILL.md") and name != "senior-software-engineer/SKILL.md" for name in names))
            self.assertEqual(version, "2.0.0")

    def test_cross_host_plugin_package_contains_all_host_manifests(self):
        self.assertEqual(get_plugin_version(), "2.0.0")
        with tempfile.TemporaryDirectory() as tmp:
            output = build_plugin_package(Path(tmp) / "plugin.zip")
            with zipfile.ZipFile(output) as archive:
                names = archive.namelist()
            self.assertIn("senior-software-engineer/plugin.json", names)
            self.assertIn("senior-software-engineer/.antigravity-plugin/plugin.json", names)
            self.assertIn("senior-software-engineer/.claude-plugin/plugin.json", names)
            self.assertIn("senior-software-engineer/skills/senior-software-engineer/SKILL.md", names)

    def test_installer_preserves_existing_copy_before_replacement(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "source" / "senior-software-engineer"
            source.mkdir(parents=True)
            (source / "SKILL.md").write_text("new", encoding="utf-8")
            destination = root / "target"
            destination.mkdir()
            existing = destination / "senior-software-engineer"
            existing.mkdir()
            (existing / "SKILL.md").write_text("old", encoding="utf-8")

            with self.assertRaises(FileExistsError):
                install_skill(source, destination, replace=False)

            target, backup = install_skill(source, destination, replace=True)
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), "new")
            self.assertIsNotNone(backup)
            self.assertEqual((backup / "SKILL.md").read_text(encoding="utf-8"), "old")

    def test_agent_install_destinations(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "project"
            home = Path(tmp) / "home"
            self.assertEqual(destination_for("junie", "workspace", cwd=root, home=home), root / ".junie/skills")
            self.assertEqual(destination_for("gemini", "workspace", cwd=root, home=home), root / ".agents/skills")
            self.assertEqual(destination_for("cursor", "user", cwd=root, home=home), home / ".cursor/skills")

    def test_version_sync_updates_all_manifests_without_duplicating_claude_entry_version(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills/senior-software-engineer").mkdir(parents=True)
            (root / "skills/senior-software-engineer/SKILL.md").write_text("Version: 3.1.4\n", encoding="utf-8")
            for relative in ("plugin.json", ".antigravity-plugin/plugin.json", ".claude-plugin/plugin.json"):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({"name": "senior-software-engineer", "version": "2.0.0"}), encoding="utf-8")
            marketplace_paths = (
                ".agents/plugins/marketplace.json",
                ".claude-plugin/marketplace.json",
                    ".github/plugin/marketplace.json",
            )
            for relative in marketplace_paths:
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                entry = {"name": "senior-software-engineer"}
                if relative != ".claude-plugin/marketplace.json":
                    entry["version"] = "2.0.0"
                path.write_text(json.dumps({"metadata": {"version": "2.0.0"}, "plugins": [entry]}), encoding="utf-8")

            changed = sync_versions(root=root)
            self.assertEqual(len(changed), 6)
            self.assertEqual(json.loads((root / "plugin.json").read_text(encoding="utf-8"))["version"], "3.1.4")
            marketplace = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
            self.assertEqual(marketplace["metadata"]["version"], "3.1.4")
            self.assertEqual(marketplace["plugins"][0]["version"], "3.1.4")
            claude_marketplace = json.loads((root / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
            self.assertNotIn("version", claude_marketplace["plugins"][0])

    def test_marketplace_manifests_are_valid_json(self):
        root = Path(__file__).resolve().parents[1]
        for relative in (
            "plugin.json",
            ".antigravity-plugin/plugin.json",
            ".agents/plugins/marketplace.json",
            ".claude-plugin/plugin.json",
            ".claude-plugin/marketplace.json",
            ".github/plugin/marketplace.json",
            ".github/copilot/settings.json",
            ".claude/settings.json",
        ):
            with self.subTest(relative=relative):
                json.loads((root / relative).read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
