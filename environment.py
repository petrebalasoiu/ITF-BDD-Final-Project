from browser import Browser
from pages.home_page import HomePage
from pages.user_account_page import UserAccountPage


def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.user_account_page = UserAccountPage()


def after_all(context):
    context.browser.close_browser()
