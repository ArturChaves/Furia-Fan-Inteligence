from database.connection import SessionLocal
from repositories.segmentar_fan_repository import salvar_segmentacao_fan
from datetime import datetime

def salvar_segmento(fan_id: str, cluster: int):
    db = SessionLocal()
    try:
        salvar_segmentacao_fan(
            db=db,
            fan_id=fan_id,
            cluster=cluster,
            criado_em=datetime.utcnow()
        )
        print(f"✅ Segmentação salva: fan_id={fan_id}, cluster={cluster}")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao salvar segmentação: {e}")
    finally:
        db.close()