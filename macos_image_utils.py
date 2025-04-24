import logging
import time
import subprocess
import os
from PIL import Image  # Assuming Pillow might be needed later for format conversion/verification

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from AppKit import NSPasteboard, NSPasteboardTypePNG, NSImage, NSArray
except ImportError:
    logging.warning("AppKit not found. Some macOS-specific clipboard operations will not be available.")
    NSPasteboard = None
    NSPasteboardTypePNG = None
    NSImage = None
    NSArray = None

def verify_clipboard_image():
    """
    Verify that an image is actually in the clipboard using AppKit.
    """
    if not NSPasteboard:
        logging.error("AppKit is required for clipboard verification.")
        return False
        
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        # Check if there are image types available
        image_types = NSArray.arrayWithArray_([NSPasteboardTypePNG]) # Add other types like TIFF if needed
        
        if pasteboard.canReadObjectForClasses_options_([NSImage], None):
             # More robust check: Try to actually get image data
            data = pasteboard.dataForType_(NSPasteboardTypePNG)
            if data:
                 logging.info("Verified PNG image data in clipboard.")
                 return True
            else:
                 # Fallback check for any image type if PNG fails
                 items = pasteboard.pasteboardItems()
                 if items:
                     for item in items:
                         if any(uti.startswith("public.image") for uti in item.types()):
                             logging.info(f"Verified generic image type in clipboard ({item.types()}).")
                             return True
                 logging.warning("Clipboard has image class but failed to get PNG data and no generic image found.")
                 return False
        else:
            logging.info("No image object found in clipboard.")
            return False
            
    except Exception as e:
        logging.error(f"Error verifying clipboard image: {e}", exc_info=True)
        return False

def try_appkit_copy(image_path):
    """
    Attempts to copy an image to the clipboard using AppKit.
    Returns True if successful, False otherwise.
    """
    if not NSPasteboard or not NSImage:
        logging.error("AppKit is required for AppKit copy method.")
        return False
        
    if not os.path.exists(image_path):
        logging.error(f"Image path does not exist: {image_path}")
        return False

    try:
        image = NSImage.alloc().initWithContentsOfFile_(image_path)
        if not image:
            logging.error(f"Failed to load image using NSImage: {image_path}")
            return False

        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        
        # Prepare the image data for the pasteboard
        imageData = image.TIFFRepresentation() # Using TIFF representation often works well
        if not imageData:
             logging.error(f"Failed to get TIFF representation for image: {image_path}")
             # Try PNG representation as a fallback
             from AppKit import NSBitmapImageRep, NSPNGFileType
             bitmapRep = NSBitmapImageRep.imageRepWithData_(image.TIFFRepresentation())
             imageData = bitmapRep.representationUsingType_properties_(NSPNGFileType, None)
             if not imageData:
                 logging.error(f"Failed to get PNG representation for image: {image_path}")
                 return False


        # Write image data to the pasteboard
        success = pasteboard.setData_forType_(imageData, NSPasteboardTypePNG) # Prefer PNG type on pasteboard

        if success:
            logging.info(f"Successfully copied image to clipboard using AppKit: {image_path}")
            # Short delay to allow clipboard to update
            time.sleep(0.2) 
            return True
        else:
            logging.error(f"Failed to set clipboard data using AppKit for: {image_path}")
            return False
            
    except Exception as e:
        logging.error(f"Error during AppKit copy: {e}", exc_info=True)
        return False

def try_applescript_copy(image_path):
    """
    Attempts to copy an image to the clipboard using AppleScript with specific format.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(image_path):
        logging.error(f"Image path does not exist: {image_path}")
        return False

    try:
        # AppleScript to copy image with specific format handling
        script = f'''
        tell application "System Events"
            set theImage to POSIX file "{image_path}"
            set the clipboard to theImage
        end tell
        '''
        
        # Run the AppleScript
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully copied image using AppleScript: {image_path}")
            # Short delay to allow clipboard to update
            time.sleep(0.3)
            return True
        else:
            logging.error(f"AppleScript copy failed: {result.stderr}")
            return False
            
    except Exception as e:
        logging.error(f"Error during AppleScript copy: {e}", exc_info=True)
        return False

def try_applescript_copy_generic(image_path):
    """
    Attempts to copy an image to the clipboard using AppleScript with generic picture type.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(image_path):
        logging.error(f"Image path does not exist: {image_path}")
        return False

    try:
        # AppleScript to copy image with generic picture type
        script = f'''
        tell application "System Events"
            set theImage to POSIX file "{image_path}"
            set the clipboard to (read theImage as picture)
        end tell
        '''
        
        # Run the AppleScript
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully copied image using generic AppleScript: {image_path}")
            # Short delay to allow clipboard to update
            time.sleep(0.3)
            return True
        else:
            logging.error(f"Generic AppleScript copy failed: {result.stderr}")
            return False
            
    except Exception as e:
        logging.error(f"Error during generic AppleScript copy: {e}", exc_info=True)
        return False

