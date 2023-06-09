from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import signal


class SearchResultsPage(BasePage):
    SEARCH_BAR = (By.XPATH, "//input[@class='autosearch-input form-control']")
    SEARCH_CONFIRM = (By.XPATH, "//button[@class='button-search btn btn-primary']")
    SEARCH_RESULTS = (By.XPATH, "//div[contains(@class, 'product-layout')]")
    FILTER_CATEGORY = (By.XPATH, "//ul[@id='subcat402']//span[text()='Tricouri cu formatii']")
    FILTER_RESULTS = (By.XPATH, "//div[@class='products-list row grid']")
    DROPDOWN_OPTIONS = (By.XPATH, "//select[@class='form-control']")
    PRICE_LIST = (By.XPATH, "//span[@class='price-new priceValue']")
    FILTERS_APPLIED = (By.XPATH, "//a[@class='link_reset']")
    FILTER_BOX = (By.XPATH, "//div[@class='box-category']")
    BUTTON_FILTER_RESET = (By.XPATH, '//a[@class="link_reset" and contains(text(), "Reseteaza filtre")]')
    # >>>>>> temp
    ACCEPT_COOKIES = (By.XPATH, "//a[contains(@class, 'btn_accept_all_cookies')]")

    # >>>>>> temp
    def accept_cookies(self):
        self.driver.find_element(*self.ACCEPT_COOKIES).click()

    def item_search(self):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('metallica')
        self.driver.find_element(*self.SEARCH_CONFIRM).click()

    def number_of_results(self):
        result_list = self.driver.find_elements(*self.SEARCH_RESULTS)
        assert len(result_list) <= 30, "Error, the search returns up to 30 items per page"

    def filter_items_per_category(self):
        select_category = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FILTER_CATEGORY))
        select_category.click()

    # Needing help with the methods below :(

    def filter_applied(self):
        result_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTER_RESULTS))
        filter_functional = True
        for i in range(len(result_list)):
            href = result_list[i].get_attribute("href").text
            if href != "Tricou":
                filter_functional = False
        assert filter_functional == True, "Error: The filter does not function properly."

    def dropdown_selection_asc(self):
        dropdown_list = Select(self.driver.find_element(*self.DROPDOWN_OPTIONS))
        dropdown_list.select_by_visible_text("Price Crescator")

    def items_sorted_asc(self):
        price_list = self.driver.find_elements(*self.PRICE_LIST)
        price_is_sorted_asc = True
        for i in range(len(price_list) - 1):
            for j in range(i + 1, len(price_list)):
                if int(price_list[i]) > int(price_list[j]):
                    price_is_sorted_asc = False
        assert price_is_sorted_asc == True, "Error, the sorting was not successful"

    def dropdown_selection_des(self):
        dropdown_list = Select(self.driver.find_element(*self.DROPDOWN_OPTIONS))
        dropdown_list.select_by_visible_text("Price Descrescator")

    def items_sorted_des(self):
        price_list = self.driver.find_elements(*self.PRICE_LIST)
        price_is_sorted_asc = True
        for i in range(len(price_list) - 1):
            for j in range(i + 1, len(price_list)):
                if int(price_list[i]) < int(price_list[j]):
                    price_is_sorted_asc = False
        assert price_is_sorted_asc == True, "Error, the sorting was not successful"

    def reset_filters(self):
        self.driver.find_element(*self.BUTTON_FILTER_RESET).click()

    def filters_reset(self):
        filters = self.driver.find_element(*self.FILTERS_APPLIED)
        filter_box = self.driver.find_element(*self.FILTER_BOX)
        assert filters.is_displayed() in filter_box, "Error, the filters were not removed"


