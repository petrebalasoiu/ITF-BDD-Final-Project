from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window() # nu a mers cand am incercat sa-l folosesc ca metoda, am incercat si cu cookies

    def quit_browser(self):
        self.driver.quit()