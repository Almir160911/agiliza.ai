from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

import os
from dotenv import load_dotenv
import sys

# Garante que o diretório raiz está no sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Carrega variáveis de ambiente do .env
load_dotenv()

# Configuração do Alembic
config = context.config

# Define a URL do banco (de preferência via variável de ambiente)
config.set_main_option("sqlalchemy.url", os.getenv("DATABASE_URL", "postgresql+psycopg2://agiliz_user:senha123@localhost/agiliz_db"))

# Configuração de logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa os modelos aqui, **depois** que o sys.path estiver pronto
from app.core.base import Base  # <<< Base separado evita importações circulares
from app import models  # Isso garante o carregamento de todos os modelos

# Metadados alvo para 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline():
    """Executa as migrações em modo offline."""
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
    """Executa as migrações em modo online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
