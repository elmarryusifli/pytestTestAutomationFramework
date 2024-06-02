import logging
from selenium.common.exceptions import NoAlertPresentException

class AlertHelper:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def get_alert(self):
        self.logger.debug("Switching to alert")
        return self.driver.switch_to.alert

    def accept_alert(self):
        self.logger.info("Accepting alert")
        self.get_alert().accept()

    def dismiss_alert(self):
        self.logger.info("Dismissing alert")
        self.get_alert().dismiss()

    def get_alert_text(self):
        text = self.get_alert().text
        self.logger.info(f"Alert text: {text}")
        return text

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
            self.logger.info("Alert is present")
            return True
        except NoAlertPresentException:
            self.logger.info("No alert present")
            return False

    def accept_alert_if_present(self):
        if self.is_alert_present():
            self.accept_alert()
            self.logger.info("Accepted alert if present")

    def dismiss_alert_if_present(self):
        if self.is_alert_present():
            self.dismiss_alert()
            self.logger.info("Dismissed alert if present")

    def accept_prompt(self, text):
        if self.is_alert_present():
            alert = self.get_alert()
            alert.send_keys(text)
            alert.accept()
            self.logger.info(f"Accepted prompt with text: {text}")
