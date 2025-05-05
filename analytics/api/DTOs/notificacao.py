from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class NotificationSchema(BaseModel):
    id: UUID
    fan_id: UUID
    type: str
    status: str
    created_at: datetime
    model_config = {"from_attributes": True}
