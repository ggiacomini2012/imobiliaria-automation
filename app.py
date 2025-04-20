from flask import Flask, render_template, jsonify, request
import subprocess
import sys
import os

app = Flask(__name__)

# Define paths relative to this app.py file
base_dir = os.path.dirname(__file__)
single_send_script_path = os.path.join(base_dir, 'modules', 'send-browser2app', 'send-back.py')
bulk_send_script_path = os.path.join(base_dir, 'codigo-final', 'bulk_sender.py') # Path to the new bulk sender

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
    script_path = single_send_script_path
    try:
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
    data = request.get_json()
    if not data or 'message_template' not in data:
        return jsonify({'success': False, 'status': 'Erro: Template da mensagem não fornecido.', 'output': ''}), 400

    message_template = data['message_template']
    # include_image = data.get('include_image', False) # Get image flag if needed later

    script_path = bulk_send_script_path
    python_executable = sys.executable

    try:
        print(f"Attempting to execute bulk send script: {script_path}")
        print(f"Using Python executable: {python_executable}")
        print(f"Message Template: \"{message_template}\"")

        # Capture output to show in the status area.
        # Prepare environment for the subprocess, ensuring UTF-8 I/O
        sub_env = os.environ.copy()
        sub_env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            [python_executable, script_path, message_template],
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


if __name__ == '__main__':
    # Makes the server accessible from other devices on the network
    # Use 0.0.0.0 to listen on all available network interfaces
    # Debug=True allows for auto-reloading on code changes and provides better error pages
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True) 