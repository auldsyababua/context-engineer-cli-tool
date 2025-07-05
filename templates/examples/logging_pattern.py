"""
Comprehensive Logging Pattern

This module demonstrates best practices for structured logging
across an application, including context, formatting, and levels.
"""

import logging
import json
import sys
from typing import Any, Dict, Optional
from datetime import datetime
from functools import wraps
import traceback


# Custom JSON formatter for structured logging
class StructuredJSONFormatter(logging.Formatter):
    """
    Custom formatter that outputs structured JSON logs.
    
    Includes contextual information like timestamp, level,
    module, function, and custom fields.
    """
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "message": record.getMessage(),
        }
        
        # Add exception info if present
        if record.exc_info:
            log_data["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": traceback.format_exception(*record.exc_info)
            }
        
        # Add custom fields from extra
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        if hasattr(record, "duration"):
            log_data["duration"] = record.duration
            
        return json.dumps(log_data)


# Console formatter for development
class ColoredConsoleFormatter(logging.Formatter):
    """
    Colored console formatter for better readability during development.
    """
    
    COLORS = {
        'DEBUG': '\033[36m',    # Cyan
        'INFO': '\033[32m',     # Green
        'WARNING': '\033[33m',  # Yellow
        'ERROR': '\033[31m',    # Red
        'CRITICAL': '\033[35m', # Magenta
    }
    RESET = '\033[0m'
    
    def format(self, record: logging.LogRecord) -> str:
        """Format with colors for console output."""
        levelname = record.levelname
        if levelname in self.COLORS:
            levelname_color = f"{self.COLORS[levelname]}{levelname}{self.RESET}"
            record.levelname = levelname_color
        
        # Format timestamp
        timestamp = datetime.fromtimestamp(record.created).strftime('%Y-%m-%d %H:%M:%S')
        
        # Build message
        message = f"{timestamp} | {record.levelname} | {record.name} | {record.getMessage()}"
        
        # Add context if available
        if hasattr(record, "user_id"):
            message += f" | user_id={record.user_id}"
            
        return message


def setup_logging(
    app_name: str,
    log_level: str = "INFO",
    log_file: Optional[str] = None,
    use_json: bool = True
) -> logging.Logger:
    """
    Set up comprehensive logging for the application.
    
    Args:
        app_name: Name of the application
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional log file path
        use_json: Whether to use JSON formatting
        
    Returns:
        Configured logger instance
    """
    # Create logger
    logger = logging.getLogger(app_name)
    logger.setLevel(getattr(logging, log_level.upper()))
    
    # Remove existing handlers
    logger.handlers = []
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    if use_json:
        console_handler.setFormatter(StructuredJSONFormatter())
    else:
        console_handler.setFormatter(ColoredConsoleFormatter())
    logger.addHandler(console_handler)
    
    # File handler if specified
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(StructuredJSONFormatter())
        logger.addHandler(file_handler)
    
    # Log startup
    logger.info(
        f"Logging initialized for {app_name}",
        extra={"log_level": log_level, "log_file": log_file}
    )
    
    return logger


# Context manager for adding request context
class LogContext:
    """
    Context manager for adding contextual information to logs.
    
    Usage:
        with LogContext(user_id=123, request_id="abc"):
            logger.info("Processing request")
    """
    
    def __init__(self, **kwargs):
        """Initialize with context fields."""
        self.context = kwargs
        self.logger = logging.getLogger()
        self.old_factory = None
    
    def __enter__(self):
        """Enter context and inject fields."""
        old_factory = logging.getLogRecordFactory()
        
        def record_factory(*args, **factory_kwargs):
            record = old_factory(*args, **factory_kwargs)
            for key, value in self.context.items():
                setattr(record, key, value)
            return record
        
        logging.setLogRecordFactory(record_factory)
        self.old_factory = old_factory
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Restore original factory."""
        if self.old_factory:
            logging.setLogRecordFactory(self.old_factory)


# Decorator for automatic function logging
def log_function_call(logger: logging.Logger, level: int = logging.DEBUG):
    """
    Decorator that logs function calls with arguments and results.
    
    Args:
        logger: Logger instance to use
        level: Log level for the messages
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Log function entry
            logger.log(
                level,
                f"Calling {func.__name__}",
                extra={
                    "function": func.__name__,
                    "args": str(args)[:100],  # Truncate long args
                    "kwargs": str(kwargs)[:100]
                }
            )
            
            start_time = datetime.now()
            try:
                result = func(*args, **kwargs)
                duration = (datetime.now() - start_time).total_seconds()
                
                # Log successful completion
                logger.log(
                    level,
                    f"Completed {func.__name__}",
                    extra={
                        "function": func.__name__,
                        "duration": duration,
                        "result_type": type(result).__name__
                    }
                )
                return result
                
            except Exception as e:
                duration = (datetime.now() - start_time).total_seconds()
                
                # Log error
                logger.error(
                    f"Error in {func.__name__}: {str(e)}",
                    exc_info=True,
                    extra={
                        "function": func.__name__,
                        "duration": duration,
                        "error_type": type(e).__name__
                    }
                )
                raise
        
        return wrapper
    return decorator


