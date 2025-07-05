# Quick Start Guide - Context Engineer with Claude Code

This guide will get you up and running with Context Engineer and Claude Code in minutes.

## Prerequisites

- Claude Code installed
- Git installed
- Node.js 18+ (only if using MCPs)

## Installation

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/context-engineer-cli-tool
cd context-engineer-cli-tool

# Run setup
./setup.sh
```

### 2. Choose Your Setup Mode

The setup script will ask about MCP (Model Context Protocol) services:

- **No MCPs** - Simplest setup, Context Engineer works fine without them
- **Local MCPs** - Enhanced features like GitHub integration and web search
- **Docker MCPs** - Coming soon, better isolation
- **Systemd MCPs** - Advanced Linux setup

For most users, we recommend either "Local MCPs" unless you have a linux machine, then we recommend "Systemd MCPs".

### 3. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit with your preferences
nano .env  # or use your favorite editor
```

Key settings:
- `MCP_MODE` - Set to `none` or `local`
- `EDITOR` - Your preferred editor (code, cursor, vim, etc.)
- `GIT_DEFAULT_BRANCH` - Usually `main`

### 4. (Optional) Setup MCPs

If you chose `local` mode and want enhanced features:

```bash
# Copy MCP template
cp .env.mcp.example .env.mcp

# Add your API keys
nano .env.mcp
```

### Recommended MCPs

We recommend installing these MCPs for the best experience:

1. **GitHub** - Essential for repository context
   - Get token at https://github.com/settings/tokens/new
   - Scopes needed: `repo`, `read:org`

2. **MCP-OmniSearch** - Unified search across multiple providers
   - Supports Brave, Kagi, Perplexity, Tavily, and more
   - You can use just one provider (e.g., only Brave's free tier)
   - Get Brave API key at https://brave.com/search/api/
   - Other providers optional but enhance search capabilities

3. **Context7** - Persistent memory across sessions
   - Sign up at https://upstash.com
   - Create a Redis database

4. **Sequential Thinking** - Advanced reasoning
   - No API key needed

## Using with Claude Code

### Basic Workflow

1. **Create a new project:**
   ```bash
   ce  # or 'context'
   ```

2. **Follow the interactive prompts:**
   - Choose project type
   - Enter project details
   - Select features

3. **Copy the generated prompt to Claude Code**
   - The tool will show you exactly what to paste
   - Claude Code will understand the project structure

4. **Use Auto-Pilot Mode (recommended):**
   ```bash
   cea  # or 'context-auto'
   ```
   - Automatically progresses through development phases
   - Shows you what to paste to Claude Code at each step
   - Commits changes automatically

### Example Session

```bash
$ ce
🚀 Welcome to Context Engineer!

What type of project? [1-5]: 1
Project name: my-awesome-api
Description: A REST API for managing todos
Language: python

✅ Created project structure at: ./my-awesome-api

Now paste this to Claude Code:
----------------------------------------
[Generated prompt with full context]
----------------------------------------
```

### Auto-Pilot Mode

```bash
$ cd my-awesome-api
$ cea

🚀 PHASE: Planning
Show this to Claude Code...

[Claude implements]

✅ Phase complete! Auto-committed.

🚀 PHASE: Core Implementation
Show this to Claude Code...

[Continues through all phases]
```

## MCP Integration (Optional)

If you enabled MCPs, Context Engineer will automatically:

1. **Detect project needs** - Knows when you need search, GitHub, etc.
2. **Include MCP hints** - Tells Claude Code which tools are available
3. **Manage access** - Only shows relevant MCPs for each phase

### Without MCPs
Claude Code works great with just the structured prompts.

### With MCPs
Claude Code can:
- Search the web (with OmniSearch)
- Access GitHub directly
- Maintain context between sessions
- Use advanced reasoning tools

## Tips for Success

1. **Start simple** - Try without MCPs first
2. **Use Auto-Pilot** - It handles the workflow for you
3. **Trust the process** - Let Claude Code follow the phases
4. **Commit often** - Auto-pilot does this automatically

## Troubleshooting

### "Command not found"
Add to your PATH:
```bash
export PATH="$PWD/bin:$PATH"
```

Or use full paths:
```bash
./bin/context
./bin/context-auto
```

### MCP Issues
- MCPs are optional - Context Engineer works without them
- Check your API keys in `.env.mcp`
- See logs in `~/.mcp/logs/`

### Claude Code Integration
- Make sure you're using the latest Claude Code
- Copy the entire prompt, including the context section
- Let Claude Code see the project structure

## Next Steps

- Read the [Full Documentation](../README.md)
- Learn about [MCP Integration](MCP_INTEGRATION.md)
- See [Example Projects](EXAMPLES.md)
- Join our community!

Remember: Context Engineer is designed to make Claude Code more powerful and structured. The magic happens when you combine the tool's organization with Claude Code's capabilities!