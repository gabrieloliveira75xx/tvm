-- Create tables
CREATE TABLE IF NOT EXISTS cliente (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    status_pagamento VARCHAR(20) NOT NULL,
    regiao VARCHAR(50) NOT NULL,
    ultima_interacao VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS pendencia (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES cliente(id),
    valor_pendente FLOAT NOT NULL,
    data_vencimento DATE NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS incidente (
    id SERIAL PRIMARY KEY,
    cliente_id INTEGER REFERENCES cliente(id),
    regiao VARCHAR(50) NOT NULL,
    tipo_incidente VARCHAR(100) NOT NULL,
    status VARCHAR(20) NOT NULL
);

-- Insert sample data
INSERT INTO cliente (nome, status_pagamento, regiao, ultima_interacao) VALUES
('João Silva', 'em dia', 'Centro', 'consulta de boleto'),
('Maria Oliveira', 'pendente', 'Zona Norte', 'alteração de senha'),
('Carlos Santos', 'em dia', 'Zona Sul', 'relato de lentidão'),
('Ana Rodrigues', 'pendente', 'Zona Leste', 'solicitação de suporte'),
('Pedro Almeida', 'em dia', 'Zona Oeste', 'consulta de planos'),
('Fernanda Lima', 'pendente', 'Centro', 'reclamação de sinal'),
('Ricardo Souza', 'em dia', 'Zona Norte', 'elogio ao atendimento'),
('Juliana Costa', 'pendente', 'Zona Sul', 'dúvida sobre fatura'),
('Marcelo Ferreira', 'em dia', 'Zona Leste', 'agendamento de visita técnica'),
('Camila Martins', 'pendente', 'Zona Oeste', 'cancelamento de serviço');

INSERT INTO pendencia (cliente_id, valor_pendente, data_vencimento, status) VALUES
(2, 100.00, '2024-11-15', 'Pendente'),
(4, 150.00, '2024-11-10', 'Pendente'),
(6, 200.00, '2024-11-20', 'Pendente'),
(8, 120.00, '2024-11-05', 'Pendente'),
(10, 180.00, '2024-11-25', 'Pendente');

INSERT INTO incidente (cliente_id, regiao, tipo_incidente, status) VALUES
(1, 'Centro', 'Lentidão de Internet', 'Em andamento'),
(3, 'Zona Sul', 'Queda de Sinal', 'Em andamento'),
(5, 'Zona Oeste', 'Instabilidade na Conexão', 'Em andamento'),
(7, 'Zona Norte', 'Manutenção Programada', 'Em andamento'),
(9, 'Zona Leste', 'Problema no Roteador', 'Em andamento');