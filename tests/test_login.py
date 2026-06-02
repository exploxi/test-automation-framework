from utils.logger import get_logger
from pages.login_page import LoginPage
from config import settings

logger = get_logger()

def test_login_success(driver):
    logger.info("Starting positive login test")
    page = LoginPage(driver)
    page.load(settings.BASE_URL)

    page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)
    message = page.get_message()

    assert "You logged into a secure area!" in message
    logger.info("Positive login test passed")

def test_login_invalid_username(driver):
    logger.info("Starting invalid username test")
    page = LoginPage(driver)
    page.load(settings.BASE_URL)

    page.login(settings.INVALID_USERNAME, settings.VALID_PASSWORD)
    message = page.get_message()

    assert "Your username is invalid!" in message
    logger.info("Invalid username test passed")

def test_login_invalid_password(driver):
    logger.info("Starting invalid password test")
    page = LoginPage(driver)
    page.load(settings.BASE_URL)

    page.login(settings.VALID_USERNAME, settings.INVALID_PASSWORD)
    message = page.get_message()

    assert "Your password is invalid!" in message
    logger.info("Invalid password test passed")
