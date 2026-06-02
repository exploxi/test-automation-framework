import pytest
from utils.driver_factory import get_driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def driver(browser):
    driver = get_driver(browser)
    yield driver
    driver.quit()
