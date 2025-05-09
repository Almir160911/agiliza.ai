from sqlalchemy.orm import Session
from typing import List, Optional
from app import models, schemas

# Criar fornecedor
def create_supplier(db: Session, supplier: schemas.SupplierCreate) -> models.Supplier:
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# Obter lista de fornecedores
def get_suppliers(db: Session, skip: int = 0, limit: int = 100) -> List[models.Supplier]:
    return db.query(models.Supplier).offset(skip).limit(limit).all()

# Obter fornecedor por ID
def get_supplier(db: Session, supplier_id: int) -> Optional[models.Supplier]:
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

# Atualizar fornecedor
def update_supplier(db: Session, supplier_id: int, supplier: schemas.SupplierUpdate) -> Optional[models.Supplier]:
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        return None
    for field, value in supplier.dict(exclude_unset=True).items():
        setattr(db_supplier, field, value)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

# Deletar fornecedor
def delete_supplier(db: Session, supplier_id: int) -> bool:
    db_supplier = db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()
    if not db_supplier:
        return False
    db.delete(db_supplier)
    db.commit()
    return True

def get_products_by_supplier(db: Session, supplier_id: int) -> Optional[models.Supplier]:
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

