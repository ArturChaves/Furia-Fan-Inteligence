from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from datetime import datetime

class Segment(Base):
    __tablename__ = "FanSegment"

    id = Column(Integer, primary_key=True, index=True)
    fan_id = Column(UUID(as_uuid=True), ForeignKey("Fan.id"), nullable=False)
    cluster = Column(Integer, nullable=False)
    label = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

# Importa depois de definir a classe Segment
from models.fan import Fan
Segment.fan = relationship("Fan", back_populates="segment")