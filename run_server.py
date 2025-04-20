import subprocess
import time
import platform
import sys
import os

# Path to the Flask app script
app_script = 'app.py'
url_to_open = 'http://localhost:5000'

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