from sqlalchemy import Table, Column, ForeignKey, Integer, String
from app.core.database import Base  # ou de onde estiver seu Base
from sqlalchemy.orm import relationship


# Tabela de associação entre Product e Supplier
product_supplier_table = Table(
    "product_supplier",
    Base.metadata,
    Column("product_id", ForeignKey("products.id"), primary_key=True),
    Column("supplier_id", ForeignKey("suppliers.id"), primary_key=True),
    extend_existing=True,
)
