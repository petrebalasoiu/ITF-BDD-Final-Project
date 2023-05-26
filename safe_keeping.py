from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions


class HomePage(BasePage):
    SEARCH_BAR = (By.XPATH, '//a[contains(@class, "link--skins") and contains(@href, "/shop/skins")]')
    LOGIN_PAGE_BUTTON = (By.XPATH, '//a[@class="link--depth-0 link link--account" and @href="/human"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="edit-name"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    LOG_IN_BUTTON = (By.XPATH, '//button[@id="edit-submit" and @value="Log in"]')
    LOGIN_CONFIRMED = (By.XPATH, '//span[@class="nolink"]')

    def navigate_to_homepage(self):
        self.driver.get("https://dbrand.com/")

    def test_page_title(self):
        expected = "dbrand » Official Shop"
        assert self.driver.title, expected

    def navigate_to_skins_page(self):
        self.driver.get("https://dbrand.com/shop/skins")

    def search_for_skins(self):
        self.driver.find_element(*self.SEARCH_BAR).send_keys('iphone 14')

    def test_search_functionality(self):
        search_term = 'iphone 14'
        assert search_term.lower() in self.driver.page_source.lower(), f'The search term {search_term} was not found'

    def navigate_to_login_screen(self):
        self.driver.get("https://dbrand.com/human")

    def type_user_credentials(self):
        insert_email = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.EMAIL_FIELD))
        insert_email.send_keys('test.user1')
        insert_password = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        insert_password.send_keys('testtest')

    def click_to_authenticate(self):
        self.driver.find_element(*self.LOG_IN_BUTTON).click()

    def test_login_outcome(self):
        assert self.driver.find_element(*self.LOGIN_CONFIRMED) is not None, 'Login unsuccessful'
