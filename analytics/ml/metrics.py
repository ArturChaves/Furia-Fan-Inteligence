"""
metrics.py - Cálculo de KPIs por cluster.
"""

import pandas as pd

def calculate_kpis(df: pd.DataFrame, labels) -> pd.DataFrame:
    """
    Calcula KPIs agregados por cluster, como percentual de opt-in.
    Retorna um DataFrame com os KPIs por cluster.
    """
    df = df.copy()
    df['cluster'] = labels
    kpis = df.groupby('cluster').agg({
        'opt_in_jogos': 'mean',
        'opt_in_promo': 'mean',
        'engajamento': 'mean',
        'fan_id': 'count'
    }).rename(columns={'fan_id': 'total_fans'})
    kpis['opt_in_jogos'] = kpis['opt_in_jogos'] * 100  # percentual
    kpis['opt_in_promo'] = kpis['opt_in_promo'] * 100  # percentual
    kpis['engajamento'] = kpis['engajamento'].fillna(0.0).astype(float)
    return kpis.reset_index() 