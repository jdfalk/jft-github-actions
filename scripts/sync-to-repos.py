#!/usr/bin/env python3
# file: scripts/sync-to-repos.py
# version: 1.0.0
# guid: s1y2n3c4-a5b6-7c8d-9e0f-1a2b3c4d5e6f

"""Sync files from jft-github-actions template to action repositories."""

import os
import subprocess
import sys
from pathlib import Path

# All action repositories to sync to
ACTION_REPOS = [
    "auto-module-tagging-action",
    "ci-generate-matrices-action",
    "ci-workflow-helpers-action",
    "detect-languages-action",
    "docs-generator-action",
    "generate-version-action",
    "get-frontend-config-action",
    "load-config-action",
    "package-assets-action",
    "pr-auto-label-action",
    "release-docker-action",
    "release-frontend-action",
    "release-go-action",
    "release-protobuf-action",
    "release-python-action",
    "release-rust-action",
    "release-strategy-action",
    "security-summary-action",
    "update-action-docker-ref-action",
]

# Files/directories to sync
SYNC_PATTERNS = [
    ".github/instructions/",
    ".github/agents/",
    ".github/ISSUE_TEMPLATE/",
    ".github/dependabot.yml",
    ".pre-commit-config.yaml",
    ".yamllint",
    ".prettierrc",
    "ruff.toml",
]

# Files to NEVER overwrite (repo-specific)
EXCLUDE_PATTERNS = [
    "*.local.instructions.md",
    ".github/workflows/",  # Don't overwrite workflows
    "README.md",  # Don't overwrite repo-specific README
]


def run_command(cmd: list[str], cwd: Path | None = None) -> tuple[int, str, str]:
    """Run a shell command and return exit code, stdout, stderr."""
    result = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
    )
    return result.returncode, result.stdout, result.stderr


def sync_to_repo(repo_name: str, dry_run: bool = False) -> bool:
    """Sync files to a single repository."""
    print(f"\n{'[DRY RUN] ' if dry_run else ''}Syncing to {repo_name}...")
    
    # Clone the repo temporarily
    temp_dir = Path(f"/tmp/{repo_name}")
    if temp_dir.exists():
        print(f"  Cleaning up existing temp directory...")
        subprocess.run(["rm", "-rf", str(temp_dir)])
    
    print(f"  Cloning repository...")
    exit_code, stdout, stderr = run_command([
        "gh", "repo", "clone", f"jdfalk/{repo_name}", str(temp_dir)
    ])
    
    if exit_code != 0:
        print(f"  ❌ Failed to clone: {stderr}")
        return False
    
    # Copy files
    template_dir = Path.cwd()
    changes_made = False
    
    for pattern in SYNC_PATTERNS:
        source = template_dir / pattern
        
        if not source.exists():
            continue
        
        if source.is_dir():
            # Sync entire directory
            target_dir = temp_dir / pattern
            target_dir.mkdir(parents=True, exist_ok=True)
            
            for file in source.rglob("*"):
                if file.is_file():
                    rel_path = file.relative_to(source)
                    target_file = target_dir / rel_path
                    
                    # Check if file should be excluded
                    should_exclude = any(
                        rel_path.match(exclude)
                        for exclude in EXCLUDE_PATTERNS
                    )
                    
                    if should_exclude:
                        print(f"  ⏭️  Skipping (excluded): {pattern}{rel_path}")
                        continue
                    
                    # Check if file needs updating
                    if target_file.exists():
                        if file.read_bytes() == target_file.read_bytes():
                            continue  # No changes needed
                    
                    print(f"  📝 Updating: {pattern}{rel_path}")
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    target_file.write_bytes(file.read_bytes())
                    changes_made = True
        else:
            # Single file
            target = temp_dir / pattern
            
            if target.exists():
                if source.read_bytes() == target.read_bytes():
                    continue  # No changes needed
            
            print(f"  📝 Updating: {pattern}")
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(source.read_bytes())
            changes_made = True
    
    if not changes_made:
        print(f"  ✅ No changes needed")
        subprocess.run(["rm", "-rf", str(temp_dir)])
        return True
    
    if dry_run:
        print(f"  🔍 [DRY RUN] Would commit and push changes")
        subprocess.run(["rm", "-rf", str(temp_dir)])
        return True
    
    # Commit and push changes
    print(f"  💾 Committing changes...")
    run_command(["git", "add", "."], cwd=temp_dir)
    run_command([
        "git", "commit", "-m",
        "chore(sync): sync files from jft-github-actions template\n\n" +
        "Automated sync of standard files from template repository."
    ], cwd=temp_dir)
    
    print(f"  🚀 Pushing changes...")
    exit_code, stdout, stderr = run_command(["git", "push"], cwd=temp_dir)
    
    if exit_code != 0:
        print(f"  ❌ Failed to push: {stderr}")
        subprocess.run(["rm", "-rf", str(temp_dir)])
        return False
    
    print(f"  ✅ Successfully synced to {repo_name}")
    subprocess.run(["rm", "-rf", str(temp_dir)])
    return True


def main():
    """Main sync function."""
    dry_run = os.getenv("DRY_RUN", "false").lower() == "true"
    target_repos_str = os.getenv("TARGET_REPOS", "all")
    
    if target_repos_str == "all":
        target_repos = ACTION_REPOS
    else:
        target_repos = [r.strip() for r in target_repos_str.split(",")]
    
    print(f"{'=' * 60}")
    print(f"Syncing jft-github-actions template to action repositories")
    print(f"{'=' * 60}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE'}")
    print(f"Target repos: {len(target_repos)}")
    print(f"{'=' * 60}")
    
    success_count = 0
    failure_count = 0
    
    for repo in target_repos:
        if repo not in ACTION_REPOS:
            print(f"\n⚠️  Unknown repo: {repo}")
            continue
        
        if sync_to_repo(repo, dry_run):
            success_count += 1
        else:
            failure_count += 1
    
    print(f"\n{'=' * 60}")
    print(f"Sync complete: {success_count} succeeded, {failure_count} failed")
    print(f"{'=' * 60}")
    
    sys.exit(0 if failure_count == 0 else 1)


if __name__ == "__main__":
    main()
