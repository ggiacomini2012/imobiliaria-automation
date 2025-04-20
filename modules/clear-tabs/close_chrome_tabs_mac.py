import subprocess
import platform

# --- IMPORTANT: Define the URL of the tab you want to KEEP open ---
URL_TO_KEEP = "https://keep.this.tab.com/" # Change this to the exact URL you want to preserve

def run_applescript(script):
    """Executes the given AppleScript string using osascript."""
    try:
        process = subprocess.run(['osascript', '-e', script], 
                                 capture_output=True, text=True, check=True)
        print("AppleScript executed successfully.")
        if process.stdout:
            print("Output:", process.stdout)
        if process.stderr:
            print("Errors:", process.stderr) # Should be empty if check=True and no error
    except FileNotFoundError:
        print("Error: 'osascript' command not found. Is this macOS?")
    except subprocess.CalledProcessError as e:
        print(f"Error executing AppleScript:")
        print(f"Command: {e.cmd}")
        print(f"Return code: {e.returncode}")
        print(f"Output: {e.output}")
        print(f"Stderr: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Define the AppleScript code
# It iterates through windows and tabs, closing those whose URL doesn't match URL_TO_KEEP
applescript_code = f'''
tell application "Google Chrome"
	set windows_list to every window
	repeat with current_window in windows_list
		set tabs_list to every tab of current_window
		-- Iterate backwards because closing a tab changes the indices
		repeat with i from (count of tabs_list) to 1 by -1
			set current_tab to item i of tabs_list
			set tab_url to URL of current_tab
			if tab_url is not "{URL_TO_KEEP}" then
				-- Check if it's the last tab in the window before closing
				if (count of tabs_list) > 1 then
					close current_tab
				else
					-- If it's the last tab, closing it might close the window
					-- Decide if you want to close the window or keep it (e.g., open a new tab first)
					-- This version closes the last tab (and potentially the window)
					 close current_tab 
				end if
			end if
		end repeat
	end repeat
end tell
'''

# Check if the OS is macOS ('Darwin') before running
if platform.system() == 'Darwin':
    print(f"Running on macOS. Attempting to close Chrome tabs except '{URL_TO_KEEP}'...")
    run_applescript(applescript_code)
else:
    print(f"This script uses AppleScript and can only run on macOS (Detected OS: {platform.system()}).") 