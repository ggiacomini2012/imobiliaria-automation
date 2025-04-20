import pygetwindow as gw
import time
import sys

# --- Configuration ---
# Adjust this title if your WhatsApp window has a different name
# Common variations: "WhatsApp", "WhatsApp Business", etc.
# You might need to check the exact title of the running application.
WINDOW_TITLE_SEARCH = "WhatsApp" 
# -------------------

def focus_whatsapp_window():
    """Finds the WhatsApp window and brings it to the foreground."""
    print(f"Searching for window with title containing: '{WINDOW_TITLE_SEARCH}'")
    
    try:
        # Get a list of windows matching the title (case-insensitive search might be better sometimes)
        whatsapp_windows = gw.getWindowsWithTitle(WINDOW_TITLE_SEARCH)
        
        if not whatsapp_windows:
            print(f"Error: No window found with title containing '{WINDOW_TITLE_SEARCH}'. Is WhatsApp running?")
            return False
            
        # If multiple windows are found, activate the first one.
        # You could add logic here to choose differently if needed.
        target_window = whatsapp_windows[0]
        print(f"Found window: '{target_window.title}'")

        # Try to bring the window to the foreground more forcefully
        try:
            print("Attempting to force focus (minimize -> restore -> activate)...")
            
            # Minimize (even if not currently minimized)
            if target_window.isMinimized:
                 print("Window already minimized.")
            else:
                 target_window.minimize()
                 print("Minimized window.")
                 time.sleep(0.2) # Brief pause after minimize

            # Restore
            target_window.restore()
            print("Restored window.")
            time.sleep(0.3) # Brief pause after restore

            # Attempt to activate
            target_window.activate()
            print("Activate command sent.")
            time.sleep(0.5) # Pause for activation

            # Check if it's active
            if target_window.isActive:
                 print("Window confirmed active.")
                 return True
            else:
                 print("Warning: Window was not confirmed active after sequence.")
                 # Attempt one more activation
                 target_window.activate()
                 time.sleep(0.5)
                 if target_window.isActive:
                     print("Window activated on second attempt.")
                     return True
                 else:
                     print("Warning: Failed to confirm active status.")
                     return False # Still treat as failure if not confirmed

        except gw.PyGetWindowException as e:
             # Check if the error is the specific 'success' code 0, still treat as potential success
             # Note: This requires parsing the error message string, which is brittle.
             # Let's keep treating all PyGetWindowExceptions as errors for now for simplicity.
             print(f"Error during focus sequence (PyGetWindowException): {e}")
             return False
        except Exception as e:
             print(f"An unexpected error occurred during focus sequence: {e}")
             return False

    except Exception as e:
        print(f"An unexpected error occurred while searching for the window: {e}")
        return False

if __name__ == "__main__":
    print("--- WhatsApp Focus Script ---")
    if focus_whatsapp_window():
        print("\nScript finished: Attempted to focus WhatsApp.")
        sys.exit(0) # Exit with success code
    else:
        print("\nScript finished: Failed to focus WhatsApp.")
        sys.exit(1) # Exit with error code 