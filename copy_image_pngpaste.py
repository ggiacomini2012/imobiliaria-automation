#!/usr/bin/env python3
# copy_image_pngpaste.py - Usa a ferramenta pngpaste para copiar imagens para o clipboard
# IMPORTANTE: Requer que pngpaste esteja instalado no macOS
# Instale com: brew install pngpaste

import sys
import os
import subprocess

def verify_pngpaste_installed():
    """Verifica se pngpaste está instalado no sistema."""
    try:
        result = subprocess.run(['which', 'pngpaste'], 
                               capture_output=True, text=True, check=False)
        if result.returncode == 0:
            print(f"pngpaste encontrado em: {result.stdout.strip()}")
            return True
        else:
            print("pngpaste não encontrado. Por favor, instale com: brew install pngpaste")
            return False
    except Exception as e:
        print(f"Erro ao verificar pngpaste: {e}")
        return False

def copy_image_to_clipboard(image_path):
    """Copia a imagem para o clipboard usando pngpaste."""
    if not verify_pngpaste_installed():
        return False
        
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Arquivo de imagem não encontrado: {abs_image_path}")
        return False
        
    try:
        # Usar pngpaste para copiar a imagem para o clipboard
        print(f"Tentando copiar {abs_image_path} para o clipboard...")
        result = subprocess.run(['pngpaste', '-i', abs_image_path], 
                               capture_output=True, text=True, check=False)
        
        if result.returncode == 0:
            print(f"Comando executado com sucesso.")
            return True
        else:
            print(f"Erro ao copiar para clipboard: {result.stderr}")
            return False
    except Exception as e:
        print(f"Erro ao executar pngpaste: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python copy_image_pngpaste.py <caminho_da_imagem>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    print(f"Tentando copiar imagem para o clipboard: {image_path}")
    
    if copy_image_to_clipboard(image_path):
        print("\n=== SUCESSO! Imagem copiada para o clipboard. ===")
        print("Você pode tentar colar (Cmd+V) em qualquer aplicativo que aceite imagens.")
    else:
        print("\n=== FALHA ao copiar imagem para o clipboard. ===")
        sys.exit(1) 