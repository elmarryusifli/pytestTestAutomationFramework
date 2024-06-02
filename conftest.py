import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def pytest_configure(config):
    config.option.htmlpath = 'reports/report.html'
