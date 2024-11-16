from flask import Flask, request, jsonify, session
from flask_cors import CORS
from models import db, Cliente, Pendencia, Incidente
from config import Config
import spacy
from sqlalchemy import func, text, inspect
import re
from datetime import datetime, timedelta
import random
import string
import logging

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure secret key
CORS(app)
db.init_app(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

nlp = spacy.load("pt_core_news_sm")

def create_schema_if_not_exists():
    with app.app_context():
        with db.engine.connect() as connection:
            connection.execute(text("CREATE SCHEMA IF NOT EXISTS chatbot_schema"))
            connection.commit()

@app.before_first_request
def check_db_connection():
    try:
        inspector = inspect(db.engine)
        schemas = inspector.get_schema_names()
        logger.info(f"Available schemas: {schemas}")
        
        if 'chatbot_schema' in schemas:
            logger.info("chatbot_schema exists")
            tables = inspector.get_table_names(schema='chatbot_schema')
            logger.info(f"Tables in chatbot_schema: {tables}")
        else:
            logger.warning("chatbot_schema does not exist!")
        
        clients = Cliente.query.all()
        logger.info(f"Number of clients in database: {len(clients)}")
        for client in clients:
            logger.info(f"Client: {client.nome}")
    except Exception as e:
        logger.error(f"Error checking database: {str(e)}")

def process_message(message):
    doc = nlp(message.lower())
    keywords = set([token.lemma_ for token in doc])
    return keywords

def get_client_info(client_name):
    logger.info(f"Procurando cliente com nome: {client_name}")
    client_name = client_name.strip().lower()

    try:
        client_id = int(''.join(filter(str.isdigit, client_name)))
        client = Cliente.query.filter_by(id=client_id).first()
        
        if not client:
            logger.warning(f"Cliente com ID {client_id} não encontrado.")
            return None
        
        logger.info(f"Cliente encontrado: {client.nome}")
        
        pendencia = Pendencia.query.filter_by(cliente_id=client.id, status='Pendente').first()
        incidente = Incidente.query.filter_by(cliente_id=client.id, status='Em andamento').first()
        
        return {
            'nome': client.nome,
            'status_pagamento': client.status_pagamento,
            'regiao': client.regiao,
            'ultima_interacao': client.ultima_interacao,
            'pendencia': pendencia,
            'incidente': incidente
        }
    except ValueError:
        logger.error(f"Erro ao extrair ID do cliente: {client_name}")
        return None
    except Exception as e:
        logger.error(f"Erro ao buscar cliente: {str(e)}")
        return None

def generate_boleto():
    return ''.join(random.choices(string.digits, k=47))

def generate_response(client_info, keywords):
    responses = []
    
    if 'senha' in keywords and 'wi-fi' in keywords:
        responses.append("Para qual senha você gostaria de alterar o Wi-Fi? Por favor, digite a nova senha.")
        session['state'] = 'waiting_for_wifi_password'
    elif 'nome' in keywords and 'wi-fi' in keywords:
        responses.append("Para qual nome você gostaria de alterar o seu Wi-Fi? Por favor, digite o novo nome.")
        session['state'] = 'waiting_for_wifi_name'
    elif 'plano' in keywords:
        responses.append("Atualmente, temos os seguintes planos disponíveis:\n\n"
                         "1. 400 Mega: R$89,90 - O MAIS VENDIDO\n"
                         "2. 600 Mega: R$99,90 - O MELHOR CUSTO BENEFÍCIO\n"
                         "3. 800 Mega: R$119,90 - O MELHOR PREÇO\n\n"
                         "Por favor, escolha um plano digitando o número correspondente.")
        session['state'] = 'waiting_for_plan_choice'
    elif 'boleto' in keywords:
        codigo_barras = generate_boleto()
        responses.append(f"Claro! Aqui está o código de barras do seu boleto: {codigo_barras}")
        responses.append("Você pode efetuar o pagamento em qualquer casa lotérica, banco ou através do seu aplicativo bancário.")
    elif client_info['pendencia']:
        pendencia_date = client_info['pendencia'].data_vencimento.strftime('%d/%m/%Y')
        codigo_barras = generate_boleto()
        responses.append(f"Verifiquei que há uma possível pendência financeira no seu cadastro, e por esse motivo sua conexão está sem serviço. A data da pendência financeira é de {pendencia_date}.")
        responses.append(f"Estarei enviando o código de barras para pagamento: {codigo_barras}.")
        responses.append("Caso tenha realizado o pagamento via PIX, por gentileza, encaminhe o comprovante.")
        responses.append("Estamos realizando a solicitação de liberação de seu cadastro, e em até 30 minutos a sua conexão será restabelecida.")
    elif client_info['incidente']:
        responses.append("Verifiquei que houve um possível incidente na sua região. Estou verificando a situação e irei te manter informado com as atualizações. *Por favor, não mexa nos equipamentos*.")
        responses.append("Detectei que há um incidente na região que lhe atende. Já agendamos uma visita técnica ao local. Por favor, não mexa nos equipamentos até a chegada do técnico.")
        responses.append("O técnico foi ao local e realizou o reparo. Verifiquei que sua conexão foi restabelecida corretamente! Estarei finalizando o seu chamado por aqui. Caso tenha mais alguma dúvida, basta chamar!")
    elif client_info['status_pagamento'] == 'em dia':
        responses.append("Verifiquei que o seu pagamento está em dia e a sua internet parece estar funcionando corretamente! Em que posso ajudar hoje?")
    
    if not responses:
        responses.append("Como posso te ajudar hoje?")
    
    return responses

def handle_wifi_password_change(new_password):
    # Implement the actual password change logic here
    return f"A senha do Wi-Fi foi alterada com sucesso para: {new_password}. Por favor, reconecte-se à rede usando a nova senha."

def handle_wifi_name_change(new_name):
    # Implement the actual Wi-Fi name change logic here
    return f"O nome do seu Wi-Fi foi alterado com sucesso para: {new_name}. Por favor, procure pela nova rede ao se conectar."

def handle_plan_change(plan_choice):
    plans = {
        "1": "400 Mega",
        "2": "600 Mega",
        "3": "800 Mega"
    }
    if plan_choice in plans:
        # Implement the actual plan change logic here
        return f"Entendi que você deseja alterar para o plano {plans[plan_choice]}. Por favor, digite o código de 6 dígitos que você recebeu por SMS para confirmar a alteração."
    else:
        return "Desculpe, não reconheci esse plano. Por favor, escolha 1, 2 ou 3 para selecionar um plano."

def handle_technical_support(keywords):
    responses = []
    if 'lentidão' in keywords or 'velocidade' in keywords:
        responses.append("Entendo que você está enfrentando problemas de lentidão. Vamos tentar algumas soluções:")
        responses.append("1. Reinicie o seu roteador desligando-o da tomada por 30 segundos e ligando-o novamente.")
        responses.append("2. Verifique se há muitos dispositivos conectados à sua rede.")
        responses.append("3. Tente conectar seu dispositivo diretamente ao modem usando um cabo de rede.")
        responses.append("Se o problema persistir, podemos agendar uma visita técnica.")
    elif 'sinal' in keywords or 'conexão' in keywords:
        responses.append("Parece que você está tendo problemas com o sinal. Vamos verificar algumas coisas:")
        responses.append("1. Verifique se o cabo de rede está bem conectado ao seu modem.")
        responses.append("2. Tente posicionar o roteador em um local mais central da sua casa.")
        responses.append("3. Verifique se há interferências de outros dispositivos eletrônicos próximos ao roteador.")
        responses.append("Se essas dicas não resolverem, posso agendar uma visita técnica para você.")
    return responses

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '').lower()
    
    logger.info(f"Mensagem recebida: {message}")
    
    if 'client_id' not in session:
        if 'cliente' in message:
            client_info = get_client_info(message)
            if client_info:
                session['client_id'] = int(''.join(filter(str.isdigit, message)))
                session['state'] = 'initial'
                keywords = process_message(message)
                responses = generate_response(client_info, keywords)
            else:
                return jsonify({'messages': ['Desculpe, não consegui encontrar suas informações. Por favor, verifique se o número do cliente está correto e tente novamente.']})
        else:
            return jsonify({'messages': ['Olá! Para iniciar o atendimento, por favor, forneça seu nome no formato "cliente X", onde X é o seu número de cliente.']})
    else:
        client_info = get_client_info(f"cliente {session['client_id']}")
        if not client_info:
            session.clear()
            return jsonify({'messages': ['Desculpe, ocorreu um erro. Por favor, inicie o atendimento novamente.']})
        
        if session['state'] == 'waiting_for_wifi_password':
            response = handle_wifi_password_change(message)
            session['state'] = 'initial'
            return jsonify({'messages': [response]})
        elif session['state'] == 'waiting_for_wifi_name':
            response = handle_wifi_name_change(message)
            session['state'] = 'initial'
            return jsonify({'messages': [response]})
        elif session['state'] == 'waiting_for_plan_choice':
            response = handle_plan_change(message)
            if "código de 6 dígitos" in response:
                session['state'] = 'waiting_for_sms_code'
                session['chosen_plan'] = message
            else:
                session['state'] = 'initial'
            return jsonify({'messages': [response]})
        elif session['state'] == 'waiting_for_sms_code':
            if message.isdigit() and len(message) == 6:
                # Implement the actual plan change confirmation logic here
                plan = session['chosen_plan']
                response = f"Alteração de plano confirmada com sucesso! Seu novo plano é o {plan}."
                session['state'] = 'initial'
                del session['chosen_plan']
            else:
                response = "Código SMS inválido. Por favor, tente novamente ou digite 'cancelar' para cancelar a alteração do plano."
            return jsonify({'messages': [response]})
        else:
            keywords = process_message(message)
            responses = generate_response(client_info, keywords)
    
    client = Cliente.query.filter_by(id=session['client_id']).first()
    if client:
        client.ultima_interacao = message
        db.session.commit()
    
    logger.info(f"Respostas geradas: {responses}")
    return jsonify({'messages': responses})

if __name__ == '__main__':
    create_schema_if_not_exists()
    with app.app_context():
        db.create_all()
    app.run(host='192.168.1.253', port=5000, debug=True)