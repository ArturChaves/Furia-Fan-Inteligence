from sqlalchemy.orm import Session
from sqlalchemy import func, desc
from models.segment import Segment
from datetime import datetime
from typing import Optional, List, Dict
from uuid import UUID


def salvar_segmentacao_fan(
    db: Session,
    fan_id: UUID,
    cluster: int,
    criado_em: Optional[datetime] = None
) -> Segment:
    nova_segmentacao = Segment(
        fan_id=fan_id,
        cluster=cluster,
        created_at=criado_em or datetime.utcnow()
    )
    db.add(nova_segmentacao)
    db.commit()
    db.refresh(nova_segmentacao)
    return nova_segmentacao

# 🔍 Consultas analíticas

def listar_segmentacoes_por_cluster(db: Session, cluster: int) -> List[Segment]:
    return db.query(Segment).filter(Segment.cluster == cluster).all()


def obter_cluster_atual_do_fan(db: Session, fan_id: UUID) -> Optional[int]:
    segmentacao = (
        db.query(Segment)
        .filter(Segment.fan_id == fan_id)
        .order_by(desc(Segment.created_at))
        .first()
    )
    return segmentacao.cluster if segmentacao else None


def contar_fans_por_cluster(db: Session) -> Dict[int, int]:
    return dict(
        db.query(Segment.cluster, func.count(Segment.fan_id))
        .group_by(Segment.cluster)
        .all()
    )


def listar_todos_segmentos(db: Session) -> List[Segment]:
    return db.query(Segment).all()


def buscar_segmentos_por_fan_id(db: Session, fan_id: UUID) -> List[Segment]:
    return db.query(Segment).filter(Segment.fan_id == fan_id).all()
