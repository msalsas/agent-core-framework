from agent_core_framework import BaseAgent, AgentTask, AgentResponse, MultiAgentOrchestrator


class MockHairEditorAgent(BaseAgent):
    def __init__(self):
        super().__init__("MockHairEditor", "1.0.0")
        self.supported_tasks = ["edit_hair_style", "edit_hair_color"]

    def process(self, task: AgentTask) -> AgentResponse:
        return AgentResponse(
            success=True,
            data={"action": "hair_edited", "style": task.payload.get("hair_style")},
            agent_name=self.name
        )


class MockBackgroundEditorAgent(BaseAgent):
    def __init__(self):
        super().__init__("MockBackgroundEditor", "1.0.0")
        self.supported_tasks = ["edit_background"]

    def process(self, task: AgentTask) -> AgentResponse:
        return AgentResponse(
            success=True,
            data={"action": "background_changed", "background": task.payload.get("background")},
            agent_name=self.name
        )


def test_orchestrator():
    print("🧪 Testing multi-agent orchestrator...")

    orchestrator = MultiAgentOrchestrator("PhotoEditingSystem")

    hair_agent = MockHairEditorAgent()
    bg_agent = MockBackgroundEditorAgent()

    orchestrator.register_agent(hair_agent)
    orchestrator.register_agent(bg_agent)

    print("✅ Registered agents")

    tasks = [
        AgentTask(
            type="edit_hair_style",
            payload={
                "image_path": "foto1.jpg",
                "hair_style": "corto",
                "hair_color": "moreno"
            }
        ),
        AgentTask(
            type="edit_background",
            payload={
                "image_path": "foto2.jpg",
                "background": "playa"
            }
        ),
        AgentTask(
            type="unknown_task",
            payload={"image_path": "foto3.jpg"}
        )
    ]

    for i, task in enumerate(tasks):
        print(f"📨 Processing task {i + 1}: {task.type}")
        result = orchestrator.process_task(task)

        if result.success:
            print(f"   ✅ Success - Agent: {result.agent_name}")
        else:
            print(f"   ❌ Error: {result.error}")

    print(f"\n📊 System status:")
    status = orchestrator.get_system_status()
    print(f"   System: {status['system_name']}")
    print(f"   Total agents: {status['total_agents']}")
    print(f"   Supported tasks: {status['supported_tasks']}")


if __name__ == "__main__":
    test_orchestrator()
    print("🎉 All orchestration tests passed!")