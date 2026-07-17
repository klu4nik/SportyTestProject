"""
Bet Slip Page class implementing the Page Object Model for the bet slip page.
"""
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.bet_slip import BetSlipLocators


class BetSlipPage(BasePage):
    """Bet slip page implementation."""
    
    def __init__(self, driver: WebDriver):
        """
        Initialize the BetSlipPage.
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
        self.locators = BetSlipLocators()
    
    def enter_stake(self, stake: str) -> None:
        """
        Enter stake amount.
        
        Args:
            stake: Stake amount to enter
        """
        self.fill(self.locators.STAKE_INPUT, stake)
    
    def click_place_bet(self) -> None:
        """Click the place bet button."""
        self.click(self.locators.PLACE_BET_BUTTON)
    
    def remove_selection(self) -> None:
        """Remove a selection from the bet slip."""
        self.click(self.locators.REMOVE_SELECTION_BUTTON)
    
    def get_balance(self) -> str:
        """
        Get current balance.
        
        Returns:
            Current balance as string
        """
        self.wait_visible(self.locators.BALANCE_TEXT)
        return self.driver.find_element(*self.locators.BALANCE_TEXT).text
    
    def get_payout(self) -> str:
        """
        Get payout amount.
        
        Returns:
            Payout amount as string
        """
        self.wait_visible(self.locators.PAYOUT_TEXT)
        return self.driver.find_element(*self.locators.PAYOUT_TEXT).text

    def get_total_stake(self) -> str:
        """
        Get total stake amount.

        Returns:
            Total stake amount as string
        """
        locator = self.wait_visible(self.locators.TOTAL_STAKE_VALUE)
        return locator.text

    def get_odds(self) -> str:
        """
        Get bet slip odds.

        Returns:
            Odds as string
        """
        locator = self.wait_visible(self.locators.BET_SLIP_ODDS)
        return locator.text

    def get_potential_payout(self) -> str:
        """
        Get potential payout amount.

        Returns:
            Potential payout amount as string
        """
        locator = self.wait_visible(self.locators.POTENTIAL_PAYOUT)
        return locator.text


    def is_receipt_displayed(self) -> bool:
        """
        Check if receipt is displayed.
        
        Returns:
            True if receipt is displayed, False otherwise
        """
        return self.driver.find_element(*self.locators.RECEIPT_DISPLAYED).is_displayed()