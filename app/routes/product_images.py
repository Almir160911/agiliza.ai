from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.schemas.product_image import ProductImage
from app.crud import product_image
from app.core.database import get_db
from typing import List
import os
import shutil
from uuid import uuid4

UPLOAD_DIR = "imagens"

router = APIRouter(prefix="/product-images", tags=["Product Images"])

@router.post("/upload", response_model=ProductImage)
def upload_image(product_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    # Gera nome único
    file_ext = os.path.splitext(file.filename)[1]
    filename = f"{uuid4()}{file_ext}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    # Salva arquivo
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Registra no banco
    return product_image.create_product_image(db, image={"filename": filename, "product_id": product_id})

@router.get("/{product_id}", response_model=List[ProductImage])
def get_images(product_id: int, db: Session = Depends(get_db)):
    return product_image.get_images_by_product_id(db, product_id)
