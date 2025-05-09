from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.product_supplier import product_supplier_table
from app.schemas.shared_schemas import SupplierBasic

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    contact_email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    products = relationship("Product", secondary=product_supplier_table, back_populates="suppliers")
