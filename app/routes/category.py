from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import category as category_model
from app.schemas import category as category_schema

router = APIRouter()

# Criar uma nova categoria
@router.post("/categories", response_model=category_schema.CategoryResponse)
def create_category(category: category_schema.CategoryCreate, db: Session = Depends(get_db)):
    db_category = category_model.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

# Listar todas as categorias
@router.get("/categories", response_model=list[category_schema.CategoryResponse])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(category_model.Category).offset(skip).limit(limit).all()

# Obter uma categoria por ID
@router.get("/categories/{category_id}", response_model=category_schema.CategoryResponse)
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

# Atualizar uma categoria existente
@router.put("/categories/{category_id}", response_model=category_schema.CategoryResponse)
def update_category(category_id: int, category_update: category_schema.CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category.name = category_update.name
    db.commit()
    db.refresh(category)
    return category

# Excluir uma categoria
@router.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(category_model.Category).filter(category_model.Category.id == category_id).first()
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()
    return {"detail": "Category deleted"}
