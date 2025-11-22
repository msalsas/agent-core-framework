from abc import ABC, abstractmethod
from typing import Dict, Any, List
from .models import AgentTask, AgentResponse


class BaseAgent(ABC):
    def __init__(self, name: str, version: str = "1.0.0"):
        self.name = name
        self.version = version
        self.supported_tasks: List[str] = []

    @abstractmethod
    def process(self, task: AgentTask) -> AgentResponse:
        pass

    def get_info(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "version": self.version,
            "supported_tasks": self.supported_tasks,
            "status": "healthy"
        }

    def can_handle(self, task_type: str) -> bool:
        return task_type in self.supported_tasks