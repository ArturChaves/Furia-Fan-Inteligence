"""
Script principal de Machine Learning para segmentação de fãs FURIA.
"""

import pandas as pd
from sqlalchemy.orm import Session
from database.connection import SessionLocal
from ml.loader import load_fan_data, preprocess, load_interaction_data
from ml.model import train_kmeans
from ml.metrics import calculate_kpis
from ml.persister import save_segments, save_kpis

# Parâmetros do pipeline
N_CLUSTERS = 2

def run_pipeline():
    # 1. Criar sessão com o banco
    session: Session = SessionLocal()

    # 2. Carregar dados
    df_fan = load_fan_data(session)
    df_inter = load_interaction_data(session)
    # Calcular engajamento: número de interações por fã
    engajamento_por_fan = df_inter.groupby('fan_id').size().rename('engajamento')
    df_fan = df_fan.merge(engajamento_por_fan, left_on='id', right_on='fan_id', how='left')
    df_fan['engajamento'] = df_fan['engajamento'].fillna(0).astype(int)

    # 3. Pré-processar dados
    df_proc = preprocess(df_fan)

    # Separe o identificador das features
    fan_ids = df_proc['fan_id']
    X = df_proc.drop(columns=['fan_id'])

    # 4. Treinar modelo KMeans
    model, labels = train_kmeans(X, n_clusters=N_CLUSTERS)

    # 5. Salvar clusters em Segment
    save_segments(session, fan_ids, labels)

    # 6. Calcular e salvar KPIs por cluster
    kpis_df = calculate_kpis(df_proc, labels)
    save_kpis(session, kpis_df)

    print("Pipeline de segmentação executado com sucesso!")

if __name__ == "__main__":
    run_pipeline() 