import webbrowser

url = "https://wa.me/47997676797"

# Specify the path to the Chrome executable if it's not in your PATH
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
# Or try common names like 'google-chrome' or 'chromium' if 'chrome' doesn't work

try:
    # Get the controller for Chrome using the specified path
    browser = webbrowser.get(chrome_path)
    # Open the URL in Chrome
    browser.open(url)
    print(f"Attempting to open {url} in Chrome.")
except webbrowser.Error as e:
    print(f"Could not find Chrome browser at the specified path: {chrome_path}. Error: {e}")
    # Optionally, fall back to the default browser
    # print("Falling back to default browser...")
    # webbrowser.open(url)
