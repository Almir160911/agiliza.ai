# app/models/product.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.association import product_supplier_table


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    price = Column(Float)
    category_id = Column(Integer, ForeignKey('categories.id'))
    images = relationship("ProductImage", back_populates="product", cascade="all, delete")
    videos = relationship("ProductVideo", back_populates="product", cascade="all, delete")


    category = relationship('Category', back_populates='products')
    order_items = relationship('OrderItem', back_populates='product')
    suppliers = relationship("Supplier", secondary=product_supplier_table, back_populates="products")


    def __repr__(self):
        return f"<Product(name={self.name}, price={self.price}, category_id={self.category_id})>"
