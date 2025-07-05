# Phase X: [Phase Name]

## FEATURE:
[Clear description of what this phase implements]

## DEPENDENCIES:
- Phase X: [What it provides that this phase needs]
- Phase Y: [What it provides that this phase needs]

## RECOMMENDED MCP SERVERS:
### Required MCPs:
- **context7**: For accessing [specific library] documentation
- **memory**: To maintain context about [specific decisions/patterns]

### Optional MCPs:
- **omnisearch**: If you need to research [specific topics]
- **github**: For creating PRs when phase is complete

### MCP Setup:
1. Enable the MCPs in `.mcp/mcp.json` by uncommenting the relevant sections
2. Add any required API keys to `.env` (see comments for where to obtain)
3. Restart Claude Code to activate the MCPs

## IMPLEMENTATION APPROACH:
1. [First major step]
2. [Second major step]
3. [Third major step]

## TECHNICAL CONSIDERATIONS:
- [Important technical decision or constraint]
- [Performance consideration]
- [Security consideration]

## SUCCESS CRITERIA:
- [ ] [Specific, testable criterion]
- [ ] [Another specific criterion]
- [ ] All tests pass
- [ ] Documentation updated
- [ ] No linting errors

## EXAMPLES TO REFERENCE:
- `examples/[relevant_pattern].py` - For [what to use it for]
- `examples/[another_pattern].py` - For [what to use it for]

## ENVIRONMENT VARIABLES:
```env
# Phase X Environment Variables
VARIABLE_NAME=description-of-value  # Get from: [where to obtain]
```

## ESTIMATED EFFORT:
- Complexity: [Simple/Medium/Complex]
- Time estimate: [1-2 days]
- Risk factors: [Any known challenges]