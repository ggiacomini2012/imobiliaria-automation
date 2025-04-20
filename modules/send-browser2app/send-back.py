import platform
import time  # Import the time module
# import pyautogui # No longer needed for GUI automation
import os # Needed for os.startfile on Windows
import subprocess # Needed for open/xdg-open on macOS/Linux

number = "5511984013378"

# Construct the direct WhatsApp URI instead of the web URL
# Note: We are omitting the text part for now, add &text=your_message if needed
whatsapp_uri = f"whatsapp://send?phone={number}"
# url = f"https://api.whatsapp.com/send/?phone={number}&text&type=phone_number&app_absent=0" # Old web URL
# browser = None # No longer needed
os_name = platform.system()

print(f"Detected OS: {os_name}")

# Remove browser detection logic
# if os_name == 'Windows':
#     # Try common Windows path first
#     try:
#         chrome_path_windows = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#         browser = webbrowser.get(chrome_path_windows)
#         print(f"Found browser using path: {chrome_path_windows}")
#     except webbrowser.Error as e:
#         print(f"Could not find browser using path {chrome_path_windows}. Error: {e}")
#         # Fallback to trying the name 'chrome' on Windows
#         try:
#             browser = webbrowser.get('chrome')
#             print("Found browser using name: 'chrome'")
#         except webbrowser.Error as e2:
#             print(f"Could not find browser using name 'chrome'. Error: {e2}")
# 
# elif os_name == 'Darwin' or os_name == 'Linux':
#     # Try common names for macOS/Linux
#     browser_names = ['chrome', 'google-chrome', 'chromium']
#     for name in browser_names:
#         try:
#             browser = webbrowser.get(name)
#             print(f"Found browser using name: {name}")
#             break
#         except webbrowser.Error:
#             print(f"Could not find browser using name: {name}")
#             continue
# else:
#     # Fallback for other OSes (try default behavior)
#     print(f"Unsupported OS ({os_name}) for specific browser detection. Trying default.")
#     try:
#         browser = webbrowser.get()
#         print("Using default system browser.")
#     except webbrowser.Error as e:
#         print(f"Could not get default browser. Error: {e}")


# Open the URL if a browser was found --- Now directly try opening the URI ---
# if browser: # Remove browser check
# ... existing code ...

# Attempt to open the WhatsApp URI directly using the OS handler
success = False
try:
    print(f"Attempting to open WhatsApp URI: {whatsapp_uri}")
    if os_name == 'Windows':
        os.startfile(whatsapp_uri)
        success = True
        print("Windows: Triggered os.startfile.")
    elif os_name == 'Darwin': # macOS
        subprocess.run(['open', whatsapp_uri], check=True)
        success = True
        print("macOS: Triggered 'open' command.")
    elif os_name == 'Linux':
        subprocess.run(['xdg-open', whatsapp_uri], check=True)
        success = True
        print("Linux: Triggered 'xdg-open' command.")
    else:
        print(f"Unsupported OS ({os_name}) for direct URI opening.")

    if success:
        print("Successfully triggered WhatsApp URI handler.")
        # Optional: Add a small delay if the subsequent script relies on WhatsApp being open
        # time.sleep(2) 

except FileNotFoundError: # Handle case where 'open' or 'xdg-open' isn't found
    print(f"Error: Command required for opening URI not found.")
    print("Please ensure the necessary command (open/xdg-open) is in your PATH.")
except subprocess.CalledProcessError as e: # Handle errors from subprocess.run
     print(f"Error running command to open URI: {e}")
except Exception as e: # Catch other potential errors (e.g., no handler for whatsapp://)
    print(f"Error opening WhatsApp URI: {e}")
    print("Please ensure WhatsApp is installed and registered to handle whatsapp:// links.")


print(f"Script finished on OS: {os_name}")
