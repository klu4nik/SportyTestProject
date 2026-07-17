"""
Home Page class implementing the Page Object Model for the home page.
"""
from decimal import Decimal

from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from locators.home import HomeLocators
from typing import Literal


class HomePage(BasePage):
    """Home page implementation."""

    def __init__(self, driver: WebDriver):
        """
        Initialize the HomePage.
        
        Args:
            driver: Selenium WebDriver instance
        """
        super().__init__(driver)
        self.locators = HomeLocators()

    def open(self) -> None:
        """Open the home page."""
        self.driver.get("https://qae-assignment-tau.vercel.app/?user-id=candidate-LCz6UDWO4U")

    def select_match(
            self,
            match_index: int,
            bet: Literal[0, 1, 2]
    ) -> None:
        """
        Select a betting option for a match.

        Args:
            match_index: Zero-based match index.
            bet: 0 = Home, 1 = Draw, 2 = Away.
        """
        self.wait_visible(self.locators.MATCH_ITEM)

        matches = self.driver.find_elements(*self.locators.MATCH_ITEM)

        if match_index >= len(matches):
            raise IndexError(f"Match with index {match_index} not found.")

        match = matches[match_index]

        bet_buttons = match.find_elements(*self.locators.BET_BUTTON)

        if bet >= len(bet_buttons):
            raise IndexError(f"Bet option {bet} not found.")

        self.click(bet_buttons[bet])

    def select_outcome(self, outcome_index: int) -> None:
        """
        Select an outcome by index.
        
        Args:
            outcome_index: Index of the outcome to select
        """
        outcomes = self.driver.find_elements(*self.locators.OUTCOME_BUTTON)
        if outcomes and len(outcomes) > outcome_index:
            outcomes[outcome_index].click()

    def open_betslip(self) -> None:
        """Open the bet slip."""
        self.click(self.locators.BETSLIP_BUTTON)

    def get_balance(self) -> Decimal:
        """Get the current account balance."""

        text= self.wait_visible(self.locators.BALANCE).text
        amount = (
            text.replace("Balance:", "")
            .replace("€", "")
            .strip()
        )
        return Decimal(amount)
