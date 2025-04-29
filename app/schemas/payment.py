from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PaymentBase(BaseModel):
    order_id: int
    payment_method: str
    amount: float
    status: str

    model_config = {
        "from_attributes": True
    }

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    id: int
    created_at: Optional[datetime]
