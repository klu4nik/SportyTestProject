"""
API test for placing a bet validation.
"""
import pytest
from assertions.api_assertions import APIAssertions


class TestPlaceBetValidation:
    """Test class for API bet placement validation."""

    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "stake",
        [1, 2, 10, 25, 50, 99, 100],
        ids=[
            "stake_1",
            "stake_2",
            "stake_10",
            "stake_25",
            "stake_50",
            "stake_99",
            "stake_100",
        ],
    )
    def test_place_bet_validation(self, api_client, stake):
        # Arrange
        matches = api_client.get_matches()
        assert matches, "No available matches"

        api_client.reset_balance()
        initial_balance = api_client.get_balance()["balance"]

        bet_data = {
            "matchId": matches[0]["id"],
            "selection": "DRAW",
            "stake": stake,
        }

        # Act
        result = api_client.place_bet(bet_data)

        # Assert
        APIAssertions.assert_successful_bet(result, bet_data)

        updated_balance = api_client.get_balance()["balance"]

        APIAssertions.assert_balance_updated(
            initial_balance=initial_balance,
            updated_balance=updated_balance,
            stake=stake,
        )