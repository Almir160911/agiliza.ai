from sqlalchemy.orm import Session
from app.models.product_video import ProductVideo
from app.schemas.product_video import ProductVideoCreate

def create_product_video(db: Session, video: ProductVideoCreate):
    db_video = ProductVideo(**video())
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def get_videos_by_product_id(db: Session, product_id: int):
    return db.query(ProductVideo).filter(ProductVideo.product_id == product_id).all()
