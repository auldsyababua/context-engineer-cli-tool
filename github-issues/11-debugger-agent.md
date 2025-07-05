# Enhancement: Specialized Debugger Agent

## Description
Migrate the Debugger/Troubleshooter Agent from ai-rails-tdd with specialized tools and MCPs for error analysis and resolution.

## Current vs Proposed

### Current Approach
- Generic "fix errors" prompts
- Manual error interpretation
- No structured debugging workflow

### Proposed Debugger Agent
- Specialized error analysis capabilities
- Access to debugging-specific MCPs
- Structured problem-solving approach
- Behavioral debugging (without seeing test internals)

## Agent Configuration

### Specialized Tools
- **Error Parser MCP**: Extract structured error information
- **Stack Trace Analyzer**: Understand error context
- **Code Search MCP**: Find related code patterns
- **Fix Suggestion Engine**: Generate targeted solutions

### Model Selection
- Primary: WizardCoder-33B-V1.1 (optimized for debugging)
- Fallback: Claude-3.5-sonnet for complex cases

### Agent Capabilities
1. **Error Analysis**
   - Parse error messages and stack traces
   - Identify root causes
   - Categorize error types

2. **Solution Generation**
   - Minimal code changes
   - Test-driven fixes
   - Performance considerations

3. **Verification**
   - Suggest test cases
   - Validate fixes
   - Prevent regression

## Integration with Context Engineer

### Workflow Integration
```
Test Phase → Test Failures → Debugger Agent → Fix Suggestions → Implementation
```

### Input Format
```json
{
  "error_type": "test_failure",
  "test_description": "User creation should return 201",
  "error_message": "Expected 201, got 400",
  "code_context": "...",
  "project_type": "api"
}
```

### Output Format
```json
{
  "diagnosis": "Missing required field validation",
  "root_cause": "Request body validation",
  "fix": {
    "file": "src/routes/users.py",
    "changes": "...",
    "explanation": "..."
  },
  "verification": "Run test_user_creation"
}
```

## Benefits
- Faster error resolution
- Learn from common patterns
- Reduce debugging iterations
- Better error messages

## Implementation Plan
1. Create debugger agent prompt template
2. Add debugging-specific MCPs
3. Integrate with test phase
4. Add error pattern learning
5. Create debugging workflow