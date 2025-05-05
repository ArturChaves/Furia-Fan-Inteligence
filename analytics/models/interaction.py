from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
from datetime import datetime
import uuid

class Interaction(Base):
    __tablename__ = "interaction"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    fan_id = Column(UUID(as_uuid=True), ForeignKey("fan.id"), nullable=False)
    question = Column(String, nullable=False)
    answer = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

# Importa depois para evitar erro de dependência circular
from models.fan import Fan
Interaction.fan = relationship("Fan", back_populates="interactions")
