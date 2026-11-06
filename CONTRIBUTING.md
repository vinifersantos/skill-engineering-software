# Contributing

This repository publishes one master engineering skill through multiple compatible plugin and skill-loading surfaces. Contributions should improve `skills/senior-software-engineer/` or its distribution adapters without fragmenting it into separately installed skills.

## Before changing content

1. Read `AGENTS.md`.
2. Read `skills/senior-software-engineer/SKILL.md` and only relevant references.
3. Decide whether the change belongs in the master orchestrator, an internal reference, a host adapter or a marketplace manifest.
4. Avoid duplicate rules and keep one source of truth.
5. If changing the version, update `Version: X.Y.Z` in `SKILL.md`, then run `python scripts/sync_version.py`.

## Before opening a pull request

```bash
python scripts/sync_version.py --check
python scripts/validate_repository.py
python -m unittest discover -s skills/senior-software-engineer/scripts -p 'test_*.py' -v
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/package_skill.py --output-dir dist
python scripts/package_plugin.py --output-dir dist
```

Update `skills/senior-software-engineer/CHANGELOG.md` for meaningful behavior changes. Do not change marketplace names casually: installed plugin identifiers include them.

## Review expectations

- Keep examples accurate and distinguish recommendations from requirements.
- Do not invent platform capabilities, permissions, metrics or validation results.
- Keep destructive or production operations behind explicit authorization.
- Ensure every relative link, manifest path and referenced file exists.
- Avoid adding dependencies unless the benefit is concrete and maintainable.
- Test actual target-host activation when changing plugin manifests; valid JSON alone does not prove runtime compatibility.
