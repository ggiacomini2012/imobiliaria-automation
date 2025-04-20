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

## 🌐 Servidor Web (Flask)

Este projeto também inclui um servidor web simples para facilitar o acionamento do script de envio do WhatsApp.

1.  **Inicie o servidor e abra no navegador:**
    Certifique-se de ter instalado as dependências (incluindo Flask) com `pip install -r requirements.txt`.
    Execute o script `run_server.py`. Ele iniciará o servidor Flask em segundo plano e tentará abrir `http://localhost:5000` no Google Chrome (ou no seu navegador padrão como fallback).
    ```bash
    python run_server.py
    ```
    *Observação:* O script `run_server.py` terminará, mas o servidor Flask continuará rodando. Para parar o servidor, você precisará encontrar o terminal onde ele está sendo executado (procure pela saída do Flask) e pressionar `Ctrl+C`.

2.  **Acesse a interface (se não abrir automaticamente):**
    Abra seu navegador e vá para `http://localhost:5000` ou `http://<SEU_IP_LOCAL>:5000`.

3.  **Acione o script:**
    Clique no botão "Abrir WhatsApp" na página. Isso executará o script `modules/send-browser2app/send-back.py` no servidor, que por sua vez tentará abrir o WhatsApp Desktop com o número pré-configurado.

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