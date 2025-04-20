# paste_image_final_mac.py
import time
import pyautogui
import subprocess
import os
from PIL import Image

def copy_image_to_clipboard(image_path):
    """Copia imagem para clipboard no macOS."""
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
        subprocess.run(['osascript', '-e', 'set the clipboard to ""'], check=False)
        time.sleep(0.5)

        # Copiar imagem para clipboard usando osascript
        image_type = "JPEG picture"
        if abs_image_path.lower().endswith(".png"): 
            image_type = "PNG picture"
        elif abs_image_path.lower().endswith(".gif"): 
            image_type = "GIF picture"
        
        script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as {image_type})'
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print("Imagem copiada para clipboard com sucesso.")
            return True
        else:
            print("Falha ao copiar como tipo específico, tentando como 'picture' genérico...")
            script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as picture)'
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
            
            if result.returncode == 0:
                print("Imagem copiada para clipboard com sucesso (formato genérico).")
                return True
            else:
                print(f"Erro ao copiar imagem para clipboard: {result.stderr}")
                return False
    except Exception as e:
        print(f"Erro ao copiar imagem para clipboard: {e}")
        return False

def paste_image(image_path):
    """Espera 5 segundos e cola a imagem."""
    try:
        # 1. Copiar imagem para clipboard
        if not copy_image_to_clipboard(image_path):
            return False

        # 2. Esperar 5 segundos
        print("\nAguardando 5 segundos antes de colar a imagem...")
        time.sleep(5)

        # 3. Colar a imagem
        print("\nColando imagem...")
        pyautogui.hotkey('command', 'v')
        time.sleep(0.5)
        pyautogui.hotkey('option', 'v')
        time.sleep(0.5)
        
        #osascript paste from clipboard
        subprocess.run(['osascript', '-e', 'tell application "System Events" to paste from clipboard'], check=False)
        time.sleep(0.5)
        print("Imagem colada!")

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
    if len(sys.argv) != 2:
        print("Uso: python paste_image_final_mac.py <caminho_da_imagem>")
        sys.exit(1)

    img = sys.argv[1]
    
    print("\n--- Iniciando Script de Colar Imagem (macOS) ---")
    print(f"Imagem: {img}")
    
    if paste_image(img):
        print("--- Script finalizado: Sucesso ---")
    else:
        print("--- Script finalizado: Falha ---") 