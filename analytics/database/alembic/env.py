import os
import sys
from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv

# 🔁 Carrega .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

# 🔁 Caminho do projeto para importar os models
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from database.connection import Base  # sua Base declarativa
from models import fan, segment, interaction, notification, kpi_reports  # importa os models

# Alembic Config
config = context.config

# Logging
fileConfig(config.config_file_name)

# 🔁 Define URL do banco a partir do .env
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME")

if not all([DB_USER, DB_PASS, DB_NAME]):
    raise Exception("Variáveis de ambiente do banco não estão corretamente definidas.")

database_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
config.set_main_option("sqlalchemy.url", database_url)

# Define os metadados para autogenerate
target_metadata = Base.metadata


def run_migrations_offline():
    """Migrations sem conexão ativa."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Migrations com engine e conexão ativa."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Decide se roda online ou offline
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()