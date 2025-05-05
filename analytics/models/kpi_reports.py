from sqlalchemy import Column, String, Integer, DateTime, Float
from database.connection import Base
from datetime import datetime
import uuid

class KPIReport(Base):
    __tablename__ = "kpi_report"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    data = Column(DateTime, nullable=False)
    total_fans = Column(Integer, nullable=False)
    opt_in_jogos = Column(Float, nullable=False)
    opt_in_promo = Column(Float, nullable=False)
    engajamento = Column(Float, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
