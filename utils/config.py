"""
Configuration management for the test framework.
"""
import os
from typing import Optional


class Config:
    """Test configuration class."""
    
    # Base URL for the application
    BASE_URL = os.getenv('BASE_URL', 'https://qae-assignment-tau.vercel.app/')
    
    # User ID for authentication
    USER_ID = os.getenv('USER_ID', '')
    
    # Default timeout for waits
    DEFAULT_TIMEOUT = int(os.getenv('DEFAULT_TIMEOUT', '30'))
    
    # Browser to use for UI tests
    BROWSER = os.getenv('BROWSER', 'chrome')