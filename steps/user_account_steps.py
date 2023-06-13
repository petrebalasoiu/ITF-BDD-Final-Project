from behave import *


@given('the user is on the login page')
def step_given_user_on_login_page(context):
    context.user_account_page.navigate_to_login_page()


@when('the user inserts username "{username}" and password "{password}"')
def step_when_user_inserts_credentials(context, username, password):
    context.user_account_page.insert_username(username)
    context.user_account_page.insert_password(password)


@when('the user clicks on the login button')
def step_impl(context):
    context.user_account_page.click_login_button()


@then('the user is successfully logged into the account')
def step_impl(context):
    context.user_account_page.check_login_and_logout()


@then('the user is prompted with the "Invalid password" and cannot log into the application')
def step_impl(context):
    context.user_account_page.check_invalid_password_error()


@then('the user is prompted with the "Invalid username" and cannot log into the application')
def step_impl(context):
    context.user_account_page.check_invalid_username_error()


@then('the user is prompted with the "Invalid username" error and cannot log into the application')
def step_impl(context):
    context.user_account_page.check_invalid_username_error2()


@when('the user inserts only the username and not the password')
def step_impl(context):
    context.user_account_page.insert_username()


@when('the user inserts only the password and not the username')
def step_impl(context):
    context.user_account_page.insert_password()
