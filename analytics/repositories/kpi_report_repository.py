from sqlalchemy.orm import Session
from sqlalchemy import desc
from models.kpi_reports import KPIReport
from datetime import datetime
from typing import Optional, List


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

# 🔍 Consultas analíticas

def listar_kpis(db: Session) -> List[KPIReport]:
    return db.query(KPIReport).order_by(desc(KPIReport.data)).all()


def obter_kpi_mais_recente(db: Session) -> Optional[KPIReport]:
    return db.query(KPIReport).order_by(desc(KPIReport.data)).first()
