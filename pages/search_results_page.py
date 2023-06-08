from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException


class SearchResultsPage(BasePage):
    SEARCH_BAR = (By.XPATH, "//input[@class='autosearch-input form-control']")
    SEARCH_CONFIRM = (By.XPATH, "//button[@class='button-search btn btn-primary']")
    SEARCH_RESULTS = (By.XPATH, "//div[contains(@class, 'product-layout')]")
    FILTER_CATEGORY = (By.XPATH, "//ul[@id='subcat402']//span[text()='Tricouri cu formatii']")
    FILTER_RESULTS = (By.XPATH, "//div[@class='products-list row grid']")

    def item_search(self):
        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('tricou')

    def confirm_search(self):
        self.driver.find_element(*self.SEARCH_CONFIRM).click()

    def number_of_results(self):
        result_list = self.driver.find_elements(*self.SEARCH_RESULTS)
        assert len(result_list) <= 30, "Error, the search returns only 30 items per page"

    def filter_items_per_category(self):
        category_filter = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FILTER_CATEGORY))
        category_filter.click()

    # I need help with this one :( I don't want to go with an easy assert again
    def filter_applied(self):
        result_list = self.driver.find_elements(*self.FILTER_RESULTS)
        filter_functional = True
        for i in range(len(result_list)):
            href = result_list[i].get_attribute("href").text
            if href != "Metallica":
                filter_functional = False
        assert filter_functional is True, "Error: The filter does not function properly."


