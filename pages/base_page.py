from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException


class BasePage(Browser):
    ACCEPT_COOKIES = (By.XPATH, "//a[contains(@class, 'btn_accept_all_cookies')]")

    def accept_cookies_now(self):
        try:
            confirm_cookies = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.ACCEPT_COOKIES))
            confirm_cookies.click()
        except TimeoutException:
            print("Timeout: Accept cookies element was not clickable within the specified time.")

    def wait_for_element_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, selector)))

    def wait_and_click_element_by_selector(self, by, selector):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((by, selector)))
        self.driver.find_element(by, selector).click()
