from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..DTOs.kpi import KPISchema
from ..services.kpi_service import obter_kpi_reports, obter_kpi_mais_recente_service
from api.dependencies import get_db
from typing import List
from etl.worker import clustering_task

router = APIRouter()

@router.get("/kpis", response_model=List[KPISchema])
def listar_kpi_reports(db: Session = Depends(get_db)):
    return obter_kpi_reports(db)

@router.get("/kpis/mais-recente", response_model=KPISchema)
def kpi_mais_recente(db: Session = Depends(get_db)):
    kpi = obter_kpi_mais_recente_service(db)
    if not kpi:
        raise HTTPException(status_code=404, detail="Nenhum KPI encontrado")
    return kpi

@router.post("/kpis/clusterizar")
def acionar_clustering():
    task = clustering_task.delay()
    return {"task_id": task.id, "status": "started"}
