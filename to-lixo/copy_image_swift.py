#!/usr/bin/env python3
# copy_image_swift.py - Usa um pequeno programa Swift para copiar imagens para o clipboard
# IMPORTANTE: Requer macOS e ambiente Swift funcional

import sys
import os
import subprocess
import tempfile

def copy_with_swift(image_path):
    """Copia imagem para clipboard usando um pequeno programa Swift."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Arquivo de imagem não encontrado: {abs_image_path}")
        return False
        
    # Criando o código Swift para copiar a imagem
    swift_code = f'''
import Cocoa
import Foundation

let imagePath = "{abs_image_path}"
if let image = NSImage(contentsOfFile: imagePath) {{
    let pasteboard = NSPasteboard.general
    pasteboard.clearContents()
    let result = pasteboard.writeObjects([image])
    if result {{
        print("SUCCESS: Imagem copiada para o clipboard com sucesso.")
        exit(0)
    }} else {{
        print("ERROR: Falha ao escrever imagem no NSPasteboard.")
        exit(1)
    }}
}} else {{
    print("ERROR: Não foi possível abrir a imagem como NSImage: \\(imagePath)")
    exit(1)
}}
'''
    
    try:
        # Criar um arquivo Swift temporário
        with tempfile.NamedTemporaryFile(suffix='.swift', delete=False, mode='w') as temp:
            temp_path = temp.name
            temp.write(swift_code)
            
        print(f"Código Swift criado em {temp_path}")
        
        # Compilar o código Swift
        print("Compilando o código Swift...")
        compile_result = subprocess.run(['swiftc', temp_path, '-o', temp_path + '.out'], 
                                       capture_output=True, text=True, check=False)
        
        if compile_result.returncode != 0:
            print(f"Erro ao compilar código Swift: {compile_result.stderr}")
            return False
            
        # Executar o programa Swift compilado
        print("Executando o programa Swift...")
        run_result = subprocess.run([temp_path + '.out'], 
                                   capture_output=True, text=True, check=False)
        
        print(f"Saída: {run_result.stdout}")
        
        if run_result.returncode == 0:
            print("Programa Swift executado com sucesso.")
            return True
        else:
            print(f"Erro ao executar programa Swift: {run_result.stderr}")
            return False
            
    except Exception as e:
        print(f"Erro durante o processo: {e}")
        return False
    finally:
        # Limpeza dos arquivos temporários
        try:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            if os.path.exists(temp_path + '.out'):
                os.remove(temp_path + '.out')
        except:
            pass
            
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python copy_image_swift.py <caminho_da_imagem>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    print(f"Tentando copiar imagem para o clipboard via Swift: {image_path}")
    
    if copy_with_swift(image_path):
        print("\n=== CÓPIA VIA SWIFT CONCLUÍDA COM SUCESSO ===")
        print("Você pode tentar colar (Cmd+V) em qualquer aplicativo que aceite imagens.")
    else:
        print("\n=== FALHA na cópia via Swift ===")
        print("Verifique se você tem o Swift instalado e funcionando no macOS.")
        sys.exit(1) 