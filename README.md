# Context Engineer CLI Tool

🚀 A CLI tool designed for Claude Code that structures AI-assisted development with clear phases, automated workflows, and optional MCP (Model Context Protocol) integration.

## ✨ Features

- **Interactive Setup Wizard**: Guided project creation with smart defaults
- **Auto-Pilot Mode**: Continuous development workflow with automatic progression
- **Git Safety Net**: Auto-commits after each step for easy rollback
- **Session Persistence**: Resume development anytime, even after restarts
- **Claude Code Integration**: Optimized prompts and workflows for Claude Code
- **Optional MCP Support**: Enhanced capabilities with GitHub, search, and context persistence
- **Customizable Templates**: Pre-configured files for different project types
- **Language Support**: Python, TypeScript, JavaScript, Go, and more
- **Best Practices**: Enforces code organization, testing, and documentation standards

## 🎯 What is Context Engineering?

Context Engineering is a methodology for building software with AI coding assistants. It provides:

1. **Structured Requirements** (INITIAL.md) - Clear feature descriptions
2. **AI Rules** (CLAUDE.md) - Project-specific coding standards
3. **Generated PRPs** - Comprehensive implementation blueprints
4. **Automated Execution** - AI implements features following the PRP

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone [repository-url] ~/Desktop/projects/context-engineer-cli-tool
cd ~/Desktop/projects/context-engineer-cli-tool

# Run the installer
./install.sh

# Reload your shell
source ~/.zshrc  # or ~/.bashrc
```

### Create Your First Project

#### Standard Mode (One-Time Setup)
```bash
# Run the CLI tool
context

# Or use the alias
ce
```

Follow the interactive prompts to:
1. Name your project
2. Choose project type (full/minimal/custom)
3. Select primary language
4. Pick testing framework
5. Describe your first feature

#### Auto-Pilot Mode (Continuous Development)
```bash
# Start auto-pilot mode
context-auto

# Or use the alias
cea
```

Auto-pilot mode features:
1. **First Run**: Generates complete project roadmap
2. **Continuous Flow**: Automatically progresses through phases
3. **Git Safety**: Auto-commits after each successful step
4. **Resume Anytime**: Pick up where you left off
5. **Simple Approval**: Just press Enter to continue

## 📁 What Gets Created

```
your-project/
├── .claude/
│   └── commands/
│       ├── generate-prp.md    # Generates implementation plans
│       └── execute-prp.md     # Executes implementations
├── .mcp/
│   └── mcp.json             # MCP server configuration
├── examples/
│   ├── README.md             # Example patterns guide
│   └── *.py/js/ts           # Language-specific examples
├── tests/                    # Test directory
├── docs/                     # Documentation
├── CLAUDE.md                 # AI coding rules
├── INITIAL.md               # Your feature description
├── PLANNING.md              # Architecture decisions
├── TASK.md                  # Task tracking
├── ROADMAP.md               # Phase-based development plan
├── README.md                # Project documentation
├── .env.example             # Environment template
└── .gitignore              # Standard ignores
```

## 🔄 Development Workflow

### Standard Workflow
1. **Setup Project**
   ```bash
   context  # Creates project structure
   ```

2. **In Claude Code**
   ```bash
   # Generate implementation plan
   /generate-prp INITIAL.md

   # Execute the plan
   /execute-prp PRPs/your-feature.md
   ```

3. **AI Does The Rest**
   - Reads all context
   - Creates implementation plan
   - Writes code following patterns
   - Runs tests until they pass

### Auto-Pilot Workflow
1. **Start Auto Mode**
   ```bash
   cea  # Starts or resumes auto-pilot
   ```

2. **First Time: Generate Roadmap**
   - Answer 3 questions (name, goal, phases)
   - Copy prompt to Claude Code
   - Press Enter when done

3. **For Each Phase**
   - Script shows phase goals
   - Copy `/generate-prp` command
   - Wait for completion
   - Copy `/execute-prp` command
   - Review and approve
   - Auto-commits on success

4. **If Something Goes Wrong**
   - Choose: Rollback, Continue, or Manual Fix
   - Resume anytime with `cea`

## 🔌 MCP (Model Context Protocol) Integration

MCPs enhance Claude's capabilities with external tools. The CLI tool includes:

### MCP Manager Tool
```bash
# List all available MCPs
context-mcp list

# Show details about a specific MCP
context-mcp show omnisearch

# Get configuration for enabling an MCP
context-mcp enable context7

