"""
Base Page class containing common browser interactions.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Union


class BasePage:
    """Base page class with common browser interactions."""
    
    def __init__(self, driver: WebDriver):
        """
        Initialize the BasePage.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def click(self, locator: Union[tuple, str]) -> None:
        """
        Click on an element.
        
        Args:
            locator: Tuple of (By, value) or string selector
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def fill(self, locator: Union[tuple, str], text: str) -> None:
        """
        Fill text into an input field.
        
        Args:
            locator: Tuple of (By, value) or string selector
            text: Text to type
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)
    
    def wait_visible(self, locator: Union[tuple, str]) -> WebElement:
        """
        Wait until an element is visible.
        
        Args:
            locator: Tuple of (By, value) or string selector
        """
        return self.wait.until(EC.visibility_of_element_located(locator))