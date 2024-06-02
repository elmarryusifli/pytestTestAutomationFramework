import logging

class BrowserHelper:
    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)

    def switch_to_window(self, target_title):
        original_window = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == target_title:
                return
        self.driver.switch_to.window(original_window)

    def switch_to_parent_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.logger.info("Switched to parent window")

    def switch_to_parent_with_child_close(self):
        parent_window = self.driver.window_handles[0]
        for handle in self.driver.window_handles[1:]:
            self.driver.switch_to.window(handle)
            self.driver.close()
        self.driver.switch_to.window(parent_window)
        self.logger.info("Closed child windows and switched to parent window")

    def switch_to_frame(self, locator):
        self.driver.switch_to.frame(self.driver.find_element(*locator))
        self.logger.info(f"Switched to frame: {locator}")

    def switch_to_frame_by_id(self, name_or_id):
        self.driver.switch_to.frame(name_or_id)
        self.logger.info(f"Switched to frame: {name_or_id}")
