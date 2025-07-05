"""
Example: Project Structure and Module Organization

This module demonstrates how to organize Python code following Context Engineering patterns.
It shows the recommended structure for classes, functions, and documentation.
"""

from typing import Optional, List, Dict
from dataclasses import dataclass
from abc import ABC, abstractmethod
import logging

# Configure logging at module level
logger = logging.getLogger(__name__)


# Data models using dataclasses
@dataclass
class Task:
    """
    Example data model using dataclass for automatic __init__ and __repr__.
    
    Attributes:
        id: Unique identifier for the task
        title: Task title (required)
        description: Detailed description (optional)
        completed: Whether the task is done
    """
    id: str
    title: str
    description: Optional[str] = None
    completed: bool = False


# Abstract base class for defining interfaces
class StorageInterface(ABC):
    """Abstract interface for storage implementations."""
    
    @abstractmethod
    def save(self, task: Task) -> bool:
        """Save a task to storage."""
        pass
    
    @abstractmethod
    def load(self, task_id: str) -> Optional[Task]:
        """Load a task from storage."""
        pass


# Concrete implementation
class FileStorage(StorageInterface):
    """File-based storage implementation."""
    
    def __init__(self, base_path: str):
        """
        Initialize file storage.
        
        Args:
            base_path: Directory path for storing files
        """
        self.base_path = base_path
        logger.info(f"Initialized FileStorage at {base_path}")
    
    def save(self, task: Task) -> bool:
        """Save task to a JSON file."""
        # Implementation would go here
        logger.debug(f"Saving task {task.id}")
        return True
    
    def load(self, task_id: str) -> Optional[Task]:
        """Load task from JSON file."""
        # Implementation would go here
        logger.debug(f"Loading task {task_id}")
        return None


# Service layer
class TaskService:
    """
    Service layer for task operations.
    
    This demonstrates separation of concerns - business logic
    separate from storage implementation.
    """
    
    def __init__(self, storage: StorageInterface):
        """
        Initialize with a storage backend.
        
        Args:
            storage: Any implementation of StorageInterface
        """
        self.storage = storage
    
    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create a new task.
        
        Args:
            title: Task title
            description: Optional task description
            
        Returns:
            Created Task object
            
        Raises:
            ValueError: If title is empty
        """
        if not title:
            raise ValueError("Task title cannot be empty")
        
        # Generate ID (simplified for example)
        task_id = f"task_{len(title)}_{hash(title)}"
        
        task = Task(
            id=task_id,
            title=title,
            description=description
        )
        
        if self.storage.save(task):
            logger.info(f"Created task: {task.id}")
            return task
        else:
            raise RuntimeError("Failed to save task")


# Module-level function for common operations
def get_default_service() -> TaskService:
    """
    Factory function to create a service with default configuration.
    
    Returns:
        Configured TaskService instance
    """
    storage = FileStorage("/tmp/tasks")
    return TaskService(storage)


# Anti-pattern example (what NOT to do)
class BadExample:
    """
    ❌ ANTI-PATTERN: Don't put everything in one class.
    This violates single responsibility principle.
    """
    def __init__(self):
        self.tasks = []
        self.file_path = "/tmp/tasks.json"
        
    def create_task_and_save_and_email_and_log(self, title):
        # ❌ Too many responsibilities in one method
        pass