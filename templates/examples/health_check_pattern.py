"""
Health Check Pattern

This module demonstrates how to implement comprehensive health checks
for monitoring system components and dependencies.
"""

import asyncio
from typing import Dict, List, Optional, Tuple
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class HealthStatus:
    """Enumeration of possible health states."""
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


class HealthCheck:
    """
    Base class for implementing health checks.
    
    All health checks should inherit from this class and implement
    the check() method.
    """
    
    def __init__(self, name: str, critical: bool = True):
        """
        Initialize health check.
        
        Args:
            name: Name of the component being checked
            critical: Whether failure should mark system unhealthy
        """
        self.name = name
        self.critical = critical
    
    async def check(self) -> Tuple[str, str]:
        """
        Perform the health check.
        
        Returns:
            Tuple of (status, message)
        """
        raise NotImplementedError("Subclasses must implement check()")


class DatabaseHealthCheck(HealthCheck):
    """Example health check for database connectivity."""
    
    def __init__(self, db_connection):
        super().__init__("database", critical=True)
        self.db = db_connection
    
    async def check(self) -> Tuple[str, str]:
        """Check database connectivity and response time."""
        try:
            start = datetime.now()
            # Simulate database ping
            await self.db.execute("SELECT 1")
            elapsed = (datetime.now() - start).total_seconds()
            
            if elapsed > 1.0:
                return (HealthStatus.DEGRADED, 
                       f"Slow response: {elapsed:.2f}s")
            
            return (HealthStatus.HEALTHY, 
                   f"Response time: {elapsed:.2f}s")
                   
        except Exception as e:
            logger.error(f"Database health check failed: {e}")
            return (HealthStatus.UNHEALTHY, str(e))


class ExternalAPIHealthCheck(HealthCheck):
    """Example health check for external API dependencies."""
    
    def __init__(self, api_client, endpoint: str):
        super().__init__("external_api", critical=False)
        self.api = api_client
        self.endpoint = endpoint
    
    async def check(self) -> Tuple[str, str]:
        """Check external API availability."""
        try:
            response = await self.api.get(self.endpoint)
            if response.status_code == 200:
                return (HealthStatus.HEALTHY, "API accessible")
            else:
                return (HealthStatus.DEGRADED, 
                       f"API returned {response.status_code}")
                       
        except Exception as e:
            return (HealthStatus.UNHEALTHY, 
                   f"API unreachable: {str(e)}")


class HealthMonitor:
    """
    Centralized health monitoring system.
    
    Manages multiple health checks and provides overall system status.
    """
    
    def __init__(self):
        """Initialize health monitor."""
        self.checks: List[HealthCheck] = []
        self.last_check_time: Optional[datetime] = None
        self.last_results: Dict[str, Tuple[str, str]] = {}
    
    def register_check(self, check: HealthCheck):
        """Register a new health check."""
        self.checks.append(check)
        logger.info(f"Registered health check: {check.name}")
    
    async def run_checks(self) -> Dict[str, any]:
        """
        Run all registered health checks.
        
        Returns:
            Dictionary with overall status and individual check results
        """
        logger.info("Running health checks...")
        self.last_check_time = datetime.now()
        
        # Run all checks concurrently
        results = await asyncio.gather(
            *[self._run_single_check(check) for check in self.checks],
            return_exceptions=True
        )
        
        # Process results
        check_results = {}
        overall_status = HealthStatus.HEALTHY
        critical_failures = []
        
        for check, result in zip(self.checks, results):
            if isinstance(result, Exception):
                status = HealthStatus.UNHEALTHY
                message = f"Check failed: {str(result)}"
            else:
                status, message = result
            
            check_results[check.name] = {
                "status": status,
                "message": message,
                "critical": check.critical
            }
            
            # Update overall status
            if status == HealthStatus.UNHEALTHY and check.critical:
                overall_status = HealthStatus.UNHEALTHY
                critical_failures.append(check.name)
            elif status == HealthStatus.DEGRADED and overall_status == HealthStatus.HEALTHY:
                overall_status = HealthStatus.DEGRADED
        
        # Store results
        self.last_results = check_results
        
        return {
            "status": overall_status,
            "timestamp": self.last_check_time.isoformat(),
            "checks": check_results,
            "critical_failures": critical_failures
        }
    
    async def _run_single_check(self, check: HealthCheck) -> Tuple[str, str]:
        """Run a single health check with timeout."""
        try:
            return await asyncio.wait_for(
                check.check(),
                timeout=5.0  # 5 second timeout per check
            )
        except asyncio.TimeoutError:
            return (HealthStatus.UNHEALTHY, "Check timed out")
    
    def get_status_summary(self) -> str:
        """Get a human-readable status summary."""
        if not self.last_results:
            return "No health checks have been run yet"
        
        healthy = sum(1 for r in self.last_results.values() 
                     if r["status"] == HealthStatus.HEALTHY)
        total = len(self.last_results)
        
        return f"Health Status: {healthy}/{total} checks passing"


