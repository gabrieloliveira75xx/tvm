-- Create tables
CREATE TABLE IF NOT EXISTS chatbot_schema.cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    status_pagamento VARCHAR(20) NOT NULL,
    regiao VARCHAR(50) NOT NULL,
    ultima_interacao VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS chatbot_schema.pendencia (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES chatbot_schema.cliente(id),
    valor_pendente FLOAT NOT NULL,
    data_vencimento DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS chatbot_schema.incidente (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES chatbot_schema.cliente(id),
    regiao VARCHAR(50) NOT NULL,
    tipo_incidente VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Insert sample data
INSERT INTO chatbot_schema.cliente (nome, status_pagamento, regiao, ultima_interacao) VALUES
('cliente 1', 'em dia', 'Centro', 'consulta de boleto'),
('cliente 2', 'em dia', 'Zona Norte', 'alteração de senha'),
('cliente 3', 'em dia', 'Zona Sul', 'relato de lentidão'),
('cliente 4', 'pendente', 'Zona Leste', 'solicitação de suporte'),
('cliente 5', 'em dia', 'Zona Oeste', 'consulta de planos'),
('cliente 6', 'em dia', 'Centro', 'reclamação de sinal'),
('cliente 7', 'em dia', 'Zona Norte', 'elogio ao atendimento'),
('cliente 8', 'em dia', 'Zona Sul', 'dúvida sobre fatura'),
('cliente 9', 'em dia', 'Zona Leste', 'agendamento de visita técnica'),
('cliente 10', 'em dia', 'Zona Oeste', 'cancelamento de serviço'),
('cliente 11', 'pendente', 'Centro', 'consulta de boleto'),
('cliente 12', 'em dia', 'Zona Norte', 'alteração de plano'),
('cliente 13', 'em dia', 'Zona Sul', 'consulta de velocidade'),
('cliente 14', 'em dia', 'Zona Leste', 'problema com roteador'),
('cliente 15', 'em dia', 'Zona Oeste', 'dúvida sobre fatura');

INSERT INTO chatbot_schema.pendencia (cliente_id, valor_pendente, data_vencimento, status) VALUES
(4, 150.00, '2024-11-10', 'Pendente'),
(11, 200.00, '2024-11-20', 'Pendente');

INSERT INTO chatbot_schema.incidente (cliente_id, regiao, tipo_incidente, status) VALUES
(3, 'Zona Sul', 'Queda de Sinal', 'Em andamento'),
(9, 'Zona Leste', 'Problema no Roteador', 'Em andamento'),
(14, 'Zona Leste', 'Lentidão de Internet', 'Em andamento');