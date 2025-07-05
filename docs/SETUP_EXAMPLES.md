# Context Engineer MCP Setup Examples

This document provides configuration examples for setting up the MCP (Model Context Protocol) system with your own infrastructure.

## Configuration Methods

You can configure the MCP system in several ways:

### 1. Environment Variables

Set these in your shell profile (`~/.zshrc`, `~/.bashrc`):

```bash
export WORKHORSE_IP="your-server-ip"
export WORKHORSE_USER="your-username"
export MCP_MASTER_DIR="/path/to/mcp-master"
```

### 2. Configuration File

Create `~/.config/context-engineer/config.env`:

```bash
WORKHORSE_IP=192.168.1.100
WORKHORSE_USER=myuser
MCP_MASTER_DIR=/home/myuser/mcp-master
```

Then source it in the MCP scripts or your shell profile:
```bash
source ~/.config/context-engineer/config.env
```

## Setup Scenarios

### Scenario 1: Local Development (Single Machine)

**Configuration:**
```bash
WORKHORSE_IP=localhost
WORKHORSE_USER=$(whoami)
MCP_MASTER_DIR=$HOME/mcp-master
```

**Setup:**
1. All MCP configurations stored locally
2. No network setup required
3. API keys stored in `~/mcp-master/api-keys.env`

### Scenario 2: Dedicated MCP Server

**Configuration:**
```bash
WORKHORSE_IP=mcp-server.local
WORKHORSE_USER=mcpuser
MCP_MASTER_DIR=/opt/mcp-master
```

**Requirements:**
- SSH key authentication to your server
- Server accessible on your network
- Sufficient storage for MCP configurations

### Scenario 3: Home Lab Setup

**Configuration:**
```bash
WORKHORSE_IP=192.168.1.50
WORKHORSE_USER=labuser
MCP_MASTER_DIR=/home/labuser/mcp-configs
```

**Network Setup:**
- Ensure your development machine can reach the lab server
- Consider using SSH config for easy access

## Initial Setup Process

### 1. Prepare Your Server

```bash
# SSH to your chosen server
ssh your-user@your-server

# Create the master directory
mkdir -p /path/to/mcp-master/phase-configs

# Set up basic structure
cd /path/to/mcp-master
```

### 2. Create Master Configuration

Create `mcp-config-master.json` with your MCP definitions:

```json
{
  "servers": {
    "omnisearch": {
      "command": "npx",
      "args": ["-y", "@copilotkit/mcp-omnisearch"],
      "env": {
        "TAVILY_API_KEY": "${TAVILY_API_KEY}",
        "BRAVE_API_KEY": "${BRAVE_API_KEY}"
      }
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"],
      "env": {
        "CONTEXT7_API_KEY": "${CONTEXT7_API_KEY}"
      }
    }
  }
}
```

### 3. Create API Keys File

Create `api-keys.env` with your actual API keys:

```bash
# api-keys.env - KEEP THIS SECURE!
TAVILY_API_KEY=tvly-your-actual-key-here
BRAVE_API_KEY=your-brave-api-key-here
CONTEXT7_API_KEY=your-context7-key-here
OPENAI_API_KEY=sk-your-openai-key-here
```

**Security Note:** This file contains sensitive information. Ensure proper file permissions:
```bash
chmod 600 api-keys.env
```

### 4. Set Up Phase Configurations

Create phase-specific MCP configurations in `phase-configs/`:

**research-phase.json:**
```json
{
  "name": "Research & Analysis Phase",
  "description": "MCPs for research and problem analysis",
  "mcps": ["omnisearch", "sequential-thinking", "memory", "context7"],
  "rationale": {
    "omnisearch": "Web research and information gathering",
    "sequential-thinking": "Structured problem decomposition",
    "memory": "Track research findings and decisions",
    "context7": "Access to up-to-date library documentation"
  }
}
```

**development-phase.json:**
```json
{
  "name": "Development Phase",
  "description": "MCPs for coding and implementation",
  "mcps": ["context7", "memory", "github", "filesystem"],
  "rationale": {
    "context7": "API documentation and examples",
    "memory": "Maintain implementation context",
    "github": "Version control operations",
    "filesystem": "Enhanced file operations"
  }
}
```

## SSH Configuration

For easier access, set up SSH config in `~/.ssh/config`:

```
Host mcp-server
    HostName your-server-ip
    User your-username
    IdentityFile ~/.ssh/id_rsa
    ServerAliveInterval 60
```

Then you can use:
```bash
export WORKHORSE_IP=mcp-server
export WORKHORSE_USER=your-username
```

## Security Best Practices

### 1. Network Security
- Use SSH key authentication (no passwords)
- Consider VPN for remote access
- Firewall rules to restrict access

### 2. File Permissions
```bash
# Secure the master directory
chmod 700 /path/to/mcp-master
chmod 600 /path/to/mcp-master/api-keys.env
```

### 3. Backup Strategy
```bash
# Regular backups of your MCP configurations
tar -czf mcp-backup-$(date +%Y%m%d).tar.gz /path/to/mcp-master
```

### 4. API Key Rotation
- Regularly rotate API keys
- Update `api-keys.env` on your server
- Test with `mcp-inject` after updates

## Troubleshooting

### Connection Issues
```bash
# Test SSH connectivity
ssh -o ConnectTimeout=5 your-user@your-server exit

# Test MCP sync
mcp-sync
```

### Configuration Issues
```bash
# Check current configuration
echo "IP: $WORKHORSE_IP"
echo "User: $WORKHORSE_USER" 
echo "Dir: $MCP_MASTER_DIR"

# Verify master directory exists
ssh $WORKHORSE_USER@$WORKHORSE_IP "ls -la $MCP_MASTER_DIR"
```

### Permission Issues
```bash
# Fix common permission problems
ssh $WORKHORSE_USER@$WORKHORSE_IP "chmod 700 $MCP_MASTER_DIR && chmod 600 $MCP_MASTER_DIR/api-keys.env"
```

## Advanced Configurations

### Multiple Environments

You can set up different configurations for different projects:

```bash
# Development environment
export MCP_ENV=dev
export WORKHORSE_IP=dev-server.local

# Production environment  
export MCP_ENV=prod
export WORKHORSE_IP=prod-server.local
```

### Load Balancing

For high availability, you can set up multiple MCP servers:

```bash
# Primary server
WORKHORSE_IP=mcp-primary.local

# Fallback servers in scripts
WORKHORSE_FALLBACK_IPS=("mcp-backup1.local" "mcp-backup2.local")
```

## Getting Help

If you encounter issues:

1. Check the configuration variables are set correctly
2. Verify SSH connectivity to your server
3. Ensure the MCP master directory exists and has proper permissions
4. Check the Context Engineer documentation for additional troubleshooting

For more advanced setups, consider:
- Docker containers for MCP servers
- Kubernetes deployments for scalability
- Configuration management tools (Ansible, etc.)