# Bot - FURIA Fan Intelligence Platform

Este diretório contém o chatbot oficial da FURIA, responsável por interagir com fãs via WhatsApp, coletar dados, gerenciar onboarding e integrar o ecossistema de inteligência de fãs.

---

## Visão Geral

O módulo `bot` é responsável por:
- Conectar-se ao WhatsApp usando `whatsapp-web.js` para comunicação em tempo real com fãs.
- Gerenciar o fluxo de onboarding, coleta de consentimento, dados cadastrais e preferências dos fãs.
- Validar e persistir dados no banco PostgreSQL.
- Publicar eventos relevantes (cadastro, interação, segmentação) em filas RabbitMQ para integração com o módulo analytics.
- Responder dúvidas, enviar notificações e interagir de forma personalizada com cada fã.

---

## Estrutura de Pastas

- **src/app/**: Lógica principal de tratamento de mensagens e fluxo conversacional.
- **src/core/**: Gerenciamento de estado do usuário, lógica de segmentação.
- **src/domain/**: Modelos de dados e entidades do domínio do fã.
- **src/queue/**: Integração com RabbitMQ (publicação de eventos).
- **src/utils/**: Funções utilitárias (validação de CPF, respostas booleanas, etc).
- **src/tests/**: Testes unitários e de integração.
- **index.ts**: Ponto de entrada do bot.
- **package.json / tsconfig.json**: Configuração do projeto Node.js/TypeScript.

---

## Fluxo de Funcionamento

1. **Conexão com WhatsApp**
   - Utiliza `whatsapp-web.js` para autenticação e envio/recebimento de mensagens.

2. **Onboarding e Coleta de Dados**
   - Gerencia o fluxo de perguntas para coletar: consentimento, nome, cidade, CPF, preferências de jogos e promoções.
   - Valida dados (ex: CPF) e armazena no banco.

3. **Persistência e Integração**
   - Salva dados dos fãs no PostgreSQL via Prisma ORM.
   - Publica eventos de cadastro, interação e segmentação em filas RabbitMQ.

4. **Interação e Notificações**
   - Responde dúvidas frequentes, envia mensagens personalizadas e notificações de campanhas.

---

## Integração com Analytics

- Eventos publicados no RabbitMQ são consumidos pelo módulo analytics para processamento de clusters, KPIs e segmentação.
- O bot pode receber comandos para acionar segmentações ou campanhas específicas.

---

## Tecnologias Utilizadas

- **Node.js** (runtime)
- **TypeScript** (tipagem e organização)
- **whatsapp-web.js** (integração WhatsApp)
- **Prisma ORM** (acesso ao PostgreSQL)
- **RabbitMQ** (mensageria)
- **PostgreSQL** (banco de dados)

---

## Como Executar

1. **Configure o `.env`** com as variáveis de ambiente necessárias (WhatsApp, banco, RabbitMQ).
2. **Instale as dependências** com `npm install`.
3. **Compile o projeto** com `npx tsc`.
4. **Inicie o bot** com `npm start` ou `node dist/index.js`.
5. **Escaneie o QR Code** no WhatsApp para autenticar.
6. **Interaja com o bot** via WhatsApp e acompanhe os eventos publicados.

---

## Observações

- O bot está pronto para ser expandido com novos fluxos, integrações e automações.
- Para produção, utilize variáveis de ambiente seguras e monitore o consumo de filas.
- Consulte os arquivos em `src/` para detalhes de cada módulo.

---

**FURIA Fan Intelligence — Bot: o canal oficial de engajamento e inteligência de fãs via WhatsApp!**
