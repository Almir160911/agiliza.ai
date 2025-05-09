from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, Base
from app.routes import (
    user as user_routes,
    category as category_routes,
    product as product_routes,
    order as order_routes,
    order_item as order_item_routes,
    product_images as product_images_routes,
    product_videos as product_videos_routes,
    product as product_router,
    supplier as supplier_router
)

# Cria todas as tabelas do banco de dados a partir dos modelos declarados com Base
Base.metadata.create_all(bind=engine)

# Inicializa o app FastAPI
app = FastAPI()

# Configuração de CORS — em produção, restrinja os domínios permitidos
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção, troque "*" por ["https://seusite.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro das rotas da aplicação
app.include_router(user_routes.router)
app.include_router(category_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)
app.include_router(order_item_routes.router)
app.include_router(product_images_routes.router)
app.include_router(product_videos_routes.router)
app.include_router(product_router.router)
app.include_router(supplier_router.router)

@app.get("/")
def read_root():
    return {"message": "API Agiliz.AI rodando!"}
