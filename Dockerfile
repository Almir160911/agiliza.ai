# Imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos locais para dentro do container
COPY . .

# Atualiza o pip e instala as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta 8000 (padrão FastAPI)
EXPOSE 8000

# Comando para iniciar o app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
