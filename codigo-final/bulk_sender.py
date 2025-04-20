import sys
import os
import subprocess
import platform
import time
import urllib.parse
import pyautogui
import pygetwindow as gw

print("\n=== EXECUTANDO: codigo-final/bulk_sender.py ===\n")

# --- Import custom modules ---
# Add the parent directory (workspace root) to the Python path
# to allow importing from 'codigo-final'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) # This should be the project root
sys.path.append(parent_dir)
# Define path to the focus script (assuming it's in the project root)
focus_script_path = os.path.join(parent_dir, 'focus_whatsapp.py')
# Define path to the new image sending script
send_image_gui_script_path = os.path.join(parent_dir, 'send_image_gui.py')
# Define path to the paste image only script
paste_script_path = os.path.join(parent_dir, 'paste_image_only.py')

try:
    from contacts_template import cleaned_contacts2
    from message_func import messages_function
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Ensure contacts_template.py and message_func.py exist in codigo-final/" 
          "and the script is run from the project root or adjust sys.path.")
    sys.exit(1)

def open_uri(uri):
    """Opens the WhatsApp URI using the appropriate OS command."""
    os_name = platform.system()
    print(f"Attempting to open URI: {uri[:100]}...")
    try:
        if os_name == 'Windows':
            os.startfile(uri)
        elif os_name == 'Darwin': # macOS
            subprocess.run(['open', uri], check=True)
        elif os_name == 'Linux':
            subprocess.run(['xdg-open', uri], check=True)
        else:
            print(f"Unsupported OS ({os_name}) for direct URI opening.")
            return False
        print("URI open command triggered.")
        return True
    except Exception as e:
        print(f"Error opening URI: {e}")
        return False

def wait_for_whatsapp_active(max_wait=4):
    print(f"Waiting up to {max_wait}s for WhatsApp window to become active...")
    start_time = time.time()
    while time.time() - start_time < max_wait:
        try:
            active_window = gw.getActiveWindow()
            if active_window and active_window.title and "WhatsApp" in active_window.title:
                print("WhatsApp window is active.")
                return True
        except Exception as e:
             pass 
        time.sleep(0.5)
    print("Warning: WhatsApp window did not become active.")
    return False

