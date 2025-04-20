#!/usr/bin/env python3
# sudoiamge_mac.py - Script para enviar imagem para WhatsApp no macOS
# Baseado no send-back_mac.py, com funcionalidade de imagem adicionada

import platform
import time
import os
import subprocess
import pyautogui
from PIL import Image
import sys

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_OPEN = 7.0  # Segundos após abrir o WhatsApp
WAIT_AFTER_PASTE = 5.0  # Segundos após colar imagem
WAIT_BEFORE_SEND_ENTER = 0.5  # Segundos antes do Enter

def copy_with_preview(image_path):
    """Copia imagem para clipboard abrindo no Preview e usando Command+C."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Arquivo de imagem não encontrado: {abs_image_path}")
        return False
        
    try:
        # 1. Abrir a imagem no Preview
        print(f"Abrindo imagem no Preview: {abs_image_path}")
        result_open = subprocess.run(['open', '-a', 'Preview', abs_image_path], 
                                   capture_output=True, text=True, check=False)
        
        if result_open.returncode != 0:
            print(f"Erro ao abrir imagem no Preview: {result_open.stderr}")
            return False
            
        # 2. Esperar o Preview abrir
        print("Aguardando 2 segundos para o Preview abrir...")
        time.sleep(2.0)
        
        # 3. Selecionar tudo (Command+A)
        print("Enviando Command+A para selecionar tudo...")
        select_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "a" using command down
            end tell
        end tell
        '''
        result_select = subprocess.run(['osascript', '-e', select_script], 
                                     capture_output=True, text=True, check=False)
        
        if result_select.returncode != 0:
            print(f"Erro ao enviar Command+A: {result_select.stderr}")
            return False
            
        time.sleep(0.5)
        
        # 4. Copiar (Command+C)
        print("Enviando Command+C para copiar...")
        copy_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "c" using command down
            end tell
        end tell
        '''
        result_copy = subprocess.run(['osascript', '-e', copy_script], 
                                    capture_output=True, text=True, check=False)
        
        if result_copy.returncode != 0:
            print(f"Erro ao enviar Command+C: {result_copy.stderr}")
            return False
            
        time.sleep(0.5)
        
        # 5. Fechar Preview (Command+W)
        print("Enviando Command+W para fechar...")
        close_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "w" using command down
            end tell
        end tell
        '''
        result_close = subprocess.run(['osascript', '-e', close_script], 
                                     capture_output=True, text=True, check=False)
        
        # Não verificamos o resultado do fechamento, pois pode haver diálogo
        # perguntando se quer salvar, etc.
        
        # 6. Pressionando Esc para cancelar qualquer diálogo
        cancel_script = '''
        tell application "System Events"
            key code 53  # Código para a tecla Esc
        end tell
        '''
        subprocess.run(['osascript', '-e', cancel_script], 
                      capture_output=True, text=True, check=False)
                      
        print("Sequência de comando para copiar via Preview concluída.")
        return True
        
    except Exception as e:
        print(f"Erro durante o processo: {e}")
        return False

def open_whatsapp_with_number(phone_number, message=None):
    """Abre o WhatsApp com o número especificado."""
    os_name = platform.system()
    
    if os_name != 'Darwin':  # Só funciona em macOS
        print(f"Este script é específico para macOS, mas foi detectado: {os_name}")
        return False
    
    # Construir a URI do WhatsApp
    whatsapp_uri = f"whatsapp://send?phone={phone_number}"
    if message:
        import urllib.parse
        encoded_message = urllib.parse.quote(message)
        whatsapp_uri += f"&text={encoded_message}"
    
    try:
        print(f"Tentando abrir URI do WhatsApp: {whatsapp_uri}")
        subprocess.run(['open', whatsapp_uri], check=True)
        print("Comando 'open' executado com sucesso.")
        return True
    except Exception as e:
        print(f"Erro ao abrir URI do WhatsApp: {e}")
        return False

def send_image_to_whatsapp(phone_number, image_path):
    """Envia imagem para o WhatsApp no macOS."""
    try:
        # 1. Copiar imagem para clipboard com Preview
        print("\n--- Etapa 1: Copiar imagem para clipboard ---")
        if not copy_with_preview(image_path):
            print("Falha ao copiar imagem. Abortando.")
            return False
        
        # 2. Abrir WhatsApp com o número
        print("\n--- Etapa 2: Abrir WhatsApp ---")
        if not open_whatsapp_with_number(phone_number):
            print("Falha ao abrir WhatsApp. Abortando.")
            return False
        
        # 3. Esperar WhatsApp abrir
        print(f"\n--- Etapa 3: Aguardar {WAIT_AFTER_OPEN}s para WhatsApp abrir ---")
        time.sleep(WAIT_AFTER_OPEN)
        
        # 4. Colar a imagem
        print("\n--- Etapa 4: Colar imagem ---")
        print("Colando imagem (Command+V)...")
        pyautogui.hotkey('command', 'v')
        
        # 5. Esperar imagem carregar e pressionar Enter
        print(f"Aguardando {WAIT_AFTER_PASTE}s para imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)
        print("\n--- Etapa 5: Enviar imagem (Enter) ---")
        pyautogui.press('enter')
        time.sleep(WAIT_BEFORE_SEND_ENTER)
        
        print("\nSequência de automação finalizada com sucesso.")
        return True
        
    except Exception as e:
        print(f"Erro durante o processo: {e}")
        return False

# Bloco principal
if __name__ == "__main__":
    # Verificar argumentos
    if len(sys.argv) != 3:
        print("Uso: python sudoiamge_mac.py <número_telefone> <caminho_imagem>")
        sys.exit(1)
    
    phone_number = sys.argv[1]
    image_path = sys.argv[2]
    
    print(f"\n--- Iniciando envio de imagem para WhatsApp (macOS) ---")
    print(f"Número: {phone_number}")
    print(f"Imagem: {image_path}")
    
    if send_image_to_whatsapp(phone_number, image_path):
        print("--- Envio de imagem concluído com sucesso ---")
        sys.exit(0)
    else:
        print("--- Falha no envio de imagem ---")
        sys.exit(1) 