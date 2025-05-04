from sqlalchemy.orm import Session
from models.segment import Segment
from datetime import datetime

def salvar_segmentacao_fan(
    db: Session,
    fan_id: str,
    cluster: int,
    criado_em: datetime
) -> Segment:
    nova_segmentacao = Segment(
        fan_id=fan_id,
        cluster=cluster,
        created_at=criado_em
    )
    db.add(nova_segmentacao)
    db.commit()
    db.refresh(nova_segmentacao)
    return nova_segmentacao