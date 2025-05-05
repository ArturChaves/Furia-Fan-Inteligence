# no topo
from sqlalchemy import Column, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from database.connection import Base
import uuid

class Fan(Base):
    __tablename__ = "fan"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    whatsapp_number = Column(String, nullable=False, unique=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    cpf = Column(String, nullable=True)
    optin_jogos = Column(String, nullable=False)
    optin_promocoes = Column(String, nullable=False)
    criado_em = Column(TIMESTAMP, nullable=False)

# Importações após a definição da classe Fan
from models.segment import Segment
from models.interaction import Interaction
from models.notification import Notification

Fan.segment = relationship("Segment", back_populates="fan", uselist=False)
Fan.interactions = relationship("Interaction", back_populates="fan", cascade="all, delete-orphan")
Fan.notifications = relationship("Notification", back_populates="fan", cascade="all, delete-orphan")
