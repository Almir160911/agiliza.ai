from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import user as user_model
from app.schemas import user as user_schema
from app.core.database import get_db

router = APIRouter()

@router.post("/users", response_model=user_schema.UserResponse)
def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(user_model.User).filter(user_model.User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    db_user = user_model.User(name=user.name, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/users", response_model=list[user_schema.UserResponse])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(user_model.User).offset(skip).limit(limit).all()

@router.get("/users/{user_id}", response_model=user_schema.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=user_schema.UserResponse)
def update_user(user_id: int, user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.email = user.email
    db_user.password = user.password
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(user_model.User).filter(user_model.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": "User deleted"}
