from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud
from app.core.database import get_db
from app.schemas.product import ProductCreate
from app.schemas.product import Product
from app.schemas.product import ProductUpdate
from app.schemas.supplier import Supplier

router = APIRouter(
    prefix="/products",
    tags=["products"]
)

# Criar produto
@router.post("/", response_model=ProductCreate)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud.product.create_product(db=db, product=product)

# Listar todos os produtos
@router.get("/", response_model=List[Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.product.get_products(db=db, skip=skip, limit=limit)

# Obter produto por ID
@router.get("/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.product.get_product(db=db, product_id=product_id)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return db_product

# Atualizar produto
@router.put("/{product_id}", response_model=Product)
def update_product(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.product.update_product(db=db, product_id=product_id, product=product)
    if not db_product:
        raise HTTPException(status_code=404, detail="Produto não encontrado para atualização")
    return db_product

# Deletar produto
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    success = crud.product.delete_product(db=db, product_id=product_id)
    if not success:
        raise HTTPException(status_code=404, detail="Produto não encontrado para exclusão")
    return {"ok": True, "message": "Produto deletado com sucesso"}

@router.get("/{product_id}/suppliers", response_model=list[Supplier])
def read_product_suppliers(product_id: int, db: Session = Depends(get_db)):
    suppliers = crud.product.get_suppliers_by_product(db, product_id)
    if suppliers is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return suppliers
