from database.connection import SessionLocal
from repositories.segmentar_fan_repository import salvar_segmentacao_fan
from repositories.fan_repository import get_fan_by_whatsapp
from datetime import datetime

def salvar_segmento(whatsapp_number: str, cluster: int):
    db = SessionLocal()
    try:
        fan = get_fan_by_whatsapp(db, whatsapp_number)
        if not fan:
            print(f"❌ Fan com número {whatsapp_number} não encontrado.")
            return

        salvar_segmentacao_fan(
            db=db,
            fan_id=fan.id,
            cluster=cluster,
            criado_em=datetime.utcnow()
        )
        print(f"✅ Segmentação salva: fan_id={fan.id}, cluster={cluster}")
    except Exception as e:
        db.rollback()
        print(f"❌ Erro ao salvar segmentação: {e}")
    finally:
        db.close()
