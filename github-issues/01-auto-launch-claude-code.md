# Enhancement: Auto-Launch Claude Code with Context

## Description
Automatically start Claude Code session and pass in the generated prompt, eliminating the manual copy-paste step.

## Current Behavior
1. User runs `ce` or `cea`
2. Tool generates a prompt
3. User must manually copy the prompt
4. User must manually paste into Claude Code

## Proposed Solution
Add a `--launch` flag (or make it default) that:
1. Detects if Claude Code is installed
2. Launches Claude Code with the generated prompt
3. Automatically creates new conversation
4. Injects the context prompt

## Implementation Ideas
- Use `claude` CLI if available
- Fall back to API integration
- Support for different OS launch methods
- Configuration for Claude Code path

## Benefits
- Eliminates manual copy-paste
- Faster workflow
- Less context switching
- Better user experience

## Example Usage
```bash
# Auto-launch by default
ce

# Or with explicit flag
ce --launch

# Disable auto-launch
ce --no-launch
```

## Technical Requirements
- Detect Claude Code installation
- Handle different OS (Mac, Linux, Windows)
- Support Claude Code CLI interface
- Graceful fallback if not available