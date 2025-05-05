"""
model.py - Treinamento e aplicação do KMeans para segmentação de fãs.
"""

import pandas as pd
from sklearn.cluster import KMeans

def train_kmeans(X: pd.DataFrame, n_clusters: int = 5):
    """
    Treina um modelo KMeans e retorna o modelo e os labels dos clusters.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42)
    labels = model.fit_predict(X)
    return model, labels

def predict_clusters(model: KMeans, X: pd.DataFrame):
    """
    Aplica um modelo KMeans já treinado e retorna os clusters.
    """
    return model.predict(X)

# Outras funções relacionadas ao modelo podem ser adicionadas aqui 