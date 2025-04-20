#!/bin/bash
# Script para iniciar o servidor Flask no macOS com um duplo clique

# Obtém o diretório onde este script está localizado
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

# Muda para o diretório do script (raiz do projeto)
cd "$SCRIPT_DIR" || exit 1 # Sai se o diretório não puder ser acessado

# Executa o servidor Flask usando python3
#executa run_server.py

echo "Iniciando o servidor Flask (run_server.py)..."
echo "Diretório atual: $(pwd)"
echo "Executando: python3 run_server.py"
echo "-----------------------------------------"

# Certifique-se de que 'python3' aponta para a instalação correta do Python,
# especialmente se você usa ambientes virtuais (venv, conda, etc.).
# Se necessário, ative seu ambiente virtual aqui antes de executar run_server.py.
python3 run_server.py

# O servidor Flask manterá o terminal aberto. Pressione Ctrl+C no terminal para parar.
# echo "Servidor encerrado. Pressione Enter para fechar esta janela."
# read -p "" # Descomente se quiser que a janela espere após o servidor parar 