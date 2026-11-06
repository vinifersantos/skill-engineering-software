<p align="center">
  <img src="skills/senior-software-engineer/assets/icon.svg" alt="Senior Software Engineer" width="112" />
</p>

<h1 align="center">Senior Software Engineer</h1>

<p align="center"><strong>One master skill. A complete engineering system. Multiple agent runtimes.</strong></p>

<p align="center">
  <a href="https://github.com/vinifersantos/skill-engineering-software/actions/workflows/validate.yml"><img src="https://github.com/vinifersantos/skill-engineering-software/actions/workflows/validate.yml/badge.svg?branch=main" alt="Validate" /></a>
  <img src="https://img.shields.io/badge/version-2.0.0-blue" alt="Version 2.0.0" />
  <img src="https://img.shields.io/badge/Agent_Skills-portable-7c3aed" alt="Portable Agent Skill" />
</p>

A portable master engineering skill for AI coding agents. It combines Code-First implementation, bounded Grill-Me discovery, Agent Harness & Orchestration, architecture, data engineering, testing, security, CI/CD, debugging, observability, SRE and disaster recovery.

**The only installable skill is `skills/senior-software-engineer/SKILL.md`.** Its `references/` directory contains internal playbooks loaded on demand, not separate skills to install.

## Engineering capabilities

| Capability | Responsibility |
| --- | --- |
| Code-First & Impact-Driven | Direct code location, contract impact, minimal safe changes and evidence-based validation. |
| Grill-Me discovery | Challenge unresolved high-impact assumptions before implementation. Routine bounded work stays direct. |
| Agent Harness & Orchestration | Context, risk R0-R3, autonomy, subagents, MCP tools, delegation and accountable handoffs. |
| Architecture & API design | Boundaries, contracts, distributed systems, trade-offs and ADRs. |
| Data Engineering | PostgreSQL, Supabase, RLS, safe migrations, integrity and LGPD-aware handling. |
| Testing & Quality | Unit, integration, contract, E2E, security, migration and performance testing. |
| Security & Secret Management | Identity, authorization, least privilege, vaults, credential lifecycle and privacy. |
| CI/CD & Release Engineering | GitHub Actions, GitLab CI, Docker, reproducible builds, releases and rollback. |
| Debugging & Refactoring | Evidence-led diagnosis, RCA, regression protection and behavior-preserving refactoring. |
| Context, Memory & Tooling | MCP, RAG, LSP, code search, ADRs and project continuity. |
| Observability & SRE | Structured logs, metrics, tracing, SLOs, incidents and operational reliability. |
| Disaster Recovery | Backups, restore drills, RPO/RTO, failover and business continuity. |

## Install

Choose one route per agent. Do not install a plugin and also copy the same skill into the same runtime unless duplicate copies are intentional.

### Codex CLI

The repository contains a Codex marketplace at `.agents/plugins/marketplace.json` and an Agent Plugins 1.0 package at the repository root.

```bash
codex plugin marketplace add vinifersantos/skill-engineering-software
codex plugin install senior-software-engineer@skill-engineering-software
codex plugin list
```

Start a new Codex session after installation. If you prefer a standalone skill instead of a plugin, use `python scripts/install_skill.py --agent codex --scope user`.

### ChatGPT workspace

A ChatGPT workspace admin can import the GitHub marketplace:

1. Open **Admin > Plugins > Add > Import marketplace**.
2. Source: `https://github.com/vinifersantos/skill-engineering-software`.
3. Path: `.agents/plugins`.
4. Branch: `main`.
5. Import, review the result and set the plugin's installation policy in the workspace.

The importing administrator must have GitHub read access. New marketplaces sync daily; an admin can request **Sync now**. Importing the plugin does not grant access to connected apps, accounts or credentials. Personal workspaces without admin access cannot perform this workspace import.

### Claude Code

Inside Claude Code:

```text
/plugin marketplace add vinifersantos/skill-engineering-software
/plugin install senior-software-engineer@skill-engineering-software
```

The repository includes `.claude/settings.json` to register and enable the plugin when this repository is opened in Claude Code. For a user-level install in other repositories, use the commands above.

Custom marketplace auto-update is opt-in. Open `/plugin`, go to **Marketplaces**, select `skill-engineering-software`, and enable **Auto-update**. To update manually:

```text
/plugin update senior-software-engineer@skill-engineering-software
```

### GitHub Copilot CLI

```bash
copilot plugin marketplace add vinifersantos/skill-engineering-software
copilot plugin install senior-software-engineer@skill-engineering-software
copilot plugin list
```

The repository includes `.github/copilot/settings.json`, which registers the marketplace and enables the plugin for Copilot CLI and Copilot in the cloud when working in this repository.

For automatic updates across your own repositories, merge the following entry into `~/.copilot/settings.json` without overwriting your existing settings:

```json
{
  "extraKnownMarketplaces": {
    "skill-engineering-software": {
      "source": {
        "source": "github",
        "repo": "vinifersantos/skill-engineering-software"
      },
      "autoUpdate": true
    }
  }
}
```

Then install the plugin once with the commands above. The `autoUpdate` opt-in is honored in user settings, not repository settings, and applies to interactive and `-p` sessions.

### GitHub Copilot in VS Code

1. Open the Command Palette.
2. Run **Chat: Manage Plugin Marketplaces**.
3. Select **Add Marketplace...** and enter `https://github.com/vinifersantos/skill-engineering-software`.
4. Open **Customize** in the Chat side panel or Agents window, find **Senior Software Engineer**, and install it.

You can also run **Chat: Install Plugin from Source** and enter the repository URL.

