from pydantic import BaseModel
from datetime import datetime

class KPISchema(BaseModel):
    id: str
    data: datetime
    total_fans: int
    opt_in_jogos: float
    opt_in_promo: float
    engajamento: float
    created_at: datetime
    model_config = {"from_attributes": True}
