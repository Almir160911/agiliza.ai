from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.order_item import OrderItemCreate, OrderItemResponse
from models.order import OrderItem
from app.core.database import get_db

router = APIRouter(prefix="/order-items", tags=["OrderItems"])

@router.post("/", response_model=OrderItemResponse)
def create_order_item(order_item: OrderItemCreate, db: Session = Depends(get_db)):
    new_item = OrderItem(**order_item.dict())
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.get("/{item_id}", response_model=OrderItemResponse)
def get_order_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(OrderItem).get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Order item not found")
    return item
