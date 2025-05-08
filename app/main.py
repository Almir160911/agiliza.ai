from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine
from app.models import user, order, payment, product, category, order_item, product_image, product_video  # importa os models
from app.routes import user as user_routes
from app.routes import category as category_routes
from app.routes import product as product_routes
from app.routes import order as order_routes
from app.routes import order_item as order_item_routes
from app.routes import product_images as product_images_routes
from app.routes import product_videos as product_videos_routes



# Cria as tabelas no banco
user.Base.metadata.create_all(bind=engine)
category.Base.metadata.create_all(bind=engine)
product.Base.metadata.create_all(bind=engine)
order.Base.metadata.create_all(bind=engine)
product_image.Base.metadata.create_all(bind=engine)
product_video.Base.metadata.create_all(bind=engine)


# Inicializa o app
app = FastAPI()

# Configura o CORS (permite requisições de outras origens, ajuste para produção!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # em produção, troque "*" pelos domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registra as rotas
app.include_router(user_routes.router)
app.include_router(category_routes.router)
app.include_router(product_routes.router)
app.include_router(order_routes.router)
app.include_router(order_item_routes.router)
app.include_router(product_images_routes.router)
app.include_router(product_videos_routes.router)

@app.get("/")
def read_root():
    return {"message": "API Agiliz.AI rodando!"}
