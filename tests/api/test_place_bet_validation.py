"""
API test for placing a bet validation.
"""
import pytest
from api.api_client import APIClient


class TestPlaceBetValidation:
    """Test class for API bet placement validation."""
    
    @pytest.mark.api
    @pytest.mark.smoke
    def test_place_bet_validation(self, api_client):
        """
        Test placing a bet through the API with validation.
        
        Args:
            api_client: API client instance
        """
        # Arrange - Get available matches
        matches = api_client.get_matches()
        assert len(matches) > 0
        
        # Act - Place a bet with valid data
        bet_data = {
            "match_id": matches[0]["id"],
            "outcome": "1",
            "stake": "10.00"
        }
        
        result = api_client.place_bet(bet_data)
        
        # Assert - Verify bet was placed successfully
        assert "bet_id" in result
        assert result["status"] == "placed"
        assert float(result["stake"]) == 10.00
        
        # Act - Get updated balance
        balance = api_client.get_balance()
        
        # Assert - Verify balance was updated
        assert "balance" in balance
        assert float(balance["balance"]) < 1000.00