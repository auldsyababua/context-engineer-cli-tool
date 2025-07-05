# Secure MCP Setup Guide

This guide explains how to set up secure API key management for MCPs (Model Context Protocol) using a dedicated server or secure workstation.

## Architecture Overview

```
Development Machine    Network Connection    Secure MCP Server
(Your Computer)     <-------------------->   (API Key Storage)
                         SSH + rsync        

• Project Development        • Master MCP Configurations
• MCP Phase Activation       • API Keys (Secure Storage)
• Template Storage           • Backup & Sync Service
```

## Benefits of This Approach

1. **Security**: API keys stored only on secure server
2. **Centralization**: One place to manage all API keys
3. **Sharing**: Multiple development machines can access same keys
4. **Backup**: Centralized backup of MCP configurations
5. **Audit**: Track API key usage and access

## Prerequisites

- A secure server or dedicated workstation (Linux/macOS)
- SSH key authentication between machines
- Network connectivity (local network recommended)
- Basic command line familiarity

## Setup Process

### 1. Configure Your Environment

Set these environment variables on your development machine:

```bash
# Add to ~/.zshrc or ~/.bashrc
export WORKHORSE_IP="your-server-ip"           # e.g., "192.168.1.100"
export WORKHORSE_USER="your-username"          # e.g., "mcpuser"
export MCP_MASTER_DIR="/path/to/mcp-master"    # e.g., "/home/mcpuser/mcp-master"
```

**Example configurations:**
- Local server: `WORKHORSE_IP="192.168.1.50"`
- Remote server: `WORKHORSE_IP="mcp-server.example.com"`
- Localhost: `WORKHORSE_IP="localhost"` (for single-machine setup)

### 2. Prepare the Secure Server

SSH to your designated MCP server:

```bash
ssh your-username@your-server-ip
```

Create the master directory structure:

```bash
mkdir -p ~/mcp-master/phase-configs
cd ~/mcp-master
```

### 3. Initialize Server Configuration

Run the setup script from your development machine:

```bash
mcp-workhorse-setup
```

This creates the basic structure on your server:
```
~/mcp-master/
├── api-keys.env              # Your API keys (secure)
├── mcp-config-master.json    # Master MCP definitions
└── phase-configs/            # Phase-specific configurations
    ├── research-phase.json
    ├── development-phase.json
    └── testing-phase.json
```

### 4. Add Your API Keys

SSH to your server and edit the API keys file:

```bash
ssh your-username@your-server-ip
nano ~/mcp-master/api-keys.env
```

Add your actual API keys:

```bash
# API Keys - KEEP SECURE!
TAVILY_API_KEY=tvly-your-actual-key-here
BRAVE_API_KEY=your-brave-api-key-here
CONTEXT7_API_KEY=your-context7-key-here
OPENAI_API_KEY=sk-your-openai-key-here
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_your-github-token
TODOIST_API_TOKEN=your-todoist-token
```

Secure the file:
```bash
chmod 600 api-keys.env
```

### 5. Configure Master MCP Definitions

Edit the master configuration:

```bash
nano ~/mcp-master/mcp-config-master.json
```

Example configuration:

```json
{
  "servers": {
    "omnisearch": {
      "command": "npx",
      "args": ["-y", "@copilotkit/mcp-omnisearch"],
      "env": {
        "TAVILY_API_KEY": "${TAVILY_API_KEY}",
        "BRAVE_API_KEY": "${BRAVE_API_KEY}",
        "KAGI_API_KEY": "${KAGI_API_KEY}",
        "FIRECRAWL_API_KEY": "${FIRECRAWL_API_KEY}"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "${CONTEXT7_API_KEY}"
      }
    },
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@copilotkit/mcp-sequential-thinking"]
    },
    "memory": {
      "command": "npx",
      "args": ["-y", "@copilotkit/mcp-memory"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@copilotkit/mcp-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

## Daily Workflow

### 1. Sync Configurations

Pull latest configurations from your server:

```bash
mcp-sync
```

This creates/updates:
- `~/.config/context-engineer/mcp/mcp-config.json` (template with `${VARIABLES}`)
- `~/.config/context-engineer/mcp/phase-configs/` (phase definitions)

### 2. Activate MCPs for Your Project

Choose MCPs for your current development phase:

```bash
# For research/analysis work
mcp-phase activate research

