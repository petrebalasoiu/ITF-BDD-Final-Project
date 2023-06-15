from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UserAccountPage(BasePage):
    FIELD_USERNAME = (By.XPATH, "//input[@id='username']")
    FIELD_PASSWORD = (By.XPATH, "//input[@id='password']")
    BUTTON_LOGIN = (By.XPATH, "//input[@value='Logare']")
    BUTTON_LOGOUT = (By.XPATH, "//a[@href='/logout.html']")
    BUTTON_MY_ACCOUNT = (By.XPATH, "//a[@href='/contul-meu.html']")
    LOGIN_CONFIRMED = (By.XPATH, "//span[@id='active']")
    ERROR_USERNAME1 = (By.XPATH, "//div[@class='error' and text()='Utilizatorul nu exista!']")
    ERROR_USERNAME2 = (By.XPATH, "//div[@class='error' and text()='Utilizator invalid!']")
    ERROR_PASSWORD = (By.XPATH, "//div[@class='error' and text()='Parola incorecta!']")

    def navigate_to_login_page(self):
        login_page_url = 'https://www.bestial.ro/login.html'
        self.driver.get(login_page_url)

    def insert_username(self, username="test.user1"):
        username_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIELD_USERNAME))
        username_input.send_keys(username)

    def insert_password(self, password="test"):
        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FIELD_PASSWORD))
        password_input.send_keys(password)

    def click_login_button(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_LOGIN)

    def check_login(self):
        user_login_confirmation = self.driver.find_element(*self.LOGIN_CONFIRMED)
        assert user_login_confirmation.is_displayed(), 'Login unsuccessful'

    def user_logout(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_MY_ACCOUNT)
        self.wait_and_click_element_by_selector(*self.BUTTON_LOGOUT)

    def check_invalid_username_error(self):
        invalid_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ERROR_USERNAME1))
        assert invalid_username.is_displayed(), 'Login successful'

    def check_invalid_username_error2(self):
        invalid_username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ERROR_USERNAME2))
        assert invalid_username.is_displayed(), 'Login successful'

    def check_invalid_password_error(self):
        invalid_password = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ERROR_PASSWORD))
        assert invalid_password.is_displayed(), 'Login successful'
