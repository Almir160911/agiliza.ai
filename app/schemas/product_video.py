from pydantic import BaseModel

class ProductVideoBase(BaseModel):
    filename: str

class ProductVideoCreate(ProductVideoBase):
    product_id: int

class ProductVideo(ProductVideoBase):
    id: int

    class Config:
        orm_mode = True
