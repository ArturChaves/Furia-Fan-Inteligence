# Módulo de Machine Learning - FURIA Fan Intelligence

Este diretório contém o pipeline de Machine Learning para segmentação de fãs da FURIA.

## Objetivo
Segmentar a base de fãs em clusters de comportamento semelhante usando KMeans, e calcular KPIs por cluster.

## Pipeline
1. Coleta de dados do banco (fan, interaction, etc.)
2. Pré-processamento (normalização, encoding)
3. Treinamento do modelo KMeans
4. Associação de clusters aos fãs (tabela segment)
5. Cálculo e persistência de KPIs por cluster (tabela kpi_reports)

## Estrutura
- `segmenter.py`: Script principal do pipeline de ML
- `utils.py`: Funções auxiliares (normalização, encoding, etc.)

## Como rodar

1. Instale as dependências:
   ```
   pip install -r ../requirements.txt
   ```
2. Execute o script principal:
   ```
   python segmenter.py
   ```

## Observações
- O pipeline pode ser executado manualmente ou automatizado via cron/container.
- Adapte as funções de acordo com o schema real do banco e as necessidades do negócio. 