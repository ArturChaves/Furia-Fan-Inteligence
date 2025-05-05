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

- **Docker** e **Docker Compose** (recomendado: Docker Desktop)
- **Node.js** (v18+) e **npm** (para desenvolvimento do bot)
- **Python** (3.11+) e **pip** (para desenvolvimento do analytics)
- (Opcional) **Make** para comandos utilitários

---

## Como Rodar o Projeto Completo

### 1. Clone o repositório

```sh
git clone <url-do-repo>
cd Furia-Fan-Inteligence
```

### 2. Configure os arquivos `.env`

- Copie os arquivos `.env.example` para `.env` em `analytics/` e `bot/` e ajuste as variáveis conforme necessário.

### 3. Suba toda a infraestrutura com Docker Compose

```sh
cd infra
docker-compose -f docker-compose.yml -f docker-compose.analytics.yml up -d
```
(ou make up se tiver ele instalado)

Isso irá subir:
- PostgreSQL
- RabbitMQ
- API analytics (FastAPI)
- Celery worker
- Consumers
- Alembic (migrations)
- (Adapte para incluir o bot se desejar rodar via container)

### 4. Instale e rode o bot (WhatsApp)

Em outro terminal:

```sh
cd bot
npm install
npx tsc
npm start
```
- Escaneie o QR Code no WhatsApp para autenticar o bot.

### 5. Acesse a API e teste os endpoints

- Documentação Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)
- Teste endpoints de fãs, clusters, KPIs, notificações e acione o pipeline de clustering.

### 6. Teste o fluxo completo

- Interaja com o bot via WhatsApp.
- Veja os dados sendo processados, segmentados e salvos.
- Consulte os resultados via API ou diretamente no banco.

---

## Estrutura de Pastas

- **analytics/**: API, pipeline ML, tasks, consumers, modelos, repositórios.
- **bot/**: Chatbot WhatsApp, integração com RabbitMQ e banco.
- **infra/**: Docker Compose, Makefile, scripts de infraestrutura.
- **dashboard/**: (Opcional) Visualização de dados e clusters.
- **docs/**: Documentação adicional.

---

## Observações

- Para produção, configure variáveis seguras, monitore recursos e rode workers/bot com usuários não-root.
- O projeto está pronto para ser expandido com novos fluxos, integrações e automações.
- Consulte os READMEs de cada módulo para detalhes específicos.

---

**FURIA Fan Intelligence — Plataforma completa para engajamento, análise e segmentação de fãs!**
