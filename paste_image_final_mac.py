# paste_image_final_mac.py - Copia via Finder + Cmd+C, Espera e Cola
import time
import subprocess
import os
from PIL import Image # Ainda útil para verificar a imagem
import sys
import pyautogui # Adicionado de volta

def copy_image_via_finder(image_path):
    """Copia imagem para clipboard no macOS via Finder + Cmd+C."""
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
        # Limpar o clipboard antes de copiar a imagem (opcional, mas pode ajudar)
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

        if result.returncode == 0:
            print("\n*** COMANDO DE CÓPIA (Cmd+C) ENVIADO VIA FINDER. ***")
            print("Verifique se a imagem está no clipboard e pode colar manualmente.")
            return True
        else:
            print(f"\nErro ao executar o script de cópia do Finder.")
            return False
            
    except Exception as e:
        print(f"\nErro EXCEPCIONAL ao copiar imagem para clipboard via Finder: {e}")
        return False

def copy_wait_and_paste(image_path):
    """Copia via Finder, espera 5s e cola."""
    # 1. Copiar via Finder
    if not copy_image_via_finder(image_path):
        print("Falha ao enviar comando de cópia. Abortando.")
        return False

    # 2. Esperar 5 segundos
    print("\nAguardando 5 segundos antes de colar a imagem...")
    time.sleep(5)

    # 3. Colar a imagem
    try:
        print("\nColando imagem (Cmd+V)...")
        pyautogui.hotkey('command', 'v')
        print("Comando de colar enviado!")
        return True
    except pyautogui.FailSafeException:
        print("\nFAILSAFE TRIGGERED (mouse no canto). Parando automação GUI.")
        return False
    except Exception as e:
        print(f"\nErro durante a colagem: {e}")
        return False

# --- Bloco Principal --- 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python paste_image_final_mac.py <caminho_da_imagem>")
        sys.exit(1)

    img_path_arg = sys.argv[1]
    
    print("\n--- Iniciando Script de CÓPIA (Finder Cmd+C), ESPERA e COLA (macOS) ---")
    print(f"Imagem: {img_path_arg}")
    
    # Chama a função que copia, espera e cola
    if copy_wait_and_paste(img_path_arg):
        print("--- Script finalizado: Sequência concluída (verifique o resultado) --- ")
    else:
        print("--- Script finalizado: Falha durante a sequência --- ") 