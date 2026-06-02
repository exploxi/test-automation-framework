from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def get_driver(browser_name="chrome"):
    if browser_name == "chrome":
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(service=service, options=options)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        options.add_argument("--start-maximized")
        return webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")
