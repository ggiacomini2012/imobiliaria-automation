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
    try:
        # Get form data
        message_template = request.form.get('message_template')
        include_image = request.form.get('include_image') == 'true'
        image_file = request.files.get('image') if include_image else None
        
        if not message_template:
            return jsonify({'error': 'Message template is required'}), 400
            
        # Save image if included
        image_path = None
        if include_image and image_file:
            if not image_file.filename:
                return jsonify({'error': 'No image file selected'}), 400
                
            # Create uploads directory if it doesn't exist
            os.makedirs('uploads', exist_ok=True)
            
            # Save image
            image_path = os.path.join('uploads', image_file.filename)
            image_file.save(image_path)
            
        # Determine OS and construct command
        if sys.platform == 'darwin':  # macOS
            if include_image and image_path:
                # Use bulk_sender_mac.py with image support
                cmd = ['python', 'bulk_sender_mac.py', message_template, image_path]
            else:
                # Use bulk_sender_mac.py without image
                cmd = ['python', 'bulk_sender_mac.py', message_template]
        else:  # Windows
            if include_image and image_path:
                # Use bulk_sender.py with image support
                cmd = ['python', 'bulk_sender.py', message_template, image_path]
            else:
                # Use bulk_sender.py without image
                cmd = ['python', 'bulk_sender.py', message_template]
                
        # Run the command
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        
        if process.returncode == 0:
            return jsonify({'success': True, 'message': 'Messages sent successfully'})
        else:
            return jsonify({
                'error': 'Failed to send messages',
                'details': stderr.decode('utf-8')
            }), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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