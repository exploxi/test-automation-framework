# Test Automation Framework (PyTest + Selenium)

This project implements a clean, modular, and scalable UI Test Automation Framework using:

- Python
- PyTest
- Selenium WebDriver
- Page Object Model (POM)
- Logging
- Configurable browser selection (Chrome / Firefox)
- Fixtures via conftest.py

The framework automates login functionality for a demo web application and is designed to be easily extended for additional test scenarios.

---

## 🚀 Features

- Selenium WebDriver with Chrome and Firefox support
- Browser selection via command-line argument: `--browser=chrome/firefox`
- PyTest fixtures for clean setup and teardown
- Page Object Model (POM) for maintainability
- Centralised driver factory
- Logging for debugging and traceability
- Configurable test data and URLs
- Clean project structure suitable for interviews and real-world automation

---

## 📦 Installation

Install dependencies:

pip install -r requirements.txt

Ensure you have at least one browser installed:

- Chrome (recommended)
- Firefox (optional, required for `--browser=firefox`)

---

## ▶ Running Tests

### Run all tests (default: Chrome)
pytest

### Run tests with a specific browser
pytest --browser=chrome
pytest --browser=firefox

### Run with HTML report (optional)
pytest --html=report.html --self-contained-html

---

## 📁 Project Structure

test-automation-framework/
│
├── conftest.py                # Global fixtures + pytest options
├── config/
│   └── settings.py            # Base URL + test data
│
├── utils/
│   ├── driver_factory.py      # WebDriver setup logic
│   └── logger.py              # Logging configuration
│
├── pages/
│   └── login_page.py          # Page Object for Login page
│
├── tests/
│   └── test_login.py          # Login test suite
│
└── README.txt

---

## 🧩 How Browser Selection Works

### 1. `conftest.py` defines a pytest option:
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

### 2. A fixture reads the value:
@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

### 3. The driver fixture passes it to the driver factory:
@pytest.fixture
def driver(browser):
    driver = get_driver(browser)
    yield driver
    driver.quit()

### 4. Tests simply request the `driver` fixture:
def test_login_success(driver):
    ...

No imports needed — pytest injects fixtures automatically.

---

## 🏎️ Driver Factory

`utils/driver_factory.py` handles browser setup:

- Chrome → ChromeDriverManager
- Firefox → GeckoDriverManager
- Selenium 4 syntax (`service=...`, `options=...`)
- Window maximisation
- Clean, centralised WebDriver logic

---

## 🧱 Page Object Model (POM)

Each page is represented as a class with:

- Locators
- Page actions
- Helper methods

Example usage:

page = LoginPage(driver)
page.load(settings.BASE_URL)
page.login(username, password)
message = page.get_message()

---

## 🧪 Example Test (test_login.py)

def test_login_success(driver):
    page = LoginPage(driver)
    page.load(settings.BASE_URL)
    page.login(settings.VALID_USERNAME, settings.VALID_PASSWORD)
    assert "You logged into a secure area!" in page.get_message()

---

## 📝 Logging

All tests use a shared logger:

logger = get_logger()
logger.info("Starting test...")

Logs include timestamps, log levels, and messages.

---

## 🔧 Configuration

All test data and URLs live in:

config/settings.py

Example:

BASE_URL = "https://the-internet.herokuapp.com/login"
VALID_USERNAME = "tomsmith"
VALID_PASSWORD = "SuperSecretPassword!"

---

## 📌 Design Choices

- **PyTest** for fixtures, readability, and plugin ecosystem
- **POM** for maintainability and scalability
- **Driver Factory** to centralise WebDriver logic
- **Logging** for debugging and interview demonstration
- **Config module** for clean separation of test data

---

## 🚀 Future Improvements

If given more time, the following enhancements could be added:

- CI pipeline (GitHub Actions)
- Parallel execution (pytest-xdist)
- Environment switching (dev/stage/prod)
- Allure reporting
- Dockerised test execution
- Test data from JSON/YAML
- Retry logic for flaky tests

---

## ✔ Summary

This framework is clean, modular, and interview-ready.
It demonstrates strong understanding of:

- Selenium WebDriver
- PyTest fixtures
- POM design
- Logging
- Test architecture
- Browser configuration

Perfect for showcasing automation engineering skills.