from sqlalchemy.orm import Session
from models.interaction import Interaction
from datetime import datetime
from typing import Optional

def criar_interacao(
    db: Session,
    fan_id: str,
    question: str,
    answer: str,
    criado_em: Optional[datetime] = None
) -> Interaction:
    nova_interacao = Interaction(
        fan_id=fan_id,
        question=question,
        answer=answer,
        created_at=criado_em or datetime.utcnow()
    )
    db.add(nova_interacao)
    db.commit()
    db.refresh(nova_interacao)
    return nova_interacao