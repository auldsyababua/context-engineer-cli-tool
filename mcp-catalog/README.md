# MCP (Model Context Protocol) Catalog

This directory contains configurations and documentation for MCP servers that can enhance AI capabilities during different phases of development.

## 🔌 Available MCP Servers

### Core MCPs (Recommended for All Projects)

#### 📚 **context7**
- **Purpose**: Provides up-to-date library documentation
- **Use Cases**: 
  - Fetching current API docs during implementation
  - Understanding library changes and updates
  - Getting code examples from official docs
- **Phases**: All phases involving external libraries

#### 🔍 **omnisearch**
- **Purpose**: Advanced web search and content extraction
- **Use Cases**:
  - Researching implementation approaches
  - Finding solutions to technical problems
  - Extracting content from documentation sites
- **Phases**: Research, planning, debugging phases

#### 🧠 **sequential-thinking**
- **Purpose**: Structured problem-solving and planning
- **Use Cases**:
  - Breaking down complex problems
  - Creating implementation plans
  - Analyzing architectural decisions
- **Phases**: Planning, architecture, complex feature phases

### Development MCPs

#### 💾 **memory**
- **Purpose**: Knowledge graph for project context
- **Use Cases**:
  - Storing project-specific knowledge
  - Tracking decisions and rationale
  - Building domain understanding
- **Phases**: All phases (cumulative knowledge)

#### 🐙 **github**
- **Purpose**: GitHub repository interaction
- **Use Cases**:
  - Creating pull requests
  - Managing issues
  - Searching code across repos
- **Phases**: Integration, deployment, collaboration phases

#### ✅ **todoist**
- **Purpose**: Task management integration
- **Use Cases**:
  - Creating development tasks
  - Tracking progress
  - Managing deadlines
- **Phases**: Project management phases

### Infrastructure MCPs

#### 📊 **graphql**
- **Purpose**: GraphQL API interaction
- **Use Cases**:
  - Schema introspection
  - Query generation
  - API testing
- **Phases**: API development phases

#### 🔐 **filesystem**
- **Purpose**: Enhanced file system operations
- **Use Cases**:
  - Bulk file operations
  - Directory analysis
  - File search and replace
- **Phases**: Refactoring, migration phases

## 🚀 Phase-Based MCP Activation

### Planning & Architecture Phases
```json
{
  "mcps": ["context7", "omnisearch", "sequential-thinking", "memory"],
  "reason": "Need research, documentation, and structured planning"
}
```

### Implementation Phases
```json
{
  "mcps": ["context7", "github", "memory"],
  "reason": "Need docs, version control, and context retention"
}
```

### Testing & Debugging Phases
```json
{
  "mcps": ["omnisearch", "memory"],
  "reason": "Need to search for solutions and track findings"
}
```

### Deployment & Documentation Phases
```json
{
  "mcps": ["github", "todoist"],
  "reason": "Need to manage releases and track tasks"
}
```

## 📋 MCP Configuration Template

Each MCP configuration should include:

```json
{
  "name": "mcp-name",
  "description": "What this MCP does",
  "use_cases": ["primary use", "secondary use"],
  "recommended_phases": ["phase1", "phase2"],
  "env_vars": {
    "MCP_NAME_API_KEY": "Description of where to get this key"
  },
  "setup_instructions": "How to set up this MCP",
  "documentation": "Link to MCP documentation"
}
```

## 🔧 Integration with Context Engineer

The Context Engineer CLI Tool can:
1. Suggest relevant MCPs for each phase
2. Generate MCP configuration in `.mcp/` directory
3. Add required environment variables to `.env.example`
4. Include MCP activation instructions in phase documentation

## 💡 Best Practices

1. **Start Minimal**: Don't activate all MCPs at once
2. **Phase Alignment**: Match MCPs to phase needs
3. **Performance**: More MCPs = slower startup
4. **Security**: Always use environment variables for API keys
5. **Documentation**: Document why each MCP is needed