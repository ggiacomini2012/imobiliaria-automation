# paste_image_final_mac.py - APENAS COPIA PARA CLIPBOARD
import time
import subprocess
import os
from PIL import Image # Ainda útil para verificar a imagem
import sys

def copy_image_to_clipboard_only(image_path):
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
            print("\n*** IMAGEM COPIADA PARA O CLIPBOARD (formato genérico). ***")
            print("Pode colar manualmente agora (Command + V).")
            return True
        else:
            print(f"\nErro final ao copiar imagem para clipboard.")
            return False
            
    except Exception as e:
        print(f"\nErro EXCEPCIONAL ao copiar imagem para clipboard: {e}")
        return False

# --- Bloco Principal --- 
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python paste_image_final_mac.py <caminho_da_imagem>")
        sys.exit(1)

    img_path_arg = sys.argv[1]
    
    print("\n--- Iniciando Script de CÓPIA de Imagem (macOS) ---")
    print(f"Imagem: {img_path_arg}")
    
    if copy_image_to_clipboard_only(img_path_arg):
        print("--- Script finalizado: Cópia bem-sucedida --- ")
    else:
        print("--- Script finalizado: Falha na cópia --- ") 