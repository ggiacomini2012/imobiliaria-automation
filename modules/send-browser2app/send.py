import webbrowser
import platform
import time  # Import the time module
import pyautogui

number = "5547997676797"

url = f"https://api.whatsapp.com/send/?phone={number}&text&type=phone_number&app_absent=0"
browser = None
os_name = platform.system()

print(f"Detected OS: {os_name}")

if os_name == 'Windows':
    # Try common Windows path first
    try:
        chrome_path_windows = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        browser = webbrowser.get(chrome_path_windows)
        print(f"Found browser using path: {chrome_path_windows}")
    except webbrowser.Error as e:
        print(f"Could not find browser using path {chrome_path_windows}. Error: {e}")
        # Fallback to trying the name 'chrome' on Windows
        try:
            browser = webbrowser.get('chrome')
            print("Found browser using name: 'chrome'")
        except webbrowser.Error as e2:
            print(f"Could not find browser using name 'chrome'. Error: {e2}")

elif os_name == 'Darwin' or os_name == 'Linux':
    # Try common names for macOS/Linux
    browser_names = ['chrome', 'google-chrome', 'chromium']
    for name in browser_names:
        try:
            browser = webbrowser.get(name)
            print(f"Found browser using name: {name}")
            break
        except webbrowser.Error:
            print(f"Could not find browser using name: {name}")
            continue
else:
    # Fallback for other OSes (try default behavior)
    print(f"Unsupported OS ({os_name}) for specific browser detection. Trying default.")
    try:
        browser = webbrowser.get()
        print("Using default system browser.")
    except webbrowser.Error as e:
        print(f"Could not get default browser. Error: {e}")


# Open the URL if a browser was found
if browser:
    try:
            
        browser.open(url)
        print(f"Attempting to open {url}...")
        if os_name == 'Windows':
            time.sleep(2)
            #navegate to chrome maybe with tab alt + tab
            pyautogui.hotkey('alt', 'tab')
            time.sleep(1)
            #close one tab with pyautogui ctrl + w
            #close one tab with pyautogui ctrl + w
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            #go back to whatsapp app with pyautogui alt + tab
            pyautogui.hotkey('alt', 'tab')
            
        if os_name == 'Darwin' or os_name == 'Linux':
            time.sleep(1)
            #navegate to chrome
            pyautogui.hotkey('command', 'space')
            time.sleep(1)
            #type chrome
            pyautogui.typewrite('chrome')
            time.sleep(1)
            #press enter
            pyautogui.press('enter')
            time.sleep(1)   
            #close one tab with pyautogui ctrl + w
            pyautogui.hotkey('ctrl', 'w')
            time.sleep(1)
            #go back to whatsapp app with pyautogui command + tab
            pyautogui.hotkey('command', 'tab')
            time.sleep(1)


    except Exception as e:
        print(f"Error opening URL: {e}")
else:
    print("Could not find a suitable browser to open the URL.")
    # Optionally, try opening with the system default regardless
    # print("Attempting to open with system default...")
    # try:
    #     webbrowser.open(url)
    # except Exception as e:
    #     print(f"Failed to open with system default: {e}")

print(f"Running on OS: {os_name}")
