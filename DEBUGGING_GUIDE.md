# Debugging Guide for macOS Image Pasting

This guide provides step-by-step instructions for debugging the application to identify exactly where the image pasting fails on macOS.

## Prerequisites

1. **Install Required Tools**:
   - Python 3.6+ (already installed)
   - Visual Studio Code with Python extension (recommended)
   - PyCharm (alternative)
   - Python debugger (pdb)

2. **Install Debugging Dependencies**:
   ```bash
   pip install ipdb  # Enhanced Python debugger
   pip install debugpy  # For VS Code debugging
   ```

## Method 1: Using Visual Studio Code (Recommended)

### Setup

1. **Open the project in VS Code**:
   ```bash
   code /path/to/imobiliaria-automation
   ```

2. **Create a launch configuration**:
   - Click on the "Run and Debug" icon in the sidebar (or press `Ctrl+Shift+D`)
   - Click "create a launch.json file"
   - Select "Python"
   - Choose "Flask" as the application type
   - Set the following configuration:

   ```json
   {
       "version": "0.2.0",
       "configurations": [
           {
               "name": "Flask: app.py",
               "type": "python",
               "request": "launch",
               "module": "flask",
               "env": {
                   "FLASK_APP": "app.py",
                   "FLASK_ENV": "development",
                   "FLASK_DEBUG": "1"
               },
               "args": [
                   "run",
                   "--no-debugger",
                   "--no-reload"
               ],
               "jinja": true,
               "justMyCode": false
           },
           {
               "name": "Python: send_image_mac.py",
               "type": "python",
               "request": "launch",
               "program": "${workspaceFolder}/send_image_mac.py",
               "args": ["${input:phoneNumber}", "${input:imagePath}"],
               "console": "integratedTerminal",
               "justMyCode": false
           }
       ],
       "inputs": [
           {
               "id": "phoneNumber",
               "type": "promptString",
               "description": "Phone number to send to"
           },
           {
               "id": "imagePath",
               "type": "promptString",
               "description": "Path to the image file"
           }
       ]
   }
   ```

### Debugging Steps

1. **Set Breakpoints**:
   - Open `app.py` and set breakpoints at:
     - Line 84: `@app.route('/send_messages', methods=['POST'])`
     - Line 89: `message_template = request.form.get('message_template')`
     - Line 91: `include_image_str = request.form.get('include_image')`
     - Line 142: `cmd_args = [python_executable, script_path, message_template]`

   - Open `send_image_mac.py` and set breakpoints at:
     - Line 78: `def send_image(phone_number, image_path):`
     - Line 82: `if not validate_image(image_path):`
     - Line 86: `if not copy_image_to_clipboard(image_path):`
     - Line 90: `if not open_whatsapp_with_number(phone_number):`
     - Line 97: `pyautogui.hotkey('command', 'v')`

2. **Start Debugging**:
   - Select the "Flask: app.py" configuration from the dropdown
   - Click the green play button or press F5
   - The application will start in debug mode

3. **Test the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`
   - Fill out the form with a message and select an image
   - Click "Iniciar Envio"

4. **Step Through the Code**:
   - When the first breakpoint is hit, use the following controls:
     - F10: Step Over (execute the current line and move to the next)
     - F11: Step Into (go into function calls)
     - Shift+F11: Step Out (exit the current function)
     - F5: Continue (run until the next breakpoint)
     - Shift+F5: Stop Debugging

5. **Inspect Variables**:
   - In the Variables panel, you can see the values of all variables
   - Hover over variables in the code to see their values
   - Use the Debug Console to evaluate expressions

## Method 2: Using Python Debugger (pdb)

### Setup

1. **Modify the code to add breakpoints**:
   - Open `app.py` and add the following line at the beginning of the `/send_messages` route:
     ```python
     import pdb; pdb.set_trace()
     ```

   - Open `send_image_mac.py` and add the following line at the beginning of the `send_image` function:
     ```python
     import pdb; pdb.set_trace()
     ```

2. **Run the application**:
   ```bash
   python app.py
   ```

### Debugging Steps

1. **Test the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`
   - Fill out the form with a message and select an image
   - Click "Iniciar Envio"

2. **Use pdb Commands**:
   - When a breakpoint is hit, you'll see a `(Pdb)` prompt
   - Use the following commands:
     - `n`: Next line (step over)
     - `s`: Step into function
     - `c`: Continue execution
     - `p variable_name`: Print variable value
     - `l`: List source code around current line
     - `q`: Quit debugger
     - `h`: Help

## Method 3: Using Logging for Detailed Tracing

### Setup

1. **Add logging to the code**:
   - Create a new file `debug_logger.py`:

   ```python
   import logging
   import os
   import sys

   # Create logs directory if it doesn't exist
   os.makedirs('logs', exist_ok=True)

   # Configure logging
   logging.basicConfig(
       level=logging.DEBUG,
       format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
       handlers=[
           logging.FileHandler('logs/debug.log'),
           logging.StreamHandler(sys.stdout)
       ]
   )

   # Create a logger
   logger = logging.getLogger('imobiliaria')

   # Function to log function entry and exit
   def log_function(func):
       def wrapper(*args, **kwargs):
           logger.debug(f"ENTERING: {func.__name__}")
           try:
               result = func(*args, **kwargs)
               logger.debug(f"EXITING: {func.__name__} with result: {result}")
               return result
           except Exception as e:
               logger.error(f"ERROR in {func.__name__}: {str(e)}", exc_info=True)
               raise
       return wrapper
   ```

