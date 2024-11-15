# Cat-Box Inteligente Integrado com CWMP

Este projeto implementa uma **Cat-Box inteligente**, que é integrada ao **CWMP** (CPE WAN Management Protocol), oferecendo uma solução técnica melhorada para monitoramento e controle remoto de dispositivos. A arquitetura do sistema envolve uma **API backend** desenvolvida com **FastAPI**, um **frontend** em **React**, e um banco de dados relacional **PostgreSQL**.

## Descrição

A **Cat-Box Inteligente** foi projetada para permitir que os usuários monitorem e interajam com suas caixas de gato (ou outros dispositivos) por meio de uma plataforma intuitiva, garantindo maior controle e automação no processo. A integração com **CWMP** permite uma comunicação eficiente e segura entre os dispositivos e o backend da aplicação.

O sistema também inclui melhorias técnicas, como:
- **Interação em tempo real** com a aplicação via **React**.
- **Comunicação e controle de dispositivos** usando o protocolo **CWMP**.
- **Armazenamento robusto** dos dados no banco de dados **PostgreSQL**.
- **Backend** otimizado com **FastAPI**, garantindo alta performance.

## Tecnologias Utilizadas

- **Python 3.8+**
- **PostgreSQL** (banco de dados relacional)
- **FastAPI** (framework para API)
- **React** (frontend)
- **Flask** (para integração com o backend)
- **spacy** (para processamento de linguagem natural, caso aplicável)
- **psycopg2-binary** (driver PostgreSQL para Python)
- **CWMP** (integração com dispositivos)

### Pacotes Python utilizados:

- `Flask==2.0.1`
- `Flask-SQLAlchemy==2.5.1`
- `Flask-CORS==3.0.10`
- `python-dotenv==0.19.0`
- `spacy==3.1.0`
- `psycopg2-binary==2.9.1`

## Como Iniciar o Projeto

### Pré-requisitos

Antes de começar, certifique-se de ter o **Python 3.8+** e **PostgreSQL** instalados. Você também precisará do **Node.js** e **npm** para rodar o frontend (React).

1. **Instalar as dependências do backend (Python)**

   No diretório do projeto, crie e ative um ambiente virtual:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate     # No Windows
