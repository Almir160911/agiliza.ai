from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import order as order_model
from app.schemas import order as order_schema

router = APIRouter()

# Criar um novo pedido
@router.post("/orders", response_model=order_schema.OrderResponse)
def create_order(order: order_schema.OrderCreate, db: Session = Depends(get_db)):
    db_order = order_model.Order(user_id=order.user_id, total_amount=order.total_amount, payment_status=order.payment_status)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# Listar todos os pedidos
@router.get("/orders", response_model=list[order_schema.OrderResponse])
def read_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(order_model.Order).offset(skip).limit(limit).all()

# Obter um pedido por ID
@router.get("/orders/{order_id}", response_model=order_schema.OrderResponse)
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(order_model.Order).filter(order_model.Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

# Atualizar um pedido existente
@router.put("/orders/{order_id}", response_model=order_schema.OrderResponse)
def update_order(order_id: int, order_update: order_schema.OrderCreate, db: Session = Depends(get_db)):
    order = db.query(order_model.Order).filter(order_model.Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.total_amount = order_update.total_amount
    order.payment_status = order_update.payment_status
    db.commit()
    db.refresh(order)
    return order

# Excluir um pedido
@router.delete("/orders/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(order_model.Order).filter(order_model.Order.id == order_id).first()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    db.delete(order)
    db.commit()
    return {"detail": "Order deleted"}
