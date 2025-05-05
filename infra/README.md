# Infra - FURIA Fan Intelligence Platform

Este diretório contém toda a infraestrutura como código (IaC) para orquestrar, monitorar e dar suporte ao ecossistema FURIA Fan Intelligence.

---

## Visão Geral

O módulo `infra` é responsável por:
- Orquestrar todos os serviços do projeto (API, bot, banco, mensageria, workers) via Docker Compose.
- Configurar e expor o banco de dados PostgreSQL e o broker RabbitMQ.
- Automatizar deploy, setup, backup e monitoramento.
- Fornecer scripts utilitários para desenvolvedores e operações.
- Preparar o ambiente para observabilidade (Prometheus, Grafana) e logging centralizado (ELK Stack).

---

## Estrutura de Pastas e Arquivos

- **docker-compose.yml**: Orquestração dos serviços principais (PostgreSQL, RabbitMQ, etc).
- **docker-compose.analytics.yml**: Orquestração dos serviços de analytics (API, workers, consumers, etc).
- **Makefile**: Comandos utilitários para build, deploy, logs, backup, restore, etc.
- **README.md**: Este arquivo de documentação.
- **127e9484e35b,**: (placeholder ou arquivo temporário, pode ser removido se não utilizado).

---

## Serviços Orquestrados

### **Banco de Dados**
- **PostgreSQL**: Armazena dados de fãs, interações, segmentos, notificações e KPIs.
  - Persistência de dados via volume Docker.
  - Usuário, senha e nome do banco configuráveis via `.env`.

### **Mensageria**
- **RabbitMQ**: Broker de mensagens para integração assíncrona entre bot, analytics e outros serviços.
  - Painel de administração exposto na porta 15672.
  - Usuário e senha configuráveis via `.env`.

### **Analytics**
- **API FastAPI**: Exposta na porta 8000 para consultas e acionamento do pipeline.
- **Celery Worker**: Executa o pipeline de Machine Learning de forma assíncrona.
- **Consumers**: Serviços que consomem eventos das filas RabbitMQ.
- **Alembic**: Serviço para rodar migrations do banco.


---

## Principais Comandos

- **Subir todos os serviços:**
  ```sh
  docker-compose -f docker-compose.yml -f docker-compose.analytics.yml up -d
  ```
- **Derrubar todos os serviços:**
  ```sh
  docker-compose -f docker-compose.yml -f docker-compose.analytics.yml down
  ```
- **Ver logs de um serviço:**
  ```sh
  docker-compose -f docker-compose.analytics.yml logs <serviço>
  ```
- **Executar migrations Alembic:**
  ```sh
  docker-compose -f docker-compose.analytics.yml run --rm alembic upgrade head
  ```
- **Backup/Restore**: Consulte o `Makefile` para comandos de backup e restore do banco.

---

## Variáveis de Ambiente

- Configure o arquivo `.env` na raiz do projeto ou nos submódulos (`analytics`, `bot`) com:
  - Credenciais do banco (`DB_USER`, `DB_PASSWORD`, `DB_NAME`, etc)
  - Credenciais do RabbitMQ (`RABBITMQ_USER`, `RABBITMQ_PASSWORD`, etc)
  - URLs de conexão para Celery, API, etc.

---

## Observações

- Para ambientes de produção, configure volumes persistentes, variáveis seguras e monitore recursos.
- O ambiente está pronto para ser expandido com novos serviços, monitoramento e automações.
- Consulte os arquivos de compose e o Makefile para detalhes de cada serviço e comando.

---

**FURIA Fan Intelligence — Infra: infraestrutura robusta, escalável e pronta para o futuro do engajamento de fãs!**
