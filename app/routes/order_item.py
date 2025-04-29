from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import order_item as order_item_model
from app.schemas import order_item as order_item_schema

router = APIRouter()

# Criar um novo item de pedido
@router.post("/order-items", response_model=order_item_schema.OrderItemResponse)
def create_order_item(order_item: order_item_schema.OrderItemCreate, db: Session = Depends(get_db)):
    db_order_item = order_item_model.OrderItem(order_id=order_item.order_id, product_id=order_item.product_id, quantity=order_item.quantity, price=order_item.price)
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

# Listar todos os itens de pedido
@router.get("/order-items", response_model=list[order_item_schema.OrderItemResponse])
def read_order_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(order_item_model.OrderItem).offset(skip).limit(limit).all()

# Obter um item de pedido por ID
@router.get("/order-items/{order_item_id}", response_model=order_item_schema.OrderItemResponse)
def read_order_item(order_item_id: int, db: Session = Depends(get_db)):
    order_item = db.query(order_item_model.OrderItem).filter(order_item_model.OrderItem.id == order_item_id).first()
    if order_item is None:
        raise HTTPException(status_code=404, detail="Order Item not found")
    return order_item

# Atualizar um item de pedido existente
@router.put("/order-items/{order_item_id}", response_model=order_item_schema.OrderItemResponse)
def update_order_item(order_item_id: int, order_item_update: order_item_schema.OrderItemCreate, db: Session = Depends(get_db)):
    order_item = db.query(order_item_model.OrderItem).filter(order_item_model.OrderItem.id == order_item_id).first()
    if order_item is None:
        raise HTTPException(status_code=404, detail="Order Item not found")
    
    order_item.quantity = order_item_update.quantity
    order_item.price = order_item_update.price
    db.commit()
    db.refresh(order_item)
    return order_item

# Excluir um item de pedido
@router.delete("/order-items/{order_item_id}")
def delete_order_item(order_item_id: int, db: Session = Depends(get_db)):
    order_item = db.query(order_item_model.OrderItem).filter(order_item_model.OrderItem.id == order_item_id).first()
    if order_item is None:
        raise HTTPException(status_code=404, detail="Order Item not found")
    
    db.delete(order_item)
    db.commit()
    return {"detail": "Order Item deleted"}
