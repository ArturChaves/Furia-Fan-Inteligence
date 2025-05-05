from sqlalchemy.orm import Session
from uuid import UUID
from repositories.interacao_repository import interacoes_por_fan, get_todas_interacoes
from api.DTOs.interacao import InteractionSchema
from typing import List 


def listar_todas_interacoes(db: Session) -> List[InteractionSchema]:
    interacoes = get_todas_interacoes(db)
    return [InteractionSchema.from_orm(i) for i in interacoes]


def obter_interacoes_por_fan(db: Session, fan_id: UUID) -> List[InteractionSchema]:
    interacoes = interacoes_por_fan(db, fan_id)
    return [InteractionSchema.from_orm(i) for i in interacoes]