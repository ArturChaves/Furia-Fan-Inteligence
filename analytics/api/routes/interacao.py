from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..DTOs.interacao import InteractionSchema
from ..services.interacao_service import listar_todas_interacoes, obter_interacoes_por_fan
from api.dependencies import get_db
from typing import List
from uuid import UUID

router = APIRouter()


@router.get("/interacoes", response_model=List[InteractionSchema])
def listar_interacoes(db: Session = Depends(get_db)):
    return listar_todas_interacoes(db)

@router.get("/interacoes/{fan_id}", response_model=List[InteractionSchema])
def interacoes_por_fan(fan_id: UUID, db: Session = Depends(get_db)):
    return obter_interacoes_por_fan(db, fan_id)
