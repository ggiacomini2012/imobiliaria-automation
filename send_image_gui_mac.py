# send_image_gui.py (Versão Copy-Paste Imagem + Copy-Paste Legenda + Enter)
import sys
import os
import time
import pyautogui
# import pygetwindow as gw # REMOVED
import platform
import urllib.parse
import subprocess
import io
from PIL import Image # Pillow é necessário
import pyperclip # Adicionar import

# Import específicos do OS
if platform.system() == 'Windows':
    try:
        import win32clipboard
        import win32con # Necessário para CF_DIB
    except ImportError:
        print("Erro: A biblioteca 'pywin32' é necessária no Windows para copiar imagens.")
        print("Instale com: pip install pywin32")
        # Não sair imediatamente, permitir que o script continue se não for Windows
        # sys.exit(1) 
        pass # A função copy_image_windows lidará com NameError

# --- Configuração GUI (NECESSÁRIO AJUSTAR!) ---
# Você precisará encontrar as coordenadas (x, y) destes botões na sua tela
# ou salvar pequenas imagens (.png) deles e fornecer os caminhos aqui.
# Usar imagens é MAIS ROBUSTO que coordenadas, mas mais lento.
# Exemplo com coordenadas (AJUSTE!):
MESSAGE_INPUT_POS = (500, 650) # Posição da caixa de entrada de texto
SEND_BUTTON_POS = (700, 650)   # Posição do botão Enviar (seta verde)

# Exemplo com imagens:
# MESSAGE_INPUT_IMG = 'gui_images/message_input.png'
# SEND_BUTTON_IMG = 'gui_images/send_button.png'

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_OPEN = 10.0  # Aumentado para 10 segundos
WAIT_AFTER_PASTE = 6.0  # Aumentado para 6 segundos
WAIT_BEFORE_SEND_ENTER = 1.0  # Aumentado para 1 segundo
ENTER_ATTEMPTS = 3
ENTER_INTERVAL = 0.8  # Aumentado intervalo entre Enters
# -------------------------------------------------

# --- Funções de Clipboard ---

def copy_image_windows(image_path):
    """Copia imagem para clipboard no Windows (formato DIB)."""
    try:
        image = Image.open(image_path)
        output = io.BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:] 
        output.close()

        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32con.CF_DIB, data) 
        win32clipboard.CloseClipboard()
        print("Imagem copiada para clipboard (Windows).")
        return True
    except FileNotFoundError:
        print(f"Erro (Win Clipboard): Imagem não encontrada em {image_path}")
        return False
    except NameError: 
         print("Erro (Win Clipboard): Biblioteca pywin32 não encontrada ou falhou ao importar.")
         return False
    except Exception as e:
        print(f"Erro ao copiar imagem para clipboard (Windows): {e}")
        try: win32clipboard.CloseClipboard()
        except: pass
        return False

