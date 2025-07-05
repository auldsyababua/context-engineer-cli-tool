# Changelog

## [1.1.0] - 2024-01-15

### Added
- **MCP (Model Context Protocol) Integration**
  - New `context-mcp` tool for managing MCP servers
  - MCP catalog with pre-configured servers (context7, omnisearch, sequential-thinking, memory, github)
  - Phase-aware MCP recommendations in roadmap generation
  - MCP configuration templates in `.mcp/mcp.json`
  - Comprehensive MCP setup documentation

- **Enhanced Refactor/Retry Workflow**
  - Interactive questionnaire for understanding refactor/retry context
  - Required analysis phase before roadmap creation
  - Analysis templates (REFACTOR_ANALYSIS.md, RETRY_ANALYSIS.md)
  - Confidence rating system for roadmaps
  - Roadmap approval step for refactor/retry projects

- **New Example Patterns**
  - `health_check_pattern.py` - System health monitoring
  - `logging_pattern.py` - Structured logging with JSON
  - `phase_management_pattern.py` - Phase-aware feature flags
  - Enhanced examples README with pattern selection guide

- **Template Improvements**
  - ROADMAP.md template for phase-based development
  - Phase template with MCP recommendations
  - MCP_SETUP.md guide for users
  - Updated CLAUDE.md with roadmap awareness

### Changed
- Refactor/Retry now require codebase analysis before planning
- Environment setup checks now include `jq` for MCP manager
- Updated installer with `cem` alias for context-mcp
- Enhanced roadmap generation prompt with MCP integration

### Fixed
- Proper handling of refactor/retry project planning phase
- Template directory creation for analysis documents

## [1.0.0] - 2024-01-10

### Initial Release
- Interactive project setup wizard (`context`)
- Auto-pilot mode with session persistence (`context-auto`)
- Git integration with auto-commits
- Multi-language support (Python, TypeScript, JavaScript, Go)
- Comprehensive template system
- Claude Code command integration
- Environment variable management
- Example code patterns