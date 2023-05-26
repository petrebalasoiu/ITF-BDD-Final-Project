from behave import *

@given('Given the user is on the home page')
def step_impl(context):
    pass

# +1
@when('The user clicks on the "ADAUGA IN COS" button under any item')
def step_impl(context):
    pass


@then('The item is added to the user\'s cart and the item count increased by one')
def step_impl(context):
    pass


@when('The user clicks on the heart button under any item')
def step_impl(context):
    pass


@then('The item is added to the user\'s wishlist and the item count increased by one')
def step_impl(context):
    pass


@when('The user has at least one item into the shopping cart')
def step_impl(context):
    pass

@when('The user clicks on "COSUL MEU" button to view the items in the cart')
def step_impl(context):
    pass


@when('The user clicks to remove an item from the shopping cart')
def step_impl(context):
    pass


@then('The the item has been removed from the user\'s cart')
def step_impl(context):
    pass


@when('The user has at least one item into the wishlist')
def step_impl(context):
    pass


@when('The user clicks on "Wishlist" button to view the items in the cart')
def step_impl(context):
    pass


@when('The user clicks to remove an item from the wishlist')
def step_impl(context):
    pass


@then('The the item has been removed from the user\'s wishlist')
def step_impl(context):
    pass

# +1
@when('The user successfully logs into the account')
def step_impl(context):
    pass

@when('The user relogs into the account')
def step_impl(context):
    pass

@then('The item added before relog has been saved into the shopping cart and is visible')
def step_impl(context):
    pass

@then('The item added before relog has been saved into the wishlist and is visible')
def step_impl(context):
    pass