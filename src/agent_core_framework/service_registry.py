from typing import Dict, List, Set
from .base_agent import BaseAgent
from collections import defaultdict

class ServiceRegistry:

    def __init__(self):
        self._services: Dict[str, List[BaseAgent]] = defaultdict(list)

    def register_service(self, task_type: str, agent: BaseAgent) -> None:
        if agent not in self._services[task_type]:
            self._services[task_type].append(agent)

    def get_services(self, task_type: str) -> List[BaseAgent]:
        return self._services[task_type].copy()

    def get_all_task_types(self) -> Set[str]:
        return set(self._services.keys())