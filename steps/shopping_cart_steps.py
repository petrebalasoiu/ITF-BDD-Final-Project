from behave import *


@given('the user has searched for a band name')
def step_impl(context):
    context.shopping_cart_page.new_url_after_search()


@when('the user clicks to add one item into the cart')
def step_impl(context):
    context.shopping_cart_page.add_item_to_cart()


@when('the user clicks view the cart')
def step_impl(context):
    context.shopping_cart_page.open_shopping_cart()


@then('the item has been added to the user\'s cart')
def step_impl(context):
    context.shopping_cart_page.check_item_added_to_cart()


@when('the user clicks to remove the item from the shopping cart')
def step_impl(context):
    context.shopping_cart_page.remove_item_from_cart()


@then('the item has been removed from the user\'s cart')
def step_impl(context):
    context.shopping_cart_page.check_item_removed_from_cart()


@when('the user clicks to add one item to the Wishlist')
def step_impl(context):
    context.shopping_cart_page.add_item_to_wishlist()


@when('the user clicks to view the Wishlist')
def step_impl(context):
    context.shopping_cart_page.open_wishlist()


@then('the item has been added to the user\'s Wishlist')
def step_impl(context):
    context.shopping_cart_page.check_item_added_to_wishlist()


@when('the user clicks to remove the item from the Wishlist')
def step_impl(context):
    context.shopping_cart_page.remove_item_from_wishlist()


@then('the item has been removed from the user\'s Wishlist')
def step_impl(context):
    context.shopping_cart_page.check_item_removed_from_wishlist()