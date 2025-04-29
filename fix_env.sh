#!/bin/bash

echo "🔵 Deletando ambiente virtual antigo (se existir)..."
rm -rf venv

echo "🟡 Criando novo ambiente virtual..."
python3 -m venv venv

echo "🟢 Ativando novo ambiente virtual..."
source venv/bin/activate

echo "🟣 Instalando pacotes necessários..."
pip install --upgrade pip
pip install fastapi uvicorn[standard] sqlalchemy psycopg2-binary python-dotenv alembic

echo "🧹 Atualizando requirements.txt..."
pip freeze > requirements.txt

echo "✅ Ambiente virtual criado e dependências instaladas com sucesso!"
echo "--------------------------------------------"
echo "ℹ️ Agora rode:"
echo "source venv/bin/activate"
echo "uvicorn app.main:app --reload"
echo "--------------------------------------------"


