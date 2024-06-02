import logging
from selenium.common.exceptions import NoSuchElementException

class GenericHelper:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_element(self, locator):
        self.logger.info(locator)
        if self.is_element_present(locator):
            return self.driver.find_element(*locator)
        raise NoSuchElementException(f"Element not found: {locator}")

    def get_element_with_null(self, locator):
        self.logger.info(locator)
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return None

    def is_element_present(self, locator):
        flag = len(self.driver.find_elements(*locator)) >= 1
        self.logger.info(flag)
        return flag
