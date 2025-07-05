#!/bin/bash

# Test script for Context Engineer CLI Tool

set -e

GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m'

echo "Testing Context Engineer CLI Tool..."

# Test 1: Check if main script exists and is executable
if [[ -x "bin/context" ]]; then
    echo -e "${GREEN}✅ Main script is executable${NC}"
else
    echo -e "${RED}❌ Main script not found or not executable${NC}"
    exit 1
fi

# Test 2: Check if all template files exist
required_files=(
    "templates/CLAUDE.md"
    "templates/PLANNING.md"
    "templates/TASK.md"
    "templates/.claude/commands/generate-prp.md"
    "templates/.claude/commands/execute-prp.md"
    "templates/examples/README.md"
)

all_good=true
for file in "${required_files[@]}"; do
    if [[ -f "$file" ]]; then
        echo -e "${GREEN}✅ Found: $file${NC}"
    else
        echo -e "${RED}❌ Missing: $file${NC}"
        all_good=false
    fi
done

if $all_good; then
    echo -e "\n${GREEN}All tests passed! The tool is ready to use.${NC}"
    echo -e "\nRun ${GREEN}./install.sh${NC} to install"
else
    echo -e "\n${RED}Some files are missing. Please check the installation.${NC}"
    exit 1
fi