"""
Bet slip page locators.
"""
from selenium.webdriver.common.by import By


class BetPlacingPopupLocators:
    """Locators for the bet slip page."""
    
    SUCCESS_MODAL = (By.CSS_SELECTOR,"[id='modal-success']")
    MODAL_STAKE = (By.CSS_SELECTOR, "[id='modal-success-stake']")
    MODAL_ODDS = (By.CSS_SELECTOR, "[id='modal-success-odds']")
    MODAL_TOTAL_STAKE_VALUE = (By.CSS_SELECTOR, "[id='bet-slip-total-stake']")
    POTENTIAL_PAYOUT = (By.CSS_SELECTOR, "[id='modal-success-payout']")
    CLOSE_BUTTON = (By.CSS_SELECTOR,"[id='modal-success-close']")