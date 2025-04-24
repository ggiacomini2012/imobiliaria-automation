#!/usr/bin/env python3
# send_image_mac.py - Script para enviar imagem para WhatsApp no macOS
# Script independente para testes de automação

import sys
import os
import time
import logging
import subprocess
import pyautogui
from PIL import Image
from macos_image_utils import copy_image_macos_reliable

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

print("\n=== EXECUTANDO: send_image_mac.py ===\n")

# Configurações e constantes
WAIT_AFTER_OPEN = 7.0  # Segundos após abrir o WhatsApp
WAIT_AFTER_PASTE = 2.0  # Segundos após colar imagem
WAIT_BEFORE_SEND = 1.0  # Segundos antes de enviar

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

def send_image(phone_number, image_path):
    """Função principal que envia uma imagem para um contato no WhatsApp."""
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
    
    # 5. Colar a imagem (Command+V)
    try:
        print("Colando imagem (Command+V)...")
        pyautogui.hotkey('command', 'v')
        print("Comando para colar enviado.")
        
        # 6. Aguardar a imagem carregar
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)
        
        # 7. Enviar a imagem (Enter)
        print("Pressionando Enter para enviar...")
        pyautogui.press('enter')
        print("Imagem enviada.")
        
        return True
        
    except Exception as e:
        print(f"Erro na automação GUI: {e}")
        return False

def send_image_to_whatsapp(image_path, contact_number, caption=None):
    """
    Send an image to a WhatsApp contact on macOS.
    
    Args:
        image_path (str): Path to the image file
        contact_number (str): Contact's phone number
        caption (str, optional): Caption text for the image
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Verify image exists
        if not os.path.exists(image_path):
            logging.error(f"Image file not found: {image_path}")
            return False
            
        # Copy image to clipboard
        logging.info(f"Copying image to clipboard: {image_path}")
        if not copy_image_macos_reliable(image_path):
            logging.error("Failed to copy image to clipboard")
            return False
            
        # Open WhatsApp with contact
        logging.info(f"Opening WhatsApp for contact: {contact_number}")
        whatsapp_url = f"whatsapp://send?phone={contact_number}"
        subprocess.run(['open', whatsapp_url])
        
        # Wait for WhatsApp to open
        time.sleep(2.0)
        
        # Paste image (Command+V)
        logging.info("Pasting image from clipboard")
        subprocess.run(['osascript', '-e', 
            'tell application "System Events" to keystroke "v" using command down'])
        
        # Wait for image to load
        time.sleep(1.0)
        
        # Add caption if provided
        if caption:
            logging.info("Adding caption")
            # Press Tab to move to caption field
            subprocess.run(['osascript', '-e', 
                'tell application "System Events" to keystroke tab'])
            time.sleep(0.5)
            
            # Type caption
            subprocess.run(['osascript', '-e', 
                f'tell application "System Events" to keystroke "{caption}"'])
            time.sleep(0.5)
        
        # Send message (Return key)
        logging.info("Sending message")
        subprocess.run(['osascript', '-e', 
            'tell application "System Events" to keystroke return'])
        
        # Wait for send to complete
        time.sleep(1.0)
        
        logging.info("Image sent successfully")
        return True
        
    except Exception as e:
        logging.error(f"Error sending image: {e}", exc_info=True)
        return False

# Bloco principal
if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python send_image_mac.py <número_telefone> <caminho_imagem>")
        sys.exit(1)
        
    phone_number = sys.argv[1]
    image_path = sys.argv[2]
    
    print(f"\n--- Iniciando envio de imagem para WhatsApp (macOS) ---")
    print(f"Número: {phone_number}")
    print(f"Imagem: {image_path}")
    
    if send_image_to_whatsapp(image_path, phone_number):
        print("--- Envio de imagem completado com sucesso ---")
        sys.exit(0)
    else:
        print("--- Falha no envio de imagem ---")
        sys.exit(1) 