from agent_core_framework import AgentTask, AgentResponse
from datetime import datetime


def test_agent_task_creation():
    task = AgentTask(
        type="test_task",
        payload={"key": "value"},
        source="test_source",
        priority=2
    )

    assert task.type == "test_task"
    assert task.payload == {"key": "value"}
    assert task.source == "test_source"
    assert task.priority == 2
    assert isinstance(task.id, str)
    assert isinstance(task.created_at, datetime)


def test_agent_task_defaults():
    task = AgentTask(type="test_task")

    assert task.payload == {}
    assert task.source == "unknown"
    assert task.priority == 1


def test_agent_response_creation():
    response = AgentResponse(
        success=True,
        data={"result": "ok"},
        error="",
        agent_name="TestAgent",
        execution_time=1.5,
        task_id="123"
    )

    assert response.success is True
    assert response.data == {"result": "ok"}
    assert response.error == ""
    assert response.agent_name == "TestAgent"
    assert response.execution_time == 1.5
    assert response.task_id == "123"


def test_agent_response_defaults():
    response = AgentResponse(success=False, agent_name="TestAgent")

    assert response.success is False
    assert response.data == {}
    assert response.error == ""
    assert response.execution_time is None
    assert response.task_id == ""


if __name__ == "__main__":
    test_agent_task_creation()
    test_agent_task_defaults()
    test_agent_response_creation()
    test_agent_response_defaults()
    print("✅ All model tests passed!")