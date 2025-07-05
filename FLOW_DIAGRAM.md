# Context Engineer CLI Tool - Complete Flow Diagram

**Updated**: Includes MCP integration, analysis phases, and git workflows

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 CONTEXT ENGINEER CLI TOOL                                   │
│                                         Entry Points                                        │
└──────────────────────────────────────────────────────────────────────────────────────────────┘
                                              │
        ┌─────────────────────────────────────┴─────────────────────────────────────┐
        │                                                                           │
  ┌─────▼─────┐                     ┌─────────────┐                      ┌────────▼─────────┐
  │  context  │                     │context-auto │                      │context-auto-git │
  │   (ce)    │                     │   (cea)     │                      │    (cea-git)    │
  └─────┬─────┘                     └──────┬──────┘                      └────────┬─────────┘
        │                                  │                                      │
┌───────▼───────┐              ┌───────────▼────────────┐            ┌───────────▼────────────┐
│ STANDARD MODE │              │   AUTO-PILOT MODE      │            │  GIT-ENHANCED MODE     │
│ One-time init │              │ Linear commits on main │            │ Full branching strategy│
└───────┬───────┘              └────────────┬───────────┘            └───────────┬────────────┘
        │                                   │                                    │
        │                                   └────────────────┬───────────────────┘
        │                                                    │
        │                                          ┌─────────▼──────────┐
        │                                          │   Session Check    │
        │                                          │ .context-session   │
        │                                          └─────────┬──────────┘
        │                                                    │
        │                                          ┌─────────▼──────────┐
        │                                          │ Existing Session?  │
        │                                          └────┬────────┬──────┘
        │                                               │        │
        │                                             NO│        │YES
        │                                               │        │
┌───────▼──────────────┐                    ┌───────────▼──┐  ┌─▼───────────┐
│  Interactive Setup   │                    │  In Context  │  │Resume from  │
├──────────────────────┤                    │  Project?    │  │saved phase  │
│ 1. Project Type?     │                    └───────┬──────┘  └─────────────┘
│    □ Full            │                            │NO
│    □ Minimal         │                    ┌───────▼───────────────┐
│    □ Custom          │                    │ Project Type Menu     │
│ 2. Primary Language? │                    ├───────────────────────┤
│ 3. Testing Framework?│                    │ 1) New from scratch   │
│ 4. First Feature?    │                    │ 2) Refactor existing  │
└───────┬──────────────┘                    │ 3) Retry previous     │
        │                                   └───┬───────┬───────┬───┘
        │                                       │       │       │
┌───────▼──────────────┐                   ┌───▼───┐ ┌─▼──────┐ ┌▼──────┐
│ Create Project Dir   │                   │ New   │ │Refactor│ │Retry  │
│ ~/Desktop/projects/  │                   └───┬───┘ └───┬────┘ └──┬────┘
│ └── project-name/    │                       │         │         │
│     ├── .claude/     │                 ┌─────▼────┐ ┌──▼─────┐ ┌─▼──────┐
│     ├── templates/   │                 │Get Proj │ │Get Path│ │Get Path│
│     ├── CLAUDE.md    │                 │Name     │ │to Old  │ │to Prev │
│     ├── PLANNING.md  │                 └────┬────┘ └───┬────┘ └───┬────┘
│     ├── TASK.md      │                      │          │          │
│     └── ...          │              ┌───────▼────────┐ │ ┌────────▼────┐
└───────┬──────────────┘              │Simple Context │ │ │Interactive  │
        │                             │Creation       │ │ │Questionnaire│
        │                             └───────┬────────┘ │ └────────┬────┘
        │                                     │          │          │
┌───────▼──────────────┐              ┌──────▼──────┐ ┌─▼───────┐ ┌▼───────┐
│ Language Setup       │              │ NEW_CONTEXT │ │ANALYSIS │ │RETRY   │
│ - Python: venv       │              │ .md         │ │.md      │ │CONTEXT │
│ - Node: package.json │              └──────┬──────┘ └─┬───────┘ └┬───────┘
└───────┬──────────────┘                     │          │          │
        │                             ┌──────▼──────────▼──────────▼───────┐
┌───────▼──────────────┐              │    Create Project Dir & Init Git    │
│ Git Init & Commit    │              └────────────────────────────────────┘
└───────┬──────────────┘                              │
        │                                             │
        └─────────────────────┬───────────────────────┘
                              │
                    ┌─────────▼─────────────────────┐
                    │  🔍 MCP REQUIREMENTS CHECK    │
                    │  - context-mcp recommend      │
                    │  - Check MCP_RECOMMENDATIONS │
                    └─────────┬─────────────────────┘
                              │
                    ┌─────────▼─────────────────────┐
                    │  📋 ROADMAP GENERATION PHASE  │
                    ├─────────────────────────────────┤
                    │ Claude analyzes:                │
                    │  - Project scope & complexity   │
                    │  - Optimal phase breakdown      │
                    │  - MCP recommendations per phase│
                    │  - Environment variables needed │
                    │                                 │
                    │ For Refactor/Retry:             │
                    │  - Analyzes existing codebase   │
                    │  - Creates detailed ANALYSIS.md │
                    │  - Confidence level assessment  │
                    │  - Preserves working components │
                    └─────────┬─────────────────────┘
                              │
                    ┌─────────▼─────────────────────┐
                    │  AUTO-PILOT PHASE EXECUTION   │
                    │  (context-auto or -git)       │
                    └─────────┬─────────────────────┘
                              │
        ┌─────────────────────┴─────────────────────┐
        │                                           │
