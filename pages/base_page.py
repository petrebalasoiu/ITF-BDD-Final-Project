from browser import Browser

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait


class BasePage(Browser):
    pass

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def find_element(self, locator):
    #     return self.driver.find_element(*locator)
    #
    # def wait_for_element_visibility(self, locator, timeout=10):
    #     WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    #
    # def wait_for_element_clickable(self, locator, timeout=10):
    #     WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #
    # def click_element(self, locator):
    #     element = self.find_element(locator)
    #     element.click()
    #
    # def enter_text(self, locator, text):
    #     element = self.find_element(locator)
    #     element.clear()
    #     element.send_keys(text)
    #
    # def get_element_text(self, locator):
    #     element = self.find_element(locator)
    #     return element.text
    #
    # def exp_wait(self, selector, timeout=10):
    #     WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(selector))
    #
    #
    # def is_element_visible(self, locator):
    #     try:
    #         self.wait_for_element_visibility(locator, timeout=5)
    #         return True
    #     except TimeoutException:
    #         return False
    #
    # def is_element_present(self, locator):
    #     elements = self.driver.find_elements(*locator)
    #     return len(elements) > 0
    #
    # def get_page_title(self):
    #     return self.driver.title
    #
    # def switch_to_frame(self, locator):
    #     frame = self.find_element(locator)
    #     self.driver.switch_to.frame(frame)
    #
    # def switch_to_default_content(self):
    #     self.driver.switch_to.default_content()
    #
    # def take_screenshot(self, filename):
    #     self.driver.save_screenshot(filename)
    #
    # def scroll_to_element(self, locator):
    #     element = self.find_element(locator)
    #     self.driver.execute_script("arguments[0].scrollIntoView(true);", element)