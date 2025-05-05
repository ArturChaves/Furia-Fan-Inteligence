# analytics/api/services/notificacao_service.py

from sqlalchemy.orm import Session
from repositories.notification_repository import obter_ultima_notificacao
from ..DTOs.notificacao import NotificationSchema
from typing import Optional
from uuid import UUID

def obter_ultima_notificacao_service(db: Session) -> Optional[NotificationSchema]:
    """
    Retorna a última notificação criada no sistema (de qualquer fã).
    """
    from repositories.notification_repository import listar_notificacoes
    notificacoes = listar_notificacoes(db)
    if notificacoes:
        return NotificationSchema.from_orm(notificacoes[0])
    return None

def obter_ultima_notificacao_fan_service(db: Session, fan_id: UUID) -> Optional[NotificationSchema]:
    """
    Retorna a última notificação de um fã específico.
    """
    notificacao = obter_ultima_notificacao(db, fan_id)
    if notificacao:
        return NotificationSchema.from_orm(notificacao)
    return None
