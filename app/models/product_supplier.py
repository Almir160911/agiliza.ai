from sqlalchemy import Column, Integer, ForeignKey, Table
from app.core.database import Base

product_supplier_table = Table(
    "product_supplier",
    Base.metadata,
    Column("product_id", Integer, ForeignKey("products.id"), primary_key=True),
    Column("supplier_id", Integer, ForeignKey("suppliers.id"), primary_key=True),
)
