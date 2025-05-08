# 🧠 Agiliz.ai API

API para gerenciamento de pedidos, usuários, produtos, imagens e vídeos. Desenvolvido com **FastAPI**, **SQLAlchemy**, **Alembic** e conteinerizado com **Docker**.

---

## 📁 Estrutura do Projeto

app/
├── core/ # Configurações, segurança, banco de dados
├── crud/ # Operações com o banco de dados (Create, Read, Update, Delete)
├── models/ # Modelos SQLAlchemy
├── routes/ # Rotas da API
├── schemas/ # Esquemas Pydantic
├── services/ # Lógicas auxiliares (ex: envio de push)
├── main.py # Ponto de entrada da aplicação


---

## 🚀 Como Rodar Localmente

### 1. Clone o repositório

```bash
    git clone https://github.com/seu-usuario/agiliz.ai.git
    cd agiliz.ai

 ### Crie e ative o ambiente virtual

    python3 -m venv venv
    source venv/bin/activate

### Instale as dependências

    pip install -r requirements.txt

### Configure variáveis de ambiente

    Crie um arquivo .env (ou configure diretamente em core/config.py):

    DATABASE_URL=postgresql://usuario:senha@localhost:5432/agiliz.ai
    SECRET_KEY=sua-chave-secreta
    ALGORITHM=HS256


### Execute as migrações com Alembic

    alembic upgrade head

### Rode o servidor

    uvicorn app.main:app --reload --port 8001

A API estará disponível em: http://localhost:8001

### Usando Docker (Opcional)

    docker-compose up --build

Testes

    Ainda não configurado. Sugestão: usar pytest e httpx.

Scripts úteis

    setup_env.sh – Cria variáveis de ambiente

    setup_postgres.sh – Inicializa banco PostgreSQL

    fix_env.sh – Corrige permissões do ambiente virtual

Tecnologias Utilizadas

    FastAPI

    SQLAlchemy

    Alembic

    Pydantic v2

    Uvicorn

    Docker

🧑‍💻 Autor

Desenvolvido por [Almir]
📧 fernandesalmir31@gmail.com
📦 GitHub: @Almir160911