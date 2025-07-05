# MCP Configuration System

## Overview

The Context Engineer MCP system now supports:
1. **Phase-based MCP activation** - Different MCPs for different phases
2. **Automatic API key injection** - From .env to mcp.json
3. **Agent personas** - Different configurations for different tasks

## How It Works

### 1. Master Configuration
All available MCPs are defined in `.mcp/mcp-config.json` with their full configurations, including environment variable placeholders:

```json
{
  "available_mcps": {
    "omnisearch": {
      "command": "npx",
      "args": ["-y", "@neomantra/mcp-omnisearch"],
      "env": {
        "TAVILY_API_KEY": "${TAVILY_API_KEY}",
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    }
  }
}
```

### 2. Phase Configurations
Each phase has its own configuration in `.mcp/phase-configs/`:

```json
{
  "name": "Research & Analysis Phase",
  "mcps": ["omnisearch", "sequential-thinking", "memory"],
  "rationale": {
    "omnisearch": "Research patterns and solutions"
  }
}
```

### 3. Environment Variables
All API keys live in `.env`:

```env
# MCP API Keys
TAVILY_API_KEY=tvly-xxx
BRAVE_API_KEY=xxx
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_xxx
TODOIST_API_TOKEN=xxx
```

### 4. Activation
Use the `mcp-phase` command to activate MCPs for a phase:

```bash
# List available phases
mcp-phase list

# Activate research phase MCPs
mcp-phase activate research

# Show current MCPs
mcp-phase current
```

## Setting Up Your Project

### Step 1: Global MCP Config (One Time)

Create `~/.config/context-engineer/mcp/` with your master configs:

```bash
mkdir -p ~/.config/context-engineer/mcp/phase-configs
cp mcp-catalog/* ~/.config/context-engineer/mcp/
```

### Step 2: Project Setup

In your project:

```bash
# Copy templates
cp -r templates/.mcp .mcp

# Add your API keys to .env
echo "TAVILY_API_KEY=your-key" >> .env
echo "GITHUB_PERSONAL_ACCESS_TOKEN=your-token" >> .env
```

### Step 3: Phase Activation

When starting a phase:

```bash
# For research/analysis phase
mcp-phase activate research

# For development phase
mcp-phase activate development

# Restart Claude Code
```

## Agent Personas

Different agent personas can be created by combining:
1. Phase-specific MCPs
2. Custom Claude settings
3. Specific prompts in CLAUDE.md

### Research Agent
```bash
mcp-phase activate research
# Gets: omnisearch, sequential-thinking, memory, context7
```

### Development Agent
```bash
mcp-phase activate development
# Gets: context7, memory, github, filesystem
```

### Testing Agent
```bash
mcp-phase activate testing
# Gets: memory, filesystem, test runners
```

## Advanced: Custom Phase Configs

Create your own phase in `.mcp/phase-configs/custom-phase.json`:

```json
{
  "name": "Custom Analysis Phase",
  "description": "Special MCPs for my use case",
  "mcps": ["omnisearch", "github", "custom-mcp"],
  "rationale": {
    "omnisearch": "Research competitor implementations",
    "github": "Analyze similar repos"
  }
}
```

Then activate:
```bash
mcp-phase activate custom
```

## Automatic Phase Detection

Future enhancement: The system could automatically activate MCPs based on:
- Current phase number from roadmap
- Task type from INITIAL.md
- Git branch name conventions

## Best Practices

1. **Don't activate all MCPs** - Only what you need for the phase
2. **Keep API keys in .env** - Never in mcp.json
3. **Use phase activation** - Cleaner than manual editing
4. **Document custom phases** - So team knows what's available
5. **Restart Claude after changes** - MCPs load at startup

## Troubleshooting

### MCPs not working?
```bash
# Check current config
mcp-phase current

# Verify API keys
grep "API_KEY" .env

# Check Claude logs
tail -f ~/Library/Logs/Claude/claude.log
```

### Need to debug?
```bash
# See generated mcp.json
cat .mcp/mcp.json | jq .

# Test MCP directly
npx -y @modelcontextprotocol/server-omnisearch
```