def copy_image_macos(image_path):
    """Copia imagem para clipboard no macOS usando AppleScript."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
         print(f"Erro (Mac Clipboard): Imagem não encontrada em {abs_image_path}")
         return False
    try:
        # Primeiro, tenta verificar se a imagem é válida
        try:
            with Image.open(abs_image_path) as img:
                print(f"Imagem válida detectada: {img.format} {img.size}")
        except Exception as img_e:
            print(f"Aviso: Erro ao verificar imagem: {img_e}")
            return False

        image_type = "JPEG picture"
        if abs_image_path.lower().endswith(".png"): 
            image_type = "PNG picture"
        elif abs_image_path.lower().endswith(".gif"): 
            image_type = "GIF picture"
        
        print(f"Tentando copiar como {image_type}...")
        script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as {image_type})'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("Imagem copiada para clipboard (macOS).")
            # Tenta verificar se algo foi copiado
            verify_script = 'get the clipboard'
            verify_result = subprocess.run(['osascript', '-e', verify_script], capture_output=True, text=True, check=False)
            if verify_result.returncode == 0:
                print("Clipboard contém dados após cópia.")
                return True
            else:
                print("Aviso: Clipboard parece vazio após cópia.")
        
        print("Falha ao copiar como tipo específico, tentando como 'picture' genérico...")
        script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as picture)'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
             print("Imagem copiada para clipboard (macOS - genérico).")
             return True
        else:
             print(f"Erro ao copiar imagem para clipboard (macOS): {result.stderr}")
             return False
    except FileNotFoundError: 
        print("Erro: Comando 'osascript' não encontrado. Necessário para clipboard no macOS.")
        return False
    except Exception as e:
        print(f"Erro inesperado ao copiar imagem para clipboard (macOS): {e}")
        return False

def copy_image_to_clipboard(image_path):
    """Detecta o OS e chama a função de cópia apropriada."""
    os_name = platform.system()
    print(f"Attempting to copy image to clipboard on {os_name}...")
    if os_name == 'Windows':
        return copy_image_windows(image_path)
    elif os_name == 'Darwin': 
        return copy_image_macos(image_path)
    else: 
        print(f"Warning: Copying images to clipboard is not implemented for {os_name}.")
        return False

# --- Funções Auxiliares (mantidas da versão anterior) ---
def open_uri(uri):
    """Abre uma URI genérica (como whatsapp://)."""
    os_name = platform.system()
    print(f"Attempting to open URI: {uri[:100]}...")
    try:
        if os_name == 'Windows': os.startfile(uri)
        elif os_name == 'Darwin': subprocess.run(['open', uri], check=True)
        elif os_name == 'Linux': subprocess.run(['xdg-open', uri], check=True)
        else: print(f"Unsupported OS ({os_name})"); return False
        print("URI open command triggered.")
        return True
    except Exception as e: print(f"Error opening URI: {e}"); return False

# --- Função Principal (Método Copy-Paste Imagem + Copy-Paste Legenda + Enter - macOS Adaptation) ---
def send_whatsapp_image_no_clicks(phone_number, image_path, caption):
    """Tenta enviar imagem via Copy-Paste, legenda via Copy-Paste e pressiona Enter (macOS)."""

    # 1. Copiar imagem para clipboard
    print("\nIniciando processo de cópia da imagem...")
    if not copy_image_to_clipboard(image_path):
        print("Failed to copy image to clipboard. Aborting.")
        return False

    # 2. Abrir o chat (sem texto)
    whatsapp_uri = f"whatsapp://send?phone={phone_number}"
    if not open_uri(whatsapp_uri):
        return False
    print(f"\nAguardando {WAIT_AFTER_OPEN} segundos após abrir WhatsApp...")
    time.sleep(WAIT_AFTER_OPEN)

    # 4. Sequência de Automação GUI
    try:
        print("\nIniciando sequência de automação GUI...")

        # --- Colar a imagem ---
        print("\nColando imagem do clipboard (Cmd+V)...")
        # Tenta verificar clipboard antes de colar
        verify_script = 'get the clipboard'
        verify_result = subprocess.run(['osascript', '-e', verify_script], capture_output=True, text=True, check=False)
        if verify_result.returncode == 0:
            print("Clipboard contém dados antes de colar.")
        else:
            print("Aviso: Clipboard parece vazio antes de colar!")

        # macOS specific paste command
        paste_command = ('command', 'v')
        pyautogui.hotkey(*paste_command)
        print("Comando de colar enviado.")
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # --- Copiar e Colar a legenda ---
        print(f"\nCopiando legenda para clipboard: {caption[:50]}...")
        try:
            pyperclip.copy(caption)
            print("Legenda copiada para clipboard.")
            time.sleep(0.5)  # Aumentado para 0.5s
            print("Colando legenda do clipboard (Cmd+V)...")
            pyautogui.hotkey(*paste_command)
            print("Comando de colar legenda enviado.")
            time.sleep(WAIT_BEFORE_SEND_ENTER)
        except Exception as clip_e:
             print(f"ERRO ao copiar/colar legenda: {clip_e}")
             print("Continuando sem legenda após erro.")
             pass

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
        print("Usage: python send_image_gui.py <phone_number> <image_path> <caption>")
        sys.exit(1)

    phone = sys.argv[1]
    image = sys.argv[2]
    capt = sys.argv[3]

    print(f"\n--- Starting Image Send GUI Script (Copy-Paste Img+Caption + Enter - NO CLICKS Method) ---") # Updated title
    print(f"To: {phone}")
    print(f"Image: {image}")
    print(f"Caption: {capt[:100]}...")

    # Garantir que o caminho da imagem seja absoluto
    image_abs_path = os.path.abspath(image)
    if not os.path.exists(image_abs_path):
         print(f"ERROR: Image file not found at {image_abs_path}")
         sys.exit(1)

    # Chamada da função principal
    if send_whatsapp_image_no_clicks(phone, image_abs_path, capt):
        print("--- Script finished: Success (GUI automation completed) ---")
        sys.exit(0) # Sucesso
    else:
        print("--- Script finished: Failure (GUI automation failed) ---")
        sys.exit(1) # Falha 