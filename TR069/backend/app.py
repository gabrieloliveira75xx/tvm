from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Cliente, Pendencia, Incidente
from config import Config
import spacy

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

nlp = spacy.load("pt_core_news_sm")

def process_message(message):
    doc = nlp(message.lower())
    keywords = set([token.lemma_ for token in doc])
    return keywords

def get_client_info(client_name):
    client = Cliente.query.filter_by(nome=client_name).first()
    if not client:
        return None
    
    pendencia = Pendencia.query.filter_by(cliente_id=client.id, status='Pendente').first()
    incidente = Incidente.query.filter_by(cliente_id=client.id, status='Em andamento').first()
    
    return {
        'nome': client.nome,
        'status_pagamento': client.status_pagamento,
        'regiao': client.regiao,
        'ultima_interacao': client.ultima_interacao,
        'pendencia': pendencia.valor_pendente if pendencia else None,
        'incidente': incidente.tipo_incidente if incidente else None
    }

def generate_response(client_info, keywords):
    response = f"Olá, {client_info['nome']}! "
    
    if 'boleto' in keywords:
        if client_info['status_pagamento'] == 'em dia':
            response += "Você está com o pagamento em dia. Aqui está o seu boleto para o próximo mês: [link do boleto]"
        else:
            response += f"Você tem uma pendência de R${client_info['pendencia']}. Aqui está o link para pagamento: [link de pagamento]"
    
    elif 'lentidão' in keywords or 'internet' in keywords:
        if client_info['incidente']:
            response += f"Detectamos um incidente de {client_info['incidente']} na sua região. Nossos técnicos estão trabalhando para resolver o problema."
        else:
            response += "Não detectamos problemas na sua região. Tente reiniciar o seu roteador. Se o problema persistir, podemos agendar uma visita técnica."
    
    elif 'incidente' in keywords:
        if client_info['incidente']:
            response += f"Há um incidente de {client_info['incidente']} na sua região. Estamos trabalhando para resolver o problema o mais rápido possível."
        else:
            response += "Não há incidentes registrados na sua região no momento."
    
    else:
        response += "Como posso te ajudar hoje?"
    
    return response

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    client_name = ' '.join(message.split()[:2])
    
    client_info = get_client_info(client_name)
    if not client_info:
        return jsonify({'message': 'Desculpe, não consegui identificar você. Por favor, forneça seu nome completo.'})
    
    keywords = process_message(message)
    response = generate_response(client_info, keywords)
    
    client = Cliente.query.filter_by(nome=client_name).first()
    client.ultima_interacao = message
    db.session.commit()
    
    return jsonify({'message': response})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)