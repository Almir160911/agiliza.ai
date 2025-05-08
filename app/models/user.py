# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Boolean

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)  # ← ESTA LINHA DEVE EXISTIR
    entregador = Column(Boolean, default=False)
    # Relacionamento com pedidos
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
