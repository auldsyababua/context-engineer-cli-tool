# Claude Code Configuration

This directory contains configuration for Claude Code behavior in this project.

## Files

### `settings.json`
Default permissions and behavior settings for Claude Code. This file is committed to version control and shared across the team.

Key sections:
- **permissions**: What Claude can and cannot do
- **behavior**: How Claude should act (auto-commit, testing, etc.)
- **project**: Project-specific settings

### `settings.local.json` (optional)
Personal overrides for your local development. Copy `settings.local.json.example` to `settings.local.json` and customize.

This file is gitignored and won't be committed.

### `commands/`
Custom slash commands for Claude Code:
- `/generate-prp` - Generate implementation plans
- `/execute-prp` - Execute implementation plans
- `/check-env` - Verify environment variables

## Permission Defaults

### ✅ Allowed by Default
- Creating/editing files
- Reading all files
- Running tests
- Git operations (except push)
- Installing packages
- Running build scripts

### ❌ Blocked by Default
- Deleting files/directories
- Git push/reset/rebase
- Publishing packages
- Sudo commands
- Destructive operations

## Customizing Permissions

1. For team-wide changes: Edit `settings.json`
2. For personal preferences: Create `settings.local.json`
3. For temporary overrides: Use Claude's UI

## Safety Features

- Auto-commit after changes (configurable)
- Backup creation before edits
- Dangerous command warnings
- Test before commit option
- Verbose logging for audit trail