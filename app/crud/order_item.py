from sqlalchemy.orm import Session
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemCreate, OrderItemUpdate

def create_order_item(db: Session, item: OrderItemCreate):
    db_item = OrderItem(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_order_item(db: Session, item_id: int):
    return db.query(OrderItem).filter(OrderItem.id == item_id).first()

def update_order_item(db: Session, item_id: int, item_update: OrderItemUpdate):
    db_item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if db_item:
        for key, value in item_update.dict(exclude_unset=True).items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_order_item(db: Session, item_id: int):
    db_item = db.query(OrderItem).filter(OrderItem.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item
