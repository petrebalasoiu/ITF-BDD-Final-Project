from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Browser():

    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()

    ACCEPT_COOKIES = (By.XPATH, "//a[contains(@class, 'btn_accept_all_cookies')]")

    ####################### accepting cookies needs adjusted but the methods don't work

    def accept_cookies(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()

    def quit_browser(self):
        self.driver.quit()




