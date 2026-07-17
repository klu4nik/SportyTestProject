"""
UI test for placing a single bet.
"""
import pytest

from assertions.api_assertions import APIAssertions
from pages.home_page import HomePage
from pages.bet_slip_page import BetSlipPage
from pages.bet_placing_popup_page import BetPlacingPopupPage
from api.balance_api import BalanceAPI
from itertools import product


def _to_float(value) -> float:
    """Extract a numeric value from a currency/label-formatted string or Decimal."""
    text = str(value)
    return float("".join(ch for ch in text if ch.isdigit() or ch in ".,-"))


class TestPlaceSingleBet:
    """Test class for placing a single bet via UI."""

    @pytest.mark.test_id("TC-001")
    @pytest.mark.ui
    @pytest.mark.smoke
    def test_place_single_bet(self, driver, api_client, balance_api):
        """
        Test placing a single bet through the UI.
        
        Args:
            driver: Selenium WebDriver instance
            api_client: API client instance
            balance_api: BalanceAPI instance
        """
        # Arrange - Reset balance and navigate to home page
        balance_api.reset_balance()
        home_page = HomePage(driver)
        home_page.open()

        # Act - Select match and outcome, then open bet slip
        home_page.select_match(0, 1)

        # Assert - Verify bet slip is displayed and contains correct information
        bet_slip_page = BetSlipPage(driver)
        # Note: We can't directly assert balance here since it's not in the UI page object

        # Act - Enter stake and place bet
        bet_slip_page.enter_stake("10.00")
        bet_slip_page.click_place_bet()

        popup = BetPlacingPopupPage(driver)

        # Assert - Verify receipt is displayed
        assert popup.is_success_modal_displayed()

    @pytest.mark.test_id("TC-002")
    @pytest.mark.ui
    def test_validate_popup_fields_match_bet_slip(self, driver, api_client, balance_api):
        """
        Test that the success popup contains the same data as the bet slip.

        Args:
            driver: Selenium WebDriver instance
            api_client: API client instance
            balance_api: BalanceAPI instance
        """
        # Arrange - Reset balance and navigate to home page
        balance_api.reset_balance()
        home_page = HomePage(driver)
        home_page.open()

        # Act - Select match and outcome, then open bet slip
        home_page.select_match(0, 1)

        bet_slip_page = BetSlipPage(driver)

        # Act - Enter stake and capture bet slip values before placing the bet
        # (the bet slip is no longer visible once the success popup appears)
        bet_slip_page.enter_stake("10.00")
        bet_slip_total_stake = bet_slip_page.get_total_stake()
        # Bet slip odds text is prefixed with a label (e.g. "Odds: 3.10"),
        # while the popup odds text is just the value (e.g. "3.10")
        bet_slip_odds = bet_slip_page.get_odds().replace("Odds: ", "")
        bet_slip_potential_payout = bet_slip_page.get_potential_payout()
        bet_slip_page.click_place_bet()

        popup = BetPlacingPopupPage(driver)

        # Assert - Verify success popup is displayed
        assert popup.is_success_modal_displayed()

        # Assert - Verify popup contains the same data as the bet slip
        assert popup.get_total_stake() == bet_slip_total_stake
        assert popup.get_odds() == bet_slip_odds
        assert popup.get_potential_payout() == bet_slip_potential_payout

    @pytest.mark.test_id("TC-003")
    @pytest.mark.ui
    def test_validate_potential_payout_equals_stake_times_odds(self, driver, api_client, balance_api):
        """
        Test that the bet slip potential payout equals stake multiplied by odds.

        Args:
            driver: Selenium WebDriver instance
            api_client: API client instance
            balance_api: BalanceAPI instance
        """
        stake = "10.00"

        # Arrange - Reset balance and navigate to home page
        balance_api.reset_balance()
        home_page = HomePage(driver)
        home_page.open()

        # Act - Select match and outcome, then open bet slip
        home_page.select_match(0, 1)

        bet_slip_page = BetSlipPage(driver)

        # Act - Enter stake and capture bet slip values
        bet_slip_page.enter_stake(stake)
        bet_slip_odds = _to_float(bet_slip_page.get_odds())
        bet_slip_potential_payout = _to_float(bet_slip_page.get_potential_payout())

        # Assert - Verify potential payout equals stake * odds
        expected_payout = float(stake) * bet_slip_odds
        assert bet_slip_potential_payout == expected_payout, (
            f"Expected potential payout {expected_payout}, "
            f"but got {bet_slip_potential_payout}"
        )

    BET_INDICES = [0, 1, 2]
    STAKES = [1, 2, 25, 50, 99, 100]

    TEST_DATA = list(product(BET_INDICES, STAKES))

    @pytest.mark.test_id("TC-004")
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "bet_index, stake",
        TEST_DATA,
        ids=[
            f"bet_{bet_index}-stake_{stake}"
            for bet_index, stake in TEST_DATA
        ],
    )
    def test_validate_balance_after_bet(
            self,
            driver,
            api_client,
            balance_api,
            bet_index,
            stake,
    ):
        """
        Test that the account balance decreases by the stake after placing a bet.

        Args:
            driver: Selenium WebDriver instance
            api_client: API client instance
            balance_api: BalanceAPI instance
            bet_index: Outcome index (0=Home, 1=Draw, 2=Away)
            stake: Bet stake amount
        """
        # Arrange
        balance_api.reset_balance()

        home_page = HomePage(driver)
        home_page.open()

        # Act
        home_page.select_match(0, bet_index)
        initial_balance = _to_float(home_page.get_balance())

        bet_slip_page = BetSlipPage(driver)
        bet_slip_page.enter_stake(f"{stake:.2f}")
        bet_slip_page.click_place_bet()

        popup = BetPlacingPopupPage(driver)

        # Assert
        assert popup.is_success_modal_displayed()
        popup.close()


        current_ui_balance = _to_float(home_page.get_balance())

        APIAssertions.assert_balance_updated(
            initial_balance=initial_balance,
            updated_balance=current_ui_balance,
            stake=stake,
        )

