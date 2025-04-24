import sys
import os
import subprocess
import platform
import time
import urllib.parse
import pyautogui
import pyperclip
import logging
from PIL import Image

print("\n=== EXECUTANDO: codigo-final/bulk_sender_mac.py ===\n")

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Import custom modules ---
# Add the parent directory (workspace root) to the Python path
# to allow importing from 'codigo-final'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir) # This should be the project root
sys.path.append(parent_dir)
# Define path to the focus script (assuming it's in the project root)
focus_script_path = os.path.join(parent_dir, 'focus_whatsapp.py')
# Removidas as referências a scripts de imagem

# Import macOS image utilities
try:
    from macos_image_utils import (
        copy_image_macos_reliable,
        verify_clipboard_image,
        monitor_clipboard_changes
    )
except ImportError as e:
    logging.error(f"Failed to import macOS image utilities: {e}")
    sys.exit(1)

# --- Log File Setup ---
log_file_path = os.path.join(current_dir, 'sent_log.txt')

def load_sent_numbers(filepath):
    """Loads sent phone numbers from the log file."""
    sent = set()
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r') as f:
                for line in f:
                    sent.add(line.strip())
            print(f"Loaded {len(sent)} previously sent numbers from {filepath}")
        except Exception as e:
            print(f"Warning: Could not read log file {filepath}: {e}")
    else:
        print(f"Log file {filepath} not found. Starting fresh.")
    return sent

def log_sent_number(filepath, number):
    """Appends a sent phone number to the log file."""
    try:
        with open(filepath, 'a') as f:
            f.write(number + '\n')
    except Exception as e:
        print(f"Warning: Could not write to log file {filepath}: {e}")

def handle_image_sending(image_path, phone_number, message_text):
    """Handle the process of sending an image on macOS."""
    if not image_path or not os.path.exists(image_path):
        logging.error(f"Image path is invalid or file does not exist: {image_path}")
        return False

    try:
        # Copy image to clipboard
        if not copy_image_macos_reliable(image_path):
            logging.error("Failed to copy image to clipboard")
            return False

        # Open WhatsApp with the contact (without message, we'll type it after image)
        encoded_message = urllib.parse.quote("")
        whatsapp_uri = f"whatsapp://send?phone={phone_number}&text={encoded_message}"
        
        if not open_uri(whatsapp_uri):
            logging.error("Failed to open WhatsApp URI")
            return False

        # Wait for WhatsApp to open - increased from 3.0 to 5.0
        time.sleep(2.0)

        # Paste the image (try multiple times)
        max_paste_attempts = 3
        for attempt in range(max_paste_attempts):
            try:
                # dont follow if the image is not in the clipboard, loop and wait 1 second until the image is in the clipboard
                for i in range(10):
                    if verify_clipboard_image():
                        break
                    time.sleep(1)

                time.sleep(10.0)
                # Paste image
                logging.info("Pasting image...")
                pyautogui.hotkey('command', 'v')
                time.sleep(5.0)  # Wait for image to be pasted
                
                # Clear clipboard after image paste
                pyperclip.copy('')  # Clear clipboard
                time.sleep(0.2)  # Small wait to ensure clipboard is cleared
                
                # Type the message
                logging.info("Typing message...")
                pyperclip.copy(message_text)
                time.sleep(0.2)
                pyautogui.hotkey('command', 'v')
                time.sleep(0.5)
                
                # Press Enter to send
                logging.info("Sending message...")
                pyautogui.press('enter')
                time.sleep(2.0)  # Increased from 1.0 to 2.0
                
                # Consider it successful if we got here
                logging.info(f"Image and message sent successfully on attempt {attempt + 1}")
                return True
                
            except Exception as e:
                logging.warning(f"Send attempt {attempt + 1} failed: {e}")
                time.sleep(2.0)  # Increased from 1.0 to 2.0 - wait before next attempt
                
        logging.error("All send attempts failed")
        return False
        
    except Exception as e:
        logging.error(f"Error during image sending: {e}")
        return False

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

try:
    from contacts import cleaned_contacts
    from contacts_template import test_contacts

    # final_contacts = cleaned_contacts
    final_contacts = test_contacts

    from message_func import messages_function
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Ensure contacts_template.py and message_func.py exist in codigo-final/"
          "and the script is run from the project root or adjust sys.path.")
    sys.exit(1)

