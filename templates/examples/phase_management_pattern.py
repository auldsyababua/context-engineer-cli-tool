"""
Phase Management Pattern

This module demonstrates how to implement phase-aware development
with feature flags and progressive enhancement.
"""

import os
from typing import Dict, List, Optional, Callable, Any
from functools import wraps
from dataclasses import dataclass
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class Phase:
    """
    Represents a development phase with its requirements and features.
    """
    number: int
    name: str
    description: str
    features: List[str]
    dependencies: List[int]  # Phase numbers this depends on
    validation_criteria: List[str]
    completed: bool = False
    completed_date: Optional[datetime] = None


class PhaseManager:
    """
    Manages application phases and feature availability.
    
    Provides phase-aware feature flags and ensures proper
    progression through development phases.
    """
    
    def __init__(self):
        """Initialize phase manager."""
        self.phases: Dict[int, Phase] = {}
        self.current_phase: int = 1
        self._load_phase_config()
    
    def _load_phase_config(self):
        """Load phase configuration from environment or defaults."""
        # In a real app, this might load from a config file
        self.phases = {
            1: Phase(
                number=1,
                name="MVP",
                description="Basic functionality with local storage",
                features=["basic_crud", "local_storage", "simple_ui"],
                dependencies=[],
                validation_criteria=[
                    "All CRUD operations work",
                    "Data persists between restarts",
                    "Basic UI is functional"
                ]
            ),
            2: Phase(
                number=2,
                name="Database Integration",
                description="Replace local storage with database",
                features=["database_storage", "user_management", "data_migration"],
                dependencies=[1],
                validation_criteria=[
                    "Database connection established",
                    "All CRUD operations work with DB",
                    "Data migration completed"
                ]
            ),
            3: Phase(
                number=3,
                name="Advanced Features",
                description="Add advanced functionality",
                features=["search", "filtering", "bulk_operations", "api"],
                dependencies=[1, 2],
                validation_criteria=[
                    "Search functionality works",
                    "API endpoints tested",
                    "Performance benchmarks met"
                ]
            )
        }
        
        # Load current phase from environment
        self.current_phase = int(os.getenv("CURRENT_PHASE", "1"))
        
        # Mark completed phases
        for phase_num in range(1, self.current_phase + 1):
            if phase_num in self.phases:
                self.phases[phase_num].completed = True
    
    def is_feature_enabled(self, feature: str) -> bool:
        """
        Check if a feature is enabled in the current phase.
        
        Args:
            feature: Feature name to check
            
        Returns:
            True if feature is available in current or previous phases
        """
        for phase_num in range(1, self.current_phase + 1):
            if phase_num in self.phases:
                if feature in self.phases[phase_num].features:
                    return True
        return False
    
    def get_enabled_features(self) -> List[str]:
        """Get list of all currently enabled features."""
        features = []
        for phase_num in range(1, self.current_phase + 1):
            if phase_num in self.phases:
                features.extend(self.phases[phase_num].features)
        return features
    
    def validate_phase_progression(self, target_phase: int) -> bool:
        """
        Validate that we can progress to a target phase.
        
        Args:
            target_phase: Phase number to progress to
            
        Returns:
            True if progression is valid
        """
        if target_phase not in self.phases:
            logger.error(f"Unknown phase: {target_phase}")
            return False
        
        phase = self.phases[target_phase]
        
        # Check dependencies
        for dep in phase.dependencies:
            if dep not in self.phases or not self.phases[dep].completed:
                logger.error(
                    f"Cannot progress to phase {target_phase}: "
                    f"Dependency phase {dep} not completed"
                )
                return False
        
        # Check that previous phase is completed
        if target_phase > 1:
            prev_phase = target_phase - 1
            if prev_phase in self.phases and not self.phases[prev_phase].completed:
                logger.error(
                    f"Cannot progress to phase {target_phase}: "
                    f"Previous phase {prev_phase} not completed"
                )
                return False
        
        return True
    
    def mark_phase_complete(self, phase_num: int) -> bool:
        """
        Mark a phase as completed.
        
        Args:
            phase_num: Phase number to mark complete
            
        Returns:
            True if successfully marked
        """
        if phase_num not in self.phases:
            return False
        
        self.phases[phase_num].completed = True
        self.phases[phase_num].completed_date = datetime.now()
        
        logger.info(f"Phase {phase_num} marked as complete")
        return True
    
    def get_phase_status(self) -> Dict[str, Any]:
        """Get comprehensive phase status information."""
        return {
            "current_phase": self.current_phase,
            "enabled_features": self.get_enabled_features(),
            "phases": {
                num: {
                    "name": phase.name,
                    "completed": phase.completed,
                    "features": phase.features
                }
                for num, phase in self.phases.items()
            }
        }


