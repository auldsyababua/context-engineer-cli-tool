# MCP Integration with Context Engineer CLI Tool

## Overview

Context Engineer CLI Tool integrates with MCP services through the MCP Infrastructure Manager, which provides centralized management and profile-based access control.

## MCP Infrastructure Manager

The MCP Infrastructure Manager is a separate project located at `~/mcp-infra-manager/` that handles:
- Service registration and configuration
- Profile-based access control
- API key management
- Service lifecycle management

## Integration Method

### 1. Install the MCP Client Library

```python
# Add to your imports
import sys
sys.path.append(os.path.expanduser('~/mcp-infra-manager/api'))
from client import MCPInfraClient
```

### 2. Initialize the Client

```python
# In your initialization code
mcp_client = MCPInfraClient()
```

### 3. Use in Your Planner

```python
def create_agent_prompt(task, project_context):
    # Base prompt
    prompt = f"Task: {task}\n"
    
    # Add MCP services based on context
    profile = mcp_client.determine_profile(task, project_context)
    mcp_section = mcp_client.generate_prompt_section(profile)
    
    return prompt + mcp_section
```

## How It Works

1. **Profile Selection**: The system automatically selects an MCP profile based on:
   - Project path (e.g., "ai-rails" → ai-rails profile)
   - Task keywords (e.g., "research" → research profile)
   - Context clues (e.g., "sensitive" → restricted profile)

2. **Service Access**: Each profile defines which MCP services the agent can see:
   - `default`: Basic services (GitHub, Filesystem, Memory)
   - `research`: Extended search capabilities
   - `development`: Code analysis tools
   - `project-specific`: Custom services for specific projects

3. **Security**: Agents only know about services in their profile, preventing unauthorized access through information hiding.

## Managing MCP Services

All MCP management is handled through the MCP Infrastructure Manager:

```bash
# Check available services
mcp-manager list

# Start a service
mcp-manager start omnisearch

# Check API keys
mcp-manager keys check

# View profile services
mcp-manager profile research
```

## Adding New MCPs

To add a new MCP service:

1. Edit `~/mcp-infra-manager/registry/services.yaml`
2. Add the service definition
3. Include it in appropriate profiles
4. Set any required API keys

See the MCP Infrastructure Manager documentation for detailed instructions.

## Environment Variables

MCP-related environment variables are managed centrally:
- Global config: `~/.config/mcp/.env`
- Service-specific: Defined in the registry

## Troubleshooting

- **Service not available**: Check if it's included in the profile
- **API errors**: Verify keys with `mcp-manager keys check`
- **Connection issues**: Ensure services are running with `mcp-manager list`

For more details, see the MCP Infrastructure Manager at `~/mcp-infra-manager/`