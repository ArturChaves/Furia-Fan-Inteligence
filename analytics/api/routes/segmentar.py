from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..DTOs.segmentar import SegmentacaoSchema
from ..services.segmentar_service import (
    listar_segmentos,
    listar_segmentos_por_fan,
    listar_segmentos_por_cluster_service,
    obter_cluster_atual_do_fan_service,
    contar_fans_por_cluster_service
)
from api.dependencies import get_db
from typing import List, Dict
from uuid import UUID

router = APIRouter()

@router.get("/contagem", response_model=Dict[int, int])
def contagem_fans_por_cluster(db: Session = Depends(get_db)):
    return contar_fans_por_cluster_service(db)

@router.get("/cluster/{cluster_id}", response_model=List[SegmentacaoSchema])
def listar_por_cluster(cluster_id: int, db: Session = Depends(get_db)):
    return listar_segmentos_por_cluster_service(db, cluster_id)

@router.get("/fan/{fan_id}/cluster", response_model=int)
def cluster_atual_do_fan(fan_id: UUID, db: Session = Depends(get_db)):
    cluster = obter_cluster_atual_do_fan_service(db, fan_id)
    if cluster is None:
        raise HTTPException(status_code=404, detail="Fan não encontrado ou sem cluster")
    return cluster

@router.get("/", response_model=List[SegmentacaoSchema])
def listar(db: Session = Depends(get_db)):
    return listar_segmentos(db)

@router.get("/{fan_id}", response_model=List[SegmentacaoSchema])
def listar_por_fan(fan_id: UUID, db: Session = Depends(get_db)):
    return listar_segmentos_por_fan(db, fan_id)