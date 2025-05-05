from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class InteractionSchema(BaseModel):
    id: UUID
    fan_id: UUID
    question: str
    answer: str
    created_at: datetime
    model_config = {"from_attributes": True}