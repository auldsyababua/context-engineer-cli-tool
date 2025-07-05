# Complete MCP Workflow Guide

## Overview

This guide explains the complete workflow for using MCPs (Model Context Protocol) with the Context Engineer CLI Tool, including secure API key management via your workhorse server.

**Note**: This document focuses on the MCP subsystem. For the overall Context Engineer workflow, see [FLOW_DIAGRAM.md](../FLOW_DIAGRAM.md).

## Architecture

```
┌─────────────────────────────────┐     10Gb Direct Link     ┌─────────────────────────────────┐
│      Development Machine        │◄────────────────────────►│      Secure MCP Server          │
│     (Your Computer)             │    Network Connection     │    (Your Server)                │
│                                 │◄────────────────────────►│                                 │
│ • Claude Code Development       │       SSH + rsync         │                                 │
│ • Project Work                  │                           │ • Master MCP Configurations     │
│ • MCP Phase Activation          │                           │ • API Keys (Secure Storage)     │
│ • Template Storage              │                           │ • ~/.config/mcp/.env.new        │
└─────────────────────────────────┘                           └─────────────────────────────────┘
              │                                                              │
              │ mcp-sync                                                     │
              │ (pulls configs)                                              │
              │                                                              │
              ▼                                                              │
┌─────────────────────────────────┐                                         │
│   Local MCP Configuration       │                                         │
│ ~/.config/context-engineer/mcp/ │                                         │
│                                 │                                         │
│ • mcp-config.json (templates)   │                                         │
│ • phase-configs/                │◄────────────────────────────────────────┘
│   - research-phase.json         │         mcp-inject
│   - development-phase.json      │         (injects API keys)
│   - testing-phase.json          │
└─────────────────────────────────┘
              │
              │ mcp-phase activate
              │
              ▼
┌─────────────────────────────────┐
│      Project Directory          │
│    ~/Desktop/projects/T2T3/     │
│                                 │
│ • .mcp/mcp.json                 │ ← Contains active MCPs with injected keys
│ • .mcp/mcp.json.template        │ ← Backup with ${VARIABLES}
│ • .mcp/current-phase            │ ← Tracks active phase
│ • Claude Code has access to:    │
│   - omnisearch                  │
│   - sequential-thinking         │
│   - memory                      │
│   - context7                    │
└─────────────────────────────────┘

Network Note: Replace connection details with your actual network setup
```

## Data Flow

```
1. SYNC PHASE (mcp-sync)
   ┌──────────────┐         SSH/rsync          ┌──────────────┐
   │  Workhorse   │ ─────────────────────────► │   Mac Mini   │
   │              │                             │              │
   │ Master Files │                             │ Local Config │
   │ • mcp-config │ ───► (strips API keys) ───►│ • templates  │
   │ • phase defs │ ─────────────────────────► │ • phase defs │
   └──────────────┘                             └──────────────┘

2. ACTIVATION PHASE (mcp-phase activate)
   ┌──────────────┐         Reads from          ┌──────────────┐
   │ Local Config │ ─────────────────────────► │   Project    │
   │              │                             │   .mcp/      │
   │ Phase Config │ ───► (selects MCPs) ─────► │ mcp.json     │
   │ + Templates  │      (creates config)       │ (${VARS})    │
   └──────────────┘                             └──────────────┘

3. INJECTION PHASE (mcp-inject)
   ┌──────────────┐         SSH (secure)        ┌──────────────┐
   │  Workhorse   │ ─────────────────────────► │   Project    │
   │              │                             │   .mcp/      │
   │ api-keys.env │ ───► (envsubst) ─────────► │ mcp.json     │
   │ (real keys)  │      (replaces ${VARS})    │ (real keys)  │
   └──────────────┘                             └──────────────┘

4. USAGE PHASE
   ┌──────────────┐         Reads MCPs          ┌──────────────┐
   │ Claude Code  │ ◄────────────────────────── │   Project    │
   │              │                             │   .mcp/      │
   │ • omnisearch │ ◄── (loads at startup) ◄── │ mcp.json     │
   │ • memory     │                             │              │
   │ • etc...     │                             │              │
   └──────────────┘                             └──────────────┘
```

## Initial Setup (One Time)

### 1. Setup Workhorse Storage

```bash
# Run initial setup script
mcp-workhorse-setup

# This creates on workhorse:
# ~/mcp-master/
# ├── api-keys.env           # Your API keys
# ├── mcp-config-master.json # Master MCP definitions
# └── phase-configs/         # Phase configurations
```

### 2. Add Your API Keys

```bash
# SSH to your server and edit keys
ssh your-user@your-server-ip
nano ~/mcp-master/api-keys.env

# Add your actual API keys:
TAVILY_API_KEY=tvly-your-actual-key
BRAVE_API_KEY=your-actual-key
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your-token
# etc...
```

### 3. Sync to Local Machine

```bash
# Pull configurations (without API keys)
mcp-sync

# This creates/updates:
# ~/.config/context-engineer/mcp/
# ├── mcp-config.json  # Template with ${VARIABLES}
# └── phase-configs/   # Phase definitions
```

## Project Workflow

### 1. Create New Project

```bash
# Create project with context-engineer
context

# Or use auto-pilot mode
context-auto
```

