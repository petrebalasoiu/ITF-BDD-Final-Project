from browser import Browser
from pages.home_page import HomePage
from pages.user_account_page import UserAccountPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.search_results_page import SearchResultsPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.user_account_page = UserAccountPage()
    context.shopping_cart_page = ShoppingCartPage()
    context.search_results_page = SearchResultsPage()


def after_all(context):
    context.browser.close_browser()