# Application-specific loggers
class AppLogger:
    """
    Application logger with domain-specific methods.
    
    Provides convenient methods for common logging scenarios.
    """
    
    def __init__(self, logger: logging.Logger):
        """Initialize with base logger."""
        self.logger = logger
    
    def log_user_action(self, user_id: int, action: str, details: Dict[str, Any]):
        """Log user actions for audit trail."""
        self.logger.info(
            f"User action: {action}",
            extra={
                "user_id": user_id,
                "action": action,
                "details": details,
                "timestamp": datetime.utcnow().isoformat()
            }
        )
    
    def log_api_request(self, method: str, endpoint: str, status: int, duration: float):
        """Log API requests for monitoring."""
        level = logging.INFO if status < 400 else logging.WARNING
        self.logger.log(
            level,
            f"{method} {endpoint} - {status}",
            extra={
                "method": method,
                "endpoint": endpoint,
                "status": status,
                "duration": duration
            }
        )
    
    def log_database_query(self, query: str, duration: float, rows: int):
        """Log database queries for performance monitoring."""
        # Sanitize query for logging
        sanitized_query = query[:200] + "..." if len(query) > 200 else query
        
        self.logger.debug(
            "Database query executed",
            extra={
                "query": sanitized_query,
                "duration": duration,
                "rows_affected": rows
            }
        )
    
    def log_validation_error(self, field: str, value: Any, error: str):
        """Log validation errors for debugging."""
        self.logger.warning(
            f"Validation error on field '{field}'",
            extra={
                "field": field,
                "value": str(value)[:100],  # Truncate
                "error": error
            }
        )
    
    def log_integration_event(self, service: str, event: str, success: bool, details: Dict):
        """Log external service integration events."""
        level = logging.INFO if success else logging.ERROR
        self.logger.log(
            level,
            f"Integration event: {service} - {event}",
            extra={
                "service": service,
                "event": event,
                "success": success,
                "details": details
            }
        )


# Example usage in an application
def example_application():
    """Example of comprehensive logging in an application."""
    
    # Set up logging
    logger = setup_logging(
        app_name="my_app",
        log_level="DEBUG",
        log_file="app.log",
        use_json=False  # Use colored console for development
    )
    
    # Create app logger
    app_logger = AppLogger(logger)
    
    # Example: User action logging
    with LogContext(user_id=123, session_id="abc123"):
        app_logger.log_user_action(
            user_id=123,
            action="create_todo",
            details={"title": "Buy groceries", "priority": "high"}
        )
    
    # Example: Function logging
    @log_function_call(logger)
    def process_data(data: list) -> dict:
        """Process some data."""
        logger.info(f"Processing {len(data)} items")
        # Simulate processing
        return {"processed": len(data)}
    
    # Example: Error handling with context
    try:
        result = process_data([1, 2, 3, 4, 5])
    except Exception as e:
        logger.error(
            "Failed to process data",
            exc_info=True,
            extra={"context": "batch_processing"}
        )
    
    # Example: Performance logging
    import time
    start = time.time()
    # Simulate database query
    time.sleep(0.1)
    duration = time.time() - start
    
    app_logger.log_database_query(
        query="SELECT * FROM users WHERE active = true",
        duration=duration,
        rows=42
    )


if __name__ == "__main__":
    example_application()