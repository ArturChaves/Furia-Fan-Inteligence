# Makefile na pasta infra

# Caminho dos arquivos docker-compose
COMPOSE_FILES=-f docker-compose.yml -f docker-compose.analytics.yml

revision:
	docker compose -f docker-compose.yml -f docker-compose.analytics.yml run --rm alembic alembic revision --autogenerate -m ""

migrate:
	docker compose -f docker-compose.yml -f docker-compose.analytics.yml run --rm alembic alembic upgrade head