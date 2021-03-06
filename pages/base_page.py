from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select as WebDriverSelect
from example_tests import config

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    def _visit(self, url):
         if url.startswith("http"):
             self.driver.get(url)
         else:
             self.driver.get(config.baseurl + url)

    def _maximize_window(self):
        self.driver.maximize_window()

    def _find(self, locator):
        return self.driver.find_element(locator["by"], locator["value"])

    def _click(self, locator):
        self._find(locator).click()

    def _type(self, locator, input_text):
        self._find(locator).send_keys(input_text)

    def _is_displayed(self, locator):
        try:
            self._find(locator).is_displayed()
        except NoSuchElementException:
                return False
        return True

    def _element_count(self, locator, element_count):
        count = len(self.driver.find_elements(locator["by"], locator["value"]))
        if element_count == count:
            return True
        else:
            print "Sorry to be a letdown but the element count was actually %s as opposed " \
                  "to the %s you were expecting" % (count, element_count)
            return False

    def _wait_for_is_displayed(self, locator, timeout):
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(
                expected_conditions.visibility_of_element_located(
                    (locator['by'], locator['value'])))
        except TimeoutException("The element could not be found afe=ter waiting %s seconds" % timeout):
            return False
        return True

    def _verify_css_value(self, locator, attribute, value):
            css_property = self._find(locator).value_of_css_property(attribute).lower()
            if value.lower() in css_property:
                return True
            else:
                print "The value expected was %s but was actually %s" % (value, css_property)
                return False

    def _verify_text(self, locator):
        return self._find(locator).text

    def _drag_element(self, element, target):
        drag_drop = ActionChains(self.driver)
        drag_drop.click_and_hold(element).move_by_offset(-1, -1).move_to_element(target).release().perform()

    def _select_dropdown(self, locator, option_number):
        select_list = WebDriverSelect(locator)
        select_list.select_by_visible_text(option_number)
        selected_option = select_list.first_selected_option.text
        return selected_option == option_number, ("Selected option should be " + (option_number))

    def _switch_frame(self, locator):
        self.driver.switch_to_frame(locator)

    def _is_enabled(self, locator):
        return self._find(locator).is_enabled

    def _page_title(self, page_title):
        title = self.driver.title
        if page_title == title:
            return True
        else:
            print "Page title expected was %s but was actually %s " % (page_title, title)
            return False







