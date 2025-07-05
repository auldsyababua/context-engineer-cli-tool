# Phase Structure Template

Use this template when creating phase directories during roadmap generation.

## Directory Structure
```
phases/
├── phase-1/
│   ├── INITIAL.md           # Feature description
│   └── SUCCESS_CRITERIA.md  # Completion checklist
├── phase-2/
│   ├── INITIAL.md
│   └── SUCCESS_CRITERIA.md
└── ...
```

## INITIAL.md Template
```markdown
# Phase [N]: [Phase Title]

## Overview
[Brief description of what this phase accomplishes]

## Features to Implement
- [ ] [Feature 1]
- [ ] [Feature 2]
- [ ] [Feature 3]

## Dependencies
- Requires completion of Phase [N-1]
- [Any specific components needed from previous phases]

## Technical Approach
[High-level technical approach for this phase]

## Complexity: [Simple/Medium/Complex]

## Environment Variables Needed
- [VAR_NAME] - [Purpose] (Required/Optional)
```

## SUCCESS_CRITERIA.md Template
```markdown
# Phase [N] Success Criteria

## Functional Requirements
- [ ] [Specific testable requirement]
- [ ] [Another testable requirement]

## Technical Requirements
- [ ] All tests pass
- [ ] Code follows project conventions
- [ ] Documentation updated

## Validation Steps
1. [How to verify feature 1 works]
2. [How to verify feature 2 works]

## Performance Targets
- [Any specific performance requirements]

## Known Issues to Address
- [Any issues from previous phases to fix]
```