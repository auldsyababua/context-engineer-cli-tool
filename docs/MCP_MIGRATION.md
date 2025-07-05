# MCP Infrastructure Migration

## What Changed

The MCP (Model Context Protocol) infrastructure has been moved from context-engineer-cli-tool to a separate project: **MCP Infrastructure Manager** (`~/mcp-infra-manager/`).

### Removed from context-engineer-cli-tool:
- `/mcp-catalog/` directory
- `/lib/` directory (was empty)
- MCP-specific bin scripts:
  - `context-mcp`
  - `mcp-inject`
  - `mcp-phase`
  - `mcp-sync`
  - `mcp-workhorse-setup`
- Old MCP documentation files

### Updated:
- `bin/context` - Now references mcp-manager for MCP operations
- `bin/context-auto` - Updated to use MCP profiles instead of individual MCPs
- Removed `.mcp` directory creation from project templates

## How to Use MCPs Now

All MCP management is handled through the MCP Infrastructure Manager:

```bash
# Check available services
mcp-manager list

# Start a service
mcp-manager start omnisearch

# Check API keys
mcp-manager keys check

# View profiles
mcp-manager profile research
```

## For Existing Projects

If you have existing projects with `.mcp` directories:
1. They can be safely removed
2. MCP access is now controlled by profiles in the infrastructure manager
3. No project-specific MCP configuration needed

## Integration with Claude

When using context-engineer with Claude:
1. The planner will automatically select appropriate MCP profiles
2. Agents will only see services allowed by their profile
3. No manual MCP configuration needed

## Benefits

- **Centralized Management**: All MCPs in one place
- **No Duplicates**: System prevents multiple instances
- **Easy Updates**: Just edit YAML files to add/modify services
- **Cleaner Projects**: No MCP configuration in individual projects
- **Better Security**: Profile-based access control