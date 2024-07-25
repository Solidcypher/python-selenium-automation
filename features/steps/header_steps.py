from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search(product)


@when('Click on cart icon')
def click_cart_icon(context):
    context.app.header.click_cart_icon()


@when('Click on sign in icon')
def click_signin_icon(context):
    context.app.header.click_signin()


@when('Click on Target Circle link')
def click_target_circle_link(context):
    context.app.header.click_target_circle()


@when('Click on Target Help link')
def click_target_help_link(context):
    context.app.header.click_help_link()