# Example usage in an application
async def setup_health_monitoring(app_components):
    """
    Set up health monitoring for an application.
    
    Args:
        app_components: Dictionary of application components
    """
    monitor = HealthMonitor()
    
    # Register database check
    if "database" in app_components:
        db_check = DatabaseHealthCheck(app_components["database"])
        monitor.register_check(db_check)
    
    # Register API check
    if "api_client" in app_components:
        api_check = ExternalAPIHealthCheck(
            app_components["api_client"],
            "/health"
        )
        monitor.register_check(api_check)
    
    # Register custom checks
    class DiskSpaceCheck(HealthCheck):
        async def check(self) -> Tuple[str, str]:
            # Simulate disk space check
            free_space_gb = 50  # Would get actual value
            if free_space_gb < 10:
                return (HealthStatus.UNHEALTHY, 
                       f"Low disk space: {free_space_gb}GB")
            elif free_space_gb < 20:
                return (HealthStatus.DEGRADED, 
                       f"Disk space warning: {free_space_gb}GB")
            else:
                return (HealthStatus.HEALTHY, 
                       f"Disk space OK: {free_space_gb}GB")
    
    monitor.register_check(DiskSpaceCheck("disk_space"))
    
    return monitor


# FastAPI health endpoint example
async def health_endpoint(monitor: HealthMonitor):
    """
    Health check endpoint for web applications.
    
    Returns appropriate HTTP status codes based on health.
    """
    results = await monitor.run_checks()
    
    # Determine HTTP status code
    if results["status"] == HealthStatus.HEALTHY:
        status_code = 200
    elif results["status"] == HealthStatus.DEGRADED:
        status_code = 200  # Still return 200 for degraded
    else:
        status_code = 503  # Service unavailable
    
    return {
        "status_code": status_code,
        "body": results
    }


# CLI health check command example
async def health_check_command(monitor: HealthMonitor, format: str = "text"):
    """
    CLI command for checking system health.
    
    Args:
        monitor: Health monitor instance
        format: Output format (text, json, simple)
    """
    results = await monitor.run_checks()
    
    if format == "simple":
        # Simple one-line output
        if results["status"] == HealthStatus.HEALTHY:
            print("✅ All systems operational")
        elif results["status"] == HealthStatus.DEGRADED:
            print("⚠️  System degraded")
        else:
            print("❌ System unhealthy")
    
    elif format == "text":
        # Detailed text output
        print(f"\n🏥 Health Check Results")
        print(f"{'='*40}")
        print(f"Overall Status: {results['status'].upper()}")
        print(f"Checked at: {results['timestamp']}\n")
        
        for name, check in results["checks"].items():
            icon = {
                HealthStatus.HEALTHY: "✅",
                HealthStatus.DEGRADED: "⚠️",
                HealthStatus.UNHEALTHY: "❌"
            }[check["status"]]
            
            critical = "⚡" if check["critical"] else ""
            print(f"{icon} {name}{critical}: {check['message']}")
        
        if results["critical_failures"]:
            print(f"\n🚨 Critical failures: {', '.join(results['critical_failures'])}")
    
    else:
        # JSON output
        import json
        print(json.dumps(results, indent=2))