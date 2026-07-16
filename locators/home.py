"""
Home page locators.
"""
from selenium.webdriver.common.by import By


class HomeLocators:
    """Locators for the home page."""
    
    MATCH_LIST = (By.CSS_SELECTOR, "[id='match-list']")
    MATCH_ITEM = (By.CSS_SELECTOR, "[id^='match-card']")
    BET_BUTTON = (By.CSS_SELECTOR, "button.oddsButton")
    DATE_FILTER_BUTTON = (By.CSS_SELECTOR, "[id='date-filter']")
    MONTH_LABEL = (By.CSS_SELECTOR, "id='month-label'")
    DAYS_BUTTON = (By.CSS_SELECTOR, "button.dayCell")
    OUTCOME_BUTTON = (By.CSS_SELECTOR, "[data-testid='outcome-button']")
    BETSLIP_BUTTON = (By.CSS_SELECTOR, "[data-testid='betslip-button']")