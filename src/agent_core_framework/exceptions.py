class AgentCoreFrameworkError(Exception):
    """Base exception for the framework"""
    pass

class AgentNotFoundError(AgentCoreFrameworkError):
    """Raised when no agent can handle a task"""
    pass

class AgentExecutionError(AgentCoreFrameworkError):
    """Raised when an agent fails to process a task"""
    pass

class ConfigurationError(AgentCoreFrameworkError):
    """Raised for configuration issues"""
    pass