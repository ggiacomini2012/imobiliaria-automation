# send_message_with_image_mac.py
import platform
import time
import os
# import subprocess # Não mais necessário para copiar imagem
import pyautogui
import pyperclip
from PIL import Image

# PyObjC imports
try:
    from AppKit import NSPasteboard, NSImage, NSPasteboardTypeTIFF, NSApplication # Adicionado NSApplication
    from Foundation import NSURL
except ImportError:
    print("Erro: PyObjC não está instalado corretamente. Instale com:")
    print("pip install pyobjc-core pyobjc-framework-Cocoa")
    # sys.exit(1) # Comentado para não parar o script se já estiver rodando
    pass

# Intervalos (ajuste conforme necessário)
WAIT_AFTER_OPEN = 7.0  # Segundos após abrir o WhatsApp
WAIT_AFTER_PASTE = 5.0  # AUMENTADO! Segundos após colar imagem
WAIT_BEFORE_SEND_ENTER = 0.5  # Segundos antes do Enter

def copy_image_to_clipboard(image_path):
    """Copia imagem para clipboard no macOS usando PyObjC (NSPasteboard)."""
    abs_image_path = os.path.abspath(image_path)
    if not os.path.exists(abs_image_path):
        print(f"Erro: Imagem não encontrada em {abs_image_path}")
        return False

    try:
        # Tentar carregar a imagem com NSImage
        # Inicializa NSApplication se ainda não foi inicializado (necessário para NSImage)
        NSApplication.sharedApplication()
        
        print(f"Tentando carregar imagem com NSImage: {abs_image_path}")
        ns_image = NSImage.alloc().initWithContentsOfFile_(abs_image_path)
        
        if ns_image is None:
            print(f"Erro (PyObjC): Não foi possível carregar a imagem {abs_image_path} com NSImage.")
            return False
            
        print(f"Imagem carregada com NSImage. Tamanho: {ns_image.size()}")

        # Obter o pasteboard geral
        pasteboard = NSPasteboard.generalPasteboard()
        if pasteboard is None:
            print("Erro (PyObjC): Não foi possível acessar NSPasteboard.generalPasteboard().")
            return False
            
        # Limpar o pasteboard
        print("Limpando NSPasteboard...")
        pasteboard.clearContents()
        
        # Obter dados TIFF da imagem (formato comum para imagens no clipboard do Mac)
        tiff_data = ns_image.TIFFRepresentation()
        if tiff_data is None:
             print("Erro (PyObjC): Não foi possível obter TIFFRepresentation da imagem.")
             return False

        # Escrever os dados no pasteboard
        print("Escrevendo dados TIFF no NSPasteboard...")
        wrote_ok = pasteboard.setData_forType_(tiff_data, NSPasteboardTypeTIFF)
        
        if wrote_ok:
            print("Imagem copiada para clipboard com sucesso (via PyObjC).")
            time.sleep(0.5) # Pequena pausa
            return True
        else:
            print("Erro (PyObjC): Falha ao escrever dados no NSPasteboard.")
            return False
            
    except NameError: # Caso PyObjC não esteja carregado
         print("Erro Fatal: PyObjC não parece estar instalado ou importado corretamente.")
         return False
    except Exception as e:
        print(f"Erro EXCEPCIONAL ao copiar imagem para clipboard via PyObjC: {e}")
        import traceback
        print(traceback.format_exc()) # Imprimir traceback para depuração
        return False

def send_message_with_image(phone_number, message, image_path):
    """Envia mensagem com imagem no WhatsApp."""
    try:
        # 1. Copiar imagem para clipboard
        if not copy_image_to_clipboard(image_path):
            return False

        # 2. Abrir WhatsApp com o número
        whatsapp_uri = f"whatsapp://send?phone={phone_number}"
        print(f"Abrindo WhatsApp para {phone_number}...")
        subprocess.run(['open', whatsapp_uri], check=True)
        
        # 3. Esperar WhatsApp abrir
        print(f"Aguardando {WAIT_AFTER_OPEN} segundos para o WhatsApp abrir...")
        time.sleep(WAIT_AFTER_OPEN)

        # 4. Colar a imagem
        print("\nColando imagem...")
        pyautogui.hotkey('command', 'v')
        print(f"Aguardando {WAIT_AFTER_PASTE} segundos para a imagem carregar...")
        time.sleep(WAIT_AFTER_PASTE)

        # 5. Limpar o clipboard e copiar a mensagem
        print("\nCopiando mensagem para clipboard...")
        subprocess.run(['osascript', '-e', 'set the clipboard to ""'], check=False)
        time.sleep(0.5)
        pyperclip.copy(message)
        time.sleep(0.5)

        # 6. Colar a mensagem
        print("\nColando mensagem...")
        pyautogui.hotkey('command', 'v')
        time.sleep(0.5)

        # 7. Pressionar Enter
        print("\nPressionando Enter...")
        pyautogui.press('enter')
        time.sleep(WAIT_BEFORE_SEND_ENTER)

        print("\nSequência de automação GUI finalizada.")
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
    if len(sys.argv) != 4:
        print("Uso: python send_message_with_image_mac.py <phone_number> <message> <image_path>")
        sys.exit(1)

    phone = sys.argv[1]
    msg = sys.argv[2]
    img = sys.argv[3]
    
    print("\n--- Iniciando Script de Envio de Mensagem com Imagem (macOS) ---")
    print(f"Número: {phone}")
    print(f"Mensagem: {msg}")
    print(f"Imagem: {img}")
    
    if send_message_with_image(phone, msg, img):
        print("--- Script finalizado: Sucesso ---")
    else:
        print("--- Script finalizado: Falha ---") 