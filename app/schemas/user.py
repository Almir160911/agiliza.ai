from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    entregador: Optional[bool] = False  # novo campo
    whatsapp: str
    class Config:
        from_attributes = True

class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    entregador: bool

    class Config:
        from_attributes = True
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    entregador: bool

    class Config:
        from_attributes = True  # ou orm_mode = True se estiver usando Pydantic v1
