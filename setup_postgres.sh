#!/bin/bash

# 1. Instala PostgreSQL (caso não tenha)
echo "Instalando PostgreSQL..."
sudo apt update
sudo apt install -y postgresql postgresql-contrib

# 2. Inicializa e ativa o serviço
echo "Ativando serviço do PostgreSQL..."
sudo systemctl enable postgresql
sudo systemctl start postgresql

# 3. Configurações
DB_NAME="agiliz"    # troque aqui se seu banco tiver outro nome no database.py
DB_USER="admin"    # troque aqui pelo user do seu database.py
DB_PASS="123"      # troque aqui pela senha do seu database.py

# 4. Cria banco, usuário e permissões
echo "Configurando banco de dados..."

sudo -u postgres psql <<EOF
CREATE DATABASE $DB_NAME;
CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';
ALTER ROLE $DB_USER SET client_encoding TO 'utf8';
ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed';
ALTER ROLE $DB_USER SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

echo "PostgreSQL configurado com sucesso!"
