# Adding MCPs to the Library

## Where to Add MCPs

### 1. Local MCP Catalog (Documentation & Discovery)
**Location**: `/mcp-catalog/[mcp-name].json`

This is where you document MCPs for the `context-mcp` command to show info about them.

Example structure:
```json
{
  "name": "mcp-name",
  "description": "What this MCP does",
  "use_cases": ["Use case 1", "Use case 2"],
  "recommended_phases": ["research", "development"],
  "env_vars": {
    "API_KEY_NAME": "Where to get it"
  },
  "setup_instructions": "Step by step setup",
  "documentation": "https://docs.url",
  "mcp_config": {
    "command": "npx",
    "args": ["-y", "@org/mcp-package"],
    "env": {
      "API_KEY_NAME": "${API_KEY_NAME}"
    }
  }
}
```

### 2. Master Config on Workhorse (Actual MCP Definitions)
**Location**: `workhorse:~/mcp-master/mcp-config-master.json`

This is where the actual MCP configurations live that get injected into projects.

To add a new MCP:
```bash
# SSH to workhorse
ssh workhorse@10.0.0.2

# Edit the master config
nano ~/mcp-master/mcp-config-master.json

# Or use jq to add programmatically
jq '.available_mcps.NEW_MCP = {"command": "npx", "args": ["-y", "@org/package"], "env": {"KEY": "${KEY}"}}' mcp-config-master.json
```

### 3. API Keys on Workhorse
**Location**: `workhorse:~/mcp-master/api-keys.env`

Add the actual API keys:
```bash
ssh workhorse@10.0.0.2
echo "NEW_API_KEY=actual-key-value" >> ~/mcp-master/api-keys.env
```

## Common MCPs to Add

### 1. Slack
```json
{
  "slack": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-slack"],
    "env": {
      "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
      "SLACK_APP_TOKEN": "${SLACK_APP_TOKEN}"
    }
  }
}
```

### 2. Google Drive
```json
{
  "gdrive": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-gdrive"],
    "env": {
      "GOOGLE_CLIENT_ID": "${GOOGLE_CLIENT_ID}",
      "GOOGLE_CLIENT_SECRET": "${GOOGLE_CLIENT_SECRET}"
    }
  }
}
```

### 3. Notion
```json
{
  "notion": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-notion"],
    "env": {
      "NOTION_API_KEY": "${NOTION_API_KEY}"
    }
  }
}
```

### 4. Exa (AI-powered search)
```json
{
  "exa": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-exa"],
    "env": {
      "EXA_API_KEY": "${EXA_API_KEY}"
    }
  }
}
```

### 5. Playwright (Browser automation)
```json
{
  "playwright": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-playwright"]
  }
}
```

### 6. Puppeteer (Browser automation)
```json
{
  "puppeteer": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-puppeteer"]
  }
}
```

### 7. Gitlab
```json
{
  "gitlab": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-gitlab"],
    "env": {
      "GITLAB_PERSONAL_ACCESS_TOKEN": "${GITLAB_PERSONAL_ACCESS_TOKEN}",
      "GITLAB_API_URL": "${GITLAB_API_URL}"
    }
  }
}
```

## Quick Add Script

Create this script to quickly add MCPs:

```bash
#!/bin/bash
# add-mcp.sh

MCP_NAME=$1
PACKAGE_NAME=$2
API_KEYS=$3  # comma-separated like "KEY1,KEY2"

# Add to local catalog
cat > /path/to/mcp-catalog/$MCP_NAME.json << EOF
{
  "name": "$MCP_NAME",
  "description": "TODO: Add description",
  "use_cases": ["TODO"],
  "recommended_phases": ["development"],
  "env_vars": {
    $(echo $API_KEYS | sed 's/,/": "TODO",\n    "/g' | sed 's/$/": "TODO"/')
  },
  "mcp_config": {
    "command": "npx",
    "args": ["-y", "$PACKAGE_NAME"],
    "env": {
      $(echo $API_KEYS | sed 's/,/": "${/g' | sed 's/$/": "${/' | sed 's/$/}",/' | sed '$ s/,$//')
    }
  }
}
EOF

# Add to workhorse master config
ssh workhorse@10.0.0.2 "
  jq '.available_mcps.$MCP_NAME = {
    \"command\": \"npx\",
    \"args\": [\"-y\", \"$PACKAGE_NAME\"],
    \"env\": {
      $(echo $API_KEYS | sed 's/,/\": \"\${/g' | sed 's/$/\": \"\${/' | sed 's/$/}\",/' | sed '$ s/,$//')
    }
  }' ~/mcp-master/mcp-config-master.json > /tmp/mcp.tmp && mv /tmp/mcp.tmp ~/mcp-master/mcp-config-master.json
"

echo "Added $MCP_NAME MCP!"
echo "Don't forget to add API keys to workhorse:~/mcp-master/api-keys.env"
```

## After Adding MCPs

1. Run `mcp-sync` to pull the updated configs
2. Use `mcp-phase activate` or manually add to phase configs
3. Add API keys to `workhorse:~/mcp-master/api-keys.env`
4. Use `mcp-inject` in your project to inject the keys

## Finding MCP Packages

Official MCPs: https://github.com/modelcontextprotocol/servers
Community MCPs: Search npm for "@modelcontextprotocol"