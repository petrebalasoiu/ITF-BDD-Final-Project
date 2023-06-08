from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()

    def quit_browser(self):
        self.driver.quit()




