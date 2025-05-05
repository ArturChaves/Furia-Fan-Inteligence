# Analytics - FURIA Fan Intelligence Platform

Este diretório implementa toda a inteligência analítica, processamento de dados e API do projeto FURIA Fan Intelligence.

---

## Visão Geral

O módulo `analytics` é responsável por:
- Expor uma **API REST** para consulta e análise de fãs, clusters, KPIs e notificações.
- Processar dados de fãs e interações, segmentando-os via **Machine Learning** (KMeans).
- Calcular e armazenar **KPIs** por segmento.
- Orquestrar tarefas assíncronas e ETL com **Celery** e **RabbitMQ**.
- Persistir resultados em um banco **PostgreSQL**.

---

## Estrutura de Pastas

- **api/**: Endpoints FastAPI, rotas, DTOs e dependências.
- **models/**: Modelos ORM (SQLAlchemy) para fãs, interações, segmentos, notificações e KPIs.
- **repositories/**: Camada de acesso a dados (CRUD e queries customizadas).
- **services/**: Lógica de negócio, integração entre camadas e orquestração de operações.
- **ml/**: Pipeline de Machine Learning (loader, preprocess, clustering, KPIs, persistência).
- **etl/**: Worker Celery para rodar o pipeline de ML de forma assíncrona.
- **consumers/**: Consumidores de filas RabbitMQ para eventos de interação, cadastro e segmentação.
- **database/**: Configuração de conexão, migrations (Alembic) e setup do banco.
- **utils/**: Utilitários diversos (ex: integração com RabbitMQ).
- **requirements.txt**: Dependências do projeto.
- **Dockerfile**: Build do container de analytics.

---

## Pipeline de Machine Learning

1. **Carregamento de Dados**
   - Busca fãs e interações do banco.
   - Calcula o engajamento de cada fã (número de interações).

2. **Pré-processamento**
   - Seleciona features relevantes: cidade (one-hot), opt-ins (0/1), engajamento.
   - Remove apenas linhas com campos essenciais nulos.

3. **Clustering**
   - Executa KMeans para segmentar fãs em grupos de perfil semelhante.
   - Número de clusters configurável.

4. **KPIs por Cluster**
   - Calcula: percentual de opt-in jogos/promoções, média de engajamento, total de fãs.
   - Persiste resultados na tabela de KPIs.

5. **Persistência**
   - Salva segmentos de fãs e KPIs no banco de dados.

---

## Orquestração e Execução

- **Celery Worker** (`etl/worker.py`): Executa o pipeline de ML como task assíncrona.
- **RabbitMQ**: Orquestra eventos e comunicação entre serviços.
- **API**: Permite acionar o pipeline, consultar clusters, KPIs, fãs e notificações.

---

## Principais Endpoints (API)

- `/fans/`: Consulta e gerenciamento de fãs.
- `/kpis/`: Consulta de KPIs por cluster.
- `/segments/`: Consulta de segmentos de fãs.
- `/notifications/`: Consulta e envio de notificações.
- `/kpis/clusterizar`: Aciona o pipeline de clustering (task Celery).

---

## Tecnologias Utilizadas

- **Python 3.11+**
- **FastAPI** (API REST)
- **Celery** (tasks assíncronas)
- **RabbitMQ** (mensageria)
- **PostgreSQL** (banco de dados)
- **SQLAlchemy** (ORM)
- **Alembic** (migrations)
- **scikit-learn** (Machine Learning)
- **pandas** (manipulação de dados)
- **Docker** (containerização)

---

## Como Executar

1. **Configure o `.env`** com as variáveis de ambiente necessárias.
2. **Suba os containers** com Docker Compose (veja o arquivo de orquestração principal).
3. **Acesse a API** em `http://localhost:8000/docs` para testar os endpoints.
4. **Acione o pipeline** via endpoint ou aguarde eventos de fila.
5. **Consulte os resultados** (clusters, KPIs, segmentos) via API ou diretamente no banco.

---

## Observações

- O pipeline está pronto para ser expandido com novas features, métricas e integrações.
- Para produção, rode o worker Celery com usuário não-root.
- Consulte a documentação dos módulos para detalhes de cada função/classe.

---

**FURIA Fan Intelligence — Analytics: inteligência de dados para engajamento e segmentação de fãs!**