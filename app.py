from flask import Flask, render_template, jsonify, request, redirect, url_for
import subprocess
import sys
import os
import platform
from werkzeug.utils import secure_filename

print("\n=== EXECUTANDO: app.py ===\n")

app = Flask(__name__)

# Define paths relative to this app.py file
base_dir = os.path.dirname(__file__)
# Original paths
single_send_script_path_win = os.path.join(base_dir, 'modules', 'send-browser2app', 'send-back.py')
bulk_send_script_path_win = os.path.join(base_dir, 'codigo-final', 'bulk_sender.py')
focus_script_path = os.path.join(base_dir, 'focus_whatsapp.py') # Mantém, pois bulk_sender.py (Win) o chama
send_image_gui_script_path_win = os.path.join(base_dir, 'send_image_gui.py') # Mantém, pois bulk_sender.py (Win) o chama
# macOS specific paths
single_send_script_path_mac = os.path.join(base_dir, 'modules', 'send-browser2app', 'send-back_mac.py')
bulk_send_script_path_mac = os.path.join(base_dir, 'codigo-final', 'bulk_sender_mac.py')
# Note: send_image_gui_mac.py é chamado DENTRO de bulk_sender_mac.py, então não precisamos de um path direto aqui

# Define upload folder path
UPLOAD_FOLDER = os.path.join(base_dir, 'uploads')
# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    # Redirect root to dashboard, or keep the old index?
    # Let's redirect to dashboard for now
    # return render_template('index.html')
    return render_template('dashboard.html') # Default to dashboard

@app.route('/simple_send_page') # Optional: Keep old page accessible
def simple_send_page():
     return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# Renamed old trigger for clarity
@app.route('/trigger_single_send', methods=['POST'])
def trigger_single_send():
    # Determine which script to use based on OS
    os_name = platform.system()
    if os_name == 'Darwin': # macOS
        script_path = single_send_script_path_mac
        print("Using macOS specific script for single send.")
    else: # Default to Windows/original script
        script_path = single_send_script_path_win
        print("Using default/Windows script for single send.")

    try:
        # ---- REVERTED TO ORIGINAL subprocess.run CODE ----
        print(f"Attempting to execute single send script: {script_path}")
        python_executable = sys.executable
        print(f"Using Python executable: {python_executable}")

        result = subprocess.run(
            [python_executable, script_path],
            capture_output=True, text=True, check=False, encoding='utf-8', errors='replace'
        )
        output = f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
        print(f"Single send script finished. Exit code: {result.returncode}")
        print(output)

        if result.returncode == 0:
            return jsonify({'success': True, 'message': 'Script individual executado!', 'output': output})
        else:
            return jsonify({'success': False, 'message': f'Script individual falhou (código {result.returncode}).', 'output': output})

    except FileNotFoundError:
        error_message = f"Erro: Executável Python ou script não encontrado. Script: {script_path}"
        print(error_message)
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500
    except Exception as e:
        error_message = f"Erro inesperado ao executar script individual: {str(e)}"
        print(error_message)
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500

