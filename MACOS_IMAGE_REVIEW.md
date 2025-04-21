# macOS Image Pasting Code Review

## Current Implementation Analysis

### 1. Image Copying Methods
Currently, there are three different approaches implemented for copying images to clipboard on macOS:

1. **AppleScript Method** (Current Primary Method)
```python
def copy_image_macos(image_path):
    abs_image_path = os.path.abspath(image_path)
    image_type = "JPEG picture"
    if image_path.lower().endswith(".png"): image_type = "PNG picture"
    elif image_path.lower().endswith(".gif"): image_type = "GIF picture"
    script = f'set the clipboard to (read (POSIX file "{abs_image_path}") as {image_type})'
    result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
```

2. **AppKit Method** (Alternative in to-lixo)
```python
def copy_image_to_clipboard_appkit(image_path):
    from AppKit import NSPasteboard, NSImage
    pasteboard = NSPasteboard.generalPasteboard()
    pasteboard.clearContents()
    nsimage = NSImage.alloc().initWithContentsOfFile_(abs_image_path)
    result = pasteboard.writeObjects_([nsimage])
```

3. **Swift Method** (Alternative in to-lixo)
```python
def copy_with_swift(image_path):
    swift_code = '''
    import Cocoa
    import Foundation
    let imagePath = "{abs_image_path}"
    if let image = NSImage(contentsOfFile: imagePath) {
        let pasteboard = NSPasteboard.general
        pasteboard.clearContents()
        let result = pasteboard.writeObjects([image])
    }
    '''
```

### 2. Issues Identified

1. **Timing Issues**
   - Current wait times might be insufficient:
   ```python
   WAIT_AFTER_OPEN = 7.0      # Might need adjustment
   WAIT_AFTER_PASTE_IMG = 2.0 # Might need adjustment
   ```

2. **Clipboard Reliability**
   - No verification if the image was actually copied to clipboard
   - No fallback mechanism if the first copy attempt fails

3. **Image Format Handling**
   - Limited support for image formats (only JPEG, PNG, GIF explicitly handled)
   - No image format conversion for unsupported formats

4. **Error Handling**
   - Generic error messages that don't help diagnose specific issues
   - No retry mechanism for failed operations

## Recommended Improvements

### 1. Enhanced Image Copy Function
```python
def copy_image_macos_enhanced(image_path: str) -> bool:
    """
    Enhanced image copying function for macOS with better error handling and verification.
    """
    try:
        # 1. Validate image first
        if not validate_image(image_path):
            return False
            
        # 2. Try AppKit method first (most reliable)
        if try_appkit_copy(image_path):
            return True
            
        # 3. Fallback to AppleScript with specific format
        if try_applescript_copy(image_path):
            return True
            
        # 4. Last resort: generic picture type
        return try_applescript_copy_generic(image_path)
        
    except Exception as e:
        logging.error(f"Failed to copy image: {e}")
        return False

def try_appkit_copy(image_path: str) -> bool:
    """Attempt to copy using AppKit (most reliable method)."""
    try:
        from AppKit import NSPasteboard, NSImage
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()
        nsimage = NSImage.alloc().initWithContentsOfFile_(image_path)
        return pasteboard.writeObjects_([nsimage])
    except ImportError:
        return False

def verify_clipboard_image() -> bool:
    """Verify if an image was actually copied to clipboard."""
    try:
        from AppKit import NSPasteboard
        pasteboard = NSPasteboard.generalPasteboard()
        return len(pasteboard.pasteboardItems()) > 0
    except:
        return False
```

### 2. Improved Timing Management
```python
class TimingManager:
    """Manages timing for various operations with dynamic adjustment."""
    
    def __init__(self):
        self.base_times = {
            'after_open': 7.0,
            'after_paste': 2.0,
            'before_send': 1.0
        }
        self.retry_count = 0
        self.max_retries = 3
        
    def wait_and_verify(self, operation: str, verify_func: callable) -> bool:
        """Wait for specified time and verify operation success."""
        wait_time = self.base_times[operation]
        time.sleep(wait_time)
        
        if not verify_func():
            if self.retry_count < self.max_retries:
                self.retry_count += 1
                wait_time *= 1.5  # Increase wait time by 50%
                time.sleep(wait_time)
                return verify_func()
            return False
            
        self.retry_count = 0
        return True
```

