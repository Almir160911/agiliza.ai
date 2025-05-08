from sqlalchemy.orm import Session
from app.models.product_image import ProductImage
from app.schemas.product_image import ProductImageCreate

def create_product_image(db: Session, image: ProductImageCreate):
    db_image = ProductImage(**image())
    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image

def get_images_by_product_id(db: Session, product_id: int):
    return db.query(ProductImage).filter(ProductImage.product_id == product_id).all()