### Cursor

For Cursor Teams or Enterprise, an admin can import the repository as a team marketplace:

1. Open **Dashboard > Plugins & MCPs**.
2. In **Team Marketplaces**, choose **Add Marketplace > Import from Repo**.
3. Enter `https://github.com/vinifersantos/skill-engineering-software`.
4. Add **Senior Software Engineer** to the marketplace and choose its installation mode.
5. Optionally enable **Auto Refresh**. GitHub Auto Refresh requires the Cursor GitHub App to be installed on the repository.

For an individual Cursor installation, use the standalone skill installer:

```bash
python scripts/install_skill.py --agent cursor --scope user
```

Or use `npx skills@latest add vinifersantos/skill-engineering-software --skill senior-software-engineer --agent cursor`.

### Antigravity CLI and App

The repository includes `.antigravity-plugin/plugin.json`, so install the full plugin rather than copying only the skill folder:

```bash
agy plugin install https://github.com/vinifersantos/skill-engineering-software
agy plugin list
```

The plugin bundles the master skill and its references. In the Antigravity App, you can also install the GitHub plugin through **Customizations > Marketplace**. Plugins installed in the App sync to the CLI. To refresh a GitHub-installed CLI plugin, use the plugin manager or reinstall the repository after reviewing the version change.

### Gemini CLI

```bash
gemini skills install https://github.com/vinifersantos/skill-engineering-software.git --path skills/senior-software-engineer
gemini skills list
```

The CLI requests consent unless `--consent` is supplied. Re-run the install command to update the copied skill.

### JetBrains Junie (IDE and CLI)

Junie supports Agent Skills natively. Install the skill globally:

```bash
python scripts/install_skill.py --agent junie --scope user
```

Or install it only in the current project:

```bash
python scripts/install_skill.py --agent junie --scope workspace
```

Then open Junie and run `/skills` to verify that `senior-software-engineer` is discovered. The global destination is `~/.junie/skills/`; the workspace destination is `.junie/skills/`.

### Any other Agent Skills-compatible runtime

```bash
npx skills@latest add vinifersantos/skill-engineering-software --skill senior-software-engineer
```

Select the target agent in the installer and verify the destination. Host support and update behavior vary.

## Update and replace safely

Plugin-managed installs should be updated through the host's plugin manager or marketplace. For standalone copies, re-run `scripts/install_skill.py` with `--replace`. The installer first moves the previous copy to a timestamped backup; it never silently overwrites an existing installation.

Example:

```bash
python scripts/install_skill.py --agent junie --scope user --replace
```

Do not delete older installations until the new one appears in the target agent's skill list and a test task confirms that references load.

## How the skill behaves

- Direct Code-First engineering is the default for clear, bounded implementation, debugging and review tasks.
- Grill-Me activates automatically only when unresolved assumptions could materially change architecture, business rules, security, data integrity, scope, cost or reversibility. Explicit `/grillme` also activates discovery.
- Agent orchestration is capability-aware. It discovers agents and tools actually available, delegates only when useful, and keeps the lead agent accountable for integration and evidence.
- References load progressively. A small UI fix should not load every architecture, database and SRE playbook.
- The skill does not create permissions, agents, MCP servers, backups, observability or production access that the runtime does not provide.

## Repository structure

```text
.
├── plugin.json
├── .agents/plugins/marketplace.json
├── .antigravity-plugin/plugin.json
├── .claude-plugin/
├── .github/plugin/marketplace.json
├── .github/copilot/settings.json
├── .github/workflows/
├── .junie/rules/
├── scripts/
└── skills/senior-software-engineer/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── assets/
    ├── adapters/
    ├── references/
    └── scripts/
```

## Validate, test and package

Requirements: Python 3.11+ and the standard library. No third-party packages are required for local validation or packaging.

```bash
python scripts/sync_version.py --check
python scripts/validate_repository.py
python -m unittest discover -s skills/senior-software-engineer/scripts -p 'test_*.py' -v
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/package_skill.py --output-dir dist
python scripts/package_plugin.py --output-dir dist
```

The GitHub Actions validation workflow runs on pull requests and pushes to `main`. A `vX.Y.Z` tag triggers a release workflow that validates versions, tests and manifests, then publishes both the standalone skill ZIP and the cross-host plugin ZIP.

For a behavior change, update the relevant reference and `skills/senior-software-engineer/CHANGELOG.md`. Change `Version: X.Y.Z` in the master `SKILL.md`, then run `python scripts/sync_version.py` to synchronize all plugin manifests and marketplace metadata.

## Quality and limitations

The repository validates structure, local references, metadata, marketplace entries and packaging. CI provides repeatable checks after the branch is pushed. Runtime activation still needs to be tested in each target host. No skill can guarantee 100% reliability, security or production readiness. RPO/RTO, SLOs, secret rotation and retention must be based on real requirements, not invented defaults.

## References

The repository organization takes inspiration from [Matt Pocock's skills repository](https://github.com/mattpocock/skills), while preserving independent content and a single master skill.

- [Agent Skills format](https://agentskills.io/)
- [OpenAI plugin and marketplace documentation](https://learn.chatgpt.com/docs/enterprise/plugin-management)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [GitHub Copilot plugins](https://docs.github.com/en/copilot/concepts/customizations/plugins)
- [Cursor plugins](https://cursor.com/docs/plugins)
- [Antigravity plugins](https://antigravity.google/docs/plugins)
- [Gemini CLI Agent Skills](https://geminicli.com/docs/cli/skills/)
- [JetBrains Junie Agent Skills](https://junie.jetbrains.com/docs/agent-skills.html)