### 2. Check MCP Recommendations

After generating your roadmap, check if any MCPs were recommended:

```bash
# If MCP_RECOMMENDATIONS.md exists
cat MCP_RECOMMENDATIONS.md

# Add new MCPs to catalog if needed
context-mcp enable <new-mcp>
```

### 3. Activate Phase MCPs

```bash
# List available phases
mcp-phase list

# Activate MCPs for current phase
mcp-phase activate research    # For analysis/planning
mcp-phase activate development # For coding
mcp-phase activate testing     # For testing

# Check what's active
mcp-phase current
```

### 4. Inject API Keys

```bash
# Inject keys from workhorse into mcp.json
mcp-inject

# This:
# 1. Connects to workhorse via SSH
# 2. Retrieves api-keys.env securely
# 3. Replaces ${VARIABLES} with actual keys
# 4. Never stores keys locally
```

### 5. Restart Claude Desktop

MCPs are loaded at startup, so restart Claude Desktop after changes.

## Phase-Based Workflow

### Research & Analysis Phase
```bash
mcp-phase activate research
mcp-inject
# Restart Claude Desktop

# You now have:
# - omnisearch: Web research
# - sequential-thinking: Problem decomposition
# - memory: Track findings
# - context7: Library documentation
```

### Development Phase
```bash
mcp-phase activate development
mcp-inject
# Restart Claude Desktop

# You now have:
# - context7: API docs
# - memory: Decision tracking
# - github: Version control
# - filesystem: File operations
```

### Testing Phase
```bash
mcp-phase activate testing
mcp-inject
# Restart Claude Desktop

# You now have:
# - memory: Track test results
# - filesystem: Test file access
# - Custom test runners (if configured)
```

## Security Best Practices

### 1. API Key Security
- **Never** commit api-keys.env or injected mcp.json
- Keep master keys only on workhorse
- Use 10Gb direct connection (no internet exposure)
- SSH key auth only (no passwords)

### 2. Git Safety
Already configured in .gitignore:
```
# MCP with injected keys
.mcp/mcp.json
.mcp/mcp.json.bak

# But allow the template
!.mcp/mcp.json.template
```

### 3. Temporary Keys
```bash
# After using MCPs, optionally revert to template
cp .mcp/mcp.json.template .mcp/mcp.json

# Keys were only in memory during injection
```

## Troubleshooting

### Can't Connect to Workhorse
```bash
# Check connectivity
ping your-server-ip

# Check SSH
ssh your-user@your-server-ip echo "Connected"

# Ensure on same network (wired preferred)
```

### MCPs Not Working
```bash
# Check current configuration
mcp-phase current

# Verify mcp.json has real keys
grep -q '${' .mcp/mcp.json && echo "Template mode" || echo "Keys injected"

# Check Claude logs
tail -f ~/Library/Logs/Claude/claude.log
```

### Missing API Keys
```bash
# See what's missing
mcp-inject  # Will show missing variables

# Add to your server
ssh your-user@your-server-ip
echo "NEW_API_KEY=value" >> ~/mcp-master/api-keys.env
```

## Advanced Usage

### Custom Phase Configuration
Create `.mcp/phase-configs/custom-phase.json`:
```json
{
  "name": "Custom Analysis Phase",
  "description": "Special MCPs for my use case",
  "mcps": ["omnisearch", "github", "my-custom-mcp"],
  "rationale": {
    "omnisearch": "Research competitors",
    "github": "Analyze similar repos",
    "my-custom-mcp": "Special functionality"
  }
}
```

Then activate:
```bash
mcp-phase activate custom
```

### Adding New MCPs
1. Edit master config on workhorse:
```bash
ssh your-user@your-server-ip
nano ~/mcp-master/mcp-config-master.json
```

2. Add new MCP definition:
```json
"new-mcp": {
  "command": "npx",
  "args": ["-y", "@org/new-mcp-server"],
  "env": {
    "NEW_MCP_API_KEY": "${NEW_MCP_API_KEY}"
  }
}
```

3. Add API key:
```bash
echo "NEW_MCP_API_KEY=xxx" >> ~/mcp-master/api-keys.env
```

4. Sync and use:
```bash
mcp-sync
mcp-phase activate development  # If added to phase
mcp-inject
```

## Quick Reference

### Essential Commands
- `mcp-sync` - Pull latest configs from workhorse
- `mcp-inject` - Inject API keys into current project
- `mcp-phase activate <phase>` - Enable phase-specific MCPs
- `mcp-phase current` - Show active MCPs

### SSH Shortcuts (add to ~/.zshrc)
```bash
alias mcp-edit="ssh your-user@your-server-ip nano ~/mcp-master/mcp-config-master.json"
alias mcp-keys="ssh your-user@your-server-ip nano ~/mcp-master/api-keys.env"
```

### Emergency Fallback
If your MCP server is down:
1. Keep using template mode (${VARIABLES})
2. Set keys in shell: `export TAVILY_API_KEY=xxx`
3. Or create temporary local .env

## Integration with Context-Auto

The `context-auto` command automatically:
1. Detects recommended MCPs in roadmap
2. Prompts for phase activation
3. Reminds about API key configuration
4. Suggests mcp-inject when needed

This creates a seamless workflow from project creation through all development phases.