"""
Bet Slip Page class implementing the Page Object Model for the bet slip page.
"""
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.bet_slip import BetSlipLocators
from locators.bet_placing_popup import BetPlacingPopupLocators


class BetPlacingPopupPage(BasePage):
    """Bet slip page implementation."""
    
    def __init__(self, driver: WebDriver):
        """
        Initialize the BetPlacingPopupPage.
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
        self.locators = BetPlacingPopupLocators
    

    

    

    
    def get_potential_payout(self) -> str:
        """
        Get potential payout amount.
        
        Returns:
            Payout amount as string
        """
        self.wait_visible(self.locators.POTENTIAL_PAYOUT)
        return self.driver.find_element(*self.locators.POTENTIAL_PAYOUT).text
    
    def is_success_modal_displayed(self) -> bool:
        """
        Check if receipt is displayed.
        
        Returns:
            True if receipt is displayed, False otherwise
        """
        element = self.wait_visible(self.locators.SUCCESS_MODAL)
        return element.is_displayed()