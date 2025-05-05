# analytics/api/routes/fan.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Dict

from api.dependencies import get_db
from api.DTOs.cadastro import FanSchema
from api.services.fan_service import (
    contar_total_fans_service,
    contar_optin_jogos_service,
    contar_optin_promocoes_service,
    contar_fans_por_cidade_service
)

router = APIRouter()

@router.get("/contagem", response_model=int)
def contar_total_fans(db: Session = Depends(get_db)):
    return contar_total_fans_service(db)

@router.get("/optin-jogos", response_model=int)
def contar_optin_jogos(db: Session = Depends(get_db)):
    return contar_optin_jogos_service(db)

@router.get("/optin-promocoes", response_model=int)
def contar_optin_promocoes(db: Session = Depends(get_db)):
    return contar_optin_promocoes_service(db)

@router.get("/por-cidade", response_model=Dict[str, int])
def contar_fans_por_cidade(db: Session = Depends(get_db)):
    return contar_fans_por_cidade_service(db)
