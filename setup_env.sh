#!/bin/bash

echo "🚀 Criando ambiente virtual..."
python3 -m venv venv

echo "🚀 Ativando ambiente virtual..."
source venv/bin/activate

echo "🚀 Instalando dependências principais..."
pip install fastapi uvicorn[standard] sqlalchemy psycopg2 python-dotenv alembic

echo "🚀 Gerando arquivo requirements.txt..."
pip freeze > requirements.txt

echo "✅ Ambiente configurado com sucesso!"
echo "Agora abra o VS Code e selecione o interpretador: ./venv/bin/python"


