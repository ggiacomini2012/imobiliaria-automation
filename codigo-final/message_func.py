def messages_function(name, message):
    return f"""Olá {name}... {message}"""

messages = {
    "message1": "Olá, tudo bem?",
    "message2": "Como você está?",
    "message3": "Estou bem, obrigado!",
    "message4": "Estou bem, obrigado!",
    "message5": "Estou bem, obrigado!",
    "message6": """🙏🏾

Faça uma excepcional semana!

Vamos pra cima!

🚀""",
}

#example of how to use the messages function
print(messages_function("João", messages["message6"]))  
#output:
# """🙏🏾

# Faça uma excepcional semana!

# Vamos pra cima!

# 🚀"""


# Define which variables can be imported when using "from contacts import *"
__all__ = ['messages_function']