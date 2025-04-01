import os
import sys
from contextlib import contextmanager

def minimize_output():
    """
    Minimize terminal output by redirecting stdout and stderr to devnull.
    Returns a context manager that can be used with 'with' statement.
    """
    @contextmanager
    def _minimize():
        # Store original stdout and stderr
        original_stdout = sys.stdout
        original_stderr = sys.stderr
        
        # Open devnull
        with open(os.devnull, 'w') as devnull:
            # Redirect stdout and stderr to devnull
            sys.stdout = devnull
            sys.stderr = devnull
            try:
                yield
            finally:
                # Restore original stdout and stderr
                sys.stdout = original_stdout
                sys.stderr = original_stderr
    
    return _minimize()

def suppress_output(func):
    """
    Decorator to suppress output of a function.
    Usage:
        @suppress_output
        def my_function():
            print("This won't be shown")
    """
    def wrapper(*args, **kwargs):
        with minimize_output():
            return func(*args, **kwargs)
    return wrapper

def quiet_print(*args, **kwargs):
    """
    A print function that only prints if explicitly enabled.
    Usage:
        quiet_print("This won't print by default")
        quiet_print("This will print", force=True)
    """
    if kwargs.get('force', False):
        del kwargs['force']
        print(*args, **kwargs) 