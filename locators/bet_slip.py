"""
Bet slip page locators.
"""
from selenium.webdriver.common.by import By


class BetSlipLocators:
    """Locators for the bet slip page."""
    
    STAKE_INPUT = (By.CSS_SELECTOR, "[id='bet-slip-stake-input']")
    BET_SLIP_ODDS = (By.CSS_SELECTOR, ".betSelectionOdds")
    TOTAL_STAKE_VALUE = (By.CSS_SELECTOR, "[id='bet-slip-total-stake']")
    POTENTIAL_PAYOUT = (By.CSS_SELECTOR, "[id='bet-slip-potential-payout']")
    PLACE_BET_BUTTON = (By.CSS_SELECTOR, "[id='bet-slip-place-bet']")
    REMOVE_SELECTION_BUTTON = (By.CSS_SELECTOR, "[id='bet-slip-selection-remove']")