@app.route('/send_messages', methods=['POST'])
def send_messages():
    # Get data from form fields instead of JSON
    message_template = request.form.get('message_template')
    # Checkbox value will be 'true' (string) if checked, None otherwise
    include_image_str = request.form.get('include_image')
    include_image = include_image_str == 'true'

    print(f"Received data in /send_messages: template='{message_template}', include_image={include_image}")

    if not message_template:
        return jsonify({'success': False, 'status': 'Erro: Template da mensagem não fornecido.', 'output': ''}), 400

    image_file = request.files.get('image_file')
    saved_image_path = None

    # Determine which script to use based on OS
    os_name = platform.system()
    
    # Se for macOS e a imagem estiver selecionada, avisar que será ignorada
    if os_name == 'Darwin' and include_image:
        print("AVISO: Envio de imagem não suportado no macOS. Será enviado apenas o texto.")
        include_image = False  # Forçar include_image para False no macOS
    
    # Processar a imagem apenas se não estiver no macOS
    if include_image and os_name != 'Darwin':
        if not image_file or image_file.filename == '':
            return jsonify({'success': False, 'status': 'Erro: Imagem marcada para inclusão, mas nenhum arquivo foi enviado ou o arquivo está vazio.', 'output': ''}), 400
        
        try:
            filename = secure_filename(image_file.filename)
            saved_image_path = os.path.join(UPLOAD_FOLDER, filename)
            image_file.save(saved_image_path)
            print(f"Image saved successfully to: {saved_image_path}")
        except Exception as e:
            print(f"Error saving uploaded image: {e}")
            return jsonify({'success': False, 'status': f'Erro ao salvar a imagem: {e}', 'output': ''}), 500
    elif image_file and os_name != 'Darwin':
         print("Image file uploaded but 'Include Image' checkbox was not checked. Ignoring image.")
    elif image_file and os_name == 'Darwin':
         print("Image file uploaded but macOS doesn't support image sending. Ignoring image.")

    # Determine which script to use based on OS
    if os_name == 'Darwin': # macOS
        script_path = bulk_send_script_path_mac
        print("Using macOS specific script for bulk send.")
    else: # Default to Windows/original script
        script_path = bulk_send_script_path_win
        print("Using default/Windows script for bulk send.")

    python_executable = sys.executable

    # --- Build the command arguments ---
    cmd_args = [python_executable, script_path, message_template]
    if include_image and saved_image_path and os_name != 'Darwin':
        # Add image path as the next argument IF image is included AND not on macOS
        cmd_args.append(saved_image_path)
    # ----------------------------------

    try:
        print(f"Attempting to execute bulk send script with args: {cmd_args}")
        
        # Capture output to show in the status area.
        # Prepare environment for the subprocess, ensuring UTF-8 I/O
        sub_env = os.environ.copy()
        sub_env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            cmd_args, # Use the constructed arguments list
            capture_output=True, text=True, check=False, encoding='utf-8', errors='replace',
            cwd=base_dir, # Set the current working directory to the project root
            env=sub_env # Pass the modified environment
        )

        output = f"--- stdout ---\n{result.stdout}\n--- stderr ---\n{result.stderr}"
        print(f"Bulk send script finished. Exit code: {result.returncode}")
        print(output)

        if result.returncode == 0:
            return jsonify({'success': True, 'status': 'Processo de envio em massa concluído.', 'output': output})
        else:
            return jsonify({'success': False, 'status': f'Processo de envio em massa falhou (código {result.returncode}).', 'output': output})

    except FileNotFoundError:
        error_message = f"Erro: Executável Python ou script de envio em massa não encontrado. Script: {script_path}"
        print(error_message)
        return jsonify({'success': False, 'status': 'Erro interno do servidor (script não encontrado).', 'output': error_message}), 500
    except Exception as e:
        error_message = f"Erro inesperado ao executar o envio em massa: {str(e)}"
        print(error_message)
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'status': 'Erro interno do servidor.', 'output': error_message}), 500

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/trigger_focus', methods=['POST'])
def trigger_focus():
    """Executes the focus_whatsapp.py script."""
    script_path = focus_script_path
    python_executable = sys.executable
    print(f"Attempting to execute focus script via button: {script_path}")
    
    try:
        focus_result = subprocess.run(
            [python_executable, script_path],
            capture_output=True, text=True, check=False, encoding='utf-8', errors='replace',
            cwd=base_dir # Run from project root
        )
        output = f"--- stdout ---\n{focus_result.stdout}\n--- stderr ---\n{focus_result.stderr}"
        print(output)
        
        if focus_result.returncode == 0:
            return jsonify({'success': True, 'message': 'Focus script executado com sucesso.', 'output': output})
        else:
            return jsonify({'success': False, 'message': f'Focus script falhou (código {focus_result.returncode}).', 'output': output})
            
    except FileNotFoundError:
        error_message = f"Erro: Script de foco não encontrado. Script: {script_path}"
        print(error_message)
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500
    except Exception as e:
        error_message = f"Erro inesperado ao executar script de foco: {str(e)}"
        print(error_message)
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500

# Route to clear the sent log file
@app.route('/clear-log', methods=['POST'])
def clear_log():
    log_file_path = os.path.join(base_dir, 'codigo-final', 'sent_log.txt')
    print(f"Attempting to clear log file: {log_file_path}")
    try:
        if os.path.exists(log_file_path):
            os.remove(log_file_path)
            print(f"Successfully deleted log file: {log_file_path}")
            return jsonify({'success': True, 'message': 'Log de enviados limpo com sucesso!'})
        else:
            print(f"Log file not found, nothing to clear: {log_file_path}")
            return jsonify({'success': True, 'message': 'Log de enviados não encontrado (nada para limpar).'})
    except Exception as e:
        error_message = f"Erro ao limpar o log de enviados: {str(e)}"
        print(error_message)
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': error_message}), 500

if __name__ == '__main__':
    # Makes the server accessible from other devices on the network
    # Use 0.0.0.0 to listen on all available network interfaces
    # Debug=True allows for auto-reloading on code changes and provides better error pages
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True) 