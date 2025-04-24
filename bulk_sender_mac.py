import os
import sys
import time
import logging
from contacts import load_contacts
from send_image_mac import send_image_to_whatsapp

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_bulk_messages_mac(message_template, image_path=None):
    """
    Send bulk messages on macOS, optionally including an image.
    
    Args:
        message_template (str): Message template with {name} placeholder
        image_path (str, optional): Path to image file to include
    """
    contacts = load_contacts()
    total = len(contacts)
    success_count = 0
    
    logging.info(f"Starting bulk send to {total} contacts")
    if image_path:
        logging.info(f"Including image: {image_path}")
    
    for i, contact in enumerate(contacts, 1):
        name = contact['name']
        number = contact['number']
        
        # Format message with contact name
        message = message_template.format(name=name)
        
        logging.info(f"Processing contact {i}/{total}: {name} ({number})")
        
        try:
            if image_path:
                # Send image with caption
                success = send_image_to_whatsapp(image_path, number, message)
            else:
                # Send text message only
                whatsapp_url = f"whatsapp://send?phone={number}&text={message}"
                subprocess.run(['open', whatsapp_url])
                time.sleep(2.0)  # Wait for WhatsApp to open
                # Press Enter to send
                subprocess.run(['osascript', '-e', 
                    'tell application "System Events" to keystroke return'])
                success = True
                
            if success:
                success_count += 1
                logging.info(f"Successfully sent to {name}")
            else:
                logging.error(f"Failed to send to {name}")
                
            # Add delay between contacts
            time.sleep(3.0)
            
        except Exception as e:
            logging.error(f"Error processing {name}: {e}", exc_info=True)
    
    logging.info(f"Bulk send completed. Successfully sent to {success_count}/{total} contacts")
    return success_count == total

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bulk_sender_mac.py <message_template> [image_path]")
        sys.exit(1)
        
    message_template = sys.argv[1]
    image_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = send_bulk_messages_mac(message_template, image_path)
    sys.exit(0 if success else 1) 