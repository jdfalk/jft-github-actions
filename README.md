<!-- file: README.md -->
<!-- version: 1.0.0 -->
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

Action repositories automatically sync files from this template using GitHub Actions:

- **Schedule**: Daily at 6am UTC
- **Manual trigger**: Via workflow_dispatch
- **Files synced**: Instructions, agents, configs, issue templates

### Synced Files

All files in this repository (except README.md) are synchronized to action repos.

### Local Overrides

For repository-specific instructions that should NOT be overwritten:
- Use naming pattern: `*.local.instructions.md`
- Example: `python.local.instructions.md`

## 🚀 Using This Template

### For New Repositories

1. Click "Use this template" on GitHub
2. Create your new action repository
3. Customize action-specific files (action.yml, src/, etc.)
4. Keep standard files from template

### For Existing Repositories

1. Add the sync workflow to your repo
2. Run manual sync to pull latest files
3. Review and commit changes

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
