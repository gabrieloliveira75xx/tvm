import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Link } from 'react-scroll'
import { Menu, X } from 'lucide-react'
import ChatSimulator from './ChatSimulator'

export function LandingPageComponent() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  const [isMobile, setIsMobile] = useState(false)

  useEffect(() => {
    const checkMobile = () => setIsMobile(window.innerWidth < 768)
    checkMobile()
    window.addEventListener('resize', checkMobile)
    return () => window.removeEventListener('resize', checkMobile)
  }, [])

  const toggleMenu = () => setIsMenuOpen(!isMenuOpen)

  const menuItems = [
    { title: 'Visão Geral', id: 'visao-geral' },
    { title: 'Funcionalidades', id: 'funcionalidades' },
    { title: 'Tecnologias', id: 'tecnologias' },
    { title: 'Exemplos', id: 'exemplos' },
  ]

  return (
    <div className="min-h-screen bg-white text-gray-800 overflow-hidden">
      <header className="fixed top-0 left-0 right-0 z-50 bg-white bg-opacity-90 shadow-md">
        <nav className="container mx-auto px-6 py-4 flex justify-between items-center">
          <div className="text-2xl font-bold text-red-600">TR069 Integration</div>
          {isMobile ? (
            <button onClick={toggleMenu} className="text-red-600 focus:outline-none">
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          ) : (
            <ul className="flex space-x-8">
              {menuItems.map((item) => (
                <li key={item.id}>
                  <Link
                    to={item.id}
                    smooth={true}
                    duration={500}
                    className="text-gray-800 hover:text-red-600 transition-colors cursor-pointer"
                  >
                    {item.title}
                  </Link>
                </li>
              ))}
            </ul>
          )}
        </nav>
      </header>

      <AnimatePresence>
        {isMobile && isMenuOpen && (
          <motion.div
            initial={{ opacity: 0, y: -100 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -100 }}
            transition={{ duration: 0.3 }}
            className="fixed top-16 left-0 right-0 bg-white z-40 shadow-md"
          >
            <ul className="py-4">
              {menuItems.map((item) => (
                <li key={item.id} className="px-6 py-2">
                  <Link
                    to={item.id}
                    smooth={true}
                    duration={500}
                    className="block text-gray-800 hover:text-red-600 transition-colors cursor-pointer"
                    onClick={() => setIsMenuOpen(false)}
                  >
                    {item.title}
                  </Link>
                </li>
              ))}
            </ul>
          </motion.div>
        )}
      </AnimatePresence>

      <section className="h-screen flex items-center justify-center relative bg-gradient-to-r from-red-500 to-red-600">
        <div className="absolute inset-0 opacity-20 bg-pattern"></div>
        <div className="relative z-10 text-center text-white">
          <motion.h1
            className="text-4xl md:text-6xl font-bold mb-4"
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1, delay: 0.5 }}
          >
            Transformando a TVM com Automação e Escalabilidade
          </motion.h1>
          <motion.p
            className="text-lg md:text-xl"
            initial={{ y: 50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 1, delay: 0.7 }}
          >
            Integração TR069 com GenieACS para uma operação de rede eficiente
          </motion.p>
        </div>
      </section>

      <section id="visao-geral" className="py-20 bg-gray-100">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold mb-10 text-center text-red-600">Visão Geral do Projeto</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
            {[
              {
                title: 'Chat-Box para Clientes',
                description: 'Facilita a comunicação e o autoatendimento, realizando diagnósticos automáticos e melhorando a experiência do cliente.',
                icon: '💬'
              },
              {
                title: 'Chat-Box para Funcionários',
                description: 'Ferramenta de comunicação para equipes internas, permitindo a troca de informações rápidas e precisas, com suporte em tempo real.',
                icon: '👥'
              },
              {
                title: 'Sistema Técnico de NOC',
                description: 'Sistema de monitoramento em tempo real, fornecendo um mapa dinâmico de sinais de rede e possibilitando uma resposta rápida a falhas.',
                icon: '🖥️'
              }
            ].map((item, index) => (
              <motion.div
                key={index}
                className="bg-white p-6 rounded-lg shadow-lg"
                initial={{ opacity: 0, y: 50 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.2 }}
              >
                <div className="text-4xl mb-4">{item.icon}</div>
                <h3 className="text-2xl font-semibold mb-4 text-gray-800">{item.title}</h3>
                <p className="text-gray-800">{item.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      <section id="funcionalidades" className="py-20 bg-white">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold mb-10 text-center text-red-600">Funcionalidades Principais</h2>
          <div className="space-y-12">
            {[
              {
                title: 'Identificação do Cliente',
                description: 'Identifica automaticamente o cliente para facilitar o atendimento e personalizar a experiência.',
                icon: '🔍'
              },
              {
                title: 'Verificações Automáticas',
                description: 'Realiza diagnósticos automatizados para otimizar processos e evitar problemas antes que aconteçam.',
                icon: '🔧'
              },
              {
                title: 'Ações de Autoatendimento',
                description: 'Permite que os clientes resolvam problemas comuns por conta própria, sem a necessidade de intervenção humana.',
                icon: '🤖'
              },
              {
                title: 'Escalonamento de Suporte',
                description: 'Quando necessário, a plataforma escalará o atendimento para um técnico especializado, agilizando o processo.',
                icon: '📞'
              },
              {
                title: 'Monitoramento e Resolução de Falhas',
                description: 'Oferece uma visão em tempo real das falhas e realiza a resolução automática para garantir alta disponibilidade.',
                icon: '📊'
              }
            ].map((feature, index) => (
              <motion.div
                key={index}
                className="flex items-center space-x-6"
                initial={{ opacity: 0, x: -50 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5, delay: index * 0.2 }}
              >
                <div className="w-16 h-16 rounded-full flex items-center justify-center text-2xl font-bold text-red-600">
                  {feature.icon}
                </div>
                <div>
                  <h3 className="text-2xl font-semibold mb-2 text-gray-800">{feature.title}</h3>
                  <p className="text-gray-800">{feature.description}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      <section id="tecnologias" className="py-20 bg-gray-100 relative overflow-hidden">
        <div className="container mx-auto px-6 relative z-10">
          <h2 className="text-4xl font-bold mb-10 text-center text-gray-800">Tecnologias e Softwares Utilizados</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            {[
              {
                title: 'TR069 e GenieACS',
                description: 'Protocolo TR069 e a plataforma GenieACS para automação e gerenciamento remoto de dispositivos.',
                icon: '🔧'
              },
              {
                title: 'Integração com WhatsApp',
                description: 'Facilita a comunicação com clientes através da integração com o WhatsApp, proporcionando um canal de atendimento simples e direto.',
                icon: '📱'
              },
              {
                title: 'IA e Aprendizado de Máquina',
                description: 'Integração de Inteligência Artificial para otimização de processos e aprendizado contínuo de padrões de rede.',
                icon: '🧠'
              },
              {
                title: 'Ferramentas de Monitoramento',
                description: 'Utilização de ferramentas avançadas de monitoramento para garantir a eficiência da rede em tempo real.',
                icon: '📊'
              },
            ].map((tech, index) => (
              <motion.div
                key={index}
                className="bg-white p-6 rounded-lg shadow-lg"
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
              >
                <div className="text-4xl mb-4">{tech.icon}</div>
                <h3 className="text-xl font-semibold mb-2 text-gray-800">{tech.title}</h3>
                <p className="text-gray-800">{tech.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      <section id="exemplos" className="py-20 bg-white">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold mb-10 text-center text-red-600">Exemplos de Interação</h2>
          <div className="max-w-md mx-auto bg-gray-100 rounded-lg overflow-hidden shadow-lg">
            <div className="p-4 bg-red-600 text-white">
              <h3 className="text-xl font-semibold">Chat de Suporte</h3>
            </div>
            <div className="p-4 h-96 overflow-y-auto">
              <ChatSimulator />
            </div>
          </div>
        </div>
      </section>
    </div>
  )
}