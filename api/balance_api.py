"""
Balance API service for managing user balance.
"""
from api.api_client import APIClient


class BalanceAPI:
    """Balance API service."""
    
    def __init__(self, api_client: APIClient):
        """
        Initialize the BalanceAPI.
        
        Args:
            api_client: APIClient instance
        """
        self.api_client = api_client
    
    def reset_balance(self) -> None:
        """
        Reset user's balance to default.
        """
        self.api_client.reset_balance()