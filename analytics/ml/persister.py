"""
persister.py - Salva clusters em Segment e KPIs em KPIReport.
"""

from sqlalchemy.orm import Session
import pandas as pd
from models.segment import Segment
from models.kpi_reports import KPIReport
from datetime import datetime

def save_segments(session: Session, fan_ids, clusters):
    """
    Atualiza a tabela segment com o cluster de cada fã.
    """
    now = datetime.utcnow()
    for fan_id, cluster in zip(fan_ids, clusters):
        segment = Segment(fan_id=fan_id, cluster=int(cluster), created_at=now)
        session.add(segment)
    session.commit()


def save_kpis(session: Session, kpis_df: pd.DataFrame):
    """
    Atualiza a tabela kpi_reports com os KPIs por cluster.
    """
    if 'engajamento' not in kpis_df.columns:
        kpis_df['engajamento'] = 0.0
    kpis_df['engajamento'] = kpis_df['engajamento'].fillna(0.0).astype(float)
    now = datetime.utcnow()
    for _, row in kpis_df.iterrows():
        kpi = KPIReport(
            data=now,
            total_fans=int(row['total_fans']),
            opt_in_jogos=float(row['opt_in_jogos']),
            opt_in_promo=float(row['opt_in_promo']),
            engajamento=float(row['engajamento'])
        )
        session.add(kpi)
    session.commit() 