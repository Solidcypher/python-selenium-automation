from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify sign in page appears')
def verify_signin_page_appears(context):
    context.app.sign_in_page.verify_sign_in_page_appears()
