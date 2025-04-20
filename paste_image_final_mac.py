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
        print("Limpando clipboard...")
        clear_result = subprocess.run(['osascript', '-e', 'set the clipboard to ""'], capture_output=True, text=True, check=False)
        print(f"Limpeza - stdout: {clear_result.stdout.strip()}, stderr: {clear_result.stderr.strip()}, code: {clear_result.returncode}")
        time.sleep(0.5)

        # Copiar imagem para clipboard usando osascript
        image_type = "JPEG picture"
        if abs_image_path.lower().endswith(".png"): 
            image_type = "PNG picture"
        elif abs_image_path.lower().endswith(".gif"): 
            image_type = "GIF picture"
        
        script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as {image_type})'
        print(f"\nExecutando osascript (tipo específico): {script}")
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True, check=False)
        print(f"Resultado (tipo específico) - stdout: {result.stdout.strip()}, stderr: {result.stderr.strip()}, code: {result.returncode}")
        
        if result.returncode == 0:
            print("\nImagem copiada para clipboard com sucesso (tipo específico).")
            return True
        else:
            print("\nFalha ao copiar como tipo específico, tentando como 'picture' genérico...")
            script_generic = f'set the clipboard to (read (POSIX file "{abs_image_path}") as picture)'
            print(f"Executando osascript (genérico): {script_generic}")
            result_generic = subprocess.run(['osascript', '-e', script_generic], capture_output=True, text=True, check=False)
            print(f"Resultado (genérico) - stdout: {result_generic.stdout.strip()}, stderr: {result_generic.stderr.strip()}, code: {result_generic.returncode}")
            
            if result_generic.returncode == 0:
                print("\nImagem copiada para clipboard com sucesso (formato genérico).")
                return True
            else:
                print(f"\nErro final ao copiar imagem para clipboard.")
                return False
    except Exception as e:
        print(f"\nErro EXCEPCIONAL ao copiar imagem para clipboard: {e}")
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