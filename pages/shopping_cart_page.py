from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from time import sleep


class ShoppingCartPage(BasePage):
    SEARCH_BAR = (By.XPATH, "//input[@class='autosearch-input form-control']")
    SEARCH_CONFIRM = (By.XPATH, "//button[@class='button-search btn btn-primary']")
    BUTTON_ADD_ITEM = (By.XPATH, "//div[@id='product54790']//button[@class='addToCart']")
    CLOSE_ITEM_ADDED_POPUP = (By.XPATH, "//button[@class='jGrowl-close']")
    BUTTON_MY_CART = (By.XPATH, "//li[@class='cart']/a[@title='Cosul meu']")
    BUTTON_UPDATE_QUANTITY = (By.XPATH, "//div[@id='kart_bottom']//a[contains(@class, 'btn-default')]")
    FIELD_QUANTITY = (By.XPATH, "//input[@name='qty54790']")
    MESSAGE_EMPTY_CART = (By.XPATH, "//strong[text() = 'Cosul este gol']")
    BUTTON_ADD_WISHLIST = (By.XPATH, "//button[contains(@onclick, 'addToWishlist(54790')]")
    BUTTON_MY_WISHLIST = (By.XPATH, "//a[@href='/wishlist.html']")
    ITEM_IN_WISHLIST = (By. XPATH, "//strong[text()='Geanta 40 cm LINKIN PARK Chester']")
    BUTTON_REMOVE_WISHLIST = (By.XPATH, "//tr[@id='witem54790']//a[contains(@class, 'btn_delete_wishlist')]")

    def new_url_after_search(self):
        self.driver.get("https://www.bestial.ro/")
        search_bar = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.SEARCH_BAR))
        search_bar.send_keys('Linkin Park')
        self.wait_and_click_element_by_selector(*self.SEARCH_CONFIRM)

    def add_item_to_cart(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_ADD_ITEM)
        self.wait_and_click_element_by_selector(*self.CLOSE_ITEM_ADDED_POPUP)

    def open_shopping_cart(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_MY_CART)

    def check_item_added_to_cart(self):
        confirmation = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.BUTTON_UPDATE_QUANTITY))
        assert confirmation.is_displayed(), 'The item was not added'

    def remove_item_from_cart(self):
        remove_item = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.FIELD_QUANTITY))
        remove_item.send_keys(Keys.BACKSPACE)
        remove_item.send_keys("0")
        self.wait_and_click_element_by_selector(*self.BUTTON_UPDATE_QUANTITY)

    def check_item_removed_from_cart(self):
        cart_removal_confirmed = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.MESSAGE_EMPTY_CART))
        assert cart_removal_confirmed.is_displayed(), 'The item was not removed'

    def add_item_to_wishlist(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_ADD_WISHLIST)
        self.wait_and_click_element_by_selector(*self.CLOSE_ITEM_ADDED_POPUP)

    def open_wishlist(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_MY_WISHLIST)

    def check_item_added_to_wishlist(self):
        added_to_wishlist = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ITEM_IN_WISHLIST))
        assert added_to_wishlist.is_displayed(), 'The item was not added'

    def remove_item_from_wishlist(self):
        self.wait_and_click_element_by_selector(*self.BUTTON_REMOVE_WISHLIST)
        test = self.driver.switch_to.alert
        test.accept()
        sleep(1)

    def check_item_removed_from_wishlist(self):
        removed_from_wishlist = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.ITEM_IN_WISHLIST))
        assert removed_from_wishlist.is_displayed() is False, 'The item was not removed'