# Check MCP status for current project
context-mcp status

# Get phase-specific recommendations
context-mcp recommend planning
```

### Pre-Configured MCPs

**Planning & Research**:
- **context7** - Up-to-date library documentation
- **omnisearch** - Advanced web search and content extraction
- **sequential-thinking** - Structured problem decomposition

**Development**:
- **memory** - Project context retention
- **github** - Repository operations
- **todoist** - Task management

### Phase-Aware Activation

Each phase's `INITIAL.md` includes recommended MCPs:

```markdown
## RECOMMENDED MCP SERVERS:
### Required MCPs:
- **context7**: For accessing React 18 documentation
- **memory**: To maintain context about component patterns

### Optional MCPs:
- **omnisearch**: If you need to research state management patterns
```

### Secure MCP Setup (Recommended)

Store API keys securely on your workhorse server:

```bash
# One-time setup on workhorse (192.168.86.210)
mcp-workhorse-setup

# Sync configurations to local
mcp-sync

# In your project, activate phase MCPs
mcp-phase activate research    # For planning/analysis
mcp-phase activate development # For coding
mcp-phase activate testing     # For testing

# Inject API keys from workhorse
mcp-inject

# Restart Claude Desktop
```

### Phase-Based Workflow

Different phases get different MCPs automatically:

- **Research Phase**: omnisearch, sequential-thinking, memory, context7
- **Development Phase**: context7, memory, github, filesystem  
- **Testing Phase**: memory, filesystem, test runners

### Quick MCP Commands

```bash
mcp-phase list       # Show available phases
mcp-phase current    # Show active MCPs
mcp-sync            # Sync from workhorse
mcp-inject          # Inject API keys
```

See [MCP Workflow Guide](docs/MCP_WORKFLOW_GUIDE.md) for detailed setup.

## 🎨 Customization

### Project Types

- **Full**: All templates and examples
- **Minimal**: Just CLAUDE.md and commands
- **Custom**: Choose specific files

### Supported Languages

- Python (with pytest, unittest, nose2)
- TypeScript/JavaScript (with Jest, Mocha, Vitest)
- Go
- Any other (specify custom)

### Templates

All templates use placeholder variables:
- `PROJECT_NAME` - Your project name
- `PRIMARY_LANGUAGE` - Selected language
- `TEST_FRAMEWORK` - Selected test framework
- `FILE_EXTENSION` - Language file extension

## 🛠️ Advanced Usage

### Custom Templates

Add your own templates to `templates/`:

```bash
# Add custom example
cp your-pattern.py templates/examples/

# It will be included in future projects
```

### Environment Variables

```bash
# Change default project directory
export CONTEXT_ENGINEER_PROJECTS_DIR="$HOME/my-projects"
```

## 📚 Examples

### Creating a Python Web Scraper

```bash
$ context
🚀 Welcome to Context Engineer CLI Tool!

What are we calling this project? awesome-scraper
Project type? 1 (Full)
Primary language? 1 (Python)
Testing framework? 1 (pytest)
First feature? Build an async web scraper for e-commerce sites

✅ Project created at: ~/Desktop/projects/awesome-scraper
```

### Creating a TypeScript API

```bash
$ ce  # Using the alias
What are we calling this project? user-api
Project type? 2 (Minimal)  
Primary language? 2 (TypeScript)
Testing framework? 1 (Jest)
First feature? REST API with user authentication

✅ Project created!
```

## 🤝 Contributing

1. Fork the repository
2. Add new templates or features
3. Submit a pull request

### Adding Language Support

1. Create example files in `templates/examples/`
2. Update the CLI script language selection
3. Add language-specific `.gitignore` entries

## 📄 License

MIT License - feel free to use for any project!

## 🙏 Credits & Acknowledgments

**Humbly forked from** the original Context Engineering methodology created by Cole Medin.

This CLI tool builds upon Cole's brilliant Context Engineering approach, adding:
- Auto-pilot mode for continuous development
- Session persistence and resumability  
- Git integration with auto-commits
- Interactive project setup wizard
- Multi-language support

### Contributing Back

We'd love to contribute these enhancements back to the original project! If you find these additions useful, we plan to submit a PR to Cole's repository to share these improvements with the wider community.

### Special Thanks

- **Cole Medin** - For creating the Context Engineering methodology and making it open source
- The Context Engineering community - For inspiration and feedback

---

**Happy Context Engineering! 🎉**