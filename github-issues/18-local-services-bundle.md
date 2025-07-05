# Enhancement: Local Services Bundle (n8n, Supabase, Redis)

## Description
Bundle popular self-hosted services as optional add-ons during CLI installation, with automatic integration for new projects.

## Architecture Strategy

### Single Instance, Multiple Projects
- **One n8n instance**: Installed with CLI, shared across all projects
- **Per-project workflows**: Each project gets its own n8n workflow folder
- **Shared resources**: Redis, Supabase available to all projects
- **Project isolation**: Namespaced data and workflows

## Service Bundle

### 1. n8n (Workflow Automation)
```yaml
n8n:
  install_mode: "cli_level"  # One instance for all projects
  port: 5678
  features:
    - Per-project workflow folders
    - Pre-built Context Engineer workflows
    - Auto-import project templates
    - Credential management
```

### 2. Supabase (Backend-as-a-Service)
```yaml
supabase:
  install_mode: "cli_level"
  services:
    - PostgreSQL database
    - Authentication
    - Realtime subscriptions
    - Storage buckets
  project_setup:
    - Auto-create project database
    - Generate API keys
    - Setup auth rules
```

### 3. Redis (Cache & State)
```yaml
redis:
  install_mode: "cli_level"
  port: 6379
  features:
    - Session storage
    - Task queues
    - Caching
    - Pub/sub for real-time
```

### 4. Additional Services
```yaml
additional_services:
  - MinIO (S3-compatible storage)
  - RabbitMQ (Message queuing)
  - Prometheus + Grafana (Monitoring)
  - GitLab (Self-hosted Git)
  - Vault (Secret management)
```

## Installation Flow

### CLI Installation
```bash
# Install Context Engineer with services
./install.sh --with-services

# Options presented:
? Install local services bundle? (Y/n)
? Select services:
  ✓ n8n (Workflow automation)
  ✓ Supabase (Backend platform)
  ✓ Redis (Cache & queues)
  ○ MinIO (Object storage)
  ○ RabbitMQ (Message broker)

# Services installed via Docker Compose
Setting up local services...
✓ n8n running at http://localhost:5678
✓ Supabase running at http://localhost:3000
✓ Redis running at localhost:6379
```

### Project Creation
```bash
# Create new project
ce new my-api

# Automatic service integration
? Connect to local services?
  ✓ Create n8n workflow folder
  ✓ Create Supabase project
  ✓ Setup Redis namespace

# Generated configuration
Created: my-api/.env.services
N8N_WORKFLOW_FOLDER=/my-api
SUPABASE_PROJECT_ID=my-api-12345
REDIS_NAMESPACE=my-api
```

## Implementation Architecture

### Docker Compose Setup
```yaml
version: '3.8'
services:
  n8n:
    image: n8nio/n8n
    ports:
      - "5678:5678"
    volumes:
      - n8n_data:/home/node/.n8n
      - ./projects:/projects  # Per-project workflows
    environment:
      - N8N_BASIC_AUTH_ACTIVE=true
      - N8N_BASIC_AUTH_USER=context-engineer
  
  supabase-db:
    image: supabase/postgres
    ports:
      - "5432:5432"
    volumes:
      - supabase_db:/var/lib/postgresql/data
  
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
```

### Service Manager
```python
class LocalServicesManager:
    def __init__(self):
        self.compose_file = Path.home() / ".context-engineer/docker-compose.yml"
        self.services = ["n8n", "supabase", "redis"]
    
    def install_services(self, selected_services):
        # Generate docker-compose.yml
        self.generate_compose_file(selected_services)
        
        # Start services
        subprocess.run(["docker-compose", "up", "-d"])
        
        # Wait for health checks
        self.wait_for_services()
        
        # Initial configuration
        self.configure_services()
    
    def create_project_resources(self, project_name):
        resources = {}
        
        # n8n workflow folder
        if self.is_service_running("n8n"):
            workflow_folder = self.create_n8n_workflow_folder(project_name)
            resources["N8N_WORKFLOW_FOLDER"] = workflow_folder
        
        # Supabase project
        if self.is_service_running("supabase"):
            project = self.create_supabase_project(project_name)
            resources.update({
                "SUPABASE_URL": project.url,
                "SUPABASE_ANON_KEY": project.anon_key,
                "SUPABASE_SERVICE_KEY": project.service_key
            })
        
        # Redis namespace
        if self.is_service_running("redis"):
            resources["REDIS_NAMESPACE"] = project_name
            resources["REDIS_URL"] = "redis://localhost:6379"
        
        return resources
```

### Per-Project Integration

#### n8n Workflows
```
~/.context-engineer/n8n-workflows/
├── my-api/
│   ├── deployment.json
│   ├── testing.json
│   └── monitoring.json
├── web-app/
│   ├── ci-cd.json
│   └── notifications.json
```

#### Project Templates
```python
def create_n8n_templates(project_type, project_name):
    templates = {
        "api": ["api-testing", "deployment", "monitoring"],
        "web": ["build-deploy", "e2e-testing", "analytics"],
        "cli": ["release", "testing", "distribution"]
    }
    
    for template in templates.get(project_type, []):
        import_n8n_workflow(template, project_name)
```

## Benefits

### For Developers
- Zero-config backend services
- Integrated automation from day one
- Local development matches production
- No cloud costs during development

### For Projects
- Instant backend capabilities
- Built-in workflow automation
- Caching and queuing ready
- Authentication solved

## Configuration

### Service Selection
```yaml
# ~/.context-engineer/services.yaml
enabled_services:
  n8n:
    enabled: true
    port: 5678
    version: latest
  
  supabase:
    enabled: true
    port: 3000
    version: latest
  
  redis:
    enabled: true
    port: 6379
    version: 7-alpine
  
  minio:
    enabled: false
    port: 9000
    version: latest
```

### Project Integration
```bash
# .env.services (auto-generated)
# n8n
N8N_URL=http://localhost:5678
N8N_API_KEY=generated-key
N8N_WORKFLOW_FOLDER=/my-api

# Supabase
SUPABASE_URL=http://localhost:3000
SUPABASE_ANON_KEY=generated-anon-key
SUPABASE_SERVICE_KEY=generated-service-key

# Redis
REDIS_URL=redis://localhost:6379
REDIS_NAMESPACE=my-api
```

## Future Enhancements
- Service health monitoring dashboard
- Automatic backups
- Service templates marketplace
- Cloud deployment helpers
- Multi-environment support