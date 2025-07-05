# MCP Configuration Options

## Overview

This document explains different ways to configure MCP services for use with Context Engineer.

## Configuration Methods

### 1. Local MCPs (Recommended)

The simplest approach using npx to run MCPs locally:

```bash
# Set in .env
MCP_MODE=local

# Configure API keys in .env.mcp
cp .env.mcp.example .env.mcp
nano .env.mcp

# Generate configuration
./bin/generate-mcp-config
```

### 2. Docker-based MCPs

For better isolation and consistency:

```bash
# Set in .env
MCP_MODE=docker

# Coming soon - will provide docker-compose setup
```

### 3. System Services (Linux)

For production-like setup on Linux:

```bash
# Set in .env
MCP_MODE=systemd

# Advanced setup - see documentation
```

### 4. No MCPs

Context Engineer works fine without MCPs:

```bash
# Set in .env
MCP_MODE=none
```

## Migration from Previous Setups

If you were using a previous MCP setup:

1. **Backup your API keys** from any existing configuration
2. **Copy keys to .env.mcp** using the new format
3. **Generate new config** with `./bin/generate-mcp-config`
4. **Remove old configurations** after verifying the new setup works

## Recommended MCPs by Use Case

### For General Development
- GitHub - Repository access
- OmniSearch - Web search
- Context7 - Persistent memory

### For Research Projects
- OmniSearch - Research capabilities
- Sequential Thinking - Complex reasoning
- Context7 - Remember findings

### For Team Projects
- GitHub - Collaboration
- Context7 - Shared memory
- Custom MCPs - Team-specific tools

## Troubleshooting

### MCPs not showing in Claude Code
1. Ensure configuration was generated: `ls ~/.config/claude-code/mcp-config.json`
2. Restart Claude Code completely
3. Check for syntax errors in the config file

### API Key Issues
1. Verify keys in `.env.mcp` are correct
2. Check for extra spaces or quotes
3. Ensure keys have proper permissions

### Performance Issues
1. Consider using fewer MCPs
2. Use local mode instead of remote services
3. Check system resources

## Advanced Topics

### Custom MCP Development
See the MCP SDK documentation for creating custom MCPs.

### Enterprise Deployment
For organization-wide deployment, consider:
- Centralized API key management
- Shared MCP servers
- Custom security policies