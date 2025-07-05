# Example Patterns

This directory contains practical code patterns and examples demonstrating best practices for Context Engineering projects.

## 📁 Available Patterns

### 🏗️ **agent_architecture_pattern.py**
Shows the recommended agent/tools/prompts structure for building modular, maintainable AI-powered applications.
- Main agent orchestration
- Operational tools separation
- Centralized prompts management

### 🏥 **health_check_pattern.py**
Comprehensive health monitoring system for tracking component status and dependencies.
- Multiple health check types
- Concurrent execution
- Status aggregation
- HTTP endpoint example

### 📊 **logging_pattern.py**
Structured logging best practices with JSON formatting and contextual information.
- Custom formatters (JSON and colored console)
- Context managers for request tracking
- Function decorators for automatic logging
- Domain-specific logging methods

### 🚀 **phase_management_pattern.py**
Phase-aware development with feature flags and progressive enhancement.
- Phase configuration and validation
- Feature flag decorators
- Storage factory pattern
- Environment-based phase detection

### 📁 **project_structure.py**
Module organization patterns following Context Engineering principles.
- Dataclass models
- Abstract interfaces
- Service layer pattern
- Anti-pattern examples

### 📞 **telegram_handler_pattern.py**
Telegram bot handler implementation with natural language processing.
- Command handlers
- Message processing
- Error handling
- Async patterns

### 🧪 **test_pattern.py**
Comprehensive testing patterns including fixtures and async tests.
- Fixture organization
- Parametrized tests
- Async test patterns
- Integration test examples

### 🔧 **pydantic_model_pattern.py**
Data validation and modeling with Pydantic.
- Model inheritance
- Custom validators
- Serialization patterns
- Configuration models

## 🚀 Using These Examples

1. **For AI Assistants**: Reference these files in your INITIAL.md to show patterns to follow
2. **For Developers**: Use as templates when creating new components
3. **For PRPs**: Include relevant examples in the generated documentation

## ⚡ Pattern Selection Guide

- **Starting a new project?** → Begin with `project_structure.py` and `agent_architecture_pattern.py`
- **Adding testing?** → Reference `test_pattern.py`
- **Need monitoring?** → Use `health_check_pattern.py` and `logging_pattern.py`
- **Building in phases?** → Implement `phase_management_pattern.py`
- **Working with Telegram?** → Start with `telegram_handler_pattern.py`
- **Data validation?** → Apply `pydantic_model_pattern.py`

## 💡 Best Practices

- Examples should be minimal but complete
- Include both good patterns AND anti-patterns (clearly marked)
- Keep examples updated with project evolution
- Add new examples as patterns emerge

Remember: These are patterns, not prescriptions. Adapt them to your specific context and requirements.