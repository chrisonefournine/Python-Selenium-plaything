from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class DragDropPage(BasePage):
    _column_a = {"by": By.CSS_SELECTOR, "value": "#column-a"}
    _column_b = {"by": By.CSS_SELECTOR, "value": "#column-b"}

    def __init__(self, driver):
        self.driver = driver
        self._visit("/drag_and_drop")
        assert self._is_displayed(self._column_a)
        assert self._is_displayed(self._column_b)

    def drag_a_to_b(self):
        self._drag_element(self._column_a, self._column_b)
        time.sleep(1)
        return self._verify_text(self._column_b) == "A"

    def drag_b_to_a(self):
        self._drag_element(self._column_b, self._column_a)
        time.sleep(1)
        return self._verify_text(self._column_b) == "B"