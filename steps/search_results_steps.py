from behave import *


@given('the user has searched for an item')
def step_impl(context):
    context.search_results_page.item_search()


@when('the user clicks to search')
def step_impl(context):
    context.search_results_page.confirm_search()


@then('the first page displayed contains 30 items')
def step_impl(context):
    context.search_results_page.number_of_results()


@when('the user clicks on a certain item type to be filtered')
def step_impl(context):
    context.search_results_page.filter_items_per_category()


@then('the page displays only filtered items')
def step_impl(context):
    context.search_results_page.filter_applied()


#+1
@when('the user clicks on the sort dropdown')
def step_impl(context):
    pass


@when('the user selects the ascending order')
def step_impl(context):
    pass


@then('the page displays the items from the lowest to the highest price')
def step_impl(context):
    pass


@when('the user selects the descending order')
def step_impl(context):
    pass


@then('the page displays the items from the highest to the lowest price')
def step_impl(context):
    pass


@when('the user clicks on the filter reset button')
def step_impl(context):
    pass


@then('all the filters are removed and the page refreshes with the original search')
def step_impl(context):
    pass
