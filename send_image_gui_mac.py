# send_image_gui_mac.py (Versão macOS - PyAutoGUI)
import sys
import os
import time
import pyautogui
from PIL import Image

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_PASTE = 3.0  # Segundos após colar imagem
WAIT_BEFORE_SEND_ENTER = 0.5  # Segundos antes do Enter

def send_whatsapp_image_no_clicks(image_path):
    """Cola a imagem no WhatsApp usando PyAutoGUI."""
    
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

    # 2. Sequência de Automação GUI
    try:
        print("\nIniciando sequência de automação GUI...")

        # --- Colar a imagem ---
        print("\nColando imagem...")
        pyautogui.hotkey('command', 'v')
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # --- Pressionar Enter ---
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
    if len(sys.argv) != 2:
        print("Uso: python send_image_gui_mac.py <image_path>")
        sys.exit(1)

    image = sys.argv[1]

    print(f"\n--- Iniciando Script de Envio de Imagem (macOS) ---")
    print(f"Imagem: {image}")

    # Chamada da função principal
    if send_whatsapp_image_no_clicks(image):
        print("--- Script finalizado: Sucesso ---")
        sys.exit(0)
    else:
        print("--- Script finalizado: Falha ---")
        sys.exit(1) 