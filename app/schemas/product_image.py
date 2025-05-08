from pydantic import BaseModel

class ProductImageBase(BaseModel):
    filename: str

class ProductImageCreate(ProductImageBase):
    product_id: int

class ProductImage(ProductImageBase):
    id: int

    class Config:
        orm_mode = True
