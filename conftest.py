"""
Pytest fixtures for the test framework.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from api.api_client import APIClient
from api.balance_api import BalanceAPI
from utils.config import Config


@pytest.fixture(scope="session")
def driver() -> WebDriver:
    """
    Create and return a Selenium WebDriver instance.
    
    Returns:
        Selenium WebDriver instance
    """
    chrome_options = Options()
    chrome_options.add_argument("--headed")  # Run in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    yield driver
    
    driver.quit()


@pytest.fixture(scope="session")
def api_client() -> APIClient:
    """
    Create and return an API client instance.
    
    Returns:
        APIClient instance
    """
    return APIClient(
        base_url=Config.BASE_URL,
        user_id=Config.USER_ID,
        timeout=Config.DEFAULT_TIMEOUT
    )


@pytest.fixture(scope="session")
def balance_api(api_client) -> BalanceAPI:
    """
    Create and return a BalanceAPI instance.
    
    Args:
        api_client: API client instance
        
    Returns:
        BalanceAPI instance
    """
    return BalanceAPI(api_client)


@pytest.fixture(autouse=True)
def take_screenshot_on_failure(request, driver):
    """
    Take screenshot when a test fails.
    
    Args:
        request: Pytest request object
        driver: Selenium WebDriver instance
    """
    def _take_screenshot():
        # Create screenshots directory if it doesn't exist
        import os
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        # Take screenshot with test name as filename
        screenshot_path = f"{screenshot_dir}/{request.node.name}.png"
        driver.save_screenshot(screenshot_path)
    
    # Register the callback to run on failure
    request.addfinalizer(_take_screenshot)