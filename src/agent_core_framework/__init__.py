from .base_agent import BaseAgent
from .models import AgentTask, AgentResponse
from .orchestrator import MultiAgentOrchestrator
from .service_registry import ServiceRegistry

try:
    from .langchain_integration import LangChainBaseAgent
    __all__ = [
        "BaseAgent", "AgentTask", "AgentResponse", 
        "MultiAgentOrchestrator", "ServiceRegistry", "LangChainBaseAgent"
    ]
except ImportError:
    __all__ = [
        "BaseAgent", "AgentTask", "AgentResponse",
        "MultiAgentOrchestrator", "ServiceRegistry"
    ]

try:
    from importlib.metadata import version
    __version__ = version("agent-core-framework")
except ImportError:
    __version__ = "0.1.0-dev"