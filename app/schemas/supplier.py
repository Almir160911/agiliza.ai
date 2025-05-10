from pydantic import BaseModel
from typing import List, Optional
from app.schemas.shared_schemas import ProductBasic

class SupplierBase(BaseModel):
    name: str
    contact_email: Optional[str] = None
    whatsapp: str

class SupplierCreate(SupplierBase):
    product_ids: Optional[List[int]] = []  # IDs dos produtos fornecidos

class SupplierUpdate(SupplierBase):
    product_ids: Optional[List[int]] = []

class Supplier(SupplierBase):
    id: int
    products: Optional[List[ProductBasic]] = []

    class Config:
        from_attributes = True

class SupplierBasic(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
