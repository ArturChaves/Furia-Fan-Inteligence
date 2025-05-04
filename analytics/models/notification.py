from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from database.connection import Base
import uuid

class Notification(Base):
    __tablename__ = "Notification"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    fan_id = Column(UUID(as_uuid=True), ForeignKey("Fan.id"), nullable=False)
    type = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    fan = relationship("Fan", back_populates="notifications")