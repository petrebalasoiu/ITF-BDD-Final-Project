from behave import *

@given('the user has searched for a band name')
def step_impl(context):
    context.shopping_cart_page.new_url_after_search()

# +1
@when('the user clicks to add one item into the cart')
def step_impl(context):
    context.shopping_cart_page.add_item_to_cart()

@when('the user clicks view the cart')
def step_impl(context):
    context.shopping_cart_page.open_shopping_cart()


@then('the item has been added to the user\'s cart')
def step_impl(context):
    context.shopping_cart_page.item_added_to_cart()


@when('the user clicks to remove the item from the shopping cart')
def step_impl(context):
    context.shopping_cart_page.remove_item_from_cart()


@then('the item has been removed from the user\'s cart')
def step_impl(context):
    context.shopping_cart_page.item_removed_from_cart()


@when('the user clicks to add one item to the Wishlist')
def step_impl(context):
    context.shopping_cart_page.add_item_to_wishlist()


@when('the user clicks to view the Wishlist')
def step_impl(context):
    context.shopping_cart_page.open_wishlist()


@then('the item has been added to the user\'s Wishlist')
def step_impl(context):
    context.shopping_cart_page.item_added_to_wishlist()


@when('the user clicks to remove the item from the Wishlist')
def step_impl(context):
    context.shopping_cart_page.remove_item_from_wishlist()


@then('the item has been removed from the user\'s Wishlist')
def step_impl(context):
    context.shopping_cart_page.item_removed_from_wishlist()


# ------------------- SOON TO BE IMPLEMENTED -------------------
# @when('The user has at least one item into the shopping cart')
# def step_impl(context):
#     pass
#
# @when('The user clicks on "COSUL MEU" button to view the items in the cart')
# def step_impl(context):
#     pass
#
#
# @when('The user clicks to remove an item from the shopping cart')
# def step_impl(context):
#     pass
#
#
# @then('The the item has been removed from the user\'s cart')
# def step_impl(context):
#     pass
#
#
# @when('The user has at least one item into the wishlist')
# def step_impl(context):
#     pass
#
#
# @when('The user clicks on "Wishlist" button to view the items added to the list')
# def step_impl(context):
#     pass
#
#
# @when('The user clicks to remove an item from the wishlist')
# def step_impl(context):
#     pass
#
#
# @then('The the item has been removed from the user\'s wishlist')
# def step_impl(context):
#     pass
#
# # +1
# @when('The user successfully logs into the account')
# def step_impl(context):
#     pass
#
# @when('The user relogs into the account')
# def step_impl(context):
#     pass
#
# @then('The item added before relog has been saved into the shopping cart and is visible')
# def step_impl(context):
#     pass
#
# @then('The item added before relog has been saved into the wishlist and is visible')
# def step_impl(context):
#     pass