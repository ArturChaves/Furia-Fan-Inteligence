# FURIA Fan Intelligence Platform

Plataforma completa de inteligência de fãs para a FURIA, integrando chatbot no WhatsApp, processamento analítico, segmentação via Machine Learning, mensageria e dashboards.

---

## Visão Geral

O projeto é composto por três grandes módulos:

- **bot/**: Chatbot em Node.js/TypeScript que interage com fãs via WhatsApp, coleta dados, publica eventos no RabbitMQ e integra com o backend.
- **analytics/**: API analítica em Python/FastAPI, pipeline de Machine Learning (KMeans), cálculo de KPIs, persistência de segmentos e KPIs, tasks assíncronas com Celery.
- **infra/**: Infraestrutura como código (Docker Compose) para orquestrar todos os serviços (banco, mensageria, API, workers, bot, etc).

---

## Principais Funcionalidades

- Onboarding e coleta de dados de fãs via WhatsApp.
- Publicação de eventos em filas RabbitMQ.
- Processamento analítico e segmentação de fãs via KMeans.
- Cálculo e persistência de KPIs por cluster.
- API REST para consulta de fãs, clusters, KPIs e notificações.
- Orquestração de serviços, banco e mensageria via Docker Compose.
- Pronto para monitoramento, logging e expansão.

---

## Dependências Necessárias

- **Docker** e **Docker Compose**
- **Make** 
- **Node.js** (v18+) e **npm** (para desenvolvimento do bot)
- **Python** (3.11+) e **pip** (para desenvolvimento do analytics)

---

## Como Rodar o Projeto Completo

### 1. Clone o repositório

```sh
git clone <url-do-repo>
cd Furia-Fan-Inteligence
```

### 2. Configure os arquivos `.env`

Copie os arquivos `.env.example` para `.env` em `analytics/` e `bot/`, e ajuste as variáveis conforme necessário.

```sh
cp analytics/.env.example analytics/.env
cp bot/.env.example bot/.env
```

### 3. Suba a infraestrutura com Docker Compose

```sh
make up
```

Isso irá subir os serviços de:
- PostgreSQL
- RabbitMQ
- API analytics (FastAPI)
- Celery worker
- Consumers

### 4. Rode as migrations no serviço de analytics

```sh
make migrate
```

Esse comando aplica as migrações do banco via Alembic.

### 5. Rode o bot localmente

Em outro terminal:

```sh
cd bot
npm install
npm run dev
```

- Escaneie o QR Code no WhatsApp para autenticar o bot.

### 6. Acesse a API e teste os endpoints

- Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Estrutura de Pastas

- **analytics/**: API, pipeline ML, tasks, consumers, modelos, repositórios.
- **bot/**: Chatbot WhatsApp, integração com RabbitMQ e banco.
- **infra/**: Docker Compose, Makefile, scripts de infraestrutura.
- **dashboard/**: (Opcional) Visualização de dados e clusters.
- **docs/**: Documentação adicional.

---

## Observações

- Para produção, utilize variáveis de ambiente seguras e execute os serviços com usuários não-root.
- Todos os comandos utilizam `make` por padrão — veja o `Makefile` para opções adicionais.
- Consulte os READMEs de cada módulo para instruções específicas.

---

**FURIA Fan Intelligence — Plataforma completa para engajamento, análise e segmentação de fãs!**
