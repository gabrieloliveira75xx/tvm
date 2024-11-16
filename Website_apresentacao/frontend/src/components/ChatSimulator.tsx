import React, { useState, useEffect, useRef } from 'react'
import { Send } from 'lucide-react'

interface Message {
  text: string
  isUser: boolean
}

export default function ChatSimulator() {
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" })
  }

  useEffect(() => {
    // Envia a primeira mensagem quando o componente for montado
    setMessages([{ text: "Olá! Boa tarde, primeiro, para iniciar o atendimento preciso do seu nome", isUser: false }])
  }, [])

  useEffect(scrollToBottom, [messages])

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!input.trim()) return

    const userMessage = { text: input, isUser: true }
    setMessages(prev => [...prev, userMessage])
    setInput('')
    setIsLoading(true)

    try {
      const response = await fetch('http://192.168.1.253:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: input }),
      })

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`)
      }

      const data = await response.json()
      
      if (data.messages && Array.isArray(data.messages)) {
        const botMessages = data.messages.map((msg: string) => ({ text: msg, isUser: false }))
        setMessages(prev => [...prev, ...botMessages])
      } else {
        console.error('Unexpected response format:', data)
        setMessages(prev => [...prev, { text: 'Desculpe, ocorreu um erro. Por favor, tente novamente.', isUser: false }])
      }
    } catch (error) {
      console.error('Error:', error)
      setMessages(prev => [...prev, { text: 'Desculpe, ocorreu um erro. Por favor, tente novamente.', isUser: false }])
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-1 overflow-y-auto mb-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`mb-2 ${
              message.isUser ? 'text-right' : 'text-left'
            }`}
          >
            <span
              className={`inline-block p-2 rounded-lg ${
                message.isUser
                  ? 'bg-red-600 text-white'
                  : 'bg-gray-200 text-gray-800'
              }`}
            >
              {message.text}
            </span>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSubmit} className="flex">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Digite sua mensagem..."
          className="flex-1 p-2 border border-gray-300 rounded-l-md focus:outline-none focus:ring-2 focus:ring-red-600"
          disabled={isLoading}
        />
        <button
          type="submit"
          className="bg-red-600 text-white p-2 rounded-r-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-600"
          disabled={isLoading}
        >
          <Send size={20} />
        </button>
      </form>
    </div>
  )
}
