# Enhancement: Agent Input/Output Handoff Mechanism

## Description
Implement a standardized mechanism for agents to receive input from previous agents and pass output to subsequent agents in the workflow.

## Current Problem
As noted in ai-rails-tdd issue #1:
- Agent prompts don't have clear input placeholders
- Manual copy/paste required between agents
- No standardized data format for handoffs
- Breaks automation potential

## Proposed Solution

### 1. Standardized Placeholders
```markdown
# Agent Prompt Template

You are a specialized {{AGENT_TYPE}} agent.

## Previous Agent Output
{{PREVIOUS_AGENT_OUTPUT}}

## Your Task
{{TASK_DESCRIPTION}}

## Expected Output Format
{{OUTPUT_SCHEMA}}
```

### 2. Handoff Protocol
```json
{
  "handoff": {
    "from_agent": "planner",
    "to_agent": "tester",
    "timestamp": "2024-01-15T10:00:00Z",
    "data": {
      "planning_phase": "tdd_implementation",
      "feature_spec": {...},
      "test_specification": {...}
    },
    "metadata": {
      "session_id": "abc123",
      "phase": "testing",
      "attempt": 1
    }
  }
}
```

### 3. Context Engineer Integration

#### Automatic Injection
```python
class AgentHandoff:
    def prepare_prompt(self, agent_type, previous_output=None):
        template = self.load_template(agent_type)
        
        # Replace placeholders
        prompt = template.replace("{{PREVIOUS_AGENT_OUTPUT}}", 
                                json.dumps(previous_output, indent=2))
        prompt = prompt.replace("{{AGENT_TYPE}}", agent_type)
        
        return prompt
```

#### Handoff Storage
```
project/.context-engineer/
├── handoffs/
│   ├── 001-planner-to-tester.json
│   ├── 002-tester-to-coder.json
│   └── 003-coder-to-reviewer.json
```

## Implementation Details

### 1. Update All Agent Prompts
Add standardized sections:
- `## Input` - What this agent receives
- `## Output` - What this agent produces
- `## Handoff Format` - Expected JSON structure

### 2. Create Handoff Manager
```python
class HandoffManager:
    def __init__(self, project_path):
        self.handoff_dir = project_path / ".context-engineer/handoffs"
        self.handoff_dir.mkdir(exist_ok=True)
    
    def save_handoff(self, from_agent, to_agent, data):
        handoff = {
            "from_agent": from_agent,
            "to_agent": to_agent,
            "timestamp": datetime.now().isoformat(),
            "data": data
        }
        
        filename = f"{self.next_id:03d}-{from_agent}-to-{to_agent}.json"
        path = self.handoff_dir / filename
        path.write_text(json.dumps(handoff, indent=2))
        
        return handoff
    
    def get_latest_handoff(self, for_agent):
        # Find most recent handoff targeting this agent
        handoffs = sorted(self.handoff_dir.glob(f"*-to-{for_agent}.json"))
        if handoffs:
            return json.loads(handoffs[-1].read_text())
        return None
```

### 3. Workflow Integration

#### Manual Mode (Current)
```bash
# User runs planner
ce --phase planning
# Output saved to handoff

# User runs tester with context
ce --phase testing
# Automatically loads previous handoff
```

#### Automated Mode (Future)
```bash
# All handoffs automatic
cea --project my-api
# Each agent receives proper context
```

## Benefits

### 1. Automation Ready
- No manual copy/paste
- Agents can chain automatically
- Preserves context between phases

### 2. Better Traceability
- Clear audit trail
- Debug agent decisions
- Understand data flow

### 3. Flexibility
- Easy to add new agents
- Modify handoff formats
- Support parallel workflows

## Example Handoff Flow

### Planning → Testing
```json
{
  "handoff": {
    "from_agent": "planner",
    "to_agent": "tester",
    "data": {
      "feature": "User Authentication",
      "requirements": [
        "Users can register with email",
        "Passwords must be hashed",
        "Return JWT tokens"
      ],
      "test_strategy": "unit + integration"
    }
  }
}
```

### Testing → Implementation
```json
{
  "handoff": {
    "from_agent": "tester",
    "to_agent": "implementation",
    "data": {
      "test_file": "test_auth.py",
      "test_count": 12,
      "coverage_target": 90,
      "key_behaviors": [
        "Validates email format",
        "Rejects weak passwords",
        "Returns 201 on success"
      ]
    }
  }
}
```

## Migration Plan
1. Add placeholders to existing prompts
2. Implement HandoffManager
3. Update context/context-auto scripts
4. Test with single workflow
5. Roll out to all agents

This enhancement is crucial for enabling true multi-agent workflows and removing friction from the Context Engineer experience.