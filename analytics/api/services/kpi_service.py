from sqlalchemy.orm import Session
from repositories.kpi_report_repository import listar_kpis, obter_kpi_mais_recente
from ..DTOs.kpi import KPISchema
from typing import List, Optional

def obter_kpi_reports(db: Session) -> List[KPISchema]:
    relatorios = listar_kpis(db)
    return [KPISchema.model_validate(relatorio) for relatorio in relatorios]

def obter_kpi_mais_recente_service(db: Session) -> Optional[KPISchema]:
    kpi = obter_kpi_mais_recente(db)
    if kpi:
        return KPISchema.model_validate(kpi)
    return None