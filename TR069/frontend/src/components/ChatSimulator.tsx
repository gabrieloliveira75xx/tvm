import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';

interface Message {
  text: string;
  isBot: boolean;
}

const ChatSimulator: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    { text: "Olá! Boa tarde, primeiro, para iniciar o atendimento preciso do seu nome", isBot: true },
  ]);
  const [userInput, setUserInput] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const handleSendMessage = async () => {
    if (userInput.trim() === "") return;

    setMessages(prev => [...prev, { text: userInput, isBot: false }]);
    setUserInput("");
    setIsLoading(true);

    try {
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
      });

      if (!response.ok) {
        throw new Error('Falha na comunicação com o servidor');
      }

      const data = await response.json();
      setMessages(prev => [...prev, { text: data.message, isBot: true }]);
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error);
      setMessages(prev => [...prev, { text: "Desculpe, ocorreu um erro. Por favor, tente novamente mais tarde.", isBot: true }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto mb-4">
        {messages.map((message, index) => (
          <motion.div
            key={index}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
            className={`mb-2 ${message.isBot ? 'text-left' : 'text-right'}`}
          >
            <span className={`inline-block p-2 rounded-lg ${message.isBot ? 'bg-gray-200' : 'bg-red-100'}`}>
              {message.text}
            </span>
          </motion.div>
        ))}
        {isLoading && (
          <div className="text-center">
            <span className="inline-block p-2 rounded-lg bg-gray-200">Digitando...</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <div className="flex">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          placeholder="Digite sua mensagem..."
          className="flex-1 p-2 rounded-l-lg bg-gray-200 text-gray-800"
          disabled={isLoading}
        />
        <button
          onClick={handleSendMessage}
          className="bg-red-600 text-white p-2 rounded-r-lg disabled:bg-red-300"
          disabled={isLoading}
        >
          Enviar
        </button>
      </div>
    </div>
  );
};

export default ChatSimulator;