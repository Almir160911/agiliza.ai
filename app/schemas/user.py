from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str
    email: EmailStr

    model_config = {
        "from_attributes": True
    }

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: int
