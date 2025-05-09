from pydantic import BaseModel
from typing import List, Optional
from app.schemas.supplier import SupplierBasic  # versão reduzida

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class ProductCreate(ProductBase):
    supplier_ids: Optional[List[int]] = []  # IDs dos fornecedores

class ProductUpdate(ProductBase):
    supplier_ids: Optional[List[int]] = []

class Product(ProductBase):
    id: int
    suppliers: Optional[List[SupplierBasic]] = []

    class Config:
        from_attributes = True

class ProductBasic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
