# Enhancement: Specialized Refactor Agent

## Description
Implement a Refactor Agent that improves code quality after initial implementation, focusing on performance, readability, and maintainability without changing functionality.

## Philosophy Alignment

### Why Refactoring Fits Context Engineer
- **Phase-Based**: Natural post-implementation phase
- **Quality Focus**: Ensures production-ready code
- **Learning**: Improves patterns over time
- **Automated**: Reduces manual refactoring burden

## Agent Configuration

### Specialized Tools
- **Code Metrics MCP**: Analyze complexity, duplication
- **Pattern Detection MCP**: Identify anti-patterns
- **Performance Analyzer**: Find bottlenecks
- **Refactoring Toolkit**: Apply safe transformations

### Model Selection
- Primary: Refact-1.6B (specialized for refactoring)
- Secondary: DeepSeek-Coder for complex refactors

### Refactoring Capabilities

#### 1. Performance Optimizations
- Algorithm improvements
- Database query optimization
- Caching opportunities
- Resource usage reduction

#### 2. Code Quality
- Extract methods/functions
- Reduce complexity
- Improve naming
- Remove duplication

#### 3. Design Patterns
- Apply appropriate patterns
- Simplify over-engineering
- Improve modularity
- Enhance testability

## Integration Workflow

### Automatic Triggers
```yaml
refactor_triggers:
  after_tests_pass: true
  complexity_threshold: 10
  duplication_threshold: 20%
  performance_issues: true
```

### Refactor Process
```
Tests Pass → Code Analysis → Refactor Suggestions → Apply Changes → Verify Tests
```

### Input/Output Format
```json
// Input
{
  "code": "current implementation",
  "tests": "existing test suite",
  "metrics": {
    "complexity": 15,
    "duplication": 25,
    "performance": "slow"
  }
}

// Output
{
  "refactorings": [
    {
      "type": "extract_method",
      "description": "Extract validation logic",
      "before": "...",
      "after": "...",
      "benefits": ["Reduced complexity", "Reusable"]
    }
  ],
  "metrics_improvement": {
    "complexity": "15 → 8",
    "duplication": "25% → 5%"
  }
}
```

## Safety Mechanisms

### Test Preservation
- All tests must pass after refactoring
- No functional changes allowed
- Performance benchmarks maintained

### Incremental Changes
- Small, reviewable changes
- Git commits for each refactor
- Easy rollback capability

## Benefits
- Consistent code quality
- Reduced technical debt
- Better performance
- Easier maintenance
- Knowledge capture

## Example Scenarios

### API Endpoint Refactoring
```python
# Before: Complex endpoint with mixed concerns
@app.post("/users")
def create_user(data):
    # 50 lines of validation, DB, email logic
    
# After: Clean separation
@app.post("/users")
def create_user(data):
    validated = UserValidator.validate(data)
    user = UserService.create(validated)
    EmailService.send_welcome(user)
    return user
```

### Performance Optimization
```python
# Before: N+1 query problem
for order in orders:
    order.items = Item.query.filter_by(order_id=order.id).all()

# After: Eager loading
orders = Order.query.options(joinedload(Order.items)).all()
```