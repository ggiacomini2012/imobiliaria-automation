#!/usr/bin/env python3
# copy_image_appkit.py - Copia imagem para clipboard usando AppKit no macOS
# IMPORTANTE: Requer macOS e pip install pillow pyobjc-core pyobjc-framework-Cocoa

import sys
import os
from PIL import Image
import io

def copy_image_to_clipboard_appkit(image_path):
    """
    Copia uma imagem para o clipboard do macOS usando AppKit (forma nativa).
    Requer: pip install pillow pyobjc-core pyobjc-framework-Cocoa
    """
    try:
        # Importando AppKit - específico do macOS via PyObjC
        from AppKit import NSPasteboard, NSImage
        
        # Verificar se o arquivo existe
        abs_image_path = os.path.abspath(image_path)
        if not os.path.exists(abs_image_path):
            print(f"Erro: Arquivo de imagem não encontrado: {abs_image_path}")
            return False
        
        # Verificar se é uma imagem válida
        try:
            with Image.open(abs_image_path) as img:
                print(f"Imagem válida encontrada: {img.format} {img.size}")
                
                # Método 1: Usar NSImage diretamente com o caminho do arquivo
                print("\nMétodo 1: Usando NSImage.alloc().initWithContentsOfFile_")
                pasteboard = NSPasteboard.generalPasteboard()
                pasteboard.clearContents()
                
                nsimage = NSImage.alloc().initWithContentsOfFile_(abs_image_path)
                if nsimage:
                    result = pasteboard.writeObjects_([nsimage])
                    print(f"Resultado da cópia para clipboard (método 1): {'SUCESSO' if result else 'FALHA'}")
                else:
                    print("Falha ao criar NSImage diretamente do arquivo.")
                    
                    # Se o método 1 falhar, tenta o método 2
                    print("\nMétodo 2: Convertendo via PIL para PNG na memória")
                    # Converter para PNG na memória (independente do formato original)
                    png_data = io.BytesIO()
                    img.save(png_data, format='PNG')
                    png_bytes = png_data.getvalue()
                    
                    # Criar NSImage a partir dos dados PNG
                    from AppKit import NSData
                    ns_data = NSData.dataWithBytes_length_(png_bytes, len(png_bytes))
                    nsimage = NSImage.alloc().initWithData_(ns_data)
                    
                    if nsimage:
                        pasteboard = NSPasteboard.generalPasteboard()
                        pasteboard.clearContents()
                        result = pasteboard.writeObjects_([nsimage])
                        print(f"Resultado da cópia para clipboard (método 2): {'SUCESSO' if result else 'FALHA'}")
                        return result
                    else:
                        print("Falha ao criar NSImage a partir dos dados PNG.")
                        return False
                
                return result
                
        except Exception as img_error:
            print(f"Erro ao abrir/processar imagem: {img_error}")
            return False
            
    except ImportError as e:
        print(f"ERRO: Não foi possível importar AppKit. {e}")
        print("Este script requer macOS e as bibliotecas pyobjc-core e pyobjc-framework-Cocoa.")
        print("Instale com: pip install pyobjc-core pyobjc-framework-Cocoa")
        return False
    except Exception as e:
        print(f"ERRO INESPERADO: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python copy_image_appkit.py <caminho_da_imagem>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    print(f"Tentando copiar imagem para o clipboard: {image_path}")
    
    if copy_image_to_clipboard_appkit(image_path):
        print("\n=== SUCESSO! Imagem copiada para o clipboard. ===")
        print("Você pode tentar colar (Cmd+V) em qualquer aplicativo que aceite imagens.")
    else:
        print("\n=== FALHA ao copiar imagem para o clipboard. ===")
        sys.exit(1) 