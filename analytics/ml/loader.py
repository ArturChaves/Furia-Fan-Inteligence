"""
loader.py - Coleta e pré-processamento dos dados para o pipeline de ML.
"""

import pandas as pd
from sqlalchemy.orm import Session
from models.fan import Fan
from models.interaction import Interaction

def load_fan_data(session: Session) -> pd.DataFrame:
    """
    Carrega dados da tabela fan para um DataFrame pandas.
    """
    query = session.query(Fan)
    df = pd.read_sql(query.statement, session.bind)
    return df

def load_interaction_data(session: Session) -> pd.DataFrame:
    """
    Carrega dados da tabela interaction para um DataFrame pandas.
    """
    query = session.query(Interaction)
    df = pd.read_sql(query.statement, session.bind)
    return df

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Exemplo: remove nulos e faz one-hot encoding de cidade.
    """
    # Inclui o campo fan_id a partir do id
    if 'id' in df.columns:
        df['fan_id'] = df['id']
    # Defina as features que realmente importam para o clustering
    features = ['fan_id', 'cidade', 'optin_jogos', 'optin_promocoes', 'engajamento']
    df = df[features]
    # Remove apenas se algum desses campos essenciais estiver nulo
    df = df.dropna(subset=features)
    # One-hot encoding para cidade
    if 'cidade' in df.columns:
        df = pd.get_dummies(df, columns=['cidade'])
    # Converte optin_jogos e optin_promocoes para 0/1 se necessário
    for col in ['optin_jogos', 'optin_promocoes']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.lower().map({'true': 1, 'false': 0, '1': 1, '0': 0}).fillna(0).astype(int)
    # Renomeia para os nomes esperados pelo pipeline
    df = df.rename(columns={
        'optin_jogos': 'opt_in_jogos',
        'optin_promocoes': 'opt_in_promo'
    })
    return df 