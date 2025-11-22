from agent_core_framework import BaseAgent, AgentTask, AgentResponse


class ConcreteTestAgent(BaseAgent):

    def __init__(self):
        super().__init__("TestAgent", "1.0.0")
        self.supported_tasks = ["test_task", "another_task"]

    def process(self, task: AgentTask) -> AgentResponse:
        return AgentResponse(
            success=True,
            data={"processed": True, "task_type": task.type},
            agent_name=self.name
        )


def test_agent_creation():

    agent = ConcreteTestAgent()

    assert agent.name == "TestAgent"
    assert agent.version == "1.0.0"
    assert agent.supported_tasks == ["test_task", "another_task"]
    assert agent.can_handle("test_task") is True
    assert agent.can_handle("unknown_task") is False
    print("✅ test_agent_creation passed")


def test_agent_process():

    agent = ConcreteTestAgent()
    task = AgentTask(type="test_task", payload={"data": "test"})

    response = agent.process(task)

    assert response.success is True
    assert response.agent_name == "TestAgent"
    assert response.data["processed"] is True
    assert response.data["task_type"] == "test_task"
    print("✅ test_agent_process passed")


def test_agent_info():

    agent = ConcreteTestAgent()
    info = agent.get_info()

    assert info["name"] == "TestAgent"
    assert info["version"] == "1.0.0"
    assert info["supported_tasks"] == ["test_task", "another_task"]
    assert info["status"] == "healthy"
    print("✅ test_agent_info passed")


if __name__ == "__main__":
    test_agent_creation()
    test_agent_process()
    test_agent_info()
    print("🎉 All base_agent tests passed!")