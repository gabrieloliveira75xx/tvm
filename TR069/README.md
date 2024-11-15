# CHAT-BOX Integrado com TR069 e Chatbox

Este projeto integra um **Chatbox** inteligente com **TR069** (CWMP). Ele utiliza **Python** no backend, **React** no frontend e **PostgreSQL** como banco de dados. A aplicação simula um sistema de interação com o usuário, com um chatbot que responde a perguntas baseadas em dados simulados.

## Tecnologias Utilizadas

- **Python** (Backend)
- **PostgreSQL** (Banco de Dados)
- **FastAPI** (API)
- **React** (Frontend)

## Pré-requisitos

Antes de rodar o projeto, verifique se você tem os seguintes pré-requisitos instalados:

- **Python 3.8+**
- **Node.js 14+**
- **PostgreSQL**

## Configuração do Projeto

### 1. Configuração do Backend

#### Passo 1: Navegue até o diretório do backend

cd backend

#### Passo 2: Crie um ambiente virtual e ative-o

- No Linux/Mac:

    python -m venv venv
    source venv/bin/activate

- No Windows:

    python -m venv venv
    venv\Scripts\activate

#### Passo 3: Instale as dependências do backend

pip install -r requirements.txt

#### Passo 4: Configure o banco de dados

- Crie um banco de dados PostgreSQL.
- Atualize o arquivo `.env` com suas credenciais do banco de dados.

O arquivo `.env` deve conter a seguinte linha (exemplo):

DATABASE_URL=postgresql://usuario:senha@localhost/nome_do_banco

#### Passo 5: Inicialize o banco de dados

Rode o script SQL de inicialização do banco de dados:

psql -d seu_banco_de_dados -f ../database/init_db.sql

#### Passo 6: Execute o backend (Flask)

python app.py

### 2. Configuração do Frontend

#### Passo 1: Navegue até o diretório do frontend

cd frontend

#### Passo 2: Instale as dependências do frontend

npm install

#### Passo 3: Inicie o servidor React

npm start

### 3. Acessando o Projeto

Após rodar o **backend** e o **frontend**, acesse a aplicação em seu navegador:

http://localhost:3000

A interface do chatbox estará disponível na seção **"Exemplos de Interação"**. Você poderá interagir com o chatbot, digitando mensagens e recebendo respostas baseadas nos dados simulados do banco de dados.

## Estrutura do Projeto

Aqui está a estrutura de diretórios e arquivos do projeto:

/project-root
├── backend/                # Código do backend (API e integração com o banco de dados)
│   ├── app.py              # Arquivo principal da aplicação Flask
│   ├── .env                # Arquivo de variáveis de ambiente (não comite no Git)
│   ├── requirements.txt    # Arquivo de dependências do backend (Python)
│   └── database/           # Scripts de banco de dados
│       └── init_db.sql     # Script de inicialização do banco de dados
├── frontend/               # Código do frontend (React)
│   ├── src/                # Código-fonte do frontend React
│   ├── public/             # Arquivos públicos (HTML, ícones, etc.)
│   └── package.json        # Arquivo de dependências do frontend (React)
├── .gitignore              # Arquivo de exclusão do Git (não comite o .env)
└── README.md               # Este arquivo

### Backend

O **backend** foi implementado com **Flask**, e a aplicação se conecta a um banco de dados **PostgreSQL**. Ele expõe endpoints REST para interação com o frontend. O chatbot é alimentado por dados simulados no banco de dados.

### Frontend

O **frontend** é construído com **React** e comunica-se com o backend para enviar mensagens ao chatbox e exibir as respostas. A interface do usuário permite interação com o chatbot de forma simples e direta.

## Dependências

### Backend (Python)

As dependências do backend podem ser instaladas a partir do arquivo `requirements.txt`:

- Flask==2.0.1
- Flask-SQLAlchemy==2.5.1
- Flask-CORS==3.0.10
- python-dotenv==0.19.0
- spacy==3.1.0
- psycopg2-binary==2.9.1

Para instalar as dependências do backend, execute o seguinte comando:

pip install -r requirements.txt

### Frontend (Node.js)

As dependências do frontend podem ser instaladas utilizando o `npm`:

npm install

## Contribuições

Contribuições são bem-vindas! Se você encontrar um bug ou quiser sugerir melhorias, abra um **issue** ou envie um **pull request**.

## Licença

Este projeto está licenciado sob a **MIT License**.
