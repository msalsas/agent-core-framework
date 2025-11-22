from typing import Dict, Any
import time
import logging
from .base_agent import BaseAgent
from .models import AgentTask, AgentResponse
from .service_registry import ServiceRegistry

class MultiAgentOrchestrator:

    def __init__(self, system_name: str = "MultiAgentSystem"):
        self.system_name = system_name
        self.registry = ServiceRegistry()
        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(f"agent_framework.{self.system_name}")
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger

    def register_agent(self, agent: BaseAgent) -> None:
        for task_type in agent.supported_tasks:
            self.registry.register_service(task_type, agent)
        self.logger.info(f"Agent registered: {agent.name} for tasks: {agent.supported_tasks}")

    def process_task(self, task: AgentTask) -> AgentResponse:
        start_time = time.time()

        self.logger.info(f"Processing task: {task.type} (ID: {task.id})")

        capable_agents = self.registry.get_services(task.type)

        if not capable_agents:
            self.logger.warning(f"No agents registered for task: {task.type}")
            return AgentResponse(
                success=False,
                error=f"No agents capable to handle task: {task.type}",
                agent_name="orchestrator",
                task_id=task.id
            )

        selected_agent = capable_agents[0]

        self.logger.info(f"Delegating task to agent: {selected_agent.name}")

        try:
            response = selected_agent.process(task)
            response.execution_time = time.time() - start_time
            response.task_id = task.id

            self.logger.info(
                f"Task completed for agent: {selected_agent.name} "
                f"(success: {response.success}, time: {response.execution_time:.2f}s)"
            )

            return response

        except Exception as e:
            self.logger.error(f"Error in agent {selected_agent.name}: {str(e)}")
            return AgentResponse(
                success=False,
                error=f"Error in agent {selected_agent.name}: {str(e)}",
                agent_name=selected_agent.name,
                execution_time=time.time() - start_time,
                task_id=task.id
            )

    def get_system_status(self) -> Dict[str, Any]:
        all_agents = set()
        for agents in self.registry._services.values():
            all_agents.update(agents)

        agents_info = {}
        for agent in all_agents:
            agents_info[agent.name] = agent.get_info()

        return {
            "system_name": self.system_name,
            "total_agents": len(all_agents),
            "supported_tasks": list(self.registry.get_all_task_types()),
            "agents": agents_info
        }