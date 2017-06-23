from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DragDropPage(BasePage):
    _tile_a = {"by": By.XPATH, "value": "//div[@id='column-a']"}
    _tile_b = {"by": By.XPATH, "value": "//div[@id='column-b']"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/drag_and_drop")
        assert self._is_displayed(self._title_a)
        assert self._is_displayed(self._title_b)

    def with_(self, username, password):
        self._type(self._username_input, username)
        self._type(self._password_input, password)
        self._click(self._submit_button)

    def success_message_present(self):
        self._wait_for_is_displayed(self._success_message, 1)
        return self._is_displayed(self._success_message)

    def failure_message_present(self):
        self._wait_for_is_displayed(self._failure_message, 1)
        return self._is_displayed(self._failure_message)
