import sys
import os
import subprocess
import platform
import time
import urllib.parse

# --- Import custom modules ---
# Add the parent directory (workspace root) to the Python path
# to allow importing from 'codigo-final'
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

try:
    from contacts_template import cleaned_contacts2
    from message_func import messages_function
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Ensure contacts_template.py and message_func.py exist in codigo-final/" 
          "and the script is run from the project root or adjust sys.path.")
    sys.exit(1)

def open_whatsapp_uri(uri):
    """Opens the WhatsApp URI using the appropriate OS command."""
    os_name = platform.system()
    success = False
    print(f"Attempting to open: {uri[:100]}..." ) # Log URI start
    try:
        if os_name == 'Windows':
            os.startfile(uri)
            success = True
            print("Windows: Triggered os.startfile.")
        elif os_name == 'Darwin': # macOS
            subprocess.run(['open', uri], check=True)
            success = True
            print("macOS: Triggered 'open' command.")
        elif os_name == 'Linux':
            subprocess.run(['xdg-open', uri], check=True)
            success = True
            print("Linux: Triggered 'xdg-open' command.")
        else:
            print(f"Unsupported OS ({os_name}) for direct URI opening.")

    except FileNotFoundError:
        print(f"Error: Command required for opening URI not found (start/open/xdg-open).")
    except subprocess.CalledProcessError as e:
         print(f"Error running command to open URI: {e}")
    except Exception as e:
        print(f"Error opening WhatsApp URI: {e}")

    return success

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python codigo-final/bulk_sender.py \"Your message template with [nome] placeholder\"")
        sys.exit(1)

    message_template = sys.argv[1]
    # Argument 2 could be image flag in the future
    # include_image = sys.argv[2].lower() == 'true' if len(sys.argv) > 2 else False

    print(f"Starting bulk sending process...")
    print(f"Message template: \"{message_template}\"")
    # print(f"Include image: {include_image}") # Placeholder for future

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

        # Format the message using the imported function
        try:
            # Assuming messages_function replaces '[nome]' with public_name
            formatted_message = messages_function(message_template, public_name)
            print(f"Formatted Message: {formatted_message}")
        except Exception as e:
            print(f"Error formatting message for {public_name}: {e}")
            fail_count += 1
            continue

        # URL-encode the message for the URI
        encoded_message = urllib.parse.quote(formatted_message)

        # Construct the WhatsApp URI
        # Note: Image sending via URI is unreliable/not standard
        whatsapp_uri = f"whatsapp://send?phone={phone_number}&text={encoded_message}"

        # Attempt to open the URI
        if open_whatsapp_uri(whatsapp_uri):
            success_count += 1
        else:
            fail_count += 1

        # Pause briefly between contacts
        time.sleep(1.5) # Wait 1.5 seconds before the next one

    print("\n--- Bulk Sending Process Finished ---")
    print(f"Successfully triggered: {success_count}")
    print(f"Failed/Skipped: {fail_count}") 