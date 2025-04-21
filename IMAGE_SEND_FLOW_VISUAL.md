# Visual Representation of Image Send Flow

## Windows Flow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User Interface │     │  Frontend JS    │     │  Backend Flask  │
│  (Dashboard)    │────▶│  (script.js)    │────▶│  (app.py)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Fill Form      │     │  Collect Data   │     │  Save Image     │
│  Check Image    │     │  Create FormData│     │  Detect OS      │
│  Click Send     │     │  Send to Server │     │  Run Script     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Bulk Sender    │     │  For Each       │     │  Image Sending  │
│  (bulk_sender.py)│────▶│  Contact       │────▶│  (send_image_gui)│
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Load Contacts  │     │  Format Message │     │  Validate Image │
│  Track Progress │     │  Open WhatsApp  │     │  Copy to Clip   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Log Success    │     │  Next Contact   │     │  Paste Image    │
│  Update Stats   │◀────│  or Finish      │◀────│  Paste Caption  │
└─────────────────┘     └─────────────────┘     │  Press Enter    │
                                                └─────────────────┘
```

## macOS Flow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User Interface │     │  Frontend JS    │     │  Backend Flask  │
│  (Dashboard)    │────▶│  (script.js)    │────▶│  (app.py)       │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Fill Form      │     │  Collect Data   │     │  Detect OS      │
│  Check Image    │     │  Create FormData│     │  (macOS)        │
│  Click Send     │     │  Send to Server │     │  Disable Image  │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Bulk Sender    │     │  For Each       │     │  Text Only      │
│  (bulk_sender_mac)│────▶│  Contact       │────▶│  Send           │
└─────────────────┘     └─────────────────┘     └─────────────────┘
        │                       │                       │
        │                       │                       │
        ▼                       ▼                       ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Load Contacts  │     │  Format Message │     │  Open WhatsApp  │
│  Track Progress │     │  Encode Message │     │  with Message   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Log Success    │     │  Next Contact   │     │  Press Enter    │
│  Update Stats   │◀────│  or Finish      │◀────│  Multiple Times │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Comparison of Image Handling

```
┌─────────────────────────────────────────────────────────────────┐
│                      Windows Image Handling                      │
└─────────────────────────────────────────────────────────────────┘
                                                                    
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Validate   │     │  Copy to    │     │  Open       │     │  Paste      │
│  Image      │────▶│  Clipboard  │────▶│  WhatsApp   │────▶│  Image      │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                    
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Paste      │     │  Press      │     │  Return     │
│  Caption    │────▶│  Enter      │────▶│  Success    │
└─────────────┘     └─────────────┘     └─────────────┘

┌─────────────────────────────────────────────────────────────────┐
│                      macOS Image Handling                        │
└─────────────────────────────────────────────────────────────────┘
                                                                    
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Detect     │     │  Disable     │     │  Send Text  │
│  macOS      │────▶│  Image      │────▶│  Only       │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Current Issue in macOS Flow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User Clicks    │     │  app.py         │     │  Image Sending  │
│  Send with      │────▶│  Detects        │────▶│  Disabled       │
│  Image          │     │  macOS          │     │  for macOS      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User           │     │  Only Text      │     │  No Image       │
│  Expects        │◀────│  Message        │◀────│  Functionality  │
│  Image          │     │  Sent           │     │  Available      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

## Proposed Solution Flow

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User Clicks    │     │  app.py         │     │  Enable Image   │
│  Send with      │────▶│  Detects        │────▶│  for macOS      │
│  Image          │     │  macOS          │     │  (New Code)     │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                                                           │
                                                           │
                                                           ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  User           │     │  Image + Text   │     │  Reliable       │
│  Gets           │◀────│  Message        │◀────│  Image Copy     │
│  Expected       │     │  Sent           │     │  & Paste        │
└─────────────────┘     └─────────────────┘     └─────────────────┘
``` 