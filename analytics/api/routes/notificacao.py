from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..DTOs.notificacao import NotificationSchema
from ..services.notificacao_service import obter_ultima_notificacao_service, obter_ultima_notificacao_fan_service
from api.dependencies import get_db
from typing import Optional
from uuid import UUID

router = APIRouter()

@router.get("/notificacoes/ultima", response_model=NotificationSchema)
def ultima_notificacao(db: Session = Depends(get_db)):
    notificacao = obter_ultima_notificacao_service(db)
    if not notificacao:
        raise HTTPException(status_code=404, detail="Nenhuma notificação encontrada")
    return notificacao

@router.get("/notificacoes/ultima/{fan_id}", response_model=NotificationSchema)
def ultima_notificacao_fan(fan_id: UUID, db: Session = Depends(get_db)):
    notificacao = obter_ultima_notificacao_fan_service(db, fan_id)
    if not notificacao:
        raise HTTPException(status_code=404, detail="Nenhuma notificação encontrada para este fã")
    return notificacao