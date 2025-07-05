# Git Workflow in Context Engineer

## Overview

Context Engineer provides two auto-pilot modes with different git strategies:

1. **`context-auto`** - Simple linear commits on current branch
2. **`context-auto-git`** - Full branching strategy with merges

## Simple Mode: `context-auto`

Uses linear commits on the current branch with commits at these points:

### Commit Points

1. **Phase Start**
   - Commit: `Auto-commit: Phase N - Starting phase`
   - When: Before any work begins

2. **PRP Generated**
   - Commit: `Auto-commit: Phase N - PRP generated`
   - When: After Claude Code generates the implementation plan

3. **PRP Refined** (optional)
   - Commit: `Auto-commit: Phase N - PRP refined`
   - When: If you make manual changes to the PRP

4. **Implementation Complete**
   - Commit: `Auto-commit: Phase N - Implementation complete`
   - When: After Claude Code finishes executing the PRP

5. **Tests Passing** (if tests exist)
   - Commit: `Auto-commit: Phase N - Tests passing`
   - When: After test suite runs successfully

6. **Tests Fixed** (if needed)
   - Commit: `Auto-commit: Phase N - Tests fixed`
   - When: After fixing failing tests

7. **Phase Validated**
   - Commit: `Auto-commit: Phase N - Phase complete and validated`
   - When: After confirming success criteria are met

### Example Git Log (Simple Mode)

```
* 2f3d4e5 - Auto-commit: Phase 2 - Phase complete and validated
* 1a2b3c4 - Auto-commit: Phase 2 - Tests passing
* 9e8f7g6 - Auto-commit: Phase 2 - Implementation complete
* 5d4c3b2 - Auto-commit: Phase 2 - PRP generated
* 8h7g6f5 - Auto-commit: Phase 2 - Starting phase
* 3c2b1a0 - Auto-commit: Phase 1 - Phase complete and validated
```

## Advanced Mode: `context-auto-git`

Uses a sophisticated branching strategy:

### Branch Types

1. **`main`** - Stable, tested code
2. **`planning/phase-N`** - For PRP generation
3. **`feature/phase-N`** - For implementation
4. **`test/phase-N`** - For test fixes (if needed)

### Workflow per Phase

```
main
  |
  └─> planning/phase-1 (create branch)
       ├─ commit: "Phase initialized"
       ├─ commit: "PRP generated"
       |
       └─> feature/phase-1 (create branch)
            ├─ commit: "Implementation complete"
            |
            └─> test/phase-1 (if tests exist)
                 ├─ commit: "Tests passing"
                 └─ merge back to feature/phase-1
            |
            └─ merge back to planning/phase-1
       |
       └─ merge to main (with --no-ff)
```

### Example Git Graph (Advanced Mode)

```
*   Merge planning/phase-2
|\  
| * Phase 2: Phase validated
| * Merge test/phase-2
| |\ 
| | * Phase 2: Tests passing
| |/
| * Phase 2: Implementation complete
| * Phase 2: PRP generated
| * Phase 2: Phase initialized
|/
*   Merge planning/phase-1
|\
| * Phase 1: Phase validated
| * Phase 1: Implementation complete
| * Phase 1: PRP generated
| * Phase 1: Phase initialized
|/
* Initial commit
```

## Choosing Which Mode

### Use Simple Mode (`context-auto`) when:
- Working on personal projects
- Want quick iteration
- Don't need complex history
- Prefer linear commits

### Use Advanced Mode (`context-auto-git`) when:
- Working in teams
- Need clear phase separation
- Want to preserve planning/implementation distinction
- Need ability to revert entire phases
- Want professional git history

## Manual Git Commands

### Creating Phase Branches Manually

```bash
# Start new phase
git checkout -b planning/phase-3

# After PRP
git checkout -b feature/phase-3

# For testing
git checkout -b test/phase-3

# Merge back
git checkout feature/phase-3
git merge test/phase-3

git checkout planning/phase-3
git merge feature/phase-3

git checkout main
git merge --no-ff planning/phase-3
```

### Tagging Releases

After completing all phases:

```bash
# Tag the release
git tag -a v1.0.0 -m "Initial release: All phases complete"

# Push with tags
git push origin main --tags
```

### Reverting a Phase

If you need to undo an entire phase:

```bash
# Find the merge commit
git log --oneline --graph

# Revert the merge
git revert -m 1 <merge-commit-hash>
```

## Best Practices

1. **Commit Messages**
   - Keep auto-generated messages for traceability
   - Add descriptive body for major changes
   - Reference issue numbers when applicable

2. **Branch Hygiene**
   - Delete feature branches after merging
   - Keep planning branches for history
   - Regularly clean up old branches

3. **Testing**
   - Always run tests before marking phase complete
   - Commit test fixes separately
   - Document why tests were skipped if applicable

4. **Documentation**
   - Update README.md in phase completion commits
   - Keep ROADMAP.md current
   - Document architectural decisions

## Git Configuration

Recommended git settings for Context Engineer projects:

```bash
# Better merge commits
git config merge.ff false

# Clear branch names in logs
git config log.decorate short

# Useful aliases
git config alias.graph "log --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit"
git config alias.phases "log --oneline --grep='Phase [0-9]'"
```

## Integration with CI/CD

The branching strategy works well with CI/CD:

```yaml
# Example GitHub Actions
on:
  push:
    branches:
      - main
      - 'feature/**'
      - 'test/**'
  pull_request:
    branches:
      - main
```

This ensures tests run on feature branches before merging.