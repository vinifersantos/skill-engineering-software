# Canonical installation instructions

One plugin contains one master skill. Do not ask users to install former Code-First, Harness Engineering or Grill-Me packages separately.

## Codex CLI

```bash
codex plugin marketplace add vinifersantos/skill-engineering-software
codex plugin install senior-software-engineer@skill-engineering-software
```

## ChatGPT workspace

A workspace admin imports the repository URL `https://github.com/vinifersantos/skill-engineering-software`, with Path `.agents/plugins` and Branch `main`, through Admin > Plugins > Add > Import marketplace. The importing admin needs GitHub read access. Marketplace sync is daily; use Sync now for an immediate refresh.

## Claude Code

```text
/plugin marketplace add vinifersantos/skill-engineering-software
/plugin install senior-software-engineer@skill-engineering-software
```

Custom marketplace auto-update is opt-in. In `/plugin` > Marketplaces, select `skill-engineering-software` and enable Auto-update.

## GitHub Copilot CLI

```bash
copilot plugin marketplace add vinifersantos/skill-engineering-software
copilot plugin install senior-software-engineer@skill-engineering-software
```

For user-level auto-update, merge an `extraKnownMarketplaces` entry with `autoUpdate: true` into `~/.copilot/settings.json`. Repository settings enable the plugin in this repository but cannot opt into auto-update.

## GitHub Copilot in VS Code

Run Chat: Manage Plugin Marketplaces from the Command Palette, add the repository URL, then install Senior Software Engineer from Customize > Plugins. Alternatively, run Chat: Install Plugin from Source and enter the repository URL.

## Cursor

Use Customize > Plugins to add the GitHub repository as a marketplace/source and install Senior Software Engineer. Alternatively, use `npx skills@latest add vinifersantos/skill-engineering-software --skill senior-software-engineer --agent cursor`.

## Antigravity CLI and App

```bash
agy plugin install https://github.com/vinifersantos/skill-engineering-software
agy plugin list
```

The repository includes `.antigravity-plugin/plugin.json`. The CLI installs the plugin globally. In the App or IDE, place the cloned plugin directory in `.agents/plugins/` for workspace scope or `~/.gemini/config/plugins/` for global scope. App-installed plugins sync to the CLI.

## Gemini CLI

```bash
gemini skills install https://github.com/vinifersantos/skill-engineering-software.git --path skills/senior-software-engineer
gemini skills list
```

## JetBrains Junie

```bash
python scripts/install_skill.py --agent junie --scope user
```

Use `--scope workspace` for `.junie/skills/`. Verify discovery with `/skills`.

## Standalone skill copies

```bash
python scripts/install_skill.py --agent codex --scope user
python scripts/install_skill.py --agent claude --scope user
python scripts/install_skill.py --agent cursor --scope user
python scripts/install_skill.py --agent gemini --scope user
python scripts/install_skill.py --agent junie --scope user
```

Use `--replace` only when intentionally updating an existing copy. The installer preserves the old folder as a timestamped backup. Never delete an older installation until the new one is discovered and tested.
