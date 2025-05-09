# models/association.py
from sqlalchemy import Table, Column, ForeignKey, Integer
from app.core.database import Base

product_supplier_table = Table(
    "product_supplier",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("supplier_id", ForeignKey("suppliers.id"), primary_key=True),
)
