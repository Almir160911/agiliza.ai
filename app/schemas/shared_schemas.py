from pydantic import BaseModel

class ProductBasic(BaseModel):
    id: int
    name: str

class SupplierBasic(BaseModel):
    id: int
    name: str
