from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Input email address')
def input_email_address(context):
    context.app.sign_in_page.input_email()


@when('Input password')
def input_password(context):
    context.app.sign_in_page.input_password()


@when('Click sign in')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()


@then('Verify sign in page appears')
def verify_signin_page_appears(context):
    context.app.sign_in_page.verify_sign_in_page_appears()
