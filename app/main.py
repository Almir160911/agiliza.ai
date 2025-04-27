from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.core.database import engine, Base, get_db
from app.models import user, category, product, order

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "E-commerce API - FastAPI + PostgreSQL"}
