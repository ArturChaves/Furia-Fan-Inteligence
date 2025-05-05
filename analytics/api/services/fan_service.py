from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional, Dict

from repositories.fan_repository import listar_fans, get_fan_by_id, contar_total_fans, contar_optin_jogos, contar_optin_promocoes, contar_fans_por_cidade
from api.DTOs.cadastro import FanSchema



# Novas funções analíticas

def contar_total_fans_service(db: Session) -> int:
    return contar_total_fans(db)

def contar_optin_jogos_service(db: Session) -> int:
    return contar_optin_jogos(db)

def contar_optin_promocoes_service(db: Session) -> int:
    return contar_optin_promocoes(db)

def contar_fans_por_cidade_service(db: Session) -> Dict[str, int]:
    return contar_fans_por_cidade(db)
