# Generate PRP Command

Execute the following steps to generate a Product Requirements Prompt (PRP) from the initial feature request:

## 1. Read and Understand Feature Request

Read the file: `$ARGUMENTS`

Extract:
- Feature description
- Examples to reference
- Documentation links
- Success criteria
- Other considerations

## 2. Research Codebase

Search for relevant patterns:
- Use Glob to find similar files
- Use Grep to search for related functionality
- Read example files mentioned in INITIAL.md
- Identify coding conventions and patterns to follow

## 3. Gather Documentation

For each documentation link or API mentioned:
- Use WebFetch to retrieve relevant documentation
- Extract key implementation details
- Note any gotchas or special requirements

## 4. Create Comprehensive PRP

Generate a new file `PRPs/[feature-name].md` with:

### Structure:
```markdown
# [Feature Name] - Product Requirements Prompt

## Context
[Comprehensive background and requirements]

## Documentation
[All relevant docs, API references, examples]

## Implementation Steps
1. [Detailed step-by-step plan]
2. [Include validation at each step]
3. [Reference specific patterns to follow]

## Code Examples
[Include relevant code snippets from examples/]

## Testing Requirements
- Test files to create
- Test cases to implement
- Coverage expectations

## Success Criteria
- [ ] All features implemented
- [ ] Tests passing
- [ ] Follows project conventions
- [ ] Documentation updated

## Validation Commands
```bash
# Commands to run to validate implementation
```

## Confidence Score
[Rate 1-10 based on completeness of context]
```

## 5. Report Completion

Inform the user:
- PRP has been created at `PRPs/[feature-name].md`
- Confidence score and reasoning
- Ready to execute with `/execute-prp PRPs/[feature-name].md`