#!/usr/bin/env python3
# send_message_with_image_mac.py - Script para enviar mensagem com imagem no WhatsApp no macOS
# Script independente para testes de automação

import sys
import os
import time
import subprocess
import urllib.parse
import pyautogui
from PIL import Image

print("\n=== EXECUTANDO: send_message_with_image_mac.py ===\n")

# Configurações e constantes
WAIT_AFTER_OPEN = 7.0      # Segundos após abrir o WhatsApp
WAIT_AFTER_PASTE_IMG = 2.0 # Segundos após colar imagem
WAIT_AFTER_PASTE_TEXT = 1.0 # Segundos após colar texto
WAIT_BEFORE_SEND = 1.0     # Segundos antes de enviar

def validate_image(image_path):
    """Verifica se o arquivo de imagem existe e é válido."""
    if not os.path.exists(image_path):
        print(f"Erro: Arquivo não encontrado: {image_path}")
        return False
        
    try:
        with Image.open(image_path) as img:
            print(f"Imagem válida: {img.format} {img.size}")
            return True
    except Exception as e:
        print(f"Erro ao abrir imagem: {e}")
        return False

def copy_image_to_clipboard(image_path):
    """Copia uma imagem para o clipboard usando AppleScript."""
    try:
        abs_path = os.path.abspath(image_path)
        print(f"Copiando imagem para clipboard: {abs_path}")
        
        # Determinar o tipo de imagem baseado na extensão
        ext = os.path.splitext(abs_path)[1].lower()
        if ext == '.png':
            img_type = 'PNG picture'
        elif ext in ['.jpg', '.jpeg']:
            img_type = 'JPEG picture'
        else:
            img_type = 'picture'  # Tipo genérico
            
        # Script AppleScript para copiar a imagem
        script = f'''
        set the clipboard to (read (POSIX file "{abs_path}") as {img_type})
        '''
        
        result = subprocess.run(['osascript', '-e', script], 
                               capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"Erro ao copiar imagem: {result.stderr}")
            return False
            
        print("Imagem copiada para clipboard com sucesso.")
        return True
        
    except Exception as e:
        print(f"Erro ao copiar imagem para clipboard: {e}")
        return False

def open_whatsapp_with_number(phone_number):
    """Abre o WhatsApp com o número especificado."""
    whatsapp_uri = f"whatsapp://send?phone={phone_number}"
    
    try:
        print(f"Abrindo WhatsApp para número: {phone_number}")
        subprocess.run(['open', whatsapp_uri], check=True)
        print("WhatsApp aberto com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao abrir WhatsApp: {e}")
        return False

def send_message_with_image(phone_number, message, image_path):
    """Função principal que envia uma mensagem com imagem para um contato no WhatsApp."""
    # 1. Validar a imagem
    if not validate_image(image_path):
        return False
        
    # 2. Copiar a imagem para o clipboard
    if not copy_image_to_clipboard(image_path):
        return False
        
    # 3. Abrir o WhatsApp com o número
    if not open_whatsapp_with_number(phone_number):
        return False
    
    # 4. Esperar o WhatsApp abrir
    print(f"Aguardando {WAIT_AFTER_OPEN} segundos para o WhatsApp abrir...")
    time.sleep(WAIT_AFTER_OPEN)
    
    try:
        # 5. Colar a imagem (Command+V)
        print("Colando imagem (Command+V)...")
        pyautogui.hotkey('command', 'v')
        print("Comando para colar imagem enviado.")
        
        # 6. Aguardar a imagem carregar
        print(f"Aguardando {WAIT_AFTER_PASTE_IMG} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE_IMG)
        
        # 7. Inserir o texto da mensagem
        if message:
            print(f"Digitando mensagem: {message[:30]}...")
            pyautogui.write(message)
            time.sleep(WAIT_AFTER_PASTE_TEXT)
        
        # 8. Enviar (Enter)
        print("Pressionando Enter para enviar...")
        pyautogui.press('enter')
        print("Mensagem com imagem enviada.")
        
        return True
        
    except Exception as e:
        print(f"Erro na automação GUI: {e}")
        return False

# Bloco principal
if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) < 3:
        print("Uso: python send_message_with_image_mac.py <número_telefone> <caminho_imagem> [mensagem]")
        sys.exit(1)
        
    phone_number = sys.argv[1]
    image_path = sys.argv[2]
    message = sys.argv[3] if len(sys.argv) > 3 else ""
    
    print(f"\n--- Iniciando envio de mensagem com imagem para WhatsApp (macOS) ---")
    print(f"Número: {phone_number}")
    print(f"Imagem: {image_path}")
    print(f"Mensagem: {message[:50]}...")
    
    if send_message_with_image(phone_number, message, image_path):
        print("--- Envio completado com sucesso ---")
        sys.exit(0)
    else:
        print("--- Falha no envio ---")
        sys.exit(1) 