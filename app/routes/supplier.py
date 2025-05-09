from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.supplier import Supplier
from app import crud
from app.core.database import get_db
from app.schemas.supplier import SupplierCreate
from app.schemas.supplier import SupplierUpdate
from app.schemas.product import Product


router = APIRouter(prefix="/suppliers", tags=["suppliers"])

@router.post("/", response_model=Supplier)
def create_supplier(supplier: SupplierCreate, db: Session = Depends(get_db)):
    return crud.supplier.create_supplier(db, supplier)

@router.get("/{supplier_id}/products", response_model=List[Product])
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.supplier.get_suppliers(db, skip=skip, limit=limit)

@router.get("/{supplier_id}", response_model=Supplier)
def read_supplier(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud.supplier.get_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.put("/{supplier_id}", response_model=Supplier)
def update_supplier(supplier_id: int, supplier: SupplierUpdate, db: Session = Depends(get_db)):
    db_supplier = crud.supplier.update_supplier(db, supplier_id, supplier)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.delete("/{supplier_id}", response_model=dict)
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)):
    success = crud.supplier.delete_supplier(db, supplier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return {"detail": "Supplier deleted successfully"}

@router.get("/{supplier_id}/products", response_model=List[Product])
def get_supplier_products(supplier_id: int, db: Session = Depends(get_db)):
    db_supplier = crud.supplier.get_products_by_supplier(db, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier.products
