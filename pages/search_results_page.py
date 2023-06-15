from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.common import TimeoutException


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


    def accept_cookies(self):
        self.accept_cookies_now()

    def item_search(self):
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('Metallica')
        self.wait_and_click_element_by_selector(*self.SEARCH_CONFIRM)

    def check_number_of_results(self):
        result_list = self.driver.find_elements(*self.SEARCH_RESULTS)
        assert len(result_list) <= 30, "Error, the search returns up to 30 items per page"

    def filter_items_per_category(self):
        self.wait_and_click_element_by_selector(*self.FILTER_CATEGORY)

    def check_filter_applied(self):
        result_list = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(self.FILTER_RESULTS))
        filter_functional = True
        for element in result_list:
            if "Tricou" not in element.text:
                filter_functional = False
                break
        assert filter_functional, "Error: The filter does not function properly."

    def dropdown_selection_asc(self):
        dropdown_list = Select(self.driver.find_element(*self.DROPDOWN_OPTIONS))
        dropdown_list.select_by_visible_text("Price Crescator")

    def check_items_sorted_asc(self):
        price_list = self.driver.find_elements(*self.PRICE_LIST)
        prices = []
        for price_element in price_list:
            price_text = price_element.text.replace(',', '')
            price_value = ''.join(filter(str.isdigit, price_text))
            price = int(price_value)
            prices.append(price)

        sorted_prices = sorted(prices)
        assert prices == sorted_prices, "Error: The items are not sorted in ascending order."

    def dropdown_selection_des(self):
        dropdown_list2 = Select(self.driver.find_element(*self.DROPDOWN_OPTIONS))
        dropdown_list2.select_by_visible_text("Price Descrescator")

    def check_items_sorted_des(self):
        price_list = self.driver.find_elements(*self.PRICE_LIST)
        prices = []
        for price_element in price_list:
            price_text = price_element.text.replace(',', '')
            price_value = ''.join(filter(str.isdigit, price_text))
            price = int(price_value)
            prices.append(price)

        sorted_prices = sorted(prices)
        assert prices == sorted_prices[::-1], "Error: The items are not sorted in descending order."

    def reset_filters(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_FILTER_RESET)

    def check_filters_reset(self):
        try:
            filters = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.FILTERS_APPLIED))
            filter_box = self.driver.find_element(*self.FILTER_BOX)
            assert filters in filter_box, "Error: The filters were not removed"
        except TimeoutException:
            print("Timeout: The filters element was not found within the specified time.")
