"""
UI test for placing a single bet.
"""
import pytest

from pages.home_page import HomePage
from pages.bet_slip_page import BetSlipPage
from pages.bet_placing_popup_page import BetPlacingPopupPage
import pytest_check as check


def _to_float(value) -> float:
    """Extract a numeric value from a currency/label-formatted string or Decimal."""
    text = str(value)
    return float("".join(ch for ch in text if ch.isdigit() or ch in ".,-"))


class TestPlaceSingleBet:
    """Test class for placing a single bet via UI."""

    @pytest.mark.test_id("TC-001")
    @pytest.mark.ui
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "outcome_index,stake",
        [
            (0, 10.5),
            (1, 25.0),
            (2, 50.0),
        ],
        ids=[
            "home_stake_10.5",
            "draw_stake_25",
            "away_stake_50",
        ],
    )
    def test_place_single_bet(
            self,
            driver,
            api_client,
            balance_api,
            outcome_index,
            stake,
    ):
        """Verify a user can place a bet and all displayed values are correct."""

        # Arrange
        balance_api.reset_balance()
        initial_balance = api_client.get_balance()["balance"]

        home_page = HomePage(driver)
        home_page.open()
        home_page.select_match(0, outcome_index)

        bet_slip = BetSlipPage(driver)

        # Act
        bet_slip.enter_stake(stake)

        bet_slip_total_stake = bet_slip.get_total_stake()
        bet_slip_odds = bet_slip.get_odds().replace("Odds: ", "")
        bet_slip_potential_payout = bet_slip.get_potential_payout()

        odds = _to_float(bet_slip_odds)
        payout = _to_float(bet_slip_potential_payout)
        expected_payout = float(stake) * odds

        bet_slip.click_place_bet()

        popup = BetPlacingPopupPage(driver)

        # Assert
        check.is_true(
            popup.is_success_modal_displayed(),
            "Success popup should be displayed."
        )

        check.equal(
            popup.get_total_stake(),
            bet_slip_total_stake,
            "Popup stake should match bet slip."
        )

        check.equal(
            popup.get_odds(),
            bet_slip_odds,
            "Popup odds should match bet slip."
        )

        check.equal(
            popup.get_potential_payout(),
            bet_slip_potential_payout,
            "Popup potential payout should match bet slip."
        )

        check.equal(
            payout,
            expected_payout,
            f"Expected payout {expected_payout}, got {payout}."
        )

        popup.close()
        expected_balance = initial_balance - stake
        actual_balance_ui = home_page.get_balance()
        actual_balance_api = api_client.get_balance()["balance"]
        check.equal(expected_balance, actual_balance_ui,
                    f"Expected balance in UI {expected_balance} but got {actual_balance_ui}")
        check.equal(expected_balance, actual_balance_api,
                    f"Expected balance in API {expected_balance} but got {actual_balance_api}")
