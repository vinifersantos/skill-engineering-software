# Senior Software Engineer

A single installable master skill for AI-assisted software engineering. The `SKILL.md` file is the only entry point; the `references/` directory contains focused playbooks loaded progressively.

## Package contents

- Code-First & Impact-Driven implementation.
- Integrated Grill-Me discovery mode.
- Agent Harness & Orchestration.
- Architecture, API, database and distributed systems.
- Testing, security, secrets and CI/CD.
- Debugging, RCA, refactoring, observability, SRE and disaster recovery.
- Read-only repository inventory helper in `scripts/repo_probe.py`.

## Install

Use the repository root README for host-specific plugin and skill installation instructions. Keep this entire directory together so relative references and scripts remain available.

## Internal structure

- `SKILL.md`: master orchestrator and mode-selection rules.
- `references/`: domain playbooks, loaded only when relevant.
- `scripts/`: read-only helper and its tests.
- `agents/openai.yaml`: OpenAI skill-picker metadata.
- `assets/`: skill icon and supporting assets.
- `adapters/`: small pointers for runtimes that need an instruction file.

The former Code-First, Harness Engineering and Grill-Me packages are integrated capabilities, not separate installs.
