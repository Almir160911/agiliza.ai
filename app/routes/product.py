from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import product as product_model
from app.schemas import product as product_schema

router = APIRouter()

# Criar um novo produto
@router.post("/products", response_model=product_schema.ProductResponse)
def create_product(product: product_schema.ProductCreate, db: Session = Depends(get_db)):
    db_product = product_model.Product(name=product.name, description=product.description, price=product.price, category_id=product.category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# Listar todos os produtos
@router.get("/products", response_model=list[product_schema.ProductResponse])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(product_model.Product).offset(skip).limit(limit).all()

# Obter um produto por ID
@router.get("/products/{product_id}", response_model=product_schema.ProductResponse)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(product_model.Product).filter(product_model.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Atualizar um produto existente
@router.put("/products/{product_id}", response_model=product_schema.ProductResponse)
def update_product(product_id: int, product_update: product_schema.ProductCreate, db: Session = Depends(get_db)):
    product = db.query(product_model.Product).filter(product_model.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product.name = product_update.name
    product.description = product_update.description
    product.price = product_update.price
    product.category_id = product_update.category_id
    db.commit()
    db.refresh(product)
    return product

# Excluir um produto
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(product_model.Product).filter(product_model.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    db.delete(product)
    db.commit()
    return {"detail": "Product deleted"}
