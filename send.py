import pywhatkit as kit
import time
import pyautogui
import random

cleaned_contacts = [
    {
        "phone_number": "5547997676797",
        "public_name": "Gui"
    },
    {
        "phone_number": "5547991674477",
        "public_name": "Gabi"
    }
]

for contact in cleaned_contacts:
    phone_number = f"+{contact['phone_number']}"  # Formato internacional
    message = f"""Olá {contact['public_name']}, tudo bem?

Estou passando por aqui para compartilhar algo muito especial com você. 

Tenho me dedicado cada vez mais em trazer opções exclusivas de investimentos aqui do litoral de Santa Catarina, por isso gostaria de convidá-lo a conhecer minha Landing Page e saber um pouco mais do meu trabalho!

Acesse o link abaixo para conferir tudo com calma e, se surgir alguma dúvida ou se você quiser conversar mais sobre algum investimento, estarei à disposição para te ajudar:
https://lp.corazzaequityimob.com.br/

Fico muito feliz em poder compartilhar essa jornada com você e espero que as informações te ajudem a tomar as melhores decisões.

Grande abraço, atenciosamente  
Dieison Corazza."""

    # Envia a mensagem
    kit.sendwhatmsg_instantly(phone_number, message, 15, True, 2)
    
    time.sleep(random.uniform(3, 5))  # Pequeno intervalo para evitar bloqueios
    
    # pyautogui.hotkey('ctrl', 'w')
    
    time.sleep(1)   

print("Mensagens enviadas!")
