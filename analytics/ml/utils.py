"""
Funções auxiliares para o pipeline de Machine Learning.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler

def normalize(df: pd.DataFrame, columns):
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df

# Outras funções utilitárias podem ser adicionadas aqui 