if __name__ == "__main__":
    # --- Argument Parsing --- 
    if len(sys.argv) < 2:
        print("Usage: python codigo-final/bulk_sender.py \"Message Template\" [Optional Image Path]")
        sys.exit(1)

    message_template = sys.argv[1]
    image_path = None
    if len(sys.argv) > 2:
        image_path = sys.argv[2]
        print(f"Image path provided: {image_path}")
    # ------------------------

    print(f"Starting bulk process...")
    print(f"Message template: \"{message_template}\"")

    if not cleaned_contacts2:
        print("No contacts found in cleaned_contacts2 list. Exiting.")
        sys.exit(0)

    print(f"Found {len(cleaned_contacts2)} contacts.")
    success_count = 0
    fail_count = 0

    for i, contact in enumerate(cleaned_contacts2):
        print(f"\n--- Processing contact {i+1}/{len(cleaned_contacts2)} ---")
        phone_number = contact.get('phone_number')
        public_name = contact.get('public_name')

        if not phone_number or not public_name:
            print(f"Skipping contact due to missing phone_number or public_name: {contact}")
            fail_count += 1
            continue

        print(f"Name: {public_name}, Number: {phone_number}")

        # Format the message/caption first
        try:
            formatted_message = messages_function(public_name, message_template)
        except Exception as e:
            print(f"Error formatting message for {public_name}: {e}")
            fail_count += 1
            continue

        # --- Decide sending method ---
        if image_path:
            # --- Send with Image (via GUI Script) ---
            print(f"Attempting to send image via GUI script...")
            print(f"  To: {phone_number}")
            print(f"  Image: {image_path}")
            print(f"  Caption: {formatted_message}")
            try:
                gui_result = subprocess.run(
                    [sys.executable, send_image_gui_script_path, phone_number, image_path, formatted_message],
                    capture_output=True, text=True, check=False, encoding='utf-8', errors='replace',
                    cwd=parent_dir
                )
                print(f"GUI Script Output:\n--- stdout ---\n{gui_result.stdout}\n--- stderr ---\n{gui_result.stderr}")
                if gui_result.returncode == 0:
                    print("GUI script reported success.")
                    success_count += 1
                else:
                    print(f"GUI script reported failure (exit code {gui_result.returncode}).")
                    fail_count += 1
            except FileNotFoundError:
                 print(f"Error: send_image_gui.py not found at {send_image_gui_script_path}")
                 fail_count += 1
            except Exception as gui_e:
                print(f"Error running GUI script: {gui_e}")
                fail_count += 1
            # -----------------------------------------
        else:
            # --- Send Text Only (Current Method) ---
            print("Attempting to send text only...")
            # URL-encode the message for the URI
            encoded_message = urllib.parse.quote(formatted_message)
            # Construct the WhatsApp URI
            whatsapp_uri = f"whatsapp://send?phone={phone_number}&text={encoded_message}"

            # Attempt to open the URI
            if open_uri(whatsapp_uri):
                paste_failed = False # Flag para rastrear falha no paste
                # --- Focus Script (Windows Only) ---
                if platform.system() == 'Windows':
                    print("--- Running Focus Script (Windows Only) ---")
                    try:
                        focus_result = subprocess.run(
                            [sys.executable, focus_script_path],
                            capture_output=True, text=True, check=False, encoding='utf-8', errors='replace',
                            cwd=parent_dir
                        )
                        print(f"Focus Script Output:\n--- stdout ---\n{focus_result.stdout}\n--- stderr ---\n{focus_result.stderr}")
                        if focus_result.returncode == 0:
                            print("Focus script executed successfully.")
                        else:
                            print(f"Warning: Focus script failed with exit code {focus_result.returncode}.")
                    except Exception as focus_e:
                        print(f"Error executing focus script: {focus_e}")
                    print("--- End Focus Script ---")
                else:
                    print("Skipping focus script execution (Not on Windows).")
                # --- End Focus Script Section ---
                
                # # --- Wait for WhatsApp window to become active ---
                # print("Waiting for WhatsApp window to become active (max 5 seconds)...")
                # whatsapp_activated = False
                # max_wait_time = 5 # seconds
                # start_wait_time = time.time()
                
                # while time.time() - start_wait_time < max_wait_time:
                #     try:
                #         active_window = gw.getActiveWindow()
                #         if active_window and active_window.title and "WhatsApp" in active_window.title:
                #             print("WhatsApp window is active!")
                #             whatsapp_activated = True
                #             break
                #         else:
                #             pass
                #     except Exception as gw_e:
                #         print(f"Error checking active window: {gw_e}")
                #     time.sleep(0.5)
                
                # if not whatsapp_activated:
                #      print("Warning: WhatsApp window did not become active within the time limit.")
                # # --- End Wait Section ---
                
                # # Try to press Enter ONLY if WhatsApp window was detected as active
                # if whatsapp_activated:
                #     try:
                #         print("Attempting to press Enter...")
                #         pyautogui.press('enter')
                #         print("Enter key pressed.")
                #         # Contar sucesso APENAS se a colagem não falhou (se tentada)
                #         if not paste_failed:
                #             success_count += 1
                #         else:
                #             print("Enter pressionado, mas colagem da imagem falhou anteriormente.")
                #             fail_count += 1
                #     except Exception as auto_e:
                #         print(f"Error pressing Enter: {auto_e}")
                #         fail_count += 1 
                # else:
                #     print("Skipping Enter press because WhatsApp window was not confirmed active.")
                #     fail_count += 1 
            else: # open_uri failed
                fail_count += 1
            # -------------------------------------

        # Pause between contacts
        print("\nPausing before next contact...")
        time.sleep(2) # Wait 5 seconds before the next one

    print("\n--- Bulk Sending Process Finished ---")
    print(f"Successfully triggered/sent: {success_count}") # Updated message
    print(f"Failed/Skipped: {fail_count}") 