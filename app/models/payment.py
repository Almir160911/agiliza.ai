from sqlalchemy import Column, Integer, ForeignKey, String, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    amount = Column(Float)
    method = Column(String)  # Ex: Pix, Cartão, Dinheiro
    status = Column(String)  # Ex: pending, paid, failed

    order = relationship("Order", back_populates="payment")