┌───────▼────────────┐                    ┌─────────▼─────────────┐
│ LINEAR GIT MODE    │                    │ BRANCHING GIT MODE    │
│ (context-auto)     │                    │ (context-auto-git)    │
├────────────────────┤                    ├───────────────────────┤
│ For Phase N:       │                    │ For Phase N:          │
│                    │                    │                       │
│ → Phase start      │                    │ → planning/phase-N    │
│   commit           │                    │   └─ PRP generation   │
│ → PRP generated    │                    │                       │
│   commit           │                    │ → feature/phase-N     │
│ → Implementation   │                    │   └─ Implementation   │
│   commit           │                    │                       │
│ → Tests passing    │                    │ → test/phase-N        │
│   commit           │                    │   └─ Test fixes       │
│ → Phase validated  │                    │                       │
│   commit           │                    │ → Merge to main       │
└────────────────────┘                    └───────────────────────┘
                                                    │
                                          ┌─────────▼─────────────┐
                                          │ SUB-PHASE WORKFLOWS   │
                                          ├───────────────────────┤
                                          │ 1. MCP Activation     │
                                          │    mcp-phase activate │
                                          │ 2. API Key Injection  │
                                          │    mcp-inject         │
                                          │ 3. Environment Check  │
                                          │ 4. Implementation     │
                                          │ 5. Testing & Commit   │
                                          └───────────────────────┘
```

## Flow Descriptions

### Entry Points

1. **`context` / `ce` (Standard Mode)**
   - One-time project setup
   - Creates structure and initial files
   - User manually runs Claude commands
   - Good for: Single features, exploration

2. **`context-auto` / `cea` (Auto-Pilot Mode)**
   - Continuous development workflow
   - Linear commits on current branch
   - Auto-commits at each sub-phase
   - Good for: Complete projects, rapid development

3. **`context-auto-git` / `cea-git` (Git-Enhanced Mode)**
   - Full branching strategy
   - Separate planning/feature/test branches
   - Clean merge history
   - Good for: Team projects, production code

### Roadmap Generation Phase

All paths converge at roadmap generation where Claude:
- Analyzes project requirements
- Creates phase breakdown
- **Recommends MCPs for each phase**
- Generates comprehensive .env.example
- For refactor/retry: performs deep code analysis

### MCP Integration Points

```
┌─────────────────────────────────────────────────────────────────┐
│                    MCP ACTIVATION WORKFLOW                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. ROADMAP GENERATION                                          │
│     └─> Creates MCP_RECOMMENDATIONS.md                         │
│         └─> Lists phase-specific MCPs                          │
│                                                                 │
│  2. PHASE START                                                 │
│     └─> Check recommended MCPs                                 │
│         └─> Prompt: "Run mcp-phase activate research?"         │
│                                                                 │
│  3. MCP ACTIVATION                                              │
│     └─> mcp-phase activate <phase>                            │
│         └─> Creates .mcp/mcp.json with ${VARIABLES}           │
│                                                                 │
│  4. API KEY INJECTION                                           │
│     └─> mcp-inject                                            │
│         └─> SSH to workhorse, inject real keys                │
│                                                                 │
│  5. CLAUDE CODE RESTART                                         │
│     └─> MCPs loaded with enhanced capabilities                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Phase-Specific MCPs

**Research/Analysis Phase:**
- `omnisearch` - Web research
- `sequential-thinking` - Problem decomposition
- `memory` - Track findings
- `context7` - Library documentation

**Development Phase:**
- `context7` - API documentation
- `memory` - Decision tracking
- `github` - Version control
- `filesystem` - Enhanced file operations

**Testing Phase:**
- `memory` - Track test results
- Custom test runners
- Performance monitoring MCPs

### Git Commit Points

**Linear Mode (context-auto):**
- Phase start
- PRP generated
- PRP refined (if manual edits)
- Implementation complete
- Tests passing
- Tests fixed (if needed)
- Phase validated

**Branching Mode (context-auto-git):**
- Creates branches: planning/, feature/, test/
- Commits at same points but on branches
- Merges back to main with --no-ff
- Optional branch deletion

### Refactor/Retry Analysis

For existing projects, the tool now:
1. **Analyzes codebase** before roadmap
2. **Creates ANALYSIS.md** with:
   - Architecture assessment
   - Code quality metrics
   - Identified issues
   - Preservation recommendations
3. **Interactive questionnaire** for retry:
   - What worked well?
   - What failed?
   - Lessons learned?
4. **Confidence rating** in roadmap

### Security & API Keys

```
Mac Mini M4          10Gb Direct         AI Workhorse
(Development)  <-------------------->  (Secure Storage)
     │                                       │
     │ mcp-sync (configs only)              │
     └──────────────────────────────────────┘
     │                                       │
     │ mcp-inject (SSH for keys)            │
     └───────────────────────────────────────┘
```

API keys never stored locally, only injected at runtime.

### Session Persistence

The `.context-session` file tracks:
- Current phase
- Current step
- Git branch (if using git mode)
- Timestamp
- Project type

Allows resuming interrupted work with `--resume` flag.

## Related Documentation

- **[MCP Workflow Guide](docs/MCP_WORKFLOW_GUIDE.md)** - Detailed MCP architecture
- **[Git Workflow](docs/GIT_WORKFLOW.md)** - Branching strategies
- **[Secure MCP Setup](docs/SECURE_MCP_SETUP.md)** - API key management

## Quick Command Reference

**Project Creation:**
- `context` - Standard one-time setup
- `context-auto` - Auto-pilot with linear commits
- `context-auto-git` - Auto-pilot with branching

**MCP Management:**
- `context-mcp list` - Show available MCPs
- `mcp-phase activate <phase>` - Activate phase MCPs
- `mcp-inject` - Inject API keys from workhorse
- `mcp-sync` - Sync configs from workhorse

**Workflow Control:**
- `--resume` - Continue from last saved state
- `--status` - Show current progress
- `--help` - Show detailed help