# app/models/user.py
from sqlalchemy import Column, Integer, String
from app.core.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

    # Relacionamento com pedidos
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f"<User(username={self.username}, email={self.email})>"
