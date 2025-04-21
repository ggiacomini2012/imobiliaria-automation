# Image Send Flow - Mermaid Diagrams

## Windows Flow

```mermaid
flowchart TD
    A[User Interface<br>Dashboard] -->|Fill Form & Click Send| B[Frontend JS<br>script.js]
    B -->|FormData to Server| C[Backend Flask<br>app.py]
    C -->|Save Image & Run Script| D[Bulk Sender<br>bulk_sender.py]
    D -->|For Each Contact| E[Image Sending<br>send_image_gui.py]
    
    subgraph "User Interface"
    A
    end
    
    subgraph "Frontend Processing"
    B
    end
    
    subgraph "Backend Processing"
    C
    end
    
    subgraph "Bulk Sender Execution"
    D
    end
    
    subgraph "Image Sending"
    E
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style E fill:#bff,stroke:#333,stroke-width:2px
```

## macOS Flow

```mermaid
flowchart TD
    A[User Interface<br>Dashboard] -->|Fill Form & Click Send| B[Frontend JS<br>script.js]
    B -->|FormData to Server| C[Backend Flask<br>app.py]
    C -->|Detect macOS & Disable Image| D[Bulk Sender<br>bulk_sender_mac.py]
    D -->|For Each Contact| E[Text Only Send]
    
    subgraph "User Interface"
    A
    end
    
    subgraph "Frontend Processing"
    B
    end
    
    subgraph "Backend Processing"
    C
    end
    
    subgraph "Bulk Sender Execution"
    D
    end
    
    subgraph "Text Only Send"
    E
    end
    
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style E fill:#bff,stroke:#333,stroke-width:2px
```

## Detailed Windows Image Handling

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant BulkSender
    participant ImageSender
    participant WhatsApp
    
    User->>Frontend: Fill form & select image
    Frontend->>Backend: Send form data & image
    Backend->>Backend: Save image to uploads
    Backend->>BulkSender: Run with message & image path
    BulkSender->>BulkSender: Load contacts
    loop For each contact
        BulkSender->>ImageSender: Send image & message
        ImageSender->>ImageSender: Validate image
        ImageSender->>ImageSender: Copy to clipboard
        ImageSender->>WhatsApp: Open with contact number
        WhatsApp-->>ImageSender: WhatsApp opened
        ImageSender->>WhatsApp: Paste image (Ctrl+V)
        WhatsApp-->>ImageSender: Image pasted
        ImageSender->>WhatsApp: Paste caption
        ImageSender->>WhatsApp: Press Enter
        WhatsApp-->>ImageSender: Message sent
        ImageSender-->>BulkSender: Success status
        BulkSender->>BulkSender: Log success
    end
    BulkSender-->>Backend: Process complete
    Backend-->>Frontend: Success response
    Frontend-->>User: Show success message
```

## Detailed macOS Image Handling (Current)

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant BulkSender
    participant WhatsApp
    
    User->>Frontend: Fill form & select image
    Frontend->>Backend: Send form data & image
    Backend->>Backend: Detect macOS
    Note over Backend: Disable image sending
    Backend->>BulkSender: Run with message only
    BulkSender->>BulkSender: Load contacts
    loop For each contact
        BulkSender->>BulkSender: Format message
        BulkSender->>WhatsApp: Open with contact & message
        WhatsApp-->>BulkSender: WhatsApp opened
        BulkSender->>WhatsApp: Press Enter
        WhatsApp-->>BulkSender: Message sent
        BulkSender->>BulkSender: Log success
    end
    BulkSender-->>Backend: Process complete
    Backend-->>Frontend: Success response
    Frontend-->>User: Show success message
```

## Detailed macOS Image Handling (Proposed)

```mermaid
sequenceDiagram
    participant User
    participant Frontend
    participant Backend
    participant BulkSender
    participant ImageSender
    participant WhatsApp
    
    User->>Frontend: Fill form & select image
    Frontend->>Backend: Send form data & image
    Backend->>Backend: Save image to uploads
    Backend->>BulkSender: Run with message & image path
    BulkSender->>BulkSender: Load contacts
    loop For each contact
        BulkSender->>ImageSender: Send image & message
        ImageSender->>ImageSender: Validate image
        ImageSender->>ImageSender: Copy to clipboard (macOS)
        ImageSender->>WhatsApp: Open with contact number
        WhatsApp-->>ImageSender: WhatsApp opened
        ImageSender->>WhatsApp: Paste image (Cmd+V)
        WhatsApp-->>ImageSender: Image pasted
        ImageSender->>WhatsApp: Paste caption
        ImageSender->>WhatsApp: Press Enter
        WhatsApp-->>ImageSender: Message sent
        ImageSender-->>BulkSender: Success status
        BulkSender->>BulkSender: Log success
    end
    BulkSender-->>Backend: Process complete
    Backend-->>Frontend: Success response
    Frontend-->>User: Show success message
```

## Debugging Tools

Here are some tools you can use to visualize and debug the flow:

1. **Mermaid Live Editor**: https://mermaid.live/
   - Paste the Mermaid code to visualize the diagrams
   - Export as SVG, PNG, or other formats

2. **Draw.io (diagrams.net)**: https://app.diagrams.net/
   - Create interactive flowcharts
   - Export in various formats
   - Integrates with GitHub, Google Drive, etc.

3. **Python Visualization Libraries**:
   ```python
   # Example using Graphviz
   from graphviz import Digraph
   
   dot = Digraph(comment='Image Send Flow')
   dot.attr(rankdir='LR')
   
   # Add nodes
   dot.node('A', 'User Interface')
   dot.node('B', 'Frontend JS')
   dot.node('C', 'Backend Flask')
   dot.node('D', 'Bulk Sender')
   dot.node('E', 'Image Sending')
   
   # Add edges
   dot.edge('A', 'B', 'Fill Form & Click Send')
   dot.edge('B', 'C', 'FormData to Server')
   dot.edge('C', 'D', 'Save Image & Run Script')
   dot.edge('D', 'E', 'For Each Contact')
   
   # Save the graph
   dot.render('image_send_flow', format='png', cleanup=True)
   ```

4. **Debugging Tools**:
   - **Python Debugger (pdb)**: Add breakpoints in your code
   - **Visual Studio Code Debugger**: Set breakpoints and step through code
   - **PyCharm Debugger**: Visual debugging with variable inspection
   - **Logging**: Add detailed logging to track the flow

5. **Flow Monitoring**:
   - **Python logging**: Add detailed logs at each step
   - **Performance profiling**: Use cProfile to identify bottlenecks
   - **State tracking**: Implement state machines to track progress 