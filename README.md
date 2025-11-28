# Agent Core Framework

Lightweight framework for multi-agent systems with optional LangChain support.

A small, extensible package to register, orchestrate and implement agents that process tasks in a coordinated way.

## Features

- Registration and orchestration of multiple agents.
- Simple base interface to implement custom agents.
- Extension points to integrate LLMs (for example, via LangChain adapters).
- Unit tests included for core components.

## Installation

Install from PyPI:

```bash
pip install agent-core-framework
```

Install from the repository (editable mode):

```bash
git clone https://github.com/msalsas/agent-core-framework.git
cd agent-core-framework
pip install -e .
```

## Quick example

```python
from agent_core_framework import BaseAgent, AgentResponse, AgentTask, MultiAgentOrchestrator

class MyAgent(BaseAgent):
    def __init__(self, name: str):
        super().__init__(name)
        # declare the task types this agent can handle
        self.supported_tasks = ["simple"]

    def process(self, task: AgentTask) -> AgentResponse:
        # Simple implementation: return success with data and the agent name
        return AgentResponse(success=True, data={"result": "ok"}, agent_name=self.name, task_id=task.id)

orchestrator = MultiAgentOrchestrator()
my_agent = MyAgent("my-agent")
orchestrator.register_agent(my_agent)

# Create a task using AgentTask
task = AgentTask(type="simple", payload={"value": 42})
response = orchestrator.process_task(task)
print(response.json())
```

This example shows the basic idea: implement `process` in agents, register them into a `MultiAgentOrchestrator`, and process tasks with `process_task`.

## API summary

- `BaseAgent` — Base class to implement agents. Implement `process(self, task)` and provide `name` in the constructor.
- `AgentResponse` — Standard response structure: `success: bool`, `data: dict`, `error: Optional[str]`, `agent_name: str`.
- `AgentTask` — Representation of the task sent to an agent (use `AgentTask(type=..., payload=...)`).
- `MultiAgentOrchestrator` — Orchestrator to register agents (`register_agent(agent)`) and process tasks (`process_task(task)`).
- `ServiceRegistry` — Central registry for agents/services (if applicable).

See the source code under `agent_core_framework/` for exact names and signatures.

## LangChain integration

The project is designed to allow adapters that wrap LLMs or prompt chains. To integrate LangChain:

1. Create an agent that uses the LangChain client API inside its `process` method.
2. Register that agent in the `MultiAgentOrchestrator` like any other agent.

This makes it easy to combine LLMs with programmatic logic and orchestration across multiple agents.

## Running tests

Dependencies are declared in `pyproject.toml`. Use your project's chosen tool to install them:

- With Poetry (recommended if you use Poetry):

```bash
poetry install
poetry run pytest -q
```

- With pip (install package and pytest manually):

```bash
pip install -e .         # installs the package; does not install dev deps from pyproject
pip install pytest       # install pytest separately
pytest -q
```

If your workflow uses another tool (pip-tools, pipx, tox, etc.), use the corresponding commands to install dev dependencies before running `pytest`.

(There are tests in the `tests/` folder — run `pytest` to check them.)

## Best practices

- Wrap errors in `AgentResponse` so the orchestrator can handle failures.
- Keep `process` as deterministic as possible; extract I/O calls to make testing easier.
- Add unit tests when you add agents or critical logic.

## Contributing

1. Open an issue describing your proposal or bug.
2. Create a branch `feature/my-change` or `fix/my-bug`.
3. Add tests and documentation where applicable.
4. Open a pull request and describe your changes.

## License

MIT — see the `LICENSE` file.
