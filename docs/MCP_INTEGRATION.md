# MCP Integration Guide

## Overview

Context Engineer CLI Tool can integrate with MCP (Model Context Protocol) services to enhance Claude Code's capabilities. MCPs are optional but recommended for the best experience.

## What are MCPs?

MCPs provide Claude Code with additional capabilities like:
- **GitHub integration** - Direct repository access
- **Web search** - Research and documentation lookup
- **Persistent memory** - Context across sessions
- **File system access** - Read/write files directly

## Quick Setup

### 1. Configure API Keys

```bash
# Copy the example file
cp .env.mcp.example .env.mcp

# Edit with your API keys
nano .env.mcp  # or your preferred editor
```

### 2. Generate MCP Configuration

```bash
# Generate config for Claude Code
./bin/generate-mcp-config

# Config will be created at:
# ~/.config/claude-code/mcp-config.json
```

### 3. Restart Claude Code

After generating the configuration, restart Claude Code to load the new MCPs.

## Recommended MCPs

### Essential
1. **GitHub** - Repository integration
   - Get token at: https://github.com/settings/tokens/new
   - Scopes needed: `repo`, `read:org`

### Highly Recommended
2. **MCP-OmniSearch** - Unified web search
   - Supports multiple search providers
   - Free tier available via Brave Search API
   - Get Brave key at: https://brave.com/search/api/

3. **Context7** - Persistent memory
   - Sign up at: https://upstash.com
   - Create a Redis database
   - Copy the URL and token

4. **Sequential Thinking** - Advanced reasoning
   - No API key needed
   - Automatically included

## Environment Variables

### Basic Setup (.env)
```bash
# Project configuration
MCP_MODE=local  # Options: none, local, docker, systemd

# Editor preference
EDITOR=code  # or cursor, vim, etc.
```

### MCP API Keys (.env.mcp)
```bash
# GitHub
GITHUB_TOKEN=your-github-token

# Search (OmniSearch)
BRAVE_API_KEY=your-brave-key
# Optional additional search providers:
# KAGI_API_KEY=your-kagi-key
# PERPLEXITY_API_KEY=your-perplexity-key

# Memory (Context7)
UPSTASH_REDIS_URL=your-redis-url
UPSTASH_REDIS_TOKEN=your-redis-token
```

## MCP Modes

### 1. No MCPs (`MCP_MODE=none`)
- Simplest setup
- No additional configuration needed
- Context Engineer works fine without MCPs

### 2. Local MCPs (`MCP_MODE=local`)
- Uses npx to run MCPs locally
- Recommended for most users
- Requires Node.js 18+

### 3. Docker MCPs (`MCP_MODE=docker`)
- Better isolation
- Coming soon

### 4. Advanced Setup (`MCP_MODE=systemd`)
- For Linux users
- System-level services
- Best performance

## Phase-Based MCP Usage

Different project phases benefit from different MCPs:

### Planning/Research Phase
- **OmniSearch** - Research patterns and solutions
- **Sequential Thinking** - Complex reasoning
- **Context7** - Remember decisions

### Implementation Phase
- **GitHub** - Code repository access
- **Context7** - Maintain context
- **Filesystem** - Direct file manipulation

### Testing/Review Phase
- **GitHub** - PR and issue management
- **Sequential Thinking** - Test strategy
- **Context7** - Track test results

## Troubleshooting

### MCPs not working?
1. Check your API keys in `.env.mcp`
2. Regenerate config: `./bin/generate-mcp-config`
3. Restart Claude Code
4. Check logs: `~/.mcp/logs/`

### Which providers are free?
- **GitHub** - Free with account
- **Brave Search** - Free tier available
- **Sequential Thinking** - Always free
- **Filesystem/Memory** - Always free

### Can I use without MCPs?
Yes! Context Engineer works great without MCPs. They simply enhance the experience.

## Advanced Configuration

### Custom MCP Servers
You can add custom MCP servers by editing the generated config:

```json
{
  "mcpServers": {
    "custom-server": {
      "command": "node",
      "args": ["path/to/server.js"],
      "env": {
        "API_KEY": "your-key"
      }
    }
  }
}
```

### Project-Specific MCPs
Create `.env.mcp` in your project directory to override global settings.

## Security Notes

- Never commit `.env.mcp` files
- Use environment variables for all secrets
- Rotate API keys regularly
- Review MCP permissions