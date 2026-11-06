# Senior Software Engineer

One master engineering skill for AI coding agents. It combines Code-First implementation, bounded Grill-Me discovery, Agent Harness & Orchestration, architecture, data engineering, testing, security, CI/CD, debugging, observability, SRE and disaster recovery.

The only skill entry point is skills/senior-software-engineer/SKILL.md. Detailed playbooks are internal references loaded on demand, not separate skills to install.

## Install

Choose one route per agent. Do not install the plugin and copy the same skill into the same runtime unless you intentionally want duplicate copies.

### Codex CLI

    codex plugin marketplace add vinifersantos/skill-engineering-software --sparse .agents/plugins

Then run /plugins and install Senior Software Engineer.

### Claude Code

Inside Claude Code:

    /plugin marketplace add vinifersantos/skill-engineering-software
    /plugin install senior-software-engineer@skill-engineering-software

### GitHub Copilot CLI

    copilot plugin marketplace add vinifersantos/skill-engineering-software
    copilot plugin install senior-software-engineer@skill-engineering-software

### Cursor

Use Customize > Plugins > Add Marketplace > From GitHub Repository and enter the repository URL.

### Gemini CLI

    gemini skills install https://github.com/vinifersantos/skill-engineering-software.git --path skills/senior-software-engineer

### Antigravity

    python scripts/install_skill.py --agent antigravity --scope user

### JetBrains Junie

Merge skills/senior-software-engineer/adapters/junie/AGENTS.md into global ~/.junie/AGENTS.md or configure it as a guideline file. Preserve existing instructions and replace the skill path placeholder.

## Behavior

- Direct Code-First engineering is the default for clear, bounded tasks.
- Grill-Me activates automatically only when unresolved assumptions could materially change architecture, business rules, security, data integrity, scope, cost or reversibility.
- Agent orchestration is capability-aware and uses only agents/tools actually available.
- References load progressively; small changes do not load every playbook.

## Validation

    python scripts/validate_repository.py
    python -m unittest discover -s scripts -p 'test_*.py' -v
    python scripts/package_skill.py --output-dir dist
    python scripts/package_plugin.py --output-dir dist

A vX.Y.Z tag runs release validation and publishes skill and plugin ZIPs. Runtime activation must still be tested in each host. Valid manifests alone do not prove host compatibility.

Inspired by the organization of https://github.com/mattpocock/skills, while preserving an independent master skill and its own content.
