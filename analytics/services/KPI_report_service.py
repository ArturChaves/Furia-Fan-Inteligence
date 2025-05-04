from database.connection import SessionLocal
from repositories.kpi_report_repository import salvar_kpi_report as salvar_kpi_report_repo
from datetime import datetime

def salvar_kpi_report(data: datetime, total_fans: int, opt_in_jogos: float, opt_in_promo: float, engajamento: float):
    db = SessionLocal()
    try:
        salvar_kpi_report_repo(
            db=db,
            data=data,
            total_fans=total_fans,
            opt_in_jogos=opt_in_jogos,
            opt_in_promo=opt_in_promo,
            engajamento=engajamento
        )
        print(f"✅ KPI report salvo para a data {data}")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao salvar KPI report: {e}")
    finally:
        db.close()