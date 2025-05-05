from sqlalchemy.orm import Session
from sqlalchemy import func
from models.interaction import Interaction
from datetime import datetime
from typing import Optional, List, Tuple
from uuid import UUID


def criar_interacao(
    db: Session,
    fan_id: UUID,
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


# 🔍 Consultas analíticas

def contar_total_interacoes(db: Session) -> int:
    return db.query(func.count(Interaction.id)).scalar()


def interacoes_por_pergunta(db: Session) -> List[Tuple[str, int]]:
    return db.query(Interaction.question, func.count(Interaction.id))\
        .group_by(Interaction.question).all()


def interacoes_por_fan(db: Session, fan_id: UUID) -> List[Interaction]:
    return db.query(Interaction).filter(Interaction.fan_id == fan_id).all()


def interacoes_mais_recentes(db: Session, limite: int = 10) -> List[Interaction]:
    return db.query(Interaction).order_by(Interaction.created_at.desc()).limit(limite).all()

def get_todas_interacoes(db: Session) -> List[Interaction]:
    return db.query(Interaction).all()

def interacoes_por_data(db: Session) -> List[Tuple[datetime.date, int]]:
    return db.query(
        func.date(Interaction.created_at),
        func.count(Interaction.id)
    ).group_by(func.date(Interaction.created_at)).all()

