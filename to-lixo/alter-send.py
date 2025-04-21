from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Inicializa o navegador e abre o WhatsApp Web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
input("Escaneie o QR Code e pressione Enter para continuar...")  # Aguarde login manual

cleaned_contacts = [
    {
        "phone_number": "5547997676797",
        "public_name": "Fernando"
    },
    {
        "phone_number": "5547991674477",
        "public_name": "Ricardo"
    }
]

# Loop para enviar mensagens sem abrir novas abas
for contact in cleaned_contacts:
    phone_number = contact["phone_number"]
    message = f"""Olá {contact['public_name']}, tudo bem?

Estou passando por aqui para compartilhar algo muito especial com você. 

Tenho me dedicado cada vez mais em trazer opções exclusivas de investimentos aqui do litoral de Santa Catarina, por isso gostaria de convidá-lo a conhecer minha Landing Page e saber um pouco mais do meu trabalho!

Acesse o link abaixo para conferir tudo com calma e, se surgir alguma dúvida ou se você quiser conversar mais sobre algum investimento, estarei à disposição para te ajudar:
https://lp.corazzaequityimob.com.br/

Fico muito feliz em poder compartilhar essa jornada com você e espero que as informações te ajudem a tomar as melhores decisões.

Grande abraço, atenciosamente  
Dieison Corazza."""

    # Acessa o chat do contato
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    time.sleep(10)  # Aguarde carregar o chat
    
    # Encontra o campo de mensagem e envia
    message_box = driver.find_element(By.XPATH, "//div[@title='Digite uma mensagem']")
    message_box.click()
    message_box.send_keys(message)
    time.sleep(2)
    message_box.send_keys(Keys.ENTER)  # Envia a mensagem

    time.sleep(5)  # Aguarda antes de enviar para o próximo contato

print("Mensagens enviadas!")

# Fecha o navegador após o envio
driver.quit()
