# Context Engineer CLI Tool - Architecture

## Overview

The Context Engineer CLI Tool combines structured project setup with AI-enhanced development through MCP (Model Context Protocol) servers. This document explains how the components work together.

## System Components

### 1. CLI Tools

#### `context` (Standard Mode)
- Interactive project setup wizard
- One-time execution
- Creates project structure with templates
- Generates initial feature description

#### `context-auto` (Auto-Pilot Mode)
- Continuous development workflow
- Session persistence via `.context-session`
- Phase-based progression
- Automatic git commits for safety
- Resume capability

#### `context-mcp` (MCP Manager)
- Lists available MCP servers
- Shows MCP details and requirements
- Generates configuration snippets
- Checks project MCP status
- Provides phase-specific recommendations

### 2. Template System

```
templates/
├── CLAUDE.md              # AI behavior rules template
├── ROADMAP.md             # Phase-based roadmap template
├── PLANNING.md            # Architecture planning template
├── TASK.md                # Task tracking template
├── MCP_SETUP.md           # MCP setup guide
├── .claude/               # Claude Code commands
├── .mcp/                  # MCP configuration
├── examples/              # Code pattern examples
└── phase-template/        # Phase structure template
```

### 3. MCP Integration

#### MCP Catalog Structure
```
mcp-catalog/
├── README.md              # MCP overview and guidelines
├── context7.json          # Library documentation MCP
├── omnisearch.json        # Web search MCP
├── sequential-thinking.json # Problem decomposition MCP
├── memory.json            # Context retention MCP
└── github.json            # Repository operations MCP
```

#### MCP Configuration Flow
1. **Phase Planning** → Roadmap includes MCP recommendations
2. **Phase INITIAL.md** → Lists required and optional MCPs
3. **Developer enables MCPs** → Using `context-mcp enable`
4. **Configuration added** → To `.mcp/mcp.json`
5. **API keys added** → To `.env` file
6. **Claude restarts** → MCPs become available

## Workflow Architecture

### Standard Workflow
```
User → context → Project Setup → INITIAL.md → Claude Code
                                               ↓
                                          /generate-prp
                                               ↓
                                          /execute-prp
```

### Auto-Pilot Workflow
```
User → context-auto → Check Session → Generate Roadmap
         ↓                               ↓
    Resume/New                     Phase Structure
         ↓                               ↓
    Execute Phases ←─────────────────────┘
         ↓
    Auto-commit → Next Phase
```

### MCP-Enhanced Workflow
```
Phase Requirements → Recommended MCPs → context-mcp enable
                                              ↓
                                         Configure MCPs
                                              ↓
                                         Add API Keys
                                              ↓
                                     Claude with Enhanced Tools
```

## Phase-Based Development

### Phase Structure
Each phase contains:
- `INITIAL.md` - Feature description with MCP recommendations
- `SUCCESS_CRITERIA.md` - Completion requirements

### MCP Alignment
- **Planning Phases**: context7, omnisearch, sequential-thinking
- **Development Phases**: memory, github, context7
- **Integration Phases**: github, todoist

### Environment Management
```env
# Phase 1: Basic Setup
LOG_LEVEL=debug

# Phase 2: Database Integration
DATABASE_URL=...

# Phase 3: External APIs
OPENAI_API_KEY=...

# MCP Configuration
TAVILY_API_KEY=...
GITHUB_PERSONAL_ACCESS_TOKEN=...
```

## Session Persistence

### Session State File
```bash
# .context-session
CURRENT_PHASE="3"
CURRENT_STEP="execute-prp"
STATUS="in-progress"
TIMESTAMP="2024-01-15_10:30:00"
PROJECT_PATH="/path/to/project"
PROJECT_TYPE="1"
```

### Git Safety Net
- Auto-commit after each successful step
- Rollback capability on failures
- Clear commit messages with phase context

## Security Considerations

### Environment Variables
- Never committed (via .gitignore)
- Template provided (.env.example)
- Phase-aware organization
- MCP keys clearly documented

### MCP Security
- API keys in environment only
- Minimal token permissions
- Regular rotation reminders
- No keys in MCP config files

## Extension Points

### Adding New MCPs
1. Create JSON config in `mcp-catalog/`
2. Include in phase recommendations
3. Document in MCP_SETUP.md

### Adding Templates
1. Add to `templates/` directory
2. Update copy logic in CLI scripts
3. Include placeholders for customization

### Custom Phases
1. Modify roadmap generation prompt
2. Update phase template structure
3. Align MCP recommendations

## Best Practices

### For Users
1. Start with minimal MCPs
2. Enable phase-appropriate tools
3. Keep API keys secure
4. Commit after each phase

### For Development
1. MCPs enhance, don't replace core functionality
2. Phase progression should be incremental
3. Each phase delivers working features
4. Context builds cumulatively

## Future Enhancements

### Planned Features
- Automatic MCP enable/disable per phase
- MCP performance monitoring
- Custom MCP development guide
- Team collaboration features

### Integration Opportunities
- CI/CD pipeline generation
- Cloud deployment templates
- Testing automation
- Documentation generation

This architecture enables AI-assisted development that grows more capable with each phase while maintaining safety and control throughout the process.