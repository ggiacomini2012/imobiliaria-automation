# send_image_gui_mac.py (Versão macOS - PyAutoGUI)
import sys
import os
import time
import pyautogui
import platform
import urllib.parse
import subprocess
from PIL import Image
import pyperclip

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_OPEN = 5.0  # Segundos após abrir WhatsApp
WAIT_AFTER_PASTE = 3.0  # Segundos após colar imagem
WAIT_BEFORE_SEND_ENTER = 0.5  # Segundos antes do Enter
ENTER_ATTEMPTS = 2  # Número de tentativas de Enter
ENTER_INTERVAL = 0.5  # Segundos entre Enters

def open_uri(uri):
    """Abre uma URI no macOS."""
    print(f"Tentando abrir URI: {uri[:100]}...")
    try:
        subprocess.run(['open', uri], check=True)
        print("URI aberta com sucesso.")
        return True
    except Exception as e: 
        print(f"Erro ao abrir URI: {e}")
        return False

def send_whatsapp_image_no_clicks(phone_number, image_path, caption):
    """Envia imagem via WhatsApp usando PyAutoGUI."""

    # 1. Verificar se a imagem existe
    image_abs_path = os.path.abspath(image_path)
    if not os.path.exists(image_abs_path):
        print(f"Erro: Imagem não encontrada em {image_abs_path}")
        return False

    try:
        with Image.open(image_abs_path) as img:
            print(f"Imagem válida detectada: {img.format} {img.size}")
    except Exception as img_e:
        print(f"Erro ao verificar imagem: {img_e}")
        return False

    # 2. Abrir o chat
    whatsapp_uri = f"whatsapp://send?phone={phone_number}"
    if not open_uri(whatsapp_uri):
        return False
    print(f"\nAguardando {WAIT_AFTER_OPEN} segundos após abrir WhatsApp...")
    time.sleep(WAIT_AFTER_OPEN)

    # 3. Sequência de Automação GUI
    try:
        print("\nIniciando sequência de automação GUI...")

        # --- Colar a imagem ---
        print("\nColando imagem...")
        # Simular Command+Shift+3 para abrir seletor de arquivos
        pyautogui.hotkey('command', 'shift', '3')
        time.sleep(1)
        
        # Digitar o caminho do arquivo
        pyautogui.write(image_abs_path)
        time.sleep(0.5)
        pyautogui.press('enter')
        
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # --- Copiar e Colar a legenda ---
        if caption:
            print(f"\nColando legenda: {caption[:50]}...")
            pyperclip.copy(caption)
            time.sleep(0.5)
            print("Colando legenda...")
            pyautogui.hotkey('command', 'v')
            time.sleep(WAIT_BEFORE_SEND_ENTER)

        # --- Pressionar Enter para Enviar ---
        print(f"\nTentando pressionar Enter {ENTER_ATTEMPTS} vezes...")
        send_success = False
        for attempt in range(ENTER_ATTEMPTS):
            try:
                print(f"  Tentativa de Enter {attempt + 1}/{ENTER_ATTEMPTS}...")
                pyautogui.press('enter')
                print("  Tecla Enter pressionada.")
                send_success = True
            except pyautogui.FailSafeException:
                 print("FAILSAFE TRIGGERED (mouse no canto). Parando.")
                 send_success = False
                 break
            except Exception as press_e:
                 print(f"ERRO ao pressionar Enter na tentativa {attempt + 1}: {press_e}")
                 send_success = False

            if attempt < ENTER_ATTEMPTS - 1:
                 print(f"  Aguardando {ENTER_INTERVAL} segundos antes da próxima tentativa...")
                 time.sleep(ENTER_INTERVAL)

        if not send_success:
            print("\nFalha ao enviar comando Enter.")
            return False

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
    if len(sys.argv) != 4:
        print("Uso: python send_image_gui_mac.py <phone_number> <image_path> <caption>")
        sys.exit(1)

    phone = sys.argv[1]
    image = sys.argv[2]
    capt = sys.argv[3]

    print(f"\n--- Iniciando Script de Envio de Imagem (macOS) ---")
    print(f"Para: {phone}")
    print(f"Imagem: {image}")
    print(f"Legenda: {capt[:100]}...")

    # Chamada da função principal
    if send_whatsapp_image_no_clicks(phone, image, capt):
        print("--- Script finalizado: Sucesso ---")
        sys.exit(0)
    else:
        print("--- Script finalizado: Falha ---")
        sys.exit(1) 