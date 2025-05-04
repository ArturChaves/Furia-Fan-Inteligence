from database.connection import SessionLocal
from repositories.notification_repository import salvar_notificacao as salvar_notificacao_repo

def salvar_notificacao(fan_id: str, tipo: str, status: str):
    db = SessionLocal()
    try:
        salvar_notificacao_repo(db, fan_id=fan_id, tipo=tipo, status=status)
        print(f"✅ Notificação salva para o fã {fan_id}")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao salvar notificação: {e}")
    finally:
        db.close()