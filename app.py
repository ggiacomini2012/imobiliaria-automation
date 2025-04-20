from flask import Flask, render_template, jsonify, request
import subprocess
import sys
import os

app = Flask(__name__)

# Define the path to the script relative to this app.py file
script_path = os.path.join(os.path.dirname(__file__), 'modules', 'send-browser2app', 'send-back.py')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/trigger_send', methods=['POST'])
def trigger_send():
    try:
        print(f"Attempting to execute script: {script_path}")
        # Ensure we're using the correct python interpreter
        python_executable = sys.executable
        print(f"Using Python executable: {python_executable}")

        # Execute the script
        result = subprocess.run(
            [python_executable, script_path],
            capture_output=True, # Capture stdout and stderr
            text=True, # Decode output as text
            check=False, # Don't raise exception on non-zero exit code, we'll check manually
            encoding='utf-8', # Specify encoding
            errors='replace' # Handle potential decoding errors
        )

        output = f"--- stdout ---\
{result.stdout}\
--- stderr ---\
{result.stderr}"
        print(f"Script execution finished. Exit code: {result.returncode}")
        print(output)

        if result.returncode == 0:
            return jsonify({'success': True, 'message': 'Script executed successfully!', 'output': output})
        else:
            return jsonify({'success': False, 'message': f'Script failed with exit code {result.returncode}.', 'output': output})

    except FileNotFoundError:
        error_message = f"Error: Python executable or script not found. Searched for script at: {script_path}"
        print(error_message)
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500
    except Exception as e:
        error_message = f"An unexpected error occurred: {str(e)}"
        print(error_message)
        # Include traceback for debugging if possible, but don't necessarily send to client
        import traceback
        print(traceback.format_exc())
        return jsonify({'success': False, 'message': error_message, 'output': ''}), 500

if __name__ == '__main__':
    # Makes the server accessible from other devices on the network
    # Use 0.0.0.0 to listen on all available network interfaces
    # Debug=True allows for auto-reloading on code changes and provides better error pages
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True) 