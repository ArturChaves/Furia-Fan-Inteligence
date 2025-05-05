from sqlalchemy.orm import Session
from repositories.segmentar_fan_repository import buscar_segmentos_por_fan_id, listar_todos_segmentos
from uuid import UUID
from typing import List, Dict, Optional
from models.segment import Segment
from repositories.segmentar_fan_repository import (
    listar_segmentacoes_por_cluster,
    obter_cluster_atual_do_fan,
    contar_fans_por_cluster
)

def listar_segmentos(db: Session) -> List[Segment]:
    return listar_todos_segmentos(db)

def listar_segmentos_por_fan(db: Session, fan_id: UUID) -> List[Segment]:
    return buscar_segmentos_por_fan_id(db, fan_id)

def listar_segmentos_por_cluster_service(db: Session, cluster: int) -> List[Segment]:
    return listar_segmentacoes_por_cluster(db, cluster)

def obter_cluster_atual_do_fan_service(db: Session, fan_id: UUID) -> Optional[int]:
    return obter_cluster_atual_do_fan(db, fan_id)

def contar_fans_por_cluster_service(db: Session) -> Dict[int, int]:
    return contar_fans_por_cluster(db)
