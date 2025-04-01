# 🏡 Imobiliária Automation

Automação para comunicação com clientes e gerenciamento de contatos imobiliários.

## 📋 Visão Geral

Este projeto fornece ferramentas para automatizar o envio de mensagens personalizadas para clientes em potencial, otimizando o fluxo de trabalho em corretagem de imóveis.

## ✨ Funcionalidades

- **Envio Automatizado de Mensagens**: Envio de mensagens personalizadas via WhatsApp
- **Gestão de Contatos**: Controle de quais contatos já receberam mensagens
- **Interface Visual**: Banner indicativo de execução com controle via teclado
- **Monitoramento**: Registros detalhados das ações executadas

## 🚀 Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/ggiacomini2012/imobiliaria-automation.git
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure seus contatos no formato adequado no arquivo correspondente.

4. Execute o script principal:
   ```bash
   python enviar-mensagens.py
   ```

## ⚙️ Configuração

Edite os arquivos relevantes para personalizar:
- Lista de contatos
- Mensagens a serem enviadas
- Intervalos entre envios

## 🛑 Controles

- **ESC**: Encerra imediatamente o processo de envio

## 📊 Logging

O sistema mantém registros de todas as mensagens enviadas em `log.json`, evitando duplicidade de envios.

## 🔐 Segurança

- As credenciais e números de telefone não são compartilhados publicamente
- Uso consciente respeitando limites de APIs e termos de serviço das plataformas

## 🧩 Tecnologias

- Python
- PyAutoGUI
- Tkinter
- Bibliotecas de automação web

---

Desenvolvido por [ggiacomini2012](https://github.com/ggiacomini2012) 