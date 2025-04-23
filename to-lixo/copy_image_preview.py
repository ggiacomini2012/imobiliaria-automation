#!/usr/bin/env python3
# copy_image_preview.py - Usa o Preview.app para copiar imagens para o clipboard
# IMPORTANTE: Requer macOS e permissões de acessibilidade

import sys
import os
import subprocess
import time

def copy_with_preview(image_path):
    """Copia imagem para clipboard abrindo no Preview e usando Command+C."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Arquivo de imagem não encontrado: {abs_image_path}")
        return False
        
    try:
        # 1. Abrir a imagem no Preview
        print(f"Abrindo imagem no Preview: {abs_image_path}")
        result_open = subprocess.run(['open', '-a', 'Preview', abs_image_path], 
                                   capture_output=True, text=True, check=False)
        
        if result_open.returncode != 0:
            print(f"Erro ao abrir imagem no Preview: {result_open.stderr}")
            return False
            
        # 2. Esperar o Preview abrir
        print("Aguardando 2 segundos para o Preview abrir...")
        time.sleep(2.0)
        
        # 3. Selecionar tudo (Command+A)
        print("Enviando Command+A para selecionar tudo...")
        select_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "a" using command down
            end tell
        end tell
        '''
        result_select = subprocess.run(['osascript', '-e', select_script], 
                                     capture_output=True, text=True, check=False)
        
        if result_select.returncode != 0:
            print(f"Erro ao enviar Command+A: {result_select.stderr}")
            return False
            
        time.sleep(0.5)
        
        # 4. Copiar (Command+C)
        print("Enviando Command+C para copiar...")
        copy_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "c" using command down
            end tell
        end tell
        '''
        result_copy = subprocess.run(['osascript', '-e', copy_script], 
                                    capture_output=True, text=True, check=False)
        
        if result_copy.returncode != 0:
            print(f"Erro ao enviar Command+C: {result_copy.stderr}")
            return False
            
        time.sleep(0.5)
        
        # 5. Fechar Preview (Command+W)
        print("Enviando Command+W para fechar...")
        close_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "w" using command down
            end tell
        end tell
        '''
        result_close = subprocess.run(['osascript', '-e', close_script], 
                                     capture_output=True, text=True, check=False)
        
        # Não verificamos o resultado do fechamento, pois pode haver diálogo
        # perguntando se quer salvar, etc.
        
        # 6. Pressionando Esc para cancelar qualquer diálogo
        cancel_script = '''
        tell application "System Events"
            key code 53  # Código para a tecla Esc
        end tell
        '''
        subprocess.run(['osascript', '-e', cancel_script], 
                      capture_output=True, text=True, check=False)
                      
        print("Sequência de comando para copiar via Preview concluída.")
        return True
        
    except Exception as e:
        print(f"Erro durante o processo: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python copy_image_preview.py <caminho_da_imagem>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    print(f"Tentando copiar imagem para o clipboard via Preview: {image_path}")
    
    if copy_with_preview(image_path):
        print("\n=== SEQUÊNCIA DE CÓPIA CONCLUÍDA ===")
        print("Verifique se a imagem está no clipboard tentando colar (Cmd+V).")
        print("NOTA: Esta técnica depende de permissões de acessibilidade.")
    else:
        print("\n=== FALHA na sequência de cópia via Preview ===")
        sys.exit(1) 