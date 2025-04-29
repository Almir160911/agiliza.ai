from pydantic import BaseModel
from datetime import datetime
from typing import List
from .order_item import OrderItemRead

class OrderBase(BaseModel):
    user_id: int

    model_config = {
        "from_attributes": True
    }

class OrderCreate(OrderBase):
    pass

class OrderRead(OrderBase):
    id: int
    created_at: datetime
    items: List[OrderItemRead] = []
