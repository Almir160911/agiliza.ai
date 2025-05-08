#!/bin/bash

echo "Criando estrutura do projeto agiliz.ai..."

# Cria a pasta principal



# Arquivos na raiz
touch .env requirements.txt README.md

# Dentro de app
mkdir -p app/{models,schemas,crud,api,core,services}
touch app/__init__.py app/main.py

# Dentro de app/models
touch app/models/__init__.py app/models/user.py app/models/category.py app/models/product.py app/models/order.py app/models/order_item.py

# Dentro de app/schemas
touch app/schemas/__init__.py app/schemas/user.py app/schemas/category.py app/schemas/product.py app/schemas/order.py app/schemas/order_item.py

# Dentro de app/crud
touch app/crud/__init__.py app/crud/user.py app/crud/category.py app/crud/product.py app/crud/order.py app/crud/order_item.py

# Dentro de app/api
touch app/api/__init__.py app/api/auth.py app/api/users.py app/api/products.py app/api/orders.py app/api/categories.py app/api/push.py

# Dentro de app/core
touch app/core/__init__.py app/core/config.py app/core/database.py app/core/security.py

# Dentro de app/services
touch app/services/__init__.py app/services/push_service.py

# Cria a pasta de migrações
mkdir -p alembic

echo "Estrutura criada com sucesso!"