2. **Modify the code to use the logger**:
   - In `app.py`, add:
     ```python
     from debug_logger import logger, log_function
     
     @log_function
     @app.route('/send_messages', methods=['POST'])
     def send_messages():
         # Existing code...
     ```

   - In `send_image_mac.py`, add:
     ```python
     from debug_logger import logger, log_function
     
     @log_function
     def send_image(phone_number, image_path):
         # Existing code...
     ```

3. **Run the application**:
   ```bash
   python app.py
   ```

### Debugging Steps

1. **Test the Application**:
   - Open your browser and navigate to `http://127.0.0.1:5000`
   - Fill out the form with a message and select an image
   - Click "Iniciar Envio"

2. **Check the Logs**:
   - Open `logs/debug.log` to see detailed execution flow
   - Look for errors or unexpected behavior

## Method 4: Manual Testing of Image Copying

### Setup

1. **Create a test script**:
   - Create a new file `test_image_copy.py`:

   ```python
   import sys
   import os
   from PIL import Image
   import subprocess
   import time
   import pyautogui

   def test_copy_image_macos(image_path):
       """Test copying image to clipboard on macOS."""
       print(f"Testing image copy: {image_path}")
       
       # Validate image
       try:
           with Image.open(image_path) as img:
               print(f"Image valid: {img.format} {img.size}")
       except Exception as e:
           print(f"Error validating image: {e}")
           return False
       
       # Try AppleScript method
       print("Trying AppleScript method...")
       apple_script = f'''
       tell application "System Events"
           set the clipboard to (read (POSIX file "{image_path}") as JPEG picture)
       end tell
       '''
       try:
           subprocess.run(['osascript', '-e', apple_script], check=True)
           print("AppleScript copy successful")
           
           # Wait a moment
           time.sleep(1)
           
           # Try pasting
           print("Attempting to paste...")
           pyautogui.hotkey('command', 'v')
           print("Paste command sent")
           
           return True
       except Exception as e:
           print(f"AppleScript method failed: {e}")
       
       # Try AppKit method (if available)
       print("Trying AppKit method...")
       try:
           from AppKit import NSPasteboard, NSImage
           pasteboard = NSPasteboard.generalPasteboard()
           image = NSImage.alloc().initWithContentsOfFile_(image_path)
           pasteboard.clearContents()
           pasteboard.writeObjects_([image])
           print("AppKit copy successful")
           
           # Wait a moment
           time.sleep(1)
           
           # Try pasting
           print("Attempting to paste...")
           pyautogui.hotkey('command', 'v')
           print("Paste command sent")
           
           return True
       except Exception as e:
           print(f"AppKit method failed: {e}")
       
       # Try Preview.app method
       print("Trying Preview.app method...")
       try:
           # Open in Preview
           subprocess.run(['open', '-a', 'Preview', image_path], check=True)
           time.sleep(1)
           
           # Select all
           subprocess.run(['osascript', '-e', 
               'tell application "System Events" to keystroke "a" using command down'], 
               check=True)
           time.sleep(0.5)
           
           # Copy
           subprocess.run(['osascript', '-e', 
               'tell application "System Events" to keystroke "c" using command down'], 
               check=True)
           time.sleep(0.5)
           
           # Close Preview
           subprocess.run(['osascript', '-e', 
               'tell application "System Events" to keystroke "w" using command down'], 
               check=True)
           
           print("Preview.app copy successful")
           
           # Wait a moment
           time.sleep(1)
           
           # Try pasting
           print("Attempting to paste...")
           pyautogui.hotkey('command', 'v')
           print("Paste command sent")
           
           return True
       except Exception as e:
           print(f"Preview.app method failed: {e}")
       
       print("All methods failed")
       return False

   if __name__ == "__main__":
       if len(sys.argv) != 2:
           print("Usage: python test_image_copy.py <image_path>")
           sys.exit(1)
           
       image_path = sys.argv[1]
       if not os.path.exists(image_path):
           print(f"Error: Image path does not exist: {image_path}")
           sys.exit(1)
           
       print("=== Starting Image Copy Test ===")
       print(f"Image: {image_path}")
       
       if test_copy_image_macos(image_path):
           print("=== Test completed successfully ===")
           sys.exit(0)
       else:
           print("=== Test failed ===")
           sys.exit(1)
   ```

### Debugging Steps

1. **Run the test script**:
   ```bash
   python test_image_copy.py /path/to/your/image.jpg
   ```

2. **Observe the output**:
   - The script will try multiple methods to copy the image
   - It will attempt to paste the image after each successful copy
   - Watch for any errors or failures

3. **Test in WhatsApp**:
   - After a successful copy, open WhatsApp manually
   - Try pasting the image (Cmd+V)
   - Observe if the image appears correctly

## Troubleshooting Common Issues

1. **Clipboard Access Issues**:
   - macOS may restrict clipboard access for security reasons
   - Check System Preferences > Security & Privacy > Privacy > Accessibility
   - Ensure your terminal or IDE has the necessary permissions

2. **Image Format Issues**:
   - Try converting the image to PNG format before testing
   - Use the PIL library to convert: `Image.open('input.jpg').save('output.png')`

3. **Timing Issues**:
   - If pasting fails, try increasing the wait times between operations
   - Add more logging to identify where delays are needed

4. **WhatsApp Focus Issues**:
   - Ensure WhatsApp is in focus when pasting
   - Try using `pyautogui.click()` to click on the WhatsApp window before pasting

## Next Steps After Debugging

Once you've identified the exact point of failure:

1. **Implement a fix** based on the debugging findings
2. **Test the fix** using the same debugging methods
3. **Update the code** to handle the specific macOS image copying requirements
4. **Remove debugging code** before deploying to production 