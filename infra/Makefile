# Makefile na pasta infra

# Caminho dos arquivos docker-compose
COMPOSE_FILES=-f docker-compose.yml -f docker-compose.analytics.yml

revision:
	docker compose $(COMPOSE_FILES) run --rm alembic alembic revision --autogenerate -m ""

migrate:
	docker compose $(COMPOSE_FILES) run --rm alembic alembic upgrade head

up:
	docker compose $(COMPOSE_FILES) up -d --build

build-run:  ## 🔧 Sobe todos os containers com build forçado
	docker compose $(COMPOSE_FILES) up -d --build --remove-orphans

down:
	docker compose $(COMPOSE_FILES) down
