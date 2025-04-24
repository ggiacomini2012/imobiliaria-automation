# macOS Image Sending Process

## User Experience Flow

### 1. Image Selection
- User clicks the "Anexar Imagem" button in the dashboard (`templates/dashboard.html`)
- User selects an image file (supports PNG, JPEG, JPG, GIF)
- User checks the "Incluir Imagem Anexada?" checkbox to confirm image sending

### 2. System Processing
When the user initiates the sending process:

1. **Image Preparation**
   - System verifies the selected image file exists (`bulk_sender_mac.py:handle_image_sending()`)
   - Image is prepared for macOS clipboard compatibility (`macos_image_utils.py:prepare_image_for_macos()`)
   - If the image is too large, it's automatically optimized (`macos_image_utils.py:prepare_image_for_macos()`)

2. **WhatsApp Integration**
   - System opens WhatsApp with the target contact (`bulk_sender_mac.py:open_uri()`)
   - Waits for WhatsApp to fully load (5 seconds)
   - Ensures the chat window is ready for image pasting

3. **Image Transfer**
   - System copies the image to macOS clipboard (`macos_image_utils.py:copy_image_macos_reliable()`)
   - Verifies the image was successfully copied (`macos_image_utils.py:verify_clipboard_image()`)
   - Pastes the image into the WhatsApp chat (Command+V)
   - Waits for the image to be processed by WhatsApp

4. **Message Sending**
   - System sends the image (presses Enter)
   - Waits for confirmation of successful send
   - Logs the successful send in the system (`bulk_sender_mac.py:log_sent_number()`)

### 3. Error Handling
If any step fails, the system:
- Logs the specific error (`logging.error()`)
- Continues with the next contact
- Provides feedback in the dashboard
- Maintains a record of failed attempts

## Technical Details

### Key Files and Functions

#### Frontend Files
- `templates/dashboard.html`: User interface for image selection
- `static/js/script.js`: Handles frontend image selection and form submission

#### Backend Files
1. **Main Processing**
   - `bulk_sender_mac.py`: Main script for handling the sending process
     - `handle_image_sending()`: Orchestrates the image sending process
     - `open_uri()`: Opens WhatsApp with the target contact
     - `log_sent_number()`: Records successful sends

2. **Image Utilities**
   - `macos_image_utils.py`: Handles all macOS-specific image operations
     - `copy_image_macos_reliable()`: Main function for copying images
     - `verify_clipboard_image()`: Verifies clipboard contents
     - `monitor_clipboard_changes()`: Monitors clipboard state
     - `prepare_image_for_macos()`: Prepares images for macOS clipboard
     - `try_appkit_copy()`: Attempts AppKit-based copying
     - `try_applescript_copy()`: Attempts AppleScript-based copying
     - `try_preview_copy()`: Uses Preview.app as a fallback

### Supported Image Formats
- PNG (recommended for best quality)
- JPEG/JPG
- GIF

### System Requirements
- macOS operating system
- WhatsApp Desktop installed
- System accessibility permissions granted
- Sufficient system resources for image processing

### Performance Considerations
- Large images are automatically optimized
- System waits appropriate times between actions
- Clipboard operations are verified
- Multiple retry attempts for reliability

## Troubleshooting

### Common Issues
1. **Image Not Sending**
   - Check if WhatsApp is open
   - Verify system permissions
   - Ensure image format is supported
   - Check image file size

2. **Clipboard Issues**
   - System will automatically retry
   - Multiple copy methods are attempted
   - Clipboard state is verified

3. **WhatsApp Integration**
   - System waits for WhatsApp to be ready
   - Verifies chat window is active
   - Retries if initial attempt fails

### What to Do If...
- **Image is too large**: System will automatically optimize it
- **Send fails**: System will log the error and continue
- **WhatsApp isn't responding**: System will wait and retry
- **Clipboard issues occur**: System will try alternative methods

## Best Practices
1. Use PNG format for best results
2. Keep images under 2000x2000 pixels
3. Ensure WhatsApp is installed and updated
4. Grant necessary system permissions
5. Monitor the dashboard for status updates

## Security Considerations
- Images are processed locally
- No image data is stored permanently
- Clipboard is cleared after sending
- Temporary files are automatically cleaned up 