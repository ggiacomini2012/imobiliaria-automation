from PIL import Image
import win32clipboard
import io
import pyautogui
import time
import os
import pywhatkit as kit
import time
import pyautogui
import json
from datetime import datetime
import random
import pyperclip
import tkinter as tk
from tkinter import messagebox
import keyboard
import sys
import win32gui
import win32con
import threading
import queue
import atexit
import os
from contacts import cleaned_contacts2
from message import messages_function, messages



def copy_image_to_clipboard(image_path):
    image = Image.open(image_path)

    # Converta para BMP (clipboard do Windows exige)
    output = io.BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]  # Remove cabeçalho BMP
    output.close()

    # Coloca no clipboard
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

# Caminho da imagem
image_path_new = r"C:\Users\DELL\Downloads\cafe.jpg"


# Nome do arquivo JSON que armazena o log de envios
LOG_FILE = "log.json"

# Variável global para controlar a execução
running = True
banner = None  # Variável global para o banner
banner_queue = queue.Queue()  # Fila para comunicação entre threads

def minimize_terminal():
    """Minimiza a janela do terminal"""
    terminal = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(terminal, win32con.SW_MINIMIZE)

def run_banner():
    """Executa o banner em sua própria thread sem bordas de janela"""
    global banner
    banner = tk.Tk()
    
    # Remove bordas e decorações da janela
    banner.overrideredirect(True)
    banner.attributes('-topmost', True)
    banner.attributes("-alpha", 0.95)  # Leve transparência para melhorar visibilidade
    
    # Obtém dimensões da tela para centralizar
    screen_width = banner.winfo_screenwidth()
    screen_height = banner.winfo_screenheight()
    
    # Dimensões do banner
    banner_width = 400
    banner_height = 200
    
    # Calcula posição para centralizar
    x_position = (screen_width - banner_width) // 2
    y_position = (screen_height - banner_height) // 2
    
    # Define geometria e posição
    banner.geometry(f"{banner_width}x{banner_height}+{x_position}+{y_position}")
    
    banner.configure(bg='#e74c3c')  # Cor de fundo vermelha
    
    # Frame para conter o conteúdo
    frame = tk.Frame(banner, bg='#e74c3c', highlightthickness=3, highlightbackground="white")
    frame.pack(expand=True, fill='both', padx=10, pady=10)
    
    # Label com o texto
    label = tk.Label(
        frame,
        text="CÓDIGO EM EXECUÇÃO!",
        bg='#e74c3c',
        fg='white',
        font=('Arial', 18, 'bold')
    )
    label.pack(pady=15)
    
    # Segunda label
    label2 = tk.Label(
        frame,
        text="Pressione ESC para parar",
        bg='#e74c3c',
        fg='white',
        font=('Arial', 16, 'bold')
    )
    label2.pack(pady=15)
    
    def force_top():
        """Força o banner a ficar no topo a cada 100ms, sempre"""
        try:
            banner.attributes('-topmost', False)
            banner.attributes('-topmost', True)
            banner.lift()
            banner.update()
            banner.after(100, force_top)  # Intervalo mais curto (100ms)
        except:
            pass  # Ignora erros se o banner foi destruído
    
    # Inicia a função que força o banner a ficar no topo
    force_top()
    
    # Verifica a fila para comandos da thread principal
    def check_queue():
        try:
            # Non-blocking queue get
            cmd = banner_queue.get_nowait()
            if cmd == "quit":
                banner.quit()
            elif cmd == "destroy":
                banner.destroy()
        except queue.Empty:
            pass
        
        # Continue checking if banner exists
        if banner:
            try:
                banner.after(50, check_queue)  # Intervalo mais curto (50ms)
            except:
                pass
    
    # Inicia a verificação da fila
    check_queue()
    
    # Inicia o loop principal do Tkinter
    banner.mainloop()

def cleanup_banner():
    """Função para limpar o banner quando o programa for encerrado"""
    global banner
    try:
        banner_queue.put("quit")
        time.sleep(0.2)
        banner_queue.put("destroy")
    except:
        pass

# Registra a função de limpeza para ser chamada ao final do programa
atexit.register(cleanup_banner)

