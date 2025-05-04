from sqlalchemy.orm import Session
from models.notification import Notification
from datetime import datetime

def salvar_notificacao(
    db: Session,
    fan_id: str,
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