from typing import Dict, Any, List, Optional


try:
    from langchain.agents import AgentExecutor, create_react_agent
    from langchain.tools import BaseTool
    from langchain.llms.base import BaseLLM
    from langchain import hub

    LANGCHAIN_AVAILABLE = True
except ImportError:
    LANGCHAIN_AVAILABLE = False
    AgentExecutor = object
    BaseTool = object
    BaseLLM = object

from .base_agent import BaseAgent
from .models import AgentTask, AgentResponse

class LangChainBaseAgent(BaseAgent):

    def __init__(
            self,
            name: str,
            tools: List[BaseTool],
            llm: BaseLLM,
            agent_type: str = "react",
            supported_tasks: Optional[List[str]] = None
    ):
        if not LANGCHAIN_AVAILABLE:
            raise ImportError("LangChain is not available. Install it with: pip install langchain")

        super().__init__(name)

        if agent_type == "react":
            prompt = hub.pull("hwchase17/react")
            self.agent_executor = create_react_agent(llm, tools, prompt)
        else:
            self.agent_executor = None

        self.supported_tasks = supported_tasks or []
        self.llm = llm
        self.tools = tools

    def process(self, task: AgentTask) -> AgentResponse:
        if not self.agent_executor:
            return AgentResponse(
                success=False,
                error="LangChain agent not properly initialized",
                agent_name=self.name
            )

        try:
            result = self.agent_executor.invoke({
                "input": self._build_agent_input(task),
                **task.payload
            })

            return AgentResponse(
                success=True,
                data={
                    "output": result["output"],
                    "intermediate_steps": result.get("intermediate_steps", [])
                },
                agent_name=self.name
            )

        except Exception as e:
            return AgentResponse(
                success=False,
                error=str(e),
                agent_name=self.name
            )

    def _build_agent_input(self, task: AgentTask) -> str:
        return f"Task: {task.type}. Data: {task.payload}"