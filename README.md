<!-- file: README.md -->
<!-- version: 1.1.0 -->
<!-- guid: a1b2c3d4-e5f6-7890-abcd-ef1234567890 -->

# jft-github-actions

**Template repository for standardized GitHub Actions**

This is the **single source of truth** for all GitHub Action repositories in the `jdfalk` organization.

## 🎯 Purpose

This template repository contains:

- **Standard instruction files** (`.github/instructions/`) - Copilot/AI agent guidelines
- **Agent definitions** (`.github/agents/`) - Specialized agent configurations
- **Issue templates** (`.github/ISSUE_TEMPLATE/`) - Standardized issue reporting
- **Configuration files** - Pre-commit, linting, formatting standards
- **Sync workflows** - Automated synchronization to action repositories

## 📁 Structure

```
.github/
  ├── instructions/       # Copilot/AI coding instructions
  ├── agents/            # Specialized agent definitions
  ├── ISSUE_TEMPLATE/    # Issue templates
  ├── workflows/         # Sync workflows
  └── dependabot.yml     # Dependency updates
.pre-commit-config.yaml  # Pre-commit hooks
.yamllint               # YAML linting config
.prettierrc             # Code formatting
ruff.toml               # Python linting
```

## 🔄 Synchronization

**Pull-based sync**: Each action repository pulls files from this template and commits locally.

- **Schedule**: Daily at 6am UTC (via each repo's workflow)
- **Manual trigger**: Run `sync-from-template` workflow in any action repo
- **Files synced**: Instructions, agents, configs, issue templates
- **Workflow**: `.github/workflows/sync-from-template.yml` (included in template)

### How It Works

1. Each action repo has the `sync-from-template.yml` workflow
2. Workflow checks out both the action repo and this template
3. Compares files and copies any that changed
4. Commits changes directly to the action repo
5. Each repo manages its own sync independently

### Synced Files

The following patterns are synced from template:

- `.github/instructions/` - All instruction files
- `.github/agents/` - All agent definitions
- `.github/ISSUE_TEMPLATE/` - Issue templates
- `.github/dependabot.yml` - Dependency configuration
- `.pre-commit-config.yaml` - Pre-commit hooks
- `.yamllint` - YAML linting rules
- `.prettierrc` - Code formatting rules
- `ruff.toml` - Python linting configuration

### Files Excluded from Sync

The following files are NEVER overwritten:

- `*.local.instructions.md` - Repository-specific instructions
- `.github/workflows/*` - Repository workflows (except sync-from-template.yml)
- `README.md` - Repository documentation
- `CHANGELOG.md` - Repository changelog
- `action.yml` - Action definition

## 🚀 Using This Template

### For New Repositories

1. Click "Use this template" on GitHub
2. Create your new action repository
3. Customize action-specific files (action.yml, src/, etc.)
4. Keep standard files from template

### For Existing Repositories

The sync workflow is automatically distributed via this template. To add it:

1. Copy `.github/workflows/sync-from-template.yml` from this template
2. Commit to your action repo
3. Run workflow manually first time: `gh workflow run sync-from-template.yml`
4. Review and commit the synced files
5. Future syncs happen automatically daily at 6am UTC

## 📝 Updating Standards

To update files across all action repositories:

1. Make changes in this template repo
2. Commit and push to main branch
3. All action repos will sync within 24 hours (or trigger manually)

## 📚 Documentation

- [Action Repo Standards](https://github.com/jdfalk/ghcommon/blob/main/ACTION_REPO_STANDARDS.md)
- [Copilot Instructions](https://github.com/jdfalk/ghcommon/blob/main/.github/copilot-instructions.md)

## 🔧 Standard Files

### Required Files (All Repos)

- ✅ `action.yml` - Action definition
- ✅ `README.md` - Documentation
- ✅ `CHANGELOG.md` - Version history
- ✅ `TODO.md` - Future work tracking
- ✅ `ruff.toml` - Python linting
- ✅ `.pre-commit-config.yaml` - Pre-commit hooks
- ✅ `.yamllint` - YAML linting
- ✅ `.github/dependabot.yml` - Dependency updates

### Optional Files

- 📦 `Dockerfile` - For dockerized actions
- 📦 `LICENSE` - For open source actions
- 📦 `.prettierrc` - Code formatting
- 📦 `.gitignore` - Git ignore patterns

## 🤝 Contributing

To propose changes to the template:

1. Create an issue describing the change
2. Submit a PR with your changes
3. Once approved, changes propagate to all action repos

## 📄 License

MIT License - See individual action repositories for their licenses.
