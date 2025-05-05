from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

class FanSchema(BaseModel):
    id: UUID
    whatsapp_number: str
    nome: str
    cidade: str
    cpf: Optional[str] = None
    optin_jogos: bool
    optin_promocoes: bool
    criado_em: datetime
    model_config = {"from_attributes": True}
