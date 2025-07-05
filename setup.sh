#!/bin/bash
# Context Engineer CLI Tool - Setup Script
# For use with Claude Code

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Print colored output
print_header() {
    echo -e "\n${BLUE}=== $1 ===${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Main setup
print_header "Context Engineer CLI Tool Setup"
echo "This tool enhances Claude Code with structured project management and MCP services."
echo ""

# Check if .env exists
if [[ -f .env ]]; then
    print_success ".env file exists"
else
    if [[ -f .env.example ]]; then
        print_warning ".env file not found. Creating from template..."
        cp .env.example .env
        print_success "Created .env from .env.example"
        echo ""
        echo "Please edit .env and add your configuration."
        echo "At minimum, you'll need to set MCP_MODE and any API keys."
    else
        print_error ".env.example not found!"
        exit 1
    fi
fi

# Load environment
source .env

# Check MCP mode
print_header "MCP Configuration"
echo "MCP Mode: ${MCP_MODE:-not set}"
echo ""

case "${MCP_MODE:-none}" in
    none)
        print_warning "MCP_MODE=none - MCPs are disabled"
        echo "Context Engineer will work without MCP services."
        echo "To enable MCPs, set MCP_MODE in your .env file to: local, docker, or systemd"
        ;;
        
    local)
        print_success "Using local MCP mode"
        echo "MCPs will run on your machine alongside Claude Code."
        echo ""
        
        # Check for .env.mcp
        if [[ -f .env.mcp ]]; then
            print_success ".env.mcp file exists"
        else
            if [[ -f .env.mcp.example ]]; then
                print_warning ".env.mcp not found. Creating from template..."
                cp .env.mcp.example .env.mcp
                print_success "Created .env.mcp"
                echo ""
                print_warning "Please edit .env.mcp and add your MCP API keys:"
                echo "  - GITHUB_TOKEN (highly recommended)"
                echo "  - BRAVE_API_KEY (for web search)"
                echo "  - UPSTASH_REDIS_* (for context persistence)"
                echo ""
            fi
        fi
        
        # Check for required tools
        print_header "Checking Requirements"
        
        # Node.js
        if command -v node &> /dev/null; then
            NODE_VERSION=$(node --version)
            print_success "Node.js installed: $NODE_VERSION"
        else
            print_error "Node.js not found! Please install Node.js 18 or later."
            echo "Visit: https://nodejs.org/"
            exit 1
        fi
        
        # NPM
        if command -v npm &> /dev/null; then
            NPM_VERSION=$(npm --version)
            print_success "npm installed: $NPM_VERSION"
        else
            print_error "npm not found!"
            exit 1
        fi
        
        # Create directories
        print_header "Creating Directories"
        mkdir -p "${MCP_SERVICES_DIR:-$HOME/.mcp-services}"
        mkdir -p "${MCP_LOG_DIR:-$HOME/.mcp/logs}"
        print_success "Created MCP directories"
        
        # Offer to install recommended MCPs
        print_header "Recommended MCP Services"
        echo "The following MCPs are recommended for the best Claude Code experience:"
        echo ""
        echo "1. GitHub MCP - Repository operations"
        echo "2. Filesystem MCP - Local file access"
        echo "3. Memory MCP - Persistent context"
        echo "4. OmniSearch MCP - Web search (requires API keys)"
        echo "5. Context7 MCP - Session persistence (requires Upstash)"
        echo "6. Sequential Thinking MCP - Complex reasoning"
        echo ""
        
        read -p "Would you like to install the recommended MCPs? [Y/n]: " install_mcps
        install_mcps=${install_mcps:-Y}
        
        if [[ "$install_mcps" =~ ^[Yy] ]]; then
            print_header "Installing MCP Services"
            
            # Install each MCP
            echo "Installing GitHub MCP..."
            npm install -g @modelcontextprotocol/server-github
            
            echo "Installing Filesystem MCP..."
            npm install -g @modelcontextprotocol/server-filesystem
            
            echo "Installing Memory MCP..."
            npm install -g @modelcontextprotocol/server-memory
            
            echo "Installing OmniSearch MCP..."
            npm install -g mcp-omnisearch
            
            echo "Installing Context7 MCP..."
            npm install -g @upstash/context7-mcp
            
            echo "Installing Sequential Thinking MCP..."
            npm install -g @modelcontextprotocol/server-sequential-thinking
            
            print_success "MCP services installed!"
        fi
        ;;
        
    docker)
        print_success "Using Docker mode"
        echo "MCPs will run in Docker containers for better isolation."
        echo ""
        
        # Check for Docker
        if command -v docker &> /dev/null; then
            DOCKER_VERSION=$(docker --version)
            print_success "Docker installed: $DOCKER_VERSION"
            
            # Check if Docker is running
            if docker info &> /dev/null; then
                print_success "Docker is running"
            else
                print_error "Docker is not running! Please start Docker."
                exit 1
            fi
        else
            print_error "Docker not found! Please install Docker."
            echo "Visit: https://docs.docker.com/get-docker/"
            exit 1
        fi
        
        echo ""
        echo "Docker support coming soon!"
        echo "For now, please use 'local' mode or see the documentation."
        ;;
        
    systemd)
        print_success "Using systemd mode"
        echo "This mode is for advanced Linux users with a dedicated MCP server."
        echo ""
        echo "Please see the mcp-infra-manager repository for systemd setup."
        echo "Repository: https://github.com/yourusername/mcp-infra-manager"
        ;;
        
    *)
        print_error "Invalid MCP_MODE: $MCP_MODE"
        echo "Valid options: none, local, docker, systemd"
        exit 1
        ;;
esac

# Check PATH
print_header "PATH Configuration"
BIN_DIR="$(pwd)/bin"
if [[ ":$PATH:" == *":$BIN_DIR:"* ]]; then
    print_success "bin directory is in PATH"
else
    print_warning "bin directory is not in PATH"
    echo ""
    echo "Add this to your shell configuration (.bashrc, .zshrc, etc.):"
    echo "export PATH=\"$BIN_DIR:\$PATH\""
    echo ""
    echo "Or create aliases:"
    echo "alias ce='$BIN_DIR/context'"
    echo "alias cea='$BIN_DIR/context-auto'"
fi

# Summary
print_header "Setup Summary"

if [[ "${MCP_MODE:-none}" == "local" ]]; then
    echo "✓ Environment configured"
    echo "✓ MCP mode: ${MCP_MODE}"
    echo "✓ Directories created"
    
    if [[ "$install_mcps" =~ ^[Yy] ]]; then
        echo "✓ MCP services installed"
    fi
    
    echo ""
    echo "Next steps:"
    echo "1. Add your API keys to .env.mcp"
    echo "2. Test with: ce (or context)"
    echo "3. Use with Claude Code for enhanced capabilities"
else
    echo "✓ Environment configured"
    echo "✓ MCP mode: ${MCP_MODE:-none}"
    echo ""
    echo "Next steps:"
    echo "1. Test with: ce (or context)"
    echo "2. MCPs are optional - Context Engineer works without them"
fi

echo ""
print_success "Setup complete!"
echo ""
echo "For more information, see:"
echo "- README.md for general usage"
echo "- docs/MCP_INTEGRATION.md for MCP details"
echo "- docs/QUICK_START.md for Claude Code workflow"