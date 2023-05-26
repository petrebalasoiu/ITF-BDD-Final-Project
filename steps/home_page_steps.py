from behave import *


@given('the user is on the home page')
def step_impl(context):
    context.home_page.navigate_to_homepage()


@then('the home page title matches')
def step_impl(context):
    context.home_page.assert_page_title()


@when('the user clicks on the logo button')
def step_impl(context):
    context.home_page.click_logo_button()


# +1
@then('the user is redirected to the home page')
def step_impl(context):
    context.home_page.assert_home_page()


@when('the user clicks on the "Home" button')
def step_impl(context):
    context.home_page.click_home_button()


@when('the user clicks on the "Produse noi" button')
def step_impl(context):
    context.home_page.click_new_products_button()


@then('the user is redirected to the "Produse noi" page')
def step_impl(context):
    context.home_page.assert_new_products_page()


@when('the user clicks on the "Producatori" button')
def step_impl(context):
    context.home_page.click_manufacturers_button()


@then('the user is redirected to the "Producatori" page')
def step_impl(context):
    context.home_page.assert_manufacturers_page()


@when('the user clicks on the "Contact" button')
def step_impl(context):
    context.home_page.click_contact_button()


@then('the user is redirected to the "Contact" page')
def step_impl(context):
    context.home_page.assert_contact_page()


@when('the user types a product name in the search bar')
def step_impl(context):
    context.home_page.type_in_search_bar()


@when('the user clicks to confirm the search')
def step_impl(context):
    context.home_page.click_to_search()


@then('the items matching the search are presented to the user and displayed in the page source')
def step_impl(context):
    context.home_page.assert_search_functionality()

