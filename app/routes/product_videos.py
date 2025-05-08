from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product_video import ProductVideo
from app.crud import product_video
from app.core.database import get_db
from typing import List
import os
import shutil
from uuid import uuid4

UPLOAD_DIR = "videos"

router = APIRouter(prefix="/product-videos", tags=["Product Videos"])

@router.post("/upload", response_model=ProductVideo)
def upload_video(product_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Gera nome único
    file_ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Salva arquivo
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Registra no banco
    return product_video.create_product_video(db, video={"filename": filename, "product_id": product_id})

@router.get("/{product_id}", response_model=List[ProductVideo])
def get_videos(product_id: int, db: Session = Depends(get_db)):
    return product_video.get_videos_by_product_id(db, product_id)
