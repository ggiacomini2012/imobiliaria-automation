import pyautogui
import time
import logging

# Configuração do logger para salvar as posições em um arquivo
# logging.basicConfig(filename='mouse_positions.log', level=logging.INFO, 
#                     format='%(asctime)s - %(message)s')

try:
    while True:
        # Obtém a posição atual do mouse
        x, y = pyautogui.position()
        
        # Registra a posição com a hora
        print(f"pyautogui.click({x}, {y})")
        
        # Espera um segundo
        time.sleep(1)

except KeyboardInterrupt:
    print("\nMonitoramento encerrado.")