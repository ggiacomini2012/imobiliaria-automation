import subprocess
import time
import platform
import sys
import os

# Path to the Flask app script
app_script = 'app.py'
url_to_open = 'http://localhost:5000'

def kill_process_on_port(port):
    """Attempts to find and kill the process using the specified port."""
    system = platform.system()
    if system == 'Darwin': # macOS
        try:
            # Find the PID using the port
            result = subprocess.run(['lsof', '-ti', f':{port}'], capture_output=True, text=True, check=False)
            pid = result.stdout.strip()
            if pid:
                print(f"Found process with PID {pid} on port {port}. Attempting to kill...")
                # Kill the process
                kill_result = subprocess.run(['kill', '-9', pid], check=False)
                if kill_result.returncode == 0:
                    print(f"Successfully killed process {pid}.")
                else:
                    print(f"Failed to kill process {pid}. It might have already terminated or require sudo.")
            else:
                print(f"No process found running on port {port}.")
        except FileNotFoundError:
            print("Error: 'lsof' command not found. Cannot check/kill process on port.")
        except Exception as e:
            print(f"An error occurred while trying to kill process on port {port}: {e}")
    elif system == 'Windows':
        try:
            # Find PID using netstat
            find_pid_cmd = f'netstat -ano | findstr ":{port}"'
            result = subprocess.run(find_pid_cmd, shell=True, capture_output=True, text=True, check=False)
            output = result.stdout.strip()
            pid_to_kill = None
            if output:
                lines = output.splitlines()
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 5 and parts[1].endswith(f":{port}"):
                        pid_to_kill = parts[-1] # Last part is PID
                        break
            
            if pid_to_kill:
                print(f"Found process with PID {pid_to_kill} on port {port}. Attempting to kill...")
                # Kill the process using taskkill
                kill_cmd = f'taskkill /F /PID {pid_to_kill}'
                kill_result = subprocess.run(kill_cmd, shell=True, capture_output=True, text=True, check=False)
                if kill_result.returncode == 0:
                    print(f"Successfully killed process {pid_to_kill}.")
                else:
                    print(f"Failed to kill process {pid_to_kill}. Error: {kill_result.stderr.strip()}")
            else:
                print(f"No process found listening on port {port}.")
        except FileNotFoundError:
            print("Error: 'netstat' or 'taskkill' command not found. Cannot check/kill process on port.")
        except Exception as e:
            print(f"An error occurred while trying to kill process on port {port} on Windows: {e}")
    # Add Linux implementation if needed
    # elif system == 'Linux':
    #     pass 
    else:
        print(f"Port killing not implemented for OS: {system}")

def open_chrome(url):
    """Attempts to open the given URL specifically in Google Chrome."""
    system = platform.system()
    cmd = None
    print(f"Attempting to open {url} in Google Chrome on {system}...")

    try:
        if system == 'Windows':
            # Try using 'start chrome'
            cmd = ['start', 'chrome', url]
            subprocess.run(cmd, shell=True, check=True)
            print(f"Executed: {' '.join(cmd)}")
            return True
        elif system == 'Darwin': # macOS
            # Try using 'open -a Google Chrome'
            cmd = ['open', '-a', 'Google Chrome', url]
            subprocess.run(cmd, check=True)
            print(f"Executed: {' '.join(cmd)}")
            return True
        elif system == 'Linux':
            # Try common Linux chrome executable names
            for chrome_cmd in ['google-chrome', 'google-chrome-stable', 'chromium-browser', 'chromium']:
                try:
                    cmd = [chrome_cmd, url]
                    subprocess.run(cmd, check=True)
                    print(f"Executed: {' '.join(cmd)}")
                    return True
                except FileNotFoundError:
                    continue # Try the next command
            print("Could not find a suitable Chrome/Chromium command on Linux.")
            return False
        else:
            print(f"Unsupported OS for specific Chrome launch: {system}")
            return False
    except FileNotFoundError:
        print(f"Error: Chrome command not found or failed for command: {' '.join(cmd) if cmd else 'N/A'}")
        print("Make sure Google Chrome is installed and in your system's PATH.")
        return False
    except subprocess.CalledProcessError as e:
        print(f"Error executing command to open Chrome: {e}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred while trying to open Chrome: {e}")
        return False

def open_default_browser(url):
    """Falls back to opening the URL in the default web browser."""
    print("Falling back to opening in default browser...")
    import webbrowser
    try:
        if webbrowser.open(url):
            print(f"Successfully opened {url} in default browser.")
        else:
            print("webbrowser.open() returned false. Could not open in default browser.")
    except Exception as e:
        print(f"An error occurred opening default browser: {e}")

if __name__ == "__main__":
    if not os.path.exists(app_script):
        print(f"Error: Flask application script '{app_script}' not found.")
        sys.exit(1)

    print(f"Starting Flask server ({app_script})...")
    # Start the Flask server in a new process
    # Use sys.executable to ensure the same python interpreter is used
    try:
        server_process = subprocess.Popen([sys.executable, app_script])
        print(f"Server process started with PID: {server_process.pid}")
    except Exception as e:
        print(f"Failed to start Flask server: {e}")
        sys.exit(1)

    # Wait a few seconds for the server to initialize
    wait_seconds = 3
    print(f"Waiting {wait_seconds} seconds for server to start...")
    time.sleep(wait_seconds)

    # Attempt to open in Chrome, fall back to default browser
    if not open_chrome(url_to_open):
        open_default_browser(url_to_open)

    print("\nScript finished. The Flask server is likely still running in the background.")
    print("Press CTRL+C in the terminal where the server is running to stop it.")
    # Note: This script will exit, but the server_process continues unless explicitly managed. 