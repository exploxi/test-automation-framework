from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    MESSAGE = (By.ID, "flash")

    def __init__(self, driver):
        self.driver = driver

    def load(self, url):
        self.driver.get(url)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def get_message(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MESSAGE)
        ).text
