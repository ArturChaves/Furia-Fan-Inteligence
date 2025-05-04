from sqlalchemy.orm import Session
from database.connection import SessionLocal
from repositories.cadastro_repository import criar_cadastro
from datetime import datetime

def salvar_cadastro(dados: dict):
    session: Session = SessionLocal()
    try:
        criar_cadastro(
            db=session,
            whatsapp_number=dados["whatsapp_number"],
            nome=dados["nome"],
            cidade=dados["cidade"],
            cpf=dados.get("cpf"),
            optin_jogos=dados.get("optinJogos", "False"),
            optin_promocoes=dados.get("optinPromocoes", "False"),
            criado_em=datetime.utcnow()
        )
        print(f"✅ Cadastro salvo no banco: {dados['whatsapp_number']}")
    except Exception as e:
        session.rollback()
        print(f"❌ Erro ao salvar fan: {e}")
    finally:
        session.close()