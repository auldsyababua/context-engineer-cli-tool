"""
Agent-Based Architecture Pattern

This module demonstrates the recommended agent/tools/prompts structure
used for building modular, maintainable AI-powered applications.
"""

# Example structure for an agent-based system:
# agent.py - Main orchestration and coordination
# tools.py - Operational functions the agent uses
# prompts.py - All text templates and system prompts

# ============= agent.py =============
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class MainAgent:
    """
    Main agent that orchestrates the application logic.
    
    Coordinates between user input, tools, and responses while
    maintaining separation of concerns.
    """
    
    def __init__(self, config, tools, prompts):
        """
        Initialize agent with required components.
        
        Args:
            config: Application configuration
            tools: Tool collection for operations
            prompts: System prompts and templates
        """
        self.config = config
        self.tools = tools
        self.prompts = prompts
        logger.info("Agent initialized successfully")
    
    async def process_request(self, user_input: str) -> str:
        """
        Process user request and coordinate response.
        
        Args:
            user_input: Raw user input
            
        Returns:
            Formatted response for the user
        """
        try:
            # Parse intent
            intent = await self._parse_intent(user_input)
            
            # Route to appropriate tool
            result = await self._route_to_tool(intent)
            
            # Format response
            response = self.prompts.format_response(intent.type, result)
            
            logger.info(f"Processed {intent.type} request successfully")
            return response
            
        except Exception as e:
            logger.error(f"Error processing request: {e}")
            return self.prompts.get_error_message()


# ============= tools.py =============
class OperationalTools:
    """
    Collection of tools for performing operations.
    
    Provides high-level operations that the agent uses to interact
    with the business logic and external systems.
    """
    
    def __init__(self, storage, external_api):
        """
        Initialize tools with required dependencies.
        
        Args:
            storage: Data storage backend
            external_api: External API client
        """
        self.storage = storage
        self.api = external_api
        logger.info("Tools initialized")
    
    async def create_item(self, data: dict) -> dict:
        """
        Create a new item with validation.
        
        Args:
            data: Item data
            
        Returns:
            Created item with ID
        """
        # Validate data
        validated = self._validate_item_data(data)
        
        # Store item
        item = await self.storage.save(validated)
        
        # Log for audit
        logger.info(f"Created item {item['id']}")
        
        return item
    
    async def search_items(self, query: str) -> list:
        """
        Search for items matching query.
        
        Args:
            query: Search query
            
        Returns:
            List of matching items
        """
        results = await self.storage.search(query)
        logger.info(f"Found {len(results)} items for query: {query}")
        return results


# ============= prompts.py =============
class SystemPrompts:
    """
    Centralized system prompts and message templates.
    
    Maintains all user-facing text for consistency and easy
    localization or customization.
    """
    
    def __init__(self, app_name: str = "MyApp"):
        """Initialize with application name."""
        self.app_name = app_name
        self.version = "1.0.0"
    
    def get_welcome_message(self) -> str:
        """Get welcome message for new users."""
        return (
            f"🎉 Welcome to {self.app_name}!\n\n"
            f"I'm here to help you manage your workflow.\n"
            f"Type 'help' to see available commands."
        )
    
    def get_error_message(self, error_type: str = "general") -> str:
        """Get error message by type."""
        messages = {
            "general": "❌ Something went wrong. Please try again.",
            "not_found": "❓ Item not found. Please check and try again.",
            "validation": "⚠️ Invalid input. Please check your data."
        }
        return messages.get(error_type, messages["general"])
    
    def format_response(self, action: str, data: dict) -> str:
        """Format response based on action and data."""
        if action == "create":
            return f"✅ Created successfully!\nID: {data['id']}"
        elif action == "search":
            return f"🔍 Found {len(data)} results"
        else:
            return "✅ Operation completed"