# Decorator for phase-aware features
def requires_phase(min_phase: int):
    """
    Decorator that restricts function access based on phase.
    
    Args:
        min_phase: Minimum phase required for this feature
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get phase manager (in real app, this might be injected)
            pm = PhaseManager()
            
            if pm.current_phase < min_phase:
                raise RuntimeError(
                    f"Feature '{func.__name__}' requires phase {min_phase} "
                    f"(current phase: {pm.current_phase})"
                )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Feature flag decorator
def feature_flag(feature_name: str, fallback: Optional[Callable] = None):
    """
    Decorator that checks if a feature is enabled.
    
    Args:
        feature_name: Name of the feature to check
        fallback: Optional fallback function if feature is disabled
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            pm = PhaseManager()
            
            if pm.is_feature_enabled(feature_name):
                return func(*args, **kwargs)
            elif fallback:
                logger.info(
                    f"Feature '{feature_name}' disabled, using fallback"
                )
                return fallback(*args, **kwargs)
            else:
                raise RuntimeError(
                    f"Feature '{feature_name}' is not enabled in current phase"
                )
        return wrapper
    return decorator


# Example storage implementations showing phase progression
class StorageInterface:
    """Base storage interface."""
    
    async def save(self, key: str, data: dict) -> bool:
        raise NotImplementedError
    
    async def load(self, key: str) -> Optional[dict]:
        raise NotImplementedError


class LocalStorage(StorageInterface):
    """Phase 1: Local file storage."""
    
    async def save(self, key: str, data: dict) -> bool:
        logger.info(f"Saving to local storage: {key}")
        # Implementation
        return True
    
    async def load(self, key: str) -> Optional[dict]:
        logger.info(f"Loading from local storage: {key}")
        # Implementation
        return {}


class DatabaseStorage(StorageInterface):
    """Phase 2: Database storage."""
    
    @requires_phase(2)
    async def save(self, key: str, data: dict) -> bool:
        logger.info(f"Saving to database: {key}")
        # Implementation
        return True
    
    @requires_phase(2)
    async def load(self, key: str) -> Optional[dict]:
        logger.info(f"Loading from database: {key}")
        # Implementation
        return {}


# Phase-aware factory
class StorageFactory:
    """
    Factory that returns appropriate storage based on current phase.
    """
    
    @staticmethod
    def get_storage() -> StorageInterface:
        """Get storage implementation for current phase."""
        pm = PhaseManager()
        
        if pm.is_feature_enabled("database_storage"):
            logger.info("Using database storage")
            return DatabaseStorage()
        else:
            logger.info("Using local storage")
            return LocalStorage()


# Example application with phase-aware features
class TodoApp:
    """
    Example application showing phase-aware development.
    """
    
    def __init__(self):
        """Initialize with phase-appropriate components."""
        self.storage = StorageFactory.get_storage()
        self.pm = PhaseManager()
    
    async def create_todo(self, title: str, description: str) -> dict:
        """Create a todo item (available in all phases)."""
        todo = {
            "id": "todo_123",
            "title": title,
            "description": description,
            "created_at": datetime.now().isoformat()
        }
        
        await self.storage.save(todo["id"], todo)
        return todo
    
    @feature_flag("search")
    async def search_todos(self, query: str) -> List[dict]:
        """Search todos (Phase 3+ only)."""
        logger.info(f"Searching todos with query: {query}")
        # Advanced search implementation
        return []
    
    @feature_flag("bulk_operations")
    async def bulk_update(self, updates: List[dict]) -> int:
        """Bulk update todos (Phase 3+ only)."""
        logger.info(f"Bulk updating {len(updates)} todos")
        # Bulk update implementation
        return len(updates)
    
    @feature_flag("api", fallback=lambda self: {"error": "API not available"})
    def get_api_info(self) -> dict:
        """Get API information (Phase 3+ with fallback)."""
        return {
            "version": "1.0",
            "endpoints": ["/todos", "/search", "/bulk"]
        }
    
    def get_app_info(self) -> dict:
        """Get application information with phase details."""
        return {
            "app": "TodoApp",
            "phase": self.pm.current_phase,
            "features": self.pm.get_enabled_features(),
            "storage_type": type(self.storage).__name__
        }


# Phase validation script
async def validate_current_phase():
    """
    Validate that current phase meets all criteria.
    """
    pm = PhaseManager()
    current = pm.phases.get(pm.current_phase)
    
    if not current:
        logger.error(f"Invalid current phase: {pm.current_phase}")
        return False
    
    print(f"\n🔍 Validating Phase {current.number}: {current.name}")
    print("=" * 50)
    
    # Check each validation criterion
    all_valid = True
    for criterion in current.validation_criteria:
        # In real app, these would be actual tests
        valid = True  # Simulate validation
        status = "✅" if valid else "❌"
        print(f"{status} {criterion}")
        all_valid &= valid
    
    if all_valid:
        print(f"\n✅ Phase {current.number} validation PASSED")
    else:
        print(f"\n❌ Phase {current.number} validation FAILED")
    
    return all_valid


# Example usage
async def example_usage():
    """Example of using phase-aware features."""
    
    # Initialize app
    app = TodoApp()
    
    # Show current state
    info = app.get_app_info()
    print(f"App Info: {info}")
    
    # Basic feature (available in all phases)
    todo = await app.create_todo("Test", "Test todo")
    print(f"Created todo: {todo}")
    
    # Try advanced features
    try:
        # This will only work in phase 3+
        results = await app.search_todos("test")
        print(f"Search results: {results}")
    except RuntimeError as e:
        print(f"Search not available: {e}")
    
    # API info with fallback
    api_info = app.get_api_info()
    print(f"API Info: {api_info}")
    
    # Validate current phase
    await validate_current_phase()


if __name__ == "__main__":
    import asyncio
    asyncio.run(example_usage())