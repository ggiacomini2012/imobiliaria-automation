#!/usr/bin/env python3
# sudoiamge_mac.py - Script para enviar imagem para WhatsApp no macOS
# Baseado no send-back_mac.py, com funcionalidade de imagem adicionada

import platform
import time
import os
import subprocess
import pyautogui
from PIL import Image
import sys

print("\n=== EXECUTANDO: sudoiamge_mac.py ===\n")

# Intervalos (ajuste conforme necessário)
