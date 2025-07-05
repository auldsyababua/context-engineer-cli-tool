# MCP (Model Context Protocol) Setup Guide

## What are MCPs?

MCP servers enhance Claude's capabilities by providing access to external tools and services. Think of them as plugins that give Claude superpowers for specific tasks.

## Quick Start

1. **Check your `.mcp/mcp.json`** - MCPs are pre-configured but commented out
2. **Uncomment the MCPs you need** for your current phase
3. **Add API keys to `.env`** if required (see each MCP's config)
4. **Restart Claude Code** to activate the MCPs

## Core MCPs for Context Engineering

### 🧠 Planning & Research Phase

```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@context-labs/context-mcp"]
  },
  "omnisearch": {
    "command": "npx",
    "args": ["-y", "@neomantra/mcp-omnisearch"],
    "env": {
      "TAVILY_API_KEY": "${TAVILY_API_KEY}"
    }
  },
  "sequential-thinking": {
    "command": "npx",
    "args": ["-y", "mcp-sequentialthinking-tools"]
  }
}
```

**Why these?**
- **context7**: Get current library docs (not limited by training cutoff)
- **omnisearch**: Research patterns and find solutions
- **sequential-thinking**: Break down complex problems systematically

### 💻 Development Phase

```json
{
  "memory": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-memory"]
  },
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
    }
  }
}
```

**Why these?**
- **memory**: Keep track of decisions and project context
- **github**: Create PRs, manage issues, search code

## Environment Variables

Add to your `.env` file:

```env
# MCP API Keys
# ============================================

# Omnisearch - At least one search API
TAVILY_API_KEY=tvly-...          # Get from: https://app.tavily.com/
# BRAVE_API_KEY=...              # Alternative: https://brave.com/search/api/

# GitHub Integration  
GITHUB_PERSONAL_ACCESS_TOKEN=ghp_...  # Create at: https://github.com/settings/tokens
```

## Phase-Specific Recommendations

### Phase 1-2: Foundation
- ✅ context7 (for framework docs)
- ✅ sequential-thinking (for planning)
- ✅ memory (start building context)

### Phase 3-5: Core Development  
- ✅ context7 (for API docs)
- ✅ memory (maintain context)
- ✅ github (version control)
- ⚡ omnisearch (when stuck)

### Phase 6+: Integration & Polish
- ✅ github (PRs and releases)
- ✅ memory (accumulated knowledge)
- ⚡ omnisearch (optimization research)

## Performance Tips

1. **Don't enable all MCPs** - More MCPs = slower startup
2. **Phase-appropriate** - Only enable what you need now
3. **API keys** - Some MCPs work without keys but with limitations

## Troubleshooting

**MCPs not working?**
1. Check if uncommented in `.mcp/mcp.json`
2. Verify API keys in `.env`
3. Restart Claude Code completely
4. Check Claude Code logs for errors

**Which MCPs do I need?**
- Look at your current phase's INITIAL.md
- Planning/research → context7, omnisearch, sequential-thinking
- Implementation → context7, memory, github
- Always useful → memory (for context retention)

## Security Notes

- Never commit `.env` with real API keys
- Use `.env.example` for key templates
- Rotate API keys periodically
- Use minimal token permissions