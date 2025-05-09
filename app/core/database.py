from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Em produção, essa URL deve vir de uma variável de ambiente
DATABASE_URL = "postgresql+psycopg2://agiliz_user:senha123@localhost/agiliz_db"

# Criação do engine e da sessão
engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para os modelos
Base = declarative_base()

# Dependência de sessão para uso com FastAPI (com yield)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Opcional: Context manager útil para scripts standalone
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
