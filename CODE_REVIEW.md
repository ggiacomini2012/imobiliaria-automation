# Code Review: Imobiliária Automation Project

## Project Overview
This is a WhatsApp automation project for real estate businesses, designed to automate the sending of messages and images to potential clients. The project uses Flask for the web interface and various Python libraries for automation.

## Architecture
The project follows a web-based architecture with:
- Flask web server (`app.py`)
- Multiple automation scripts for different platforms (Windows/macOS)
- Template-based frontend
- File upload functionality for images
- Logging system for tracking sent messages

## Strengths

### 1. Cross-Platform Support
- Good separation of Windows and macOS specific code
- Clear path handling for different operating systems
- Graceful fallbacks when platform-specific features aren't available

### 2. Security Considerations
- Uses `secure_filename` for uploaded files
- Proper file path handling using `os.path.join`
- Environment variable handling for subprocesses

### 3. Error Handling
- Comprehensive try-catch blocks
- Detailed error logging
- User-friendly error messages
- Proper HTTP status codes

### 4. Code Organization
- Clear separation of concerns
- Modular structure with separate modules directory
- Well-documented README with setup instructions

## Areas for Improvement

### 1. Configuration Management
Current approach:
```python
base_dir = os.path.dirname(__file__)
single_send_script_path_win = os.path.join(base_dir, 'modules', 'send-browser2app', 'send-back.py')
```

Recommended approach:
```python
# config.py
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATHS = {
    'windows': {
        'single_send': os.path.join(BASE_DIR, 'modules', 'send-browser2app', 'send-back.py'),
        'bulk_send': os.path.join(BASE_DIR, 'codigo-final', 'bulk_sender.py'),
    },
    'macos': {
        'single_send': os.path.join(BASE_DIR, 'modules', 'send-browser2app', 'send-back_mac.py'),
        'bulk_send': os.path.join(BASE_DIR, 'codigo-final', 'bulk_sender_mac.py'),
    }
}
```

### 2. Logging System
Current logging is scattered across print statements. Recommended implementation:
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### 3. Input Validation
Add more robust input validation:
```python
def validate_message_template(template: str) -> bool:
    if not template or len(template.strip()) == 0:
        return False
    # Add more validation rules as needed
    return True

def validate_image_file(file) -> bool:
    if not file:
        return False
    if file.content_type not in ALLOWED_MIME_TYPES:
        return False
    if file.content_length > MAX_FILE_SIZE:
        return False
    return True
```

### 4. Code Duplication
Create utility functions for common operations:
```python
def run_script(script_path: str, args: Optional[List[str]] = None, cwd: Optional[str] = None) -> subprocess.CompletedProcess:
    try:
        result = subprocess.run(
            [sys.executable, script_path] + (args or []),
            capture_output=True,
            text=True,
            check=False,
            encoding='utf-8',
            errors='replace',
            cwd=cwd or base_dir,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"}
        )
        return result
    except Exception as e:
        logging.error(f"Error running script {script_path}: {e}")
        raise
```

### 5. Testing
Recommended test structure:
```
tests/
├── __init__.py
├── test_app.py
├── test_message_sender.py
├── test_image_handler.py
└── conftest.py
```

Example test:
```python
# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_send_messages_endpoint(client):
    response = client.post('/send_messages', data={
        'message_template': 'Test message',
        'include_image': 'false'
    })
    assert response.status_code == 200
    assert response.json['success'] is True
```

### 6. Documentation
Add comprehensive docstrings:
```python
def send_messages(message_template: str, include_image: bool = False) -> Dict[str, Any]:
    """
    Send messages to multiple recipients using the provided template.
    
    Args:
        message_template (str): The message template to use
        include_image (bool): Whether to include an image with the message
        
    Returns:
        Dict[str, Any]: Response containing success status and output
        
    Raises:
        ValueError: If message template is invalid
        FileNotFoundError: If required scripts are not found
    """
    # Implementation
```

### 7. Error Recovery
Implement retry mechanism:
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def send_message_with_retry(recipient: str, message: str) -> bool:
    try:
        # Send message implementation
        return True
    except Exception as e:
        logging.error(f"Failed to send message to {recipient}: {e}")
        raise
```

### 8. Performance Optimization
Implement async operations:
```python
from asyncio import gather
from typing import List

async def send_bulk_messages(recipients: List[str], message: str) -> List[bool]:
    tasks = [send_message(recipient, message) for recipient in recipients]
    results = await gather(*tasks, return_exceptions=True)
    return [isinstance(r, bool) and r for r in results]
```

## Security Recommendations

### 1. File Upload Security
```python
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def allowed_file(filename: str) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def validate_file_size(file) -> bool:
    return file.content_length <= MAX_FILE_SIZE
```

### 2. Environment Variables
Create a `.env` file:
```
WHATSAPP_API_KEY=your_api_key
MAX_RETRIES=3
DEBUG=False
```

### 3. Rate Limiting
Implement rate limiting:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/send_messages", methods=["POST"])
@limiter.limit("10 per minute")
def send_messages():
    # Implementation
```

## Code Quality Recommendations

### 1. Type Hints
Add comprehensive type hints:
```python
from typing import Optional, List, Dict, Any

def process_message(
    template: str,
    variables: Dict[str, str],
    include_image: bool = False
) -> Dict[str, Any]:
    # Implementation
```

### 2. Constants
Create a constants file:
```python
# constants.py
class Config:
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    DEFAULT_TIMEOUT = 30
    MAX_RETRIES = 3
```

### 3. Response Standardization
Create standard response format:
```python
def api_response(
    success: bool,
    message: str,
    data: Optional[Dict] = None,
    status_code: int = 200
) -> Tuple[Dict, int]:
    response = {
        'success': success,
        'message': message,
        'data': data
    }
    return response, status_code
```

## Conclusion
The project is well-structured and functional, but could benefit from some modern Python practices and additional security measures. The main areas for improvement are configuration management, error handling, and testing. The cross-platform support is a strong point, but the code could be more maintainable with better organization and documentation.

## Next Steps
1. Implement the suggested configuration management system
2. Add comprehensive testing suite
3. Improve error handling and recovery mechanisms
4. Add type hints throughout the codebase
5. Implement proper logging system
6. Add rate limiting and security measures
7. Create detailed API documentation
8. Set up CI/CD pipeline

## References
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Pytest Documentation](https://docs.pytest.org/)
- [Flask-Limiter Documentation](https://flask-limiter.readthedocs.io/) 