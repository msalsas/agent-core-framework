from pydantic import BaseModel, Field
from typing import Dict, Any, Optional
from datetime import datetime
import uuid


class AgentTask(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    type: str
    payload: Dict[str, Any] = Field(default_factory=dict)
    source: str = "unknown"
    priority: int = 1
    created_at: datetime = Field(default_factory=datetime.now)

class AgentResponse(BaseModel):
    success: bool
    data: Dict[str, Any] = Field(default_factory=dict)
    error: str = ""
    agent_name: str
    execution_time: Optional[float] = None
    task_id: str = ""