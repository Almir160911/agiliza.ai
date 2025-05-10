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
    SECRET_KEY=oyIB5PeILyZjjo5QJ3nhxbwYPpTl35NNMKQgH3fYHg4
    ALGORITHM=HS256


### Execute as migrações com Alembic
    alembic revision --autogenerate -m "migração correta sem apagar tabelas"

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

Pontos positivos da estrutura:

    Separação por responsabilidade
    Você usou diretórios como models, schemas, crud, routes, core, e services, o que é excelente. Isso segue a arquitetura recomendada para FastAPI e ajuda na manutenibilidade do código.

    Uso do Alembic
    Ter o diretório alembic e o alembic.ini indica que você está usando migrações de banco de dados versionadas, o que é uma prática profissional.

    Uso de virtualenv local (venv)
    Isso garante que dependências estão isoladas — ótimo para consistência entre ambientes.

    Presença de arquivos importantes

        requirements.txt ✅

        README.md ✅

        Dockerfile e docker-compose.yml ✅

        Scripts de setup como setup_env.sh, fix_env.sh etc. ✅
        Esses ajudam na automação e documentação do ambiente.

    Organização dentro de app/
    O main.py está dentro do diretório app/, que é o padrão em projetos estruturados com FastAPI.

⚠️ Pontos que podem ser melhorados:

    Evite __pycache__ e arquivos .pyc no repositório

        Eles não devem ser versionados. Certifique-se de que estão no .gitignore:

    __pycache__/
    *.py[cod]

Evite colocar arquivos de usuário (PDF, imagens, vídeos) na raiz

    Mover agiliz.ai.pdf, imagens/ e videos/ para um diretório como docs/ ou assets/ pode manter a raiz do projeto mais limpa.

Valide os nomes dos módulos

    O nome app está OK, mas o nome do diretório raiz agiliz.ai com ponto pode ser problemático se for usado como pacote Python. Prefira agiliz_ai ou agilizai para evitar erros em importações no futuro.

Divida main.py se ele estiver muito grande

    Se main.py crescer demais, considere extrair:

        create_app() para um arquivo como app/factory.py

        configurações para core/config.py (você já tem)

        startup e shutdown para um lifespan.py

 Veredito final:

Sua estrutura está dentro das boas práticas para aplicações Python modernas com FastAPI. Apenas recomendo ajustes menores para manter o projeto ainda mais limpo e robusto(mencionados acima).