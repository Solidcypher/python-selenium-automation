from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()


@when('Click on sign in icon')
def click_signin_icon(context):
    context.app.header.click_signin()


@when('Click on sign in on side navigation')
def click_signin_on_side_navigation(context):
    context.app.side_nav.click_signin_side_nav()


@when('Click on Target Circle link')
def click_target_circle_link(context):
    context.app.header.click_target_circle()


@when('Click on Target Help link')
def click_target_help_link(context):
    context.app.header.click_help_link()


