# Explicação do Processo de Iteração em `bulk_sender.py`

Este documento detalha como o script `codigo-final/bulk_sender.py` processa a lista de contatos para enviar mensagens em massa via WhatsApp.

## Fluxo da Iteração

O coração do processo é um loop `for` que itera sobre cada contato presente na lista `cleaned_contacts2`. Esta lista é importada do arquivo `contacts_template.py`.

```python
# (Linhas 75-109 aproximadamente)
for i, contact in enumerate(cleaned_contacts2):
    # ... corpo do loop ...
```

### Passos Dentro de Cada Iteração:

1.  **Obtenção do Contato e Índice:**
    *   `enumerate(cleaned_contacts2)` fornece o índice (`i`, começando do 0) e o dicionário do contato (`contact`) a cada passo.
    *   O índice `i` é usado para exibir o progresso (ex: "Processando contato 1/50").

2.  **Extração dos Dados do Contato:**
    *   `phone_number = contact.get('phone_number')`
    *   `public_name = contact.get('public_name')`
    *   O script tenta extrair o número de telefone e o nome público do dicionário do contato atual.

3.  **Validação dos Dados:**
    *   `if not phone_number or not public_name:`
    *   Verifica se tanto o número quanto o nome foram obtidos com sucesso.
    *   Se algum estiver faltando, o contato é **ignorado** (`continue`), uma mensagem é exibida, e o contador de falhas (`fail_count`) é incrementado.

4.  **Formatação da Mensagem:**
    *   `formatted_message = messages_function(public_name, message_template)`
    *   Chama a função `messages_function` (importada de `message_func.py`) para substituir o placeholder `[nome]` no `message_template` (recebido como argumento do script) pelo `public_name` do contato atual.
    *   Se ocorrer um erro durante a formatação, o contato é **ignorado** (`continue`), uma mensagem de erro é exibida, e `fail_count` é incrementado.

5.  **Codificação para URL:**
    *   `encoded_message = urllib.parse.quote(formatted_message)`
    *   A mensagem formatada é codificada para garantir que caracteres especiais sejam tratados corretamente quando incluídos em uma URL (o link do WhatsApp).

6.  **Construção da URI do WhatsApp:**
    *   `whatsapp_uri = f"whatsapp://send?phone={phone_number}&text={encoded_message}"`
    *   Cria o link `whatsapp://` específico para iniciar uma conversa com o `phone_number` e preencher a caixa de texto com a `encoded_message`.

7.  **Tentativa de Abertura do Link:**
    *   `open_whatsapp_uri(whatsapp_uri)`
    *   Chama uma função auxiliar que tenta abrir este link usando o comando apropriado do sistema operacional (Windows: `os.startfile`, macOS: `open`, Linux: `xdg-open`).
    *   A função retorna `True` se a abertura for iniciada com sucesso, `False` caso contrário.

8.  **Contagem de Sucesso/Falha:**
    *   `success_count` é incrementado se `open_whatsapp_uri` retornar `True`.
    *   `fail_count` é incrementado se `open_whatsapp_uri` retornar `False`.

9.  **Pausa:**
    *   `time.sleep(1.5)`
    *   O script pausa por 1.5 segundos antes de prosseguir para a próxima iteração (o próximo contato). Isso evita sobrecarregar o sistema ou ser bloqueado por ações muito rápidas.

## Finalização

Após o loop `for` terminar de processar todos os contatos em `cleaned_contacts2`, o script imprime um resumo final com a contagem total de envios bem-sucedidos (`success_count`) e falhos/ignorados (`fail_count`). 