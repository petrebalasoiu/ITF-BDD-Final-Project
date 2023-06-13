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
        self.driver.get('https://www.bestial.ro/')

    def check_page_title(self):
        expected = 'Bestial Magazin de tricouri din Timisoara - Bestial.ro'
        actual = self.driver.title
        assert expected == actual, 'The page title does not match'

    def click_logo_button(self):
        logo_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.LOGO_BUTTON))
        logo_button.click()

    def check_home_page(self):
        expected = 'https://www.bestial.ro/'
        actual = self.driver.current_url
        assert expected == actual, 'The home page does not match'

    def click_home_button(self):
        home_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.HOME_BUTTON))
        home_button.click()

    def click_new_products_button(self):
        new_products_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.NEW_PRODUCTS_BUTTON))
        new_products_button.click()

    def check_new_products_page(self):
        expected = 'https://www.bestial.ro/produse-noi.html'
        actual = self.driver.current_url
        assert expected in actual, 'The products page does not match'

    def click_manufacturers_button(self):
        manufacturers_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.MANUFACTURERS_BUTTON))
        manufacturers_button.click()

    def check_manufacturers_page(self):
        expected = 'https://www.bestial.ro/producatori.html'
        actual = self.driver.current_url
        assert expected in actual, 'The manufacturers page does not match'

    def click_contact_button(self):
        contact_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CONTACT_BUTTON))
        contact_button.click()

    def check_contact_page(self):
        expected = 'https://www.bestial.ro/contact.html'
        actual = self.driver.current_url
        assert expected in actual, 'The contact page does not match'
        assert 'https://www.bestial.ro/contact.html' in self.driver.current_url

    def type_in_search_bar(self):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('Linkin Park')

    def click_to_search(self):
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SEARCH_CONFIRM))
        search_button.click()

    def check_search_functionality(self):
        search_term = 'Linkin Park'
        page_source = self.driver.page_source
        assert search_term.upper() in page_source.upper(), f'The search term {search_term} was not found'