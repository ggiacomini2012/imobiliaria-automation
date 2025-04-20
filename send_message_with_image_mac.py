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
    """Copia imagem para clipboard no macOS usando o Finder via AppleScript."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Imagem não encontrada em {abs_image_path}")
        return False

    try:
        # Verificar se a imagem é válida (opcional, mas bom ter)
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

        # Script AppleScript para copiar via Finder
        script = f'''
tell application "Finder"
    set the_file to POSIX file "{abs_image_path}" as alias
    select the_file
    activate
    tell application "System Events"
        keystroke "c" using command down
    end tell
end tell
delay 0.5 -- Pequena pausa para garantir que a cópia ocorra
'''
        
        print(f"\nExecutando osascript (via Finder): pedindo para copiar {abs_image_path}")
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        print(f"Resultado (Finder copy) - stdout: {result.stdout.strip()}, stderr: {result.stderr.strip()}, code: {result.returncode}")

        # Verificar se a cópia foi bem-sucedida é mais difícil aqui.
        # Vamos assumir sucesso se o script não retornar erro e adicionar uma verificação manual se necessário.
        if result.returncode == 0:
            print("\nComando de cópia via Finder enviado com sucesso.")
            # AQUI PODERÍAMOS tentar ler o clipboard para verificar, mas complica.
            # Vamos confiar que funcionou por enquanto.
            return True
        else:
            print(f"\nErro ao executar o script de cópia do Finder.")
            return False
            
    except Exception as e:
        print(f"\nErro EXCEPCIONAL ao copiar imagem para clipboard via Finder: {e}")
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