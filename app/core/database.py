from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do .env
load_dotenv()

# Conexão com o banco de dados PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Criação da engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

# Criando a base de modelos
Base = declarative_base()

# Sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
