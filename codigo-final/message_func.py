def messages_function(name, message_template):
    """Replaces the placeholder '[nome]' in the message_template with the provided name."""
    # Ensure both name and template are strings
    name_str = str(name)
    template_str = str(message_template)
    
    # Perform the replacement
    formatted_message = template_str.replace("[nome]", name_str)
    return formatted_message

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
# Let's update the example to reflect the new logic
example_template = "Olá [nome], esta é uma mensagem de teste."
example_name = "Maria"
print(f"Example Input Template: {example_template}")
print(f"Example Input Name: {example_name}")
print(f"Example Output: {messages_function(example_name, example_template)}")
#print(messages_function("João", messages["message6"])) # Old example removed


# Define which variables can be imported when using "from contacts import *"
__all__ = ['messages_function']