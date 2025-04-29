from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://agiliza_user:senha123@localhost/agiliza_ai"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# ESSA função abaixo estava faltando
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
