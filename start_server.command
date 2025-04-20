#!/bin/bash
# Script para iniciar o servidor Flask no macOS com um duplo clique EM SEGUNDO PLANO (SEM LOG)

# Obtém o diretório onde este script está localizado
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

# Muda para o diretório do script (raiz do projeto)
cd "$SCRIPT_DIR" || exit 1 # Sai se o diretório não puder ser acessado

# Define o arquivo de log
# LOG_FILE="$SCRIPT_DIR/server.log" # Comentado pois não queremos log

# Executa o servidor Flask usando python3 em segundo plano com nohup
# A saída (stdout e stderr) será redirecionada para /dev/null (descartada)
echo "Iniciando o servidor Flask (run_server.py) em segundo plano SEM LOG..."
# echo "Logs serão escritos em: $LOG_FILE" # Comentado
echo "Diretório atual: $(pwd)"
echo "Executando: nohup python3 run_server.py > /dev/null 2>&1 &"
echo "-----------------------------------------"

# Certifique-se de que 'python3' aponta para a instalação correta do Python.
# Se necessário, ative seu ambiente virtual aqui antes de executar run_server.py.
# O comando 'nohup' garante que o processo continue rodando após o terminal fechar.
# O '&' no final envia o processo para o background.

nohup python3 run_server.py > /dev/null 2>&1 &

# A janela do terminal fechará automaticamente.
# Para PARAR o servidor, você precisará encontrar o ID do processo (PID) e matá-lo.
# Abra o Terminal e use:
#   ps aux | grep 'python3 run_server.py'
# Encontre o PID na segunda coluna e use:
#   kill <PID>
# (Substitua <PID> pelo número encontrado)

echo "Comando para iniciar o servidor em segundo plano (sem log) enviado."
# A janela deve fechar em breve. 