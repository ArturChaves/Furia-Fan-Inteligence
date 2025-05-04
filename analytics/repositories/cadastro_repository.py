from sqlalchemy.orm import Session
from models.fan import Fan
from datetime import datetime
from typing import Optional

def criar_cadastro(
    db: Session,
    whatsapp_number: str,
    nome: str,
    cidade: str,
    cpf: Optional[str],
    optin_jogos: str,
    optin_promocoes: str,
    criado_em: Optional[datetime] = None
) -> Fan:
    novo_fan = Fan(
        whatsapp_number=whatsapp_number,
        nome=nome,
        cidade=cidade,
        cpf=cpf,
        optin_jogos=optin_jogos,
        optin_promocoes=optin_promocoes,
        criado_em=criado_em or datetime.utcnow()
    )
    db.add(novo_fan)
    db.commit()
    db.refresh(novo_fan)
    return novo_fan