from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image_url: Optional[str] = None
    category_id: int

    model_config = {
        "from_attributes": True
    }

class ProductCreate(ProductBase):
    pass

class ProductRead(ProductBase):
    id: int

class ProductResponse(ProductBase):
    id: int

    model_config = {
        "from_attributes": True
    }