# app/models/category.py
from sqlalchemy.orm import relationship
from app.core.database import Base
from sqlalchemy import Column, Integer, String

class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)

    products = relationship('Product', back_populates='category', cascade="all, delete")

    def __repr__(self):
        return f"<Category(name={self.name}, description={self.description})>"
