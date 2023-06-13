from behave import *


@given('the user is on the homepage and has searched for an item')
def step_impl(context):
    context.home_page.navigate_to_homepage()
    context.search_results_page.item_search()


@then('the first page displayed contains 30 items')
def step_impl(context):
    context.search_results_page.check_number_of_results()


@when('the user clicks on a certain item type to be filtered')
def step_impl(context):
    context.search_results_page.accept_cookies()
    context.search_results_page.filter_items_per_category()


@then('the page displays only filtered items')
def step_impl(context):
    context.search_results_page.check_filter_applied()


@when('the user selects the ascending order from the dropdown menu')
def step_impl(context):
    context.search_results_page.dropdown_selection_asc()


@then('the page displays the items from the lowest to the highest price')
def step_impl(context):
    context.search_results_page.check_items_sorted_asc()


@when('the user selects the descending order from the dropdown menu')
def step_impl(context):
    context.search_results_page.dropdown_selection_des()


@then('the page displays the items from the highest to the lowest price')
def step_impl(context):
    context.search_results_page.check_items_sorted_des()


@when('the user clicks on the filter reset button')
def step_impl(context):
    context.search_results_page.reset_filters()


@then('all the filters are removed and the page refreshes with the original search')
def step_impl(context):
    context.search_results_page.check_filters_reset()
