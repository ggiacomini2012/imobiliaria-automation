# send_message_with_image_mac.py - Usa Preview + Cmd+C para imagem
import platform
import time
import os
import subprocess
import pyautogui
import pyperclip
from PIL import Image

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_OPEN = 7.0  # Segundos após abrir o WhatsApp
WAIT_AFTER_PASTE = 5.0  # AUMENTADO! Segundos após colar imagem
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

def send_message_with_image(phone_number, message, image_path):
    """Envia mensagem com imagem no WhatsApp."""
    try:
        # 1. Copiar imagem para clipboard (usando PREVIEW + Cmd+C)
        print("\n--- Etapa 1: Copiar Imagem via Preview --- ")
        if not copy_with_preview(image_path):
            return False

        # 2. Abrir WhatsApp com o número
        print("\n--- Etapa 2: Abrir WhatsApp --- ")
        whatsapp_uri = f"whatsapp://send?phone={phone_number}"
        print(f"Abrindo WhatsApp para {phone_number}...")
        subprocess.run(['open', whatsapp_uri], check=True)
        
        # 3. Esperar WhatsApp abrir
        print("\n--- Etapa 3: Esperar WhatsApp --- ")
        print(f"Aguardando {WAIT_AFTER_OPEN} segundos para o WhatsApp abrir...")
        time.sleep(WAIT_AFTER_OPEN)

        # 4. Colar a imagem
        print("\n--- Etapa 4: Colar Imagem --- ")
        print("Colando imagem (Cmd+V)...")
        pyautogui.hotkey('command', 'v')
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # 5. Limpar o clipboard e copiar a mensagem usando AppleScript diretamente
        print("\n--- Etapa 5: Copiar Mensagem com AppleScript --- ")
        
        # Criando um script AppleScript que define diretamente o conteúdo do clipboard
        escaped_message = message.replace('"', '\\"')  # Escape de aspas
        applescript = f'''
        set the clipboard to "{escaped_message}"
        '''
        
        print(f"Copiando mensagem via AppleScript: '{message}'")
        copy_result = subprocess.run(['osascript', '-e', applescript], 
                                 capture_output=True, text=True, check=False)
        
        if copy_result.returncode != 0:
            print(f"Aviso: Possível problema ao copiar texto: {copy_result.stderr}")
        
        # Pausa maior para garantir que o clipboard foi atualizado
        time.sleep(1.0)

        # 6. Colar a mensagem
        print("\n--- Etapa 6: Colar Mensagem --- ")
        print("Colando mensagem (Cmd+V)...")
        pyautogui.hotkey('command', 'v')
        time.sleep(0.5)

        # 7. Pressionar Enter
        print("\n--- Etapa 7: Pressionar Enter --- ")
        print("Pressionando Enter...")
        pyautogui.press('enter')
        time.sleep(WAIT_BEFORE_SEND_ENTER)

        print("\nSequência de automação GUI finalizada.")
        return True

    except pyautogui.FailSafeException:
        print("\nFAILSAFE TRIGGERED (mouse no canto). Parando automação GUI.")
        return False
    except Exception as e:
        print(f"\nErro durante automação GUI: {e}")
        try: print(f"Posição do mouse no erro: {pyautogui.position()}")
        except: pass
        return False

# --- Bloco Principal ---
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Uso: python send_message_with_image_mac.py <phone_number> <message> <image_path>")
        sys.exit(1)

    phone = sys.argv[1]
    msg = sys.argv[2]
    img = sys.argv[3]
    
    print("\n--- Iniciando Script de Envio de Mensagem com Imagem (macOS - Preview Copy) ---")
    print(f"Número: {phone}")
    print(f"Mensagem: {msg}")
    print(f"Imagem: {img}")
    
    if send_message_with_image(phone, msg, img):
        print("--- Script finalizado: Sucesso --- ")
    else:
        print("--- Script finalizado: Falha --- ") 