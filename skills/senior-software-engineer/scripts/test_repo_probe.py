#!/usr/bin/env python3
"""Run: python -m unittest discover -s scripts -p 'test_*.py' -v"""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).with_name("repo_probe.py")


class RepoProbeTests(unittest.TestCase):
    def test_existing_repo_is_inspected_without_reading_secrets(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "package.json").write_text('{"scripts":{"test":"exit 0"}}', encoding="utf-8")
            (root / "README.md").write_text("some docs", encoding="utf-8")
            (root / ".env").write_text("TOKEN=do-not-print-this", encoding="utf-8")
            (root / "tests").mkdir()
            process = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(root)],
                check=True, capture_output=True, text=True,
            )
            payload = json.loads(process.stdout)
            self.assertTrue(payload["read_only"])
            self.assertIn("package.json", payload["signals"]["manifests"])
            self.assertIn("tests", payload["signals"]["directories"])
            self.assertTrue(payload["signals"]["has_dotenv_at_root"])
            self.assertNotIn("do-not-print-this", process.stdout)
            self.assertFalse(payload["git"]["is_repository"])

    def test_invalid_root_returns_error(self):
        with tempfile.TemporaryDirectory() as tmp:
            process = subprocess.run(
                [sys.executable, str(SCRIPT), "--root", str(Path(tmp) / "missing")],
                check=False, capture_output=True, text=True,
            )
            self.assertEqual(process.returncode, 2)
            self.assertIn("invalido", process.stderr)


if __name__ == "__main__":
    unittest.main()
