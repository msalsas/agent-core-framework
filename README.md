# Agent Core Framework

Multi-agent systems framework with LangChain support.

## Installation

```bash
pip install agent-core-framework
```

## Use case

```python
from agent_core_framework import BaseAgent, AgentTask, MultiAgentOrchestrator

class MyAgent(BaseAgent):
    def process(self, task):
        return AgentResponse(success=True, data={"result": "ok"})

orchestrator = MultiAgentOrchestrator()
orchestrator.register_agent(MyAgent())
```
