# Environment Variable Example Template

Use this template when creating .env.example files during roadmap generation.

```bash
# Environment Configuration for [Project Name]
# Copy this file to .env and fill in your actual values

# ============================================
# PHASE 1: Basic Setup
# ============================================
# No environment variables required for Phase 1

# ============================================
# PHASE 2: Database Integration
# ============================================
# PostgreSQL connection string (required starting Phase 2)
# Get from: Local PostgreSQL or cloud provider (Supabase, Neon, etc.)
# Format: postgresql://user:password@localhost:5432/dbname
DATABASE_URL=postgresql://user:password@localhost:5432/myapp

# ============================================
# PHASE 3: External API Integration
# ============================================
# OpenAI API Key (required starting Phase 3)
# Get from: https://platform.openai.com/api-keys
# Cost: ~$0.01 per request
# Format: sk-...
OPENAI_API_KEY=sk-...

# Redis URL (optional starting Phase 3)
# For caching API responses
# Format: redis://localhost:6379
REDIS_URL=redis://localhost:6379

# ============================================
# PHASE 4: Authentication
# ============================================
# JWT Secret (required starting Phase 4)
# Generate with: openssl rand -base64 32
JWT_SECRET=your_random_secret_here

# OAuth credentials (optional starting Phase 4)
# Get from: https://console.cloud.google.com/
GOOGLE_CLIENT_ID=your_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_client_secret
```