# Enhancement: Development Environment Containers

## Description
Provide pre-configured development containers with language runtimes, databases, and tools for instant project startup.

## Problem Solved
- "Works on my machine" issues
- Complex local setup requirements
- Version mismatches between team members
- Time wasted on environment configuration

## Container Types

### 1. Language-Specific Containers
```yaml
containers:
  python:
    base: python:3.11-slim
    includes:
      - Poetry for dependency management
      - Common dev tools (black, flake8, pytest)
      - Database clients
      - Debug tools
  
  node:
    base: node:20-alpine
    includes:
      - pnpm, yarn, npm
      - TypeScript setup
      - ESLint, Prettier
      - Nodemon for hot reload
  
  go:
    base: golang:1.21-alpine
    includes:
      - Air for hot reload
      - Delve debugger
      - golangci-lint
      - Mock generation tools
  
  rust:
    base: rust:latest
    includes:
      - Cargo watch
      - Clippy, rustfmt
      - Sccache for faster builds
```

### 2. Full-Stack Containers
```yaml
fullstack_containers:
  nextjs_supabase:
    services:
      - Next.js dev server
      - Supabase local stack
      - Redis for sessions
      - Mailhog for email testing
  
  django_postgres:
    services:
      - Django dev server
      - PostgreSQL
      - Redis
      - Celery worker
      - Flower for monitoring
  
  rails_mysql:
    services:
      - Rails server
      - MySQL
      - Redis
      - Sidekiq
      - Webpacker
```

## Integration with Context Engineer

### Project Creation
```bash
# Create project with container
ce new my-api --container python-fastapi

# Or choose interactively
ce new my-app
? Select development container:
  > Python (FastAPI + PostgreSQL)
    Node.js (Express + MongoDB)  
    Go (Gin + PostgreSQL)
    Full-stack (Next.js + Supabase)
    Custom container
```

### Container Management
```bash
# Start development environment
ce dev start

# Container starts with:
- Mounted project directory
- Environment variables loaded
- Services initialized
- Ports forwarded

# Access container shell
ce dev shell

# Run commands in container
ce dev run pytest
ce dev run "npm test"

# Stop environment
ce dev stop
```

## Implementation Details

### Dev Container Specification
```json
// .devcontainer/devcontainer.json
{
  "name": "My API Development",
  "dockerComposeFile": "docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/workspace",
  
  "features": {
    "ghcr.io/devcontainers/features/python:1": {
      "version": "3.11"
    },
    "ghcr.io/devcontainers/features/github-cli:1": {}
  },
  
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  },
  
  "postCreateCommand": "pip install -r requirements.txt",
  "remoteUser": "vscode"
}
```

### Docker Compose Integration
```yaml
# .devcontainer/docker-compose.yml
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - ..:/workspace:cached
      - ~/.ssh:/home/vscode/.ssh:ro
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/myapp
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
  
  db:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: myapp
    volumes:
      - postgres_data:/var/lib/postgresql/data
  
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### Container Templates
```python
class ContainerTemplateManager:
    def __init__(self):
        self.templates_dir = Path(__file__).parent / "container-templates"
    
    def create_container_config(self, project_type, language, services):
        template = self.load_template(language, project_type)
        
        # Customize based on selections
        if "postgresql" in services:
            template.add_service("postgres", self.postgres_config())
        
        if "redis" in services:
            template.add_service("redis", self.redis_config())
        
        # Add development tools
        template.add_dev_tools(self.get_dev_tools(language))
        
        # Generate files
        self.write_devcontainer_json(template)
        self.write_docker_compose(template)
        self.write_dockerfile(template)
        
        return template
```

## Pre-Built Environments

### 1. API Development
- FastAPI + PostgreSQL + Redis
- Express + MongoDB + RabbitMQ
- Go + PostgreSQL + NATS
- Rails + MySQL + Sidekiq

### 2. Frontend Development
- Next.js + Supabase
- Vue + Firebase
- React + Amplify
- Angular + NestJS

### 3. Mobile Development
- React Native + Expo
- Flutter + Firebase
- Ionic + Capacitor

### 4. Data Science
- Jupyter + PostgreSQL + MLflow
- Python + DuckDB + Prefect
- R + PostgreSQL + Shiny

## Benefits

### Instant Start
```bash
# From zero to coding in 30 seconds
ce new my-project --container python-api
cd my-project
ce dev start
# Container running, dependencies installed, ready to code
```

### Consistency
- Same environment for all team members
- Dev/prod parity
- Reproducible builds
- Version-locked dependencies

### Integration
- Works with VS Code Dev Containers
- Compatible with GitHub Codespaces
- Supports JetBrains Gateway
- Cloud IDE ready

## Advanced Features

### 1. Container Composition
```bash
# Combine multiple containers
ce dev compose --add elasticsearch --add kibana
```

### 2. Environment Sync
```bash
# Share exact environment
ce dev export > environment.json

# Team member imports
ce dev import environment.json
```

### 3. Performance Optimization
- Volume caching strategies
- BuildKit optimizations
- Layer caching
- Minimal base images

## Future Enhancements
- Container registry for custom images
- Team environment sharing
- Automatic security updates
- Performance profiling tools
- GPU support for ML projects