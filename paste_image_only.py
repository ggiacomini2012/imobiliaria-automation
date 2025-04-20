# paste_image_only.py
import sys
import os
import time
import pyautogui
import platform
import io
from PIL import Image
import pyperclip # Usaremos para copiar/colar a legenda se necessário
import subprocess

# Import específicos do OS para copiar IMAGEM
if platform.system() == 'Windows':
    try:
        import win32clipboard
        import win32con
    except ImportError:
        print("Erro: pywin32 não encontrado (necessário no Windows).")
        pass # copy_image_windows lidará com NameError

# --- Funções de Clipboard (Copiadas/Adaptadas de send_image_gui.py) ---
def copy_image_windows(image_path):
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
        print("Imagem copiada (Windows).")
        return True
    except FileNotFoundError:
        print(f"Erro (Win Clipboard): Imagem não encontrada em {image_path}")
        return False
    except NameError: 
         print("Erro (Win Clipboard): Biblioteca pywin32 não encontrada ou falhou ao importar.")
         return False
    except Exception as e: 
        print(f"Erro Win Clipboard: {e}")
        try: win32clipboard.CloseClipboard() # Tenta fechar se deu erro
        except: pass
        return False

def copy_image_macos(image_path):
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
            print("Imagem copiada (macOS)."); 
            return True
        else:
            print("Tentando fallback 'picture'...")
            script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as picture)'
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
            if result.returncode == 0: 
                print("Imagem copiada (macOS - genérico)."); 
                return True
            else: 
                print(f"Erro macOS Clipboard: {result.stderr}"); 
                return False
    except FileNotFoundError:
        print("Erro: Comando 'osascript' não encontrado. Necessário para clipboard no macOS.")
        return False
    except Exception as e: 
        print(f"Erro macOS Clipboard: {e}"); 
        return False

def copy_image_to_clipboard(image_path):
    os_name = platform.system()
    print(f"Tentando copiar imagem para clipboard em {os_name}...")
    if os_name == 'Windows': return copy_image_windows(image_path)
    elif os_name == 'Darwin': return copy_image_macos(image_path)
    else: print(f"Aviso: Copiar imagem não implementado para {os_name}."); return False

# --- Função Principal ---
def paste_image(image_path):
    # 1. Copiar
    if not copy_image_to_clipboard(image_path):
        return False # Falha ao copiar

    # 2. Esperar um pouco para a janela do WhatsApp (aberta pelo outro script) aparecer
    wait_before_paste = 1 # Ajuste conforme necessário
    print(f"Esperando {wait_before_paste}s antes de colar...")
    time.sleep(wait_before_paste)

    # 3. Colar (Ctrl+V / Cmd+V) - SEM cliques, confiando no foco
    try:
        print("Colando imagem (Ctrl+V ou Cmd+V). Confiando que WhatsApp está ativo...")
        paste_command = ('command', 'v') if platform.system() == 'Darwin' else ('ctrl', 'v')
        pyautogui.hotkey(*paste_command)
        print("Comando de colar enviado.")
        return True # Sucesso (da tentativa de colar)
    except pyautogui.FailSafeException:
        print("FAILSAFE TRIGGERED.")
        return False
    except Exception as e:
        print(f"Erro ao colar: {e}")
        return False

# --- Bloco Principal ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python paste_image_only.py <image_path>")
        sys.exit(1)

    img_path = sys.argv[1]
    print(f"--- Iniciando Script de Colar Imagem ---")
    print(f"Imagem: {img_path}")

    if not os.path.exists(img_path):
        print(f"Erro: Caminho da imagem não existe: {img_path}")
        sys.exit(1)

    if paste_image(img_path):
        print("--- Script de Colar Imagem: Sucesso (tentativa de colar feita) ---")
        sys.exit(0)
    else:
        print("--- Script de Colar Imagem: Falha ---")
        sys.exit(1) 