def on_esc_press():
    """Função chamada quando ESC é pressionado"""
    global running
    running = False
    print("\nTecla ESC pressionada. Encerrando o programa imediatamente...")
    
    # Limpa o banner primeiro
    try:
        banner_queue.put("quit")
        banner_queue.put("destroy")
    except:
        pass
    
    # Encerra de forma mais agressiva
    os._exit(0)  # Força a saída imediata (mais drástico que sys.exit())

# Registra o listener para a tecla ESC
keyboard.on_press_key('esc', lambda _: on_esc_press())

# Inicia o banner em uma thread separada
banner_thread = threading.Thread(target=run_banner)
banner_thread.daemon = True  # Thread será encerrada quando o programa principal terminar
banner_thread.start()

# Aguarda um momento para o banner aparecer
time.sleep(1)

# Minimiza o terminal
minimize_terminal()

# Carrega os contatos a serem enviados

cleaned_contacts = [
    {
        "phone_number": "5547997676797",
        "public_name": "Guiyy"
    },
    {
        "phone_number": "5547991674477",
        "public_name": "Gabiyyy"
    }
]

# Função para carregar o log existente ou criar um novo
def load_log():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"enviados": []}  # Retorna estrutura vazia se o arquivo não existir ou estiver corrompido

# Função para salvar o log atualizado
def save_log(log_data):
    with open(LOG_FILE, "w", encoding="utf-8") as file:
        json.dump(log_data, file, indent=4, ensure_ascii=False)

# Carregar o log
log = load_log()

def already_sent(phone_number):
    """Verifica se o número já recebeu a mensagem."""
    return any(entry["phone_number"] == phone_number for entry in log["enviados"])

# Loop pelos contatos e envio de mensagem
for contact in cleaned_contacts2:
    if not running:  # Verifica se deve continuar a execução
        break
        
    phone_number = contact["phone_number"]
    name = contact["public_name"]

    # Se o contato já recebeu, pula
    if already_sent(phone_number):
        print(f"{name} já recebeu a mensagem. Pulando...")
        continue

    # Mensagem personalizada
    edit_message = messages_function(name, messages["message6"])
    # Envia a mensagem
    # kit.sendwhatmsg_instantly(f"+{phone_number}", message, 40, True, 6)
    
    # time.sleep(6)  # Aguarda para garantir que a mensagem foi enviada
    pyautogui.click(412, 751) #browser
    # open browser in mac maybe trigger spotlight
    pyautogui.hotkey('command', 'space')
    time.sleep(1)
    pyautogui.write('safari')
    time.sleep(1)
    pyautogui.press('enter')
    #edit url to go to wa.me/phone_number
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    pyautogui.write(f'wa.me/{phone_number}')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    #navegate to whatsapp app in mac 
    pyautogui.moveTo(619, 705)
    time.sleep(1)
    pyautogui.click(457, 751) #whats
    time.sleep(1)
    pyautogui.click(619, 705) #whats chat de mensagem
    time.sleep(1)



    pyperclip.copy(edit_message)
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.moveTo(619, 705)

    # copy_image_to_clipboard(image_path_new)
    # time.sleep(0.5)
    # pyautogui.hotkey('ctrl', 'v')
    # time.sleep(4)

    pyautogui.moveTo(619, 705)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(619, 705)

    #navegate to browser in mac
    pyautogui.hotkey('command', 'space')
    time.sleep(1)
    pyautogui.write('safari')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    #close the tab
    
    # Fecha a aba do WhatsApp Web (atalho: CTRL + W)
    # pyautogui.hotkey("ctrl", "w")
    
    # Atualiza o log com a nova entrada
    log["enviados"].append({
        "phone_number": phone_number,
        "name": name,
        "date_sent": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    
    # Salva o log atualizado
    save_log(log)
    
    print(f"Mensagem enviada para {name} e log atualizado!")
    
    time.sleep(random.uniform(2, 5))  # Pequena pausa antes de enviar para o próximo contato

# O programa terminará naturalmente aqui e o atexit será chamado automaticamente
print("Processo finalizado. Todas as mensagens foram enviadas!")
