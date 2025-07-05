# Execute PRP Command

Execute a Product Requirements Prompt to implement the specified feature.

## 1. Load PRP Context

Read the entire PRP file: `$ARGUMENTS`

This becomes your primary source of truth for:
- Implementation requirements
- Code patterns to follow
- Testing requirements
- Validation criteria

## 2. Create Implementation Plan

Use the TodoWrite tool to create a detailed task list based on the PRP's implementation steps.

Each task should be:
- Specific and actionable
- Traceable to PRP requirements
- Include validation criteria

## 3. Execute Implementation

For each task in your todo list:

1. Mark task as "in_progress" using TodoWrite
2. Implement according to PRP specifications:
   - Follow code examples provided
   - Use patterns from referenced files
   - Maintain consistency with existing code
3. Validate your work:
   - Run any test commands
   - Check linting if applicable
   - Ensure functionality works
4. Mark task as "completed" using TodoWrite
5. Move to next task

## 4. Run Validation

Execute all validation commands from the PRP:
- Run test suite
- Run linting/formatting
- Run any build commands
- Check all success criteria

If any validation fails:
- Fix the issues
- Re-run validation
- Repeat until all checks pass

## 5. Final Verification

Ensure all PRP success criteria are met:
- [ ] All features implemented
- [ ] All tests passing
- [ ] Code follows conventions
- [ ] Documentation updated (if required)

## 6. Report Completion

Inform the user:
- All implementation completed
- All validations passed
- Summary of what was created/modified
- Any next steps or considerations