# For coding/implementation
mcp-phase activate development

# For testing phases
mcp-phase activate testing
```

### 3. Inject API Keys

Replace template variables with actual API keys:

```bash
mcp-inject
```

This process:
1. Connects to your server via SSH
2. Retrieves API keys securely
3. Replaces `${VARIABLES}` with actual values in `.mcp/mcp.json`
4. Never stores keys locally permanently

### 4. Restart Claude Desktop

MCPs are loaded at startup, so restart Claude Desktop after injection.

## Security Features

### 1. API Key Security

- **Server-only storage**: API keys never stored on development machines
- **SSH encryption**: Keys transferred via encrypted SSH connection
- **Temporary injection**: Keys only exist locally during active development
- **Automatic cleanup**: Can revert to template mode anytime

### 2. Network Security

- **Local network preferred**: Avoid exposing API keys over internet
- **SSH key authentication**: No password-based access
- **Firewall protection**: Restrict access to MCP server

### 3. Access Control

```bash
# Recommended server permissions
chmod 700 ~/mcp-master                    # Directory access
chmod 600 ~/mcp-master/api-keys.env       # API keys file
chmod 644 ~/mcp-master/mcp-config-master.json  # Configuration file
```

### 4. Git Safety

Your `.gitignore` automatically includes:

```gitignore
# MCP with injected keys
.mcp/mcp.json
.mcp/mcp.json.bak

# But allow the template
!.mcp/mcp.json.template

# Session files
.context-session
.current-phase
```

## Advanced Configuration

### Multiple Development Machines

Each development machine can access the same MCP server:

```bash
# Machine 1
export WORKHORSE_IP="shared-mcp-server.local"

# Machine 2
export WORKHORSE_IP="shared-mcp-server.local"

# Both use same API keys and configurations
```

### Environment-Specific Setups

```bash
# Development environment
export MCP_MASTER_DIR="/home/user/mcp-dev"

# Production environment
export MCP_MASTER_DIR="/home/user/mcp-prod"
```

### SSH Configuration

For easier access, add to `~/.ssh/config`:

```
Host mcp-server
    HostName 192.168.1.100
    User mcpuser
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 60
```

Then use:
```bash
export WORKHORSE_IP=mcp-server
```

## Troubleshooting

### Cannot Connect to Server

```bash
# Test SSH connectivity
ssh -o ConnectTimeout=5 $WORKHORSE_USER@$WORKHORSE_IP exit

# Check configuration
echo "Server: $WORKHORSE_IP"
echo "User: $WORKHORSE_USER"
echo "Directory: $MCP_MASTER_DIR"
```

### MCPs Not Working

```bash
# Check if keys were injected
grep -q '${' .mcp/mcp.json && echo "Template mode" || echo "Keys injected"

# Verify configuration
mcp-phase current

# Check Claude Desktop logs
tail -f ~/Library/Logs/Claude/claude.log
```

### Missing API Keys

```bash
# See what variables need values
mcp-inject  # Will show missing variables

# Add missing keys on server
ssh $WORKHORSE_USER@$WORKHORSE_IP
echo "NEW_API_KEY=value" >> ~/mcp-master/api-keys.env
```

## Backup and Recovery

### Regular Backups

```bash
# On your MCP server
cd ~
tar -czf mcp-backup-$(date +%Y%m%d).tar.gz mcp-master/
```

### Recovery Process

```bash
# Restore from backup
tar -xzf mcp-backup-YYYYMMDD.tar.gz

# Re-sync to development machines
mcp-sync
```

## Security Best Practices

1. **Regular key rotation**: Update API keys periodically
2. **Access logging**: Monitor SSH access to MCP server
3. **Network isolation**: Keep MCP server on secure network
4. **Backup encryption**: Encrypt backup files
5. **Principle of least privilege**: Only necessary access to API keys

## Getting Started Checklist

- [ ] Set up secure server or dedicated workstation
- [ ] Configure SSH key authentication
- [ ] Set environment variables on development machine
- [ ] Run `mcp-workhorse-setup`
- [ ] Add API keys to server
- [ ] Test with `mcp-sync`
- [ ] Try `mcp-inject` in a project
- [ ] Restart Claude Desktop and verify MCPs work

For detailed configuration examples, see [SETUP_EXAMPLES.md](SETUP_EXAMPLES.md).