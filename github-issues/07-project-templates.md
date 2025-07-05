# Enhancement: Rich Project Template System

## Description
Expand beyond basic project types to offer rich, opinionated templates with best practices built-in.

## Current Limitation
Current project types are generic:
- Web Application
- API/Microservice
- Data Pipeline
- etc.

## Proposed Enhancement

### 1. Framework-Specific Templates

#### Web Applications
- **Next.js + TypeScript**: Full-stack React with API routes
- **Django + HTMX**: Modern Django without heavy JS
- **FastAPI + Vue**: Decoupled API with SPA
- **Rails + Stimulus**: Modern Rails stack

#### Mobile Applications
- **React Native + Expo**: Cross-platform mobile
- **Flutter + Riverpod**: State management included
- **SwiftUI + Combine**: Modern iOS development

#### Data Science
- **Jupyter + Poetry**: Research environment
- **Streamlit Dashboard**: Interactive data apps
- **MLflow Pipeline**: ML experiment tracking

### 2. Industry-Specific Templates

#### E-commerce
- Product catalog structure
- Payment integration stubs
- Order management
- Testing for edge cases

#### SaaS
- Multi-tenancy setup
- Subscription handling
- User management
- API rate limiting

#### IoT
- Device management
- Data ingestion
- Real-time processing
- Dashboard templates

### 3. Template Structure
```
templates/
├── frameworks/
│   ├── nextjs-typescript/
│   │   ├── structure.yaml
│   │   ├── dependencies.json
│   │   ├── prompts/
│   │   └── tests/
│   └── django-htmx/
├── industries/
│   ├── ecommerce/
│   └── saas/
└── custom/
```

### 4. Smart Defaults

Each template includes:
- Pre-configured testing setup
- CI/CD pipelines
- Documentation structure
- Security best practices
- Performance optimizations

### 5. Interactive Selection
```bash
$ ce --template

Choose category:
1. Framework-specific
2. Industry solutions
3. Custom templates

Choose framework:
1. Next.js + TypeScript
2. Django + HTMX
3. FastAPI + Vue

Customization:
- Add authentication? [Y/n]
- Include docker setup? [Y/n]
- Add monitoring? [Y/n]
```

## Benefits
- Faster project initialization
- Best practices built-in
- Reduced decision fatigue
- Consistent structure
- Battle-tested patterns

## Template Registry

### Online Registry
- Community templates
- Ratings and reviews
- Version management
- Auto-updates

### Local Templates
```bash
# Install template
ce template install saas-starter

# Create from template
ce new --template saas-starter

# List templates
ce template list
```

## Customization

### Template Variables
```yaml
name: nextjs-typescript
variables:
  - name: project_name
    prompt: "Project name?"
  - name: use_auth
    prompt: "Include authentication?"
    type: boolean
  - name: database
    prompt: "Database choice?"
    options: ["PostgreSQL", "MySQL", "SQLite"]
```

### Conditional Files
```yaml
files:
  - path: "src/auth/*"
    condition: "use_auth == true"
  - path: "docker-compose.yml"
    condition: "use_docker == true"
```

## Implementation Plan
1. Create template specification format
2. Build template parser and generator
3. Develop initial templates
4. Create template marketplace
5. Add template customization UI