# macOS Image Sending Process Flow

## Overview
This document explains the step-by-step process that occurs when sending an image on macOS using the WhatsApp automation system.

## Process Flow

1. **Image Selection**
   - User selects an image from the file system
   - Image is temporarily stored in the system clipboard

2. **WhatsApp Window Activation**
   - System locates the WhatsApp window using AppleScript
   - WhatsApp window is brought to focus
   - System waits for WhatsApp to be fully active

3. **Contact Selection**
   - System navigates to the contact search field
   - Contact name is entered
   - System waits for contact to be selected

4. **Image Attachment Process**
   - System clicks the attachment button (paperclip icon)
   - System selects "Photos" from the attachment menu
   - System waits for the Photos app to open

5. **Image Selection in Photos**
   - System navigates to the "Recents" album
   - System selects the most recent image (the one we copied)
   - System clicks the "Choose" button

6. **Image Processing**
   - WhatsApp processes the selected image
   - System waits for the image preview to appear

7. **Message Sending**
   - System clicks the send button
   - System waits for the image to be sent
   - Confirmation is received when the image is successfully sent

## Technical Details

### Key Components Used
- `appscript`: For AppleScript integration and window management
- `pyobjc-framework-Quartz`: For clipboard operations
- `pyobjc-framework-Cocoa`: For system integration
- `pyobjc-framework-ScriptingBridge`: For application automation

### Error Handling
- Timeout checks at each step
- Verification of window states
- Error recovery mechanisms
- Logging of each step for debugging

### Performance Considerations
- Built-in delays between actions
- Window state verification
- Error recovery timeouts
- System resource management

## Troubleshooting

### Common Issues
1. **Window Not Found**
   - Ensure WhatsApp is open
   - Check window title matches expected format

2. **Image Not Found**
   - Verify image exists in clipboard
   - Check Photos app permissions

3. **Send Failure**
   - Verify internet connection
   - Check WhatsApp connection status

### Debug Steps
1. Check system logs
2. Verify window states
3. Confirm clipboard contents
4. Test individual automation steps

## Best Practices
1. Always verify window states before actions
2. Implement appropriate delays between actions
3. Use robust error handling
4. Log all automation steps
5. Verify success of each operation 