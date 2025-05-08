from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str

    model_config = {
        "from_attributes": True
    }

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int

class CategoryResponse(CategoryBase):
    id: int

    model_config = {
        "from_attributes": True
    }

