# Image Send Flow Documentation

## Overview

This document outlines the execution flow when a user clicks the "send" or "iniciar envio" button with an image in the application. The flow differs between Windows and macOS platforms.

## Windows Flow

1. **User Interface Interaction**
   - User fills out the dashboard form with message template
   - User checks "Incluir Imagem" checkbox
   - User selects an image file
   - User clicks "Iniciar Envio" button

2. **Frontend Processing**
   - JavaScript event listener captures form submission
   - Form data is collected including message template, image file, and include_image flag
   - FormData object is created and sent to `/send_messages` endpoint via fetch API

3. **Backend Processing (app.py)**
   - Flask route `/send_messages` receives POST request
   - Message template and image file are extracted from request
   - Image is saved to uploads folder
   - OS detection determines which script to use (Windows in this case)
   - Command is constructed to run `bulk_sender.py` with message template and image path

4. **Bulk Sender Execution (bulk_sender.py)**
   - Script loads contacts from contacts.py
   - For each contact:
     - Formats message with contact name
     - Opens WhatsApp with contact number
     - Calls `send_image_gui.py` to handle image sending
     - Logs successful sends

5. **Image Sending (send_image_gui.py)**
   - Validates image file
   - Copies image to clipboard using Windows-specific method
   - Opens WhatsApp with contact number
   - Waits for WhatsApp to open
   - Pastes image from clipboard (Ctrl+V)
   - Waits for image to load
   - Pastes caption text
   - Presses Enter to send
   - Returns success/failure status

## macOS Flow

1. **User Interface Interaction**
   - User fills out the dashboard form with message template
   - User checks "Incluir Imagem" checkbox
   - User selects an image file
   - User clicks "Iniciar Envio" button

2. **Frontend Processing**
   - JavaScript event listener captures form submission
   - Form data is collected including message template, image file, and include_image flag
   - FormData object is created and sent to `/send_messages` endpoint via fetch API

3. **Backend Processing (app.py)**
   - Flask route `/send_messages` receives POST request
   - Message template and image file are extracted from request
   - OS detection determines which script to use (macOS in this case)
   - **Important**: On macOS, image sending is currently disabled
   - Command is constructed to run `bulk_sender_mac.py` with message template only

4. **Bulk Sender Execution (bulk_sender_mac.py)**
   - Script loads contacts from contacts.py
   - For each contact:
     - Formats message with contact name
     - Opens WhatsApp with contact number and encoded message
     - Waits for WhatsApp to open
     - Attempts to press Enter multiple times for reliability
     - Logs successful sends

## Key Differences Between Platforms

1. **Image Handling**
   - Windows: Supports image sending via clipboard operations
   - macOS: Currently does not support image sending (disabled in app.py)

2. **Clipboard Operations**
   - Windows: Uses win32clipboard for image copying
   - macOS: Would use AppleScript or AppKit (currently not implemented)

3. **WhatsApp Opening**
   - Windows: Opens WhatsApp Web via browser
   - macOS: Opens native WhatsApp app via URI scheme

4. **Message Sending**
   - Windows: Uses GUI automation to paste image and text
   - macOS: Uses URI scheme to pre-populate message and Enter key to send

## Current Limitations

1. **macOS Image Support**
   - Image sending is explicitly disabled on macOS in app.py
   - No implementation exists for reliable image copying on macOS

2. **Timing Issues**
   - Fixed wait times may not be sufficient on all systems
   - No verification of clipboard operations

3. **Error Handling**
   - Limited error recovery mechanisms
   - No retry logic for failed operations

## Future Improvements

1. **Implement macOS Image Support**
   - Create reliable image copying for macOS
   - Add verification after clipboard operations

2. **Improve Timing Management**
   - Replace fixed waits with dynamic verification
   - Implement exponential backoff for reliability

3. **Enhance Error Recovery**
   - Add retry mechanisms for failed operations
   - Implement fallback strategies 