from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.core.database import get_db

router = APIRouter()

@router.post("/users", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_model.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
