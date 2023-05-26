from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from time import sleep


class HomePage(BasePage):
    LOGO_BUTTON = (By.XPATH, "//img[@src='images/logo.jpg']")
    HOME_BUTTON = (By.XPATH, "//a[@href='https://www.bestial.ro/']")
    NEW_PRODUCTS_BUTTON = (By.XPATH, "//a[strong[text()='Produse noi']]")
    MANUFACTURERS_BUTTON = (By.XPATH, "//a[strong[text()='Producatori']]")
    CONTACT_BUTTON = (By.XPATH, "//a[strong[text()='Contact']]")
    SEARCH_BAR = (By.XPATH, "//input[@class='autosearch-input form-control']")
    SEARCH_CONFIRM = (By.XPATH, "//button[@class='button-search btn btn-primary']")

    def navigate_to_homepage(self):
        self.driver.get("https://www.bestial.ro/")

    def assert_page_title(self):
        expected = "Bestial Magazin de tricouri din Timisoara - Bestial.ro"
        assert self.driver.title, expected

    def click_logo_button(self):
        self.driver.find_element(*self.LOGO_BUTTON).click()

    def assert_home_page(self):
        assert 'https://www.bestial.ro/' in self.driver.current_url

    def click_home_button(self):
        self.driver.find_element(*self.HOME_BUTTON).click()

    def click_new_products_button(self):
        self.driver.find_element(*self.NEW_PRODUCTS_BUTTON).click()

    def assert_new_products_page(self):
        assert 'https://www.bestial.ro/produse-noi.html' in self.driver.current_url

    def click_manufacturers_button(self):
        self.driver.find_element(*self.MANUFACTURERS_BUTTON).click()

    def assert_manufacturers_page(self):
        assert 'https://www.bestial.ro/producatori.html' in self.driver.current_url

    def click_contact_button(self):
        self.driver.find_element(*self.CONTACT_BUTTON).click()

    def assert_contact_page(self):
        assert 'https://www.bestial.ro/contact.html' in self.driver.current_url

    def type_in_search_bar(self):
        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('Linkin Park')

    def click_to_search(self):
        self.driver.find_element(*self.SEARCH_CONFIRM).click()

    def assert_search_functionality(self):
        search_term = 'Linkin Park'
        assert search_term.upper() in self.driver.page_source.upper(), f'The search term {search_term} was not found'
