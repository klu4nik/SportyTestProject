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
        "selection,stake",
        [
            ("HOME", 1),
            ("DRAW", 30.5),
            ("AWAY", 100),
        ],
        ids=[
            "home_stake_1",
            "draw_stake_30.5",
            "away_stake_100",
        ],
    )
    def test_place_bet_validation(self, api_client, selection, stake):
        # Arrange
        matches = api_client.get_matches()
        assert matches, "No available matches"

        api_client.reset_balance()
        initial_balance = api_client.get_balance()["balance"]

        bet_data = {
            "matchId": matches[0]["id"],
            "selection": selection,
            "stake": stake,
        }

        # Act
        result = api_client.place_bet(bet_data)

        # Assert
        APIAssertions.assert_successful_bet(result, bet_data)

        updated_balance = api_client.get_balance()["balance"]

        APIAssertions.assert_balance_updated(
            initial_balance,
            updated_balance,
            stake,
        )

    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "stake",
        [
            -2,
            0,
            0.99,
            30.9954,
            100.11,
            "Eleven"
        ],
        ids=[
            "stake_-2",
            "stake_0",
            "stake_0.99",
            "stake_30.9954",
            "stake_100.11",
            "stake_Eleven"
        ],
    )
    def test_place_incorrect_bet(self, api_client, stake):
        # Arrange
        matches = api_client.get_matches()
        assert matches, "No available matches"

        api_client.reset_balance()
        initial_balance = api_client.get_balance()["balance"]

        bet_data = {
            "matchId": matches[0]["id"],
            "selection": "HOME",
            "stake": stake,
        }

        # Act
        result = api_client.place_bet(bet_data)

        # Assert
        APIAssertions.assert_failed_bet(result)

        updated_balance = api_client.get_balance()["balance"]

        APIAssertions.assert_balance_unchanged(
            initial_balance,
            updated_balance,
        )
