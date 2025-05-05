from sqlalchemy.orm import Session
from models.notification import Notification
from datetime import datetime
from uuid import UUID
from typing import List, Optional


def salvar_notificacao(
    db: Session,
    fan_id: UUID,
    tipo: str,
    status: str
) -> Notification:
    nova_notificacao = Notification(
        fan_id=fan_id,
        type=tipo,
        status=status,
        created_at=datetime.utcnow()
    )
    db.add(nova_notificacao)
    db.commit()
    db.refresh(nova_notificacao)
    return nova_notificacao

# 🔍 Consultas analíticas

def listar_notificacoes(db: Session) -> List[Notification]:
    return db.query(Notification).order_by(Notification.created_at.desc()).all()


def listar_notificacoes_por_fan(db: Session, fan_id: UUID) -> List[Notification]:
    return db.query(Notification).filter(Notification.fan_id == fan_id).order_by(Notification.created_at.desc()).all()


def obter_ultima_notificacao(db: Session, fan_id: UUID) -> Optional[Notification]:
    return db.query(Notification).filter(Notification.fan_id == fan_id).order_by(Notification.created_at.desc()).first()
