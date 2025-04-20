# send_message_with_image_mac.py
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

def copy_image_to_clipboard(image_path):
    """Copia imagem para clipboard no macOS, tentando APENAS 'as picture'."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Imagem não encontrada em {abs_image_path}")
        return False

    try:
        # Verificar se a imagem é válida
        with Image.open(abs_image_path) as img:
            print(f"Imagem válida detectada: {img.format} {img.size}")
    except Exception as img_e:
        print(f"Erro ao verificar imagem: {img_e}")
        return False

    try:
        # Limpar o clipboard antes de copiar a imagem
        print("Limpando clipboard...")
        clear_result = subprocess.run(['osascript', '-e', 'set the clipboard to ""'], capture_output=True, text=True, check=False)
        print(f"Limpeza - stdout: {clear_result.stdout.strip()}, stderr: {clear_result.stderr.strip()}, code: {clear_result.returncode}")
        time.sleep(0.5)

        # Tentar copiar APENAS com 'as picture'
        print("\nTentando copiar como 'picture' genérico...")
        script_generic = f'set the clipboard to (read (POSIX file "{abs_image_path}") as picture)'
        print(f"Executando osascript (genérico): {script_generic}")
        result_generic = subprocess.run(['osascript', '-e', script_generic], capture_output=True, text=True, check=False)
        print(f"Resultado (genérico) - stdout: {result_generic.stdout.strip()}, stderr: {result_generic.stderr.strip()}, code: {result_generic.returncode}")
        
        if result_generic.returncode == 0:
            print("\nImagem copiada para clipboard com sucesso (formato genérico).")
            print("Pausa de 1s após cópia...")
            time.sleep(1.0) # Pausa extra após a cópia bem-sucedida
            return True
        else:
            print(f"\nErro final ao copiar imagem para clipboard.")
            return False
            
    except Exception as e:
        print(f"\nErro EXCEPCIONAL ao copiar imagem para clipboard: {e}")
        return False

def send_message_with_image(phone_number, message, image_path):
    """Envia mensagem com imagem no WhatsApp."""
    try:
        # 1. Copiar imagem para clipboard
        if not copy_image_to_clipboard(image_path):
            return False

        # 2. Abrir WhatsApp com o número
        whatsapp_uri = f"whatsapp://send?phone={phone_number}"
        print(f"Abrindo WhatsApp para {phone_number}...")
        subprocess.run(['open', whatsapp_uri], check=True)
        
        # 3. Esperar WhatsApp abrir
        print(f"Aguardando {WAIT_AFTER_OPEN} segundos para o WhatsApp abrir...")
        time.sleep(WAIT_AFTER_OPEN)

        # 4. Colar a imagem
        print("\nColando imagem...")
        pyautogui.hotkey('command', 'v')
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # 5. Limpar o clipboard e copiar a mensagem
        print("\nCopiando mensagem para clipboard...")
        subprocess.run(['osascript', '-e', 'set the clipboard to ""'], check=False)
        time.sleep(0.5)
        pyperclip.copy(message)
        time.sleep(0.5)

        # 6. Colar a mensagem
        print("\nColando mensagem...")
        pyautogui.hotkey('command', 'v')
        time.sleep(0.5)

        # 7. Pressionar Enter
        print("\nPressionando Enter...")
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
    
    print("\n--- Iniciando Script de Envio de Mensagem com Imagem (macOS) ---")
    print(f"Número: {phone}")
    print(f"Mensagem: {msg}")
    print(f"Imagem: {img}")
    
    if send_message_with_image(phone, msg, img):
        print("--- Script finalizado: Sucesso ---")
    else:
        print("--- Script finalizado: Falha ---") 