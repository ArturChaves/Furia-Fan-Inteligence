from sqlalchemy.orm import Session
from database.connection import SessionLocal
from repositories.interacao_repository import criar_interacao

def salvar_interacao(fan_id: str, question: str, answer: str):
    session: Session = SessionLocal()
    try:
        criar_interacao(session, fan_id, question, answer)
        print(f"✅ Interação salva para o fã {fan_id}")
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao salvar interação: {e}")
    finally:
        session.close()