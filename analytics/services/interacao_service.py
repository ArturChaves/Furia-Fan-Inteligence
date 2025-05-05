from sqlalchemy.orm import Session
from database.connection import SessionLocal
from repositories.interacao_repository import criar_interacao
from repositories.fan_repository import get_fan_by_whatsapp
from datetime import datetime

def salvar_interacao(whatsapp_number: str, question: str, answer: str):
    session: Session = SessionLocal()
    try:
        fan = get_fan_by_whatsapp(session, whatsapp_number)
        if not fan:
            raise ValueError(f"Fã com número {whatsapp_number} não encontrado.")

        criar_interacao(
            db=session,
            fan_id=fan.id,
            question=question,
            answer=answer,
            criado_em=datetime.utcnow()
        )
        print(f"✅ Interação salva no banco: fan_id={fan.id}")
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao salvar interação: {e}")
    finally:
        session.close()
