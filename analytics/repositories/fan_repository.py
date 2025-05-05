# analytics/repositories/fan_repository.py

from sqlalchemy.orm import Session
from sqlalchemy import func
from models.fan import Fan
from typing import Optional, List, Dict
from uuid import UUID


def get_fan_by_id(db: Session, fan_id: UUID) -> Optional[Fan]:
    return db.query(Fan).filter(Fan.id == fan_id).first()


def get_fan_by_whatsapp(db: Session, whatsapp_number: str) -> Optional[Fan]:
    return db.query(Fan).filter(Fan.whatsapp_number == whatsapp_number).first()


def listar_fans(db: Session) -> List[Fan]:
    return db.query(Fan).all()


def atualizar_fan(db: Session, fan_id: UUID, **campos: dict) -> Optional[Fan]:
    fan = get_fan_by_id(db, fan_id)
    if not fan:
        return None
    for campo, valor in campos.items():
        setattr(fan, campo, valor)
    db.commit()
    db.refresh(fan)
    return fan


def deletar_fan(db: Session, fan_id: UUID) -> bool:
    fan = get_fan_by_id(db, fan_id)
    if not fan:
        return False
    db.delete(fan)
    db.commit()
    return True


# 🔍 Consultas analíticas

def contar_total_fans(db: Session) -> int:
    return db.query(func.count(Fan.id)).scalar()


def contar_optin_jogos(db: Session) -> int:
    return db.query(func.count(Fan.id)).filter(Fan.optin_jogos == "true").scalar()


def contar_optin_promocoes(db: Session) -> int:
    return db.query(func.count(Fan.id)).filter(Fan.optin_promocoes == "true").scalar()


def contar_fans_por_cidade(db: Session) -> Dict[str, int]:
    return dict(
        db.query(Fan.cidade, func.count(Fan.id))
        .group_by(Fan.cidade)
        .all()
    )
