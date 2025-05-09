from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.base import Base

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://agiliz_user:senha123@localhost/agiliz_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ✅ Adicione esta função:
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
