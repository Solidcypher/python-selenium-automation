from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Input email address')
def input_email_address(context):
    context.app.sign_in_page.input_email()


@when('Input incorrect email address')
def input_incorrect_email_address(context):
    context.app.sign_in_page.input_incorrect_email()


@when('Input password')
def input_password(context):
    context.app.sign_in_page.input_password()


@when('Click sign in')
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.sign_in_page.get_current_window()


@when('Click Terms and Conditions link')
def click_tc_link(context):
    context.app.sign_in_page.click_tc_link()


@when('Switch to newly opened window')
def switch_to_new_window(context):
    context.app.sign_in_page.switch_to_new_window()


@then('Verify Terms and Conditions page is open')
def verify_pp_opened(context):
    context.app.terms_and_conditions_page.verify_pp_url()


@then('Verify user is logged in')
def verify_user_logged_in(context):
    context.app.sign_in_page.verify_user_logged_in()


@then('Verify sign in page appears')
def verify_signin_page_appears(context):
    context.app.sign_in_page.verify_sign_in_page_appears()


@then('Verify sign in error message appears')
def verify_signin_error_message(context):
    context.app.sign_in_page.verify_sign_in_error_message()


@then('User can close current page')
def close_current_page(context):
    context.app.sign_in_page.close()


@then('user can return to original window')
def return_to_original_window(context):
    context.app.terms_and_conditions_page.switch_to_window_by_id(context.original_window)