### 3. Image Format Handling
```python
def prepare_image_for_clipboard(image_path: str) -> str:
    """
    Prepare image for clipboard by converting to a supported format if necessary.
    Returns path to the prepared image.
    """
    try:
        with Image.open(image_path) as img:
            # Convert to PNG if format is not supported
            if img.format not in ['JPEG', 'PNG', 'GIF']:
                temp_path = f"{image_path}_converted.png"
                img.save(temp_path, 'PNG')
                return temp_path
            return image_path
    except Exception as e:
        logging.error(f"Failed to prepare image: {e}")
        return None
```

### 4. Enhanced Error Recovery
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def send_image_with_retry(phone_number: str, image_path: str) -> bool:
    """
    Send image with retry mechanism and proper error handling.
    """
    try:
        # 1. Prepare image
        prepared_image = prepare_image_for_clipboard(image_path)
        if not prepared_image:
            return False
            
        # 2. Copy to clipboard
        if not copy_image_macos_enhanced(prepared_image):
            return False
            
        # 3. Open WhatsApp
        if not open_whatsapp_with_number(phone_number):
            return False
            
        # 4. Use timing manager for operations
        timing = TimingManager()
        
        # 5. Paste and verify
        pyautogui.hotkey('command', 'v')
        if not timing.wait_and_verify('after_paste', verify_clipboard_image):
            return False
            
        # 6. Send
        pyautogui.press('enter')
        return True
        
    except Exception as e:
        logging.error(f"Failed to send image: {e}")
        raise
```

## Implementation Plan

1. **Phase 1: Core Improvements**
   - Implement enhanced image copy function
   - Add clipboard verification
   - Implement proper error handling

2. **Phase 2: Timing Optimization**
   - Implement TimingManager
   - Add dynamic wait times
   - Add operation verification

3. **Phase 3: Format Support**
   - Add image format conversion
   - Implement format validation
   - Add support for more image types

4. **Phase 4: Testing and Validation**
   - Create test suite for image operations
   - Add logging for debugging
   - Implement monitoring for success rates

## Testing Strategy

1. **Basic Testing**
```python
def test_image_copy():
    """Test basic image copying functionality."""
    test_image = "test.png"
    assert copy_image_macos_enhanced(test_image)
    assert verify_clipboard_image()
```

2. **Format Testing**
```python
def test_format_handling():
    """Test handling of different image formats."""
    formats = ['jpg', 'png', 'gif', 'bmp', 'tiff']
    for fmt in formats:
        test_image = f"test.{fmt}"
        assert prepare_image_for_clipboard(test_image)
```

3. **Integration Testing**
```python
def test_full_send_process():
    """Test the complete image sending process."""
    phone = "1234567890"
    image = "test.png"
    assert send_image_with_retry(phone, image)
```

## Monitoring and Debugging

1. **Add Logging**
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('macos_image.log'),
        logging.StreamHandler()
    ]
)
```

2. **Add Performance Metrics**
```python
def track_operation_timing(operation: str):
    """Track timing of operations for optimization."""
    start_time = time.time()
    yield
    duration = time.time() - start_time
    logging.info(f"{operation} took {duration:.2f} seconds")
```

## Conclusion

The current implementation has several areas that can be improved to make image pasting more reliable on macOS. The main issues are:

1. Lack of proper verification after clipboard operations
2. Insufficient error handling and recovery
3. Basic timing management
4. Limited image format support

The proposed improvements focus on:

1. Multiple copy methods with fallback
2. Proper verification of operations
3. Dynamic timing management
4. Enhanced error handling and recovery
5. Better format support
6. Comprehensive testing and monitoring

Would you like me to start implementing any of these improvements or provide more details about any specific aspect? 