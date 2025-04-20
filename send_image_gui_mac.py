# send_image_gui.py (Versão Copy-Paste Imagem + Copy-Paste Legenda + Enter)
import sys
import os
import time
import pyautogui
import pygetwindow as gw
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
WAIT_AFTER_OPEN = 7.0 # Aumentado! Segundos para esperar após abrir o link
WAIT_AFTER_PASTE = 4.5 # Segundos para esperar a pré-visualização carregar após colar
WAIT_BEFORE_SEND_ENTER = 1.0
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
        image_type = "JPEG picture"
        if image_path.lower().endswith(".png"): image_type = "PNG picture"
        elif image_path.lower().endswith(".gif"): image_type = "GIF picture"
        
        script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as {image_type})'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("Imagem copiada para clipboard (macOS).")
            return True
        else:
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

def wait_for_whatsapp_active(max_wait=3): # Aumentado!
    """Espera a janela do WhatsApp ficar ativa."""
    print(f"Waiting up to {max_wait}s for WhatsApp window to become active...")
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            active_window = gw.getActiveWindow()
            if active_window and active_window.title and "WhatsApp" in active_window.title:
                print("WhatsApp window is active.")
                return True
        except Exception as e:
             pass 
        time.sleep(0.5)
    print("Warning: WhatsApp window did not become active.")
    return False

# --- Função Principal (Método Copy-Paste Imagem + Copy-Paste Legenda + Enter) ---
def send_whatsapp_image_no_clicks(phone_number, image_path, caption):
    """Tenta enviar imagem via Copy-Paste, legenda via Copy-Paste e pressiona Enter."""

    # 1. Copiar imagem para clipboard
    if not copy_image_to_clipboard(image_path):
        print("Failed to copy image to clipboard. Aborting.")
        return False

    # 2. Abrir o chat (sem texto)
    whatsapp_uri = f"whatsapp://send?phone={phone_number}" 
    if not open_uri(whatsapp_uri):
        return False 
    time.sleep(WAIT_AFTER_OPEN)

    # 3. Esperar a janela do WhatsApp ativar e tentar focar se necessário (Windows)
    if not wait_for_whatsapp_active():
         # Tentar focar se for Windows? (Opcional, pode adicionar chamada ao focus_whatsapp.py aqui)
         if platform.system() == 'Windows':
              print("Trying to run focus script as fallback...")
              try:
                  # Assumir que ambos os scripts estão na raiz do projeto
                  script_dir = os.path.dirname(__file__) # Diretório onde este script está
                  focus_script_path = os.path.join(script_dir, 'focus_whatsapp.py') # Caminho para focus na mesma pasta
                  print(f"Attempting to run focus script at: {focus_script_path}")
                  
                  if os.path.exists(focus_script_path):
                      # Executar a partir do diretório do script pode ser mais seguro
                      result = subprocess.run([sys.executable, focus_script_path], cwd=script_dir, check=False, capture_output=True, text=True)
                      print(f"Focus script stdout:\n{result.stdout}")
                      print(f"Focus script stderr:\n{result.stderr}")
                      print(f"Focus script return code: {result.returncode}")
                      time.sleep(2.0) # Aumentar um pouco a espera após focar
                      if not wait_for_whatsapp_active(max_wait=5): # Tente esperar mais um pouco
                           print("Failed to activate even after focus script.")
                           return False
                      else:
                           print("Successfully activated after focus script fallback.")
                           # Continua para a automação GUI...
                  else:
                      print(f"Focus script not found at expected location: {focus_script_path}")
                      return False # Cannot run focus script
              except Exception as focus_e:
                  print(f"Failed to run focus script: {focus_e}")
                  return False
         else: 
             return False # Falha se não ativou e não é Windows

    # 4. Sequência de Automação GUI (Colar Img -> Colar Legenda -> Enter)
    try:
        print("Starting GUI automation sequence (Paste Img -> Paste Caption -> Enter - NO CLICKS)...")

        # --- Colar a imagem --- (Assumindo que o foco está correto)
        print("Pasting image from clipboard (Ctrl+V or Cmd+V). Trusting focus is correct...")
        paste_command = ('command', 'v') if platform.system() == 'Darwin' else ('ctrl', 'v')
        pyautogui.hotkey(*paste_command)
        print("Image paste command sent.")
        time.sleep(WAIT_AFTER_PASTE) # Esperar pré-visualização da imagem

        # --- Copiar e Colar a legenda ---
        print(f"Copying caption to clipboard: {caption[:50]}...")
        try:
            pyperclip.copy(caption)
            print("Caption copied to clipboard.")
            time.sleep(0.2) # Pequena pausa para o clipboard atualizar
            print("Pasting caption from clipboard (Ctrl+V or Cmd+V)...")
            pyautogui.hotkey(*paste_command) # Cola a legenda
            print("Caption paste command sent.")
        except Exception as clip_e:
             print(f"ERROR copying/pasting caption: {clip_e}.")
             # Decide se continua sem legenda ou falha
             # return False # Descomente para falhar se não conseguir copiar/colar legenda
             pass # Tenta enviar mesmo assim
        time.sleep(WAIT_BEFORE_SEND_ENTER)

        # --- Pressionar Enter para Enviar ---
        print(f"Pressing Enter to send...")
        try:
            pyautogui.press('enter')
            print("Enter key pressed.")
        except Exception as press_e:
             print(f"ERROR pressing Enter key: {press_e}. Check focus/permissions.")
             return False

        return True # Sucesso na automação

    except pyautogui.FailSafeException:
        print("FAILSAFE TRIGGERED (moved mouse to corner). Stopping GUI automation.")
        return False
    except Exception as e:
        print(f"Error during GUI automation: {e}")
        try: print(f"Mouse position at error: {pyautogui.position()}")
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

    print(f"\n--- Running Send Image GUI Script (No Clicks) ---")
    print(f"Phone: {phone}")
    print(f"Image: {image}")
    print(f"Caption: {capt[:100]}...") # Limitar a exibição da legenda

    # Garantir que o caminho da imagem seja absoluto
    image_abs_path = os.path.abspath(image)
    if not os.path.exists(image_abs_path):
         print(f"ERROR: Image file not found at {image_abs_path}")
         sys.exit(1)

    # Chamada da função principal
    if send_whatsapp_image_no_clicks(phone, image_abs_path, capt):
        print("Script finished successfully (triggered send sequence).")
        sys.exit(0) # Sucesso
    else:
        print("Script finished with errors.")
        sys.exit(1) # Falha 