if __name__ == "__main__":
    # --- Argument Parsing ---
    if len(sys.argv) < 2:
        print("Usage: python codigo-final/bulk_sender.py \"Message Template\" [image_path]")
        sys.exit(1)

    message_template = sys.argv[1]
    image_path = sys.argv[2] if len(sys.argv) > 2 else None

    print(f"Starting bulk process...")
    print(f"Message template: \"{message_template}\"")
    if image_path:
        print(f"Image path: \"{image_path}\"")

    # --- Load Sent Numbers ---
    sent_numbers = load_sent_numbers(log_file_path)
    # -------------------------

    if not final_contacts:
        print("No contacts found in cleaned_contacts list. Exiting.")
        sys.exit(0)

    print(f"Found {len(final_contacts)} contacts.")
    success_count = 0
    fail_count = 0
    skipped_count = 0 # Counter for already sent numbers

    for i, contact in enumerate(final_contacts):
        print(f"\n--- Processing contact {i+1}/{len(final_contacts)} ---")
        phone_number = contact.get('phone_number')
        public_name = contact.get('public_name')

        if not phone_number or not public_name:
            print(f"Skipping contact due to missing phone_number or public_name: {contact}")
            fail_count += 1
            continue

        # --- Check if already sent ---
        if phone_number in sent_numbers:
            print(f"Skipping {public_name} ({phone_number}) - already in log file.")
            skipped_count += 1
            continue
        # ---------------------------

        print(f"Name: {public_name}, Number: {phone_number}")

        # Format the message/caption first
        try:
            formatted_message = messages_function(public_name, message_template)
        except Exception as e:
            print(f"Error formatting message for {public_name}: {e}")
            fail_count += 1
            continue

        # Handle image sending if image path is provided
        if image_path:
            print("Attempting to send image with message...")
            if handle_image_sending(image_path, phone_number, formatted_message):
                print("Image and message sent successfully")
                # --- Log successful send ---
                log_sent_number(log_file_path, phone_number)
                sent_numbers.add(phone_number) # Update in-memory set
                success_count += 1
                # --------------------------
            else:
                print("Failed to send image and message")
                fail_count += 1
        else:
            # --- Enviar Mensagem Somente Texto ---
            print("Attempting to send text only (macOS)...")
            encoded_message = urllib.parse.quote(formatted_message)
            whatsapp_uri = f"whatsapp://send?phone={phone_number}&text={encoded_message}"

            if open_uri(whatsapp_uri):
                # Wait for WhatsApp to open and potentially load the chat
                wait_after_uri_open_seconds = 5.0 # Adjust if needed
                print(f"Waiting {wait_after_uri_open_seconds} seconds for WhatsApp to open...")
                time.sleep(wait_after_uri_open_seconds)

                # Attempt to press Enter multiple times for reliability
                enter_attempts = 3
                enter_interval_seconds = 0.5 # Adjust if needed
                send_success = False
                print(f"Attempting to press Enter {enter_attempts} times...")
                for attempt in range(enter_attempts):
                    try:
                        print(f"  Enter attempt {attempt + 1}/{enter_attempts}...")
                        pyautogui.press('enter')
                        print("  Enter key pressed.")
                        send_success = True # Assume success if pyautogui doesn't raise an error
                        # No need to break here, let all attempts run unless failsafe triggers
                    except pyautogui.FailSafeException:
                         print("FAILSAFE TRIGGERED (moved mouse to corner). Stopping.")
                         fail_count += 1
                         send_success = False # Ensure failure is recorded
                         break # Exit the attempt loop
                    except Exception as auto_e:
                        print(f"  Error pressing Enter on attempt {attempt + 1}: {auto_e}")
                        send_success = False # Mark as failed for this attempt

                    if attempt < enter_attempts - 1: # Don't sleep after the last attempt
                         time.sleep(enter_interval_seconds)

                if send_success:
                     print("Successfully sent Enter command(s).")
                     # --- Log successful send ---
                     log_sent_number(log_file_path, phone_number)
                     sent_numbers.add(phone_number) # Update in-memory set
                     success_count += 1
                     # --------------------------
                else:
                     print("Failed to reliably send Enter command.")
                     fail_count += 1

            else: # open_uri failed
                print("Failed to open WhatsApp URI.")
                fail_count += 1
            # -------------------------------------

        # Pause between contacts
        print("\nPausing before next contact...")
        time.sleep(5) # Wait 5 seconds before the next one

    print("\n--- Bulk Sending Process Finished ---")
    print(f"Successfully triggered/sent: {success_count}")
    print(f"Already sent (skipped): {skipped_count}") # Added skipped count
    print(f"Failed/Skipped due to errors: {fail_count}") # Clarified failure reason 