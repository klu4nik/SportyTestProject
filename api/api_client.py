"""
API Client class for making HTTP requests to the sports betting API.
"""
import requests
from typing import Dict, Any, Optional
from urllib.parse import urljoin


class APIClient:
    """API client for interacting with the sports betting API."""
    
    def __init__(self, base_url: str, user_id: str, timeout: int = 30):
        """
        Initialize the API client.
        
        Args:
            base_url: Base URL of the API
            user_id: User ID for authentication
            timeout: Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.user_id = user_id
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'x-user-id': user_id,
            'Content-Type': 'application/json'
        })
    
    def get_matches(self) -> Dict[str, Any]:
        """
        Get list of available matches.
        
        Returns:
            Dictionary containing matches data
        """
        response = self.session.get(
            urljoin(self.base_url, 'api/matches'),
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def get_balance(self) -> Dict[str, Any]:
        """
        Get user's current balance.
        
        Returns:
            Dictionary containing balance data
        """
        response = self.session.get(
            urljoin(self.base_url, 'api/balance'),
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def place_bet(self, bet_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Place a bet.
        
        Args:
            bet_data: Dictionary containing bet details
            
        Returns:
            Dictionary containing bet result
        """
        response = self.session.post(
            urljoin(self.base_url, 'api/place-bet'),
            json=bet_data,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()
    
    def reset_balance(self) -> None:
        """
        Reset user's balance to default.
        """
        response = self.session.post(
            urljoin(self.base_url, 'api/reset-balance'),
            timeout=self.timeout
        )
        response.raise_for_status()