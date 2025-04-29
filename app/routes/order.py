from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import order as models

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)

@router.get("/")
def get_orders(db: Session = Depends(get_db)):
    return db.query(models.Order).all()

@router.post("/")
def create_order(order: models.Order, db: Session = Depends(get_db)):
    db.add(order)
    db.commit()
    db.refresh(order)
    return order
