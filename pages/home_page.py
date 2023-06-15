from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    LOGO_BUTTON = (By.XPATH, "//img[@src='images/logo.jpg']")
    HOME_BUTTON = (By.XPATH, "//a[@href='https://www.bestial.ro/']")
    NEW_PRODUCTS_BUTTON = (By.XPATH, "//a[strong[text()='Produse noi']]")
    MANUFACTURERS_BUTTON = (By.XPATH, "//a[strong[text()='Producatori']]")
    CONTACT_BUTTON = (By.XPATH, "//a[strong[text()='Contact']]")
    SEARCH_BAR = (By.XPATH, "//input[@class='autosearch-input form-control']")
    SEARCH_CONFIRM = (By.XPATH, "//button[@class='button-search btn btn-primary']")

    def navigate_to_homepage(self):
        hope_page_url = 'https://www.bestial.ro/'
        self.driver.get(hope_page_url)

    def check_page_title(self):
        expected = 'Bestial Magazin de tricouri din Timisoara - Bestial.ro'
        actual = self.driver.title
        assert expected == actual, f"Page title mismatch. Expected: '{expected}', Actual: '{actual}'"

    def click_logo_button(self):
        self.wait_and_click_element_by_selector(*self.LOGO_BUTTON)

    def check_home_page(self):
        expected = 'https://www.bestial.ro/'
        actual = self.driver.current_url
        assert expected == actual, f"Current URL mismatch. Expected: '{expected}', Actual: '{actual}'"

    def click_home_button(self):
        self.wait_and_click_element_by_selector(*self.HOME_BUTTON)

    def click_new_products_button(self):
        self.wait_and_click_element_by_selector(*self.NEW_PRODUCTS_BUTTON)

    def check_new_products_page(self):
        expected = 'https://www.bestial.ro/produse-noi.html'
        actual = self.driver.current_url
        assert expected in actual, f"Current URL mismatch. Expected: '{expected}', Actual: '{actual}'"

    def click_manufacturers_button(self):
        self.wait_and_click_element_by_selector(*self.MANUFACTURERS_BUTTON)

    def check_manufacturers_page(self):
        expected = 'https://www.bestial.ro/producatori.html'
        actual = self.driver.current_url
        assert expected in actual, f"Current URL mismatch. Expected: '{expected}', Actual: '{actual}'"

    def click_contact_button(self):
        self.wait_and_click_element_by_selector(*self.CONTACT_BUTTON)

    def check_contact_page(self):
        expected = 'https://www.bestial.ro/contact.html'
        actual = self.driver.current_url
        assert expected in actual, 'The contact page does not match'

    def type_in_search_bar(self):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('Linkin Park')

    def click_to_search(self):
        self.wait_and_click_element_by_selector(*self.SEARCH_CONFIRM)

    def check_search_functionality(self):
        search_term = 'Linkin_Park'
        current_url = self.driver.current_url
        assert search_term.lower() in current_url.lower(), f'The search term \'{search_term}\' was not found'
