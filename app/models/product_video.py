# models/product_videos.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class ProductVideo(Base):
    __tablename__ = "product_videos"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id", ondelete="CASCADE"), nullable=False)

    product = relationship("Product", back_populates="videos")
