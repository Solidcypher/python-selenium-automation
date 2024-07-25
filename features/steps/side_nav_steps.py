from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on sign in on side navigation')
def click_signin_on_side_navigation(context):
    context.app.side_nav.click_signin_side_nav()


@when('Click on close X')
def click_decline_coverage(context):
    context.app.side_nav.click_on_close_x()
