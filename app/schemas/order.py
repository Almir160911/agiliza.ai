from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class OrderItemBase(BaseModel):
    product_id: int
    quantity: int

class OrderBase(BaseModel):
    user_id: int
    status: str

class OrderCreate(OrderBase):
    items: List[OrderItemBase]

class OrderResponse(OrderBase):
    id: int
    created_at: datetime
    updated_at: datetime
    items: List[OrderItemBase]  # ou outro schema se tiver

    model_config = {
        "from_attributes": True
    }
