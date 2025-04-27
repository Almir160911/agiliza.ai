from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.crud import user
from app.core.database import get_db
from app.models.user import User

router = APIRouter()

@router.post("/users/")
def create_new_user(name: str, email: str, db: Session = Depends(get_db)):
    return user.create_user(db=db, name=name, email=email)
