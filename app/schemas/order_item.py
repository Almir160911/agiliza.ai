from pydantic import BaseModel

class OrderItemBase(BaseModel):
    order_id: int
    product_id: int
    quantity: int
    unit_price: float

    model_config = {
        "from_attributes": True
    }

class OrderItemCreate(OrderItemBase):
    pass

class OrderItemRead(OrderItemBase):
    id: int
