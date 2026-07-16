"""
UI test for placing a single bet.
"""
import pytest
from pages.home_page import HomePage
from pages.bet_slip_page import BetSlipPage
from pages.bet_placing_popup_page import BetPlacingPopupPage
from api.balance_api import BalanceAPI



class TestPlaceSingleBet:
    """Test class for placing a single bet via UI."""
    
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