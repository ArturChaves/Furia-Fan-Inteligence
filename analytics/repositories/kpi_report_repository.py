from sqlalchemy.orm import Session
from models.kpi_reports import KPIReport
from datetime import datetime

def salvar_kpi_report(
    db: Session,
    data: datetime,
    total_fans: int,
    opt_in_jogos: float,
    opt_in_promo: float,
    engajamento: float
) -> KPIReport:
    novo_relatorio = KPIReport(
        data=data,
        total_fans=total_fans,
        opt_in_jogos=opt_in_jogos,
        opt_in_promo=opt_in_promo,
        engajamento=engajamento
    )
    db.add(novo_relatorio)
    db.commit()
    db.refresh(novo_relatorio)
    return novo_relatorio