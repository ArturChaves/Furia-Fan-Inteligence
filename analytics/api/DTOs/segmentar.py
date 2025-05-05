from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class SegmentacaoSchema(BaseModel):
    id: int
    fan_id: UUID
    cluster: int
    label: Optional[str] = None
    created_at: Optional[datetime] = None
    model_config = {"from_attributes": True}
