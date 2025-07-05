#!/bin/bash

# Context Engineer CLI Tool - Installation Script

set -e

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

print_header() {
    echo -e "\n${BLUE}══════════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}$1${NC}"
    echo -e "${BLUE}══════════════════════════════════════════════════════════════${NC}\n"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

print_header "Context Engineer CLI Tool - Installation"

# Check if running from the right directory
if [[ ! -f "$SCRIPT_DIR/bin/context" ]]; then
    print_error "Installation script must be run from the context-engineer-cli-tool directory"
    exit 1
fi

# Make the scripts executable
chmod +x "$SCRIPT_DIR/bin/context"
chmod +x "$SCRIPT_DIR/bin/context-auto"
chmod +x "$SCRIPT_DIR/bin/context-mcp"
print_success "Made scripts executable"

# Detect shell
if [[ -n "$ZSH_VERSION" ]]; then
    SHELL_RC="$HOME/.zshrc"
    SHELL_NAME="zsh"
elif [[ -n "$BASH_VERSION" ]]; then
    SHELL_RC="$HOME/.bashrc"
    SHELL_NAME="bash"
else
    print_error "Unsupported shell. Please manually add $SCRIPT_DIR/bin to your PATH"
    exit 1
fi

print_success "Detected $SHELL_NAME shell"

# Check for jq (required for context-mcp)
if ! command -v jq &> /dev/null; then
    echo -e "${YELLOW}⚠️  jq is not installed (required for context-mcp)${NC}"
    echo "Install with:"
    echo "  macOS: brew install jq"
    echo "  Ubuntu/Debian: sudo apt-get install jq"
    echo "  Other: https://stedolan.github.io/jq/download/"
else
    print_success "jq is installed (required for MCP manager)"
fi

# Check if already in PATH
if echo "$PATH" | grep -q "$SCRIPT_DIR/bin"; then
    print_success "Directory already in PATH"
else
    # Add to PATH in shell RC file
    echo "" >> "$SHELL_RC"
    echo "# Context Engineer CLI Tool" >> "$SHELL_RC"
    echo "export PATH=\"$SCRIPT_DIR/bin:\$PATH\"" >> "$SHELL_RC"
    print_success "Added to PATH in $SHELL_RC"
fi

# Create aliases (optional but convenient)
if ! grep -q "alias ce=" "$SHELL_RC" 2>/dev/null; then
    echo "alias ce='context'" >> "$SHELL_RC"
    print_success "Created 'ce' alias for quick access"
fi

if ! grep -q "alias cea=" "$SHELL_RC" 2>/dev/null; then
    echo "alias cea='context-auto'" >> "$SHELL_RC"
    print_success "Created 'cea' alias for auto-pilot mode"
fi

if ! grep -q "alias cem=" "$SHELL_RC" 2>/dev/null; then
    echo "alias cem='context-mcp'" >> "$SHELL_RC"
    print_success "Created 'cem' alias for MCP manager"
fi

# Installation complete
print_header "✅ Installation Complete!"

echo "To start using Context Engineer CLI Tool:"
echo ""
echo "1. Reload your shell configuration:"
echo -e "   ${YELLOW}source $SHELL_RC${NC}"
echo ""
echo "2. Run the tool:"
echo -e "   ${YELLOW}context${NC}      (standard setup)"
echo -e "   ${YELLOW}context-auto${NC} (auto-pilot mode)"
echo -e "   ${YELLOW}context-mcp${NC}  (MCP manager)"
echo -e "   ${YELLOW}ce${NC}           (alias for context)"
echo -e "   ${YELLOW}cea${NC}          (alias for context-auto)"
echo -e "   ${YELLOW}cem${NC}          (alias for context-mcp)"
echo ""
echo "3. For help:"
echo -e "   ${YELLOW}context --help${NC}"

# Offer to reload shell now
echo ""
read -p "Reload shell configuration now? (y/n) [y]: " reload_now
reload_now=${reload_now:-y}

if [[ "$reload_now" == "y" ]]; then
    export PATH="$SCRIPT_DIR/bin:$PATH"
    alias ce='context'
    alias cea='context-auto'
    alias cem='context-mcp'
    print_success "Shell configuration reloaded. You can now use all commands!"
else
    echo -e "\n${YELLOW}Remember to run: source $SHELL_RC${NC}"
fi