def try_preview_copy(image_path):
    """
    Attempts to copy an image to the clipboard using Preview.app automation.
    This is the last resort method as it's slower but often more reliable.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(image_path):
        logging.error(f"Image path does not exist: {image_path}")
        return False

    try:
        # First, ensure Preview is not already running with our image
        cleanup_script = f'''
        tell application "Preview"
            set docs to documents
            repeat with doc in docs
                if path of doc is "{image_path}" then
                    close doc
                end if
            end repeat
        end tell
        '''
        subprocess.run(['osascript', '-e', cleanup_script], 
                      capture_output=True, 
                      text=True)
        time.sleep(0.5)  # Wait for cleanup

        # Open the image in Preview
        open_script = f'''
        tell application "Preview"
            open POSIX file "{image_path}"
            activate
        end tell
        '''
        result = subprocess.run(['osascript', '-e', open_script], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode != 0:
            logging.error(f"Failed to open image in Preview: {result.stderr}")
            return False

        time.sleep(1.0)  # Wait for Preview to open and load image

        # Select all and copy
        copy_script = '''
        tell application "System Events"
            tell process "Preview"
                keystroke "a" using command down
                delay 0.5
                keystroke "c" using command down
                delay 0.5
                keystroke "w" using command down
            end tell
        end tell
        '''
        result = subprocess.run(['osascript', '-e', copy_script], 
                              capture_output=True, 
                              text=True)
        
        if result.returncode == 0:
            logging.info(f"Successfully copied image using Preview.app: {image_path}")
            time.sleep(0.5)  # Wait for clipboard to update
            return True
        else:
            logging.error(f"Preview.app copy failed: {result.stderr}")
            return False
            
    except Exception as e:
        logging.error(f"Error during Preview.app copy: {e}", exc_info=True)
        return False

def prepare_image_for_macos(image_path):
    """
    Convert image to a format that works reliably on MacOS clipboard.
    Returns the path to the prepared image (original or converted).
    """
    try:
        with Image.open(image_path) as img:
            # Check if image is too large
            if img.size[0] > 2000 or img.size[1] > 2000:
                logging.info("Image is too large, creating optimized version")
                # Create temporary optimized version
                temp_path = f"/tmp/optimized_{os.path.basename(image_path)}"
                img.thumbnail((2000, 2000), Image.LANCZOS)
                img.save(temp_path, 'PNG', optimize=True)
                return temp_path

            # Convert to PNG if not already PNG
            if img.format != 'PNG':
                logging.info(f"Converting {img.format} to PNG for better clipboard compatibility")
                temp_path = f"/tmp/converted_{os.path.basename(image_path)}.png"
                img.save(temp_path, 'PNG', optimize=True)
                return temp_path

            return image_path
    except Exception as e:
        logging.error(f"Failed to prepare image: {e}", exc_info=True)
        return image_path  # Return original path if conversion fails

def wait_for_clipboard_ready(max_attempts=5, base_wait=0.5):
    """
    Wait for clipboard to be ready with exponential backoff.
    Returns True if clipboard is ready, False if timeout.
    """
    for attempt in range(max_attempts):
        if verify_clipboard_image():
            return True
            
        wait_time = base_wait * (2 ** attempt)  # Exponential backoff
        logging.info(f"Clipboard not ready, waiting {wait_time:.2f}s (attempt {attempt + 1}/{max_attempts})")
        time.sleep(wait_time)
        
    logging.warning("Clipboard not ready after maximum attempts")
    return False

def check_accessibility_permissions():
    """
    Check if the script has the necessary accessibility permissions for automation.
    Returns True if permissions are granted, False otherwise.
    """
    try:
        script = '''
        tell application "System Events"
            return UI elements enabled
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, 
                              text=True)
        enabled = "true" in result.stdout.lower()
        
        if not enabled:
            logging.warning("Accessibility permissions are not enabled. Some features may not work.")
            logging.warning("Please enable accessibility permissions in System Preferences > Security & Privacy > Privacy > Accessibility")
        return enabled
    except Exception as e:
        logging.error(f"Failed to check accessibility permissions: {e}")
        return False

def is_retina_display():
    """
    Check if the system is running on a Retina display.
    Returns True if Retina display is detected, False otherwise.
    """
    try:
        script = '''
        tell application "System Events"
            tell process "SystemUIServer"
                return (get value of attribute "AXScaleFactor" of window 1) > 1
            end tell
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], 
                              capture_output=True, 
                              text=True)
        return "true" in result.stdout.lower()
    except Exception as e:
        logging.warning(f"Could not determine if display is Retina: {e}")
        return False

def prepare_for_retina(image_path):
    """
    Prepare image for Retina display by scaling if needed.
    Returns the path to the prepared image.
    """
    if not is_retina_display():
        return image_path
        
    try:
        with Image.open(image_path) as img:
            # Scale image for Retina
            width, height = img.size
            if width <= 1000 and height <= 1000:  # Only scale smaller images
                logging.info("Scaling image for Retina display")
                img = img.resize((width*2, height*2), Image.LANCZOS)
                temp_path = f"/tmp/retina_{os.path.basename(image_path)}"
                img.save(temp_path, 'PNG', optimize=True)
                return temp_path
            return image_path
    except Exception as e:
        logging.error(f"Failed to prepare image for Retina: {e}")
        return image_path

def retry_with_backoff(func, *args, max_retries=3, base_delay=1.0, **kwargs):
    """
    Retry a function with exponential backoff.
    Returns the function's result or raises the last exception.
    """
    for attempt in range(max_retries):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            if attempt == max_retries - 1:  # Last attempt
                raise
            wait_time = base_delay * (2 ** attempt)
            logging.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time:.2f}s...")
            time.sleep(wait_time)

def get_image_info(image_path):
    """
    Get detailed information about an image file.
    Returns a dictionary with image properties or None if failed.
    """
    try:
        with Image.open(image_path) as img:
            return {
                'format': img.format,
                'size': img.size,
                'mode': img.mode,
                'info': img.info,
                'filename': os.path.basename(image_path),
                'path': image_path,
                'file_size': os.path.getsize(image_path)
            }
    except Exception as e:
        logging.error(f"Failed to get image info: {e}")
        return None

def cleanup_temporary_files():
    """
    Clean up any temporary files created by the script.
    Returns the number of files cleaned up.
    """
    temp_dir = "/tmp"
    cleaned = 0
    try:
        for filename in os.listdir(temp_dir):
            if filename.startswith(("optimized_", "converted_", "retina_")):
                try:
                    os.remove(os.path.join(temp_dir, filename))
                    cleaned += 1
                except Exception as e:
                    logging.warning(f"Failed to remove temporary file {filename}: {e}")
        return cleaned
    except Exception as e:
        logging.error(f"Failed to clean up temporary files: {e}")
        return cleaned

def monitor_clipboard_changes(timeout=5.0):
    """
    Monitor clipboard for changes to detect when image is copied.
    Returns True if clipboard changed within timeout, False otherwise.
    """
    if not NSPasteboard:
        logging.error("AppKit is required for clipboard monitoring")
        return False
        
    try:
        pasteboard = NSPasteboard.generalPasteboard()
        change_count = pasteboard.changeCount()
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            if pasteboard.changeCount() != change_count:
                logging.info("Clipboard changed")
                return True
            time.sleep(0.1)
            
        logging.warning(f"No clipboard changes detected within {timeout}s")
        return False
    except Exception as e:
        logging.error(f"Error monitoring clipboard: {e}")
        return False

def copy_image_macos_reliable(image_path, max_retries=2, cleanup=True):
    """
    Try multiple methods to copy image to clipboard, with verification.
    Implements all available methods in order of reliability.
    
    Args:
        image_path (str): Path to the image file
        max_retries (int): Maximum number of retries for each method
        cleanup (bool): Whether to clean up temporary files after operation
        
    Returns:
        bool: True if copy was successful, False otherwise
    """
    # Check if file exists and is readable
    if not os.path.exists(image_path):
        logging.error(f"Image file does not exist: {image_path}")
        return False
    if not os.access(image_path, os.R_OK):
        logging.error(f"Image file is not readable: {image_path}")
        return False

    # Get image info for logging
    image_info = get_image_info(image_path)
    if image_info:
        logging.info(f"Image info: {image_info}")
    
    # Check accessibility permissions first
    if not check_accessibility_permissions():
        logging.warning("Continuing without accessibility permissions - some methods may fail")
    
    logging.info(f"Attempting reliable copy for: {image_path}")
    
    # Prepare the image for MacOS clipboard
    prepared_path = prepare_image_for_macos(image_path)
    if prepared_path != image_path:
        logging.info(f"Using prepared image: {prepared_path}")
    
    # Prepare for Retina display if needed
    retina_path = prepare_for_retina(prepared_path)
    if retina_path != prepared_path:
        logging.info(f"Using Retina-optimized image: {retina_path}")
        prepared_path = retina_path
    
    # Define copy methods in order of reliability
    copy_methods = [
        (try_appkit_copy, "AppKit"),
        (try_applescript_copy, "AppleScript"),
        (try_applescript_copy_generic, "Generic AppleScript"),
        (try_preview_copy, "Preview.app")
    ]
    
    # Try each method with retries
    for copy_func, method_name in copy_methods:
        logging.info(f"Trying {method_name} copy method...")
        
        try:
            # Retry the copy operation
            if retry_with_backoff(copy_func, prepared_path, max_retries=max_retries):
                # Wait for clipboard with longer timeout for Preview
                wait_timeout = 7 if method_name == "Preview.app" else 5
                if wait_for_clipboard_ready(max_attempts=wait_timeout):
                    logging.info(f"{method_name} copy successful and verified.")
                    if cleanup:
                        cleanup_temporary_files()
                    return True
                else:
                    logging.warning(f"{method_name} copy attempt made, but verification failed.")
        except Exception as e:
            logging.error(f"Error during {method_name} copy: {e}")

    # Clean up temporary files if they were created
    if cleanup:
        cleaned = cleanup_temporary_files()
        if cleaned > 0:
            logging.info(f"Cleaned up {cleaned} temporary files")

    logging.error(f"All methods failed to copy image reliably: {image_path}")
    return False

# Example usage with improved documentation and error handling
if __name__ == '__main__':
    """
    Example usage of the image copying functionality.
    
    This script demonstrates how to use the copy_image_macos_reliable function
    with a test image. It will:
    1. Create a test image if it doesn't exist
    2. Try to copy it to the clipboard using all available methods
    3. Log the results of the operation
    4. Clean up any temporary files
    
    To test with your own image, simply replace test_image_path with your image path.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description='Copy an image to the MacOS clipboard reliably')
    parser.add_argument('image_path', nargs='?', default='test_image.png',
                       help='Path to the image file (default: test_image.png)')
    parser.add_argument('--retries', type=int, default=2,
                       help='Maximum number of retries for each method (default: 2)')
    parser.add_argument('--no-cleanup', action='store_true',
                       help='Do not clean up temporary files')
    args = parser.parse_args()
    
    test_image_path = args.image_path
    if not os.path.exists(test_image_path):
        try:
            from PIL import Image
            img = Image.new('RGB', (60, 30), color = 'red')
            img.save(test_image_path)
            logging.info(f"Created dummy test image: {test_image_path}")
        except ImportError:
            logging.error("Pillow is not installed. Cannot create a dummy test image. Please create 'test_image.png' manually.")
        except Exception as e:
            logging.error(f"Failed to create dummy test image: {e}")

    if os.path.exists(test_image_path):
        if copy_image_macos_reliable(test_image_path, 
                                   max_retries=args.retries,
                                   cleanup=not args.no_cleanup):
            print(f"Successfully copied {test_image_path} to clipboard.")
            print("You can now paste the image into any application.")
        else:
            print(f"Failed to copy {test_image_path} to clipboard.")
            print("Check the logs for detailed error information.")
    else:
        print(f"Test image '{test_image_path}' not found. Skipping example usage.") 