from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click pickup add to cart')
def click_pickup_add_to_cart(context):
    context.app.product_page.pickup_add_to_cart()


@then('Verify empty cart text appears')
def verify_empty_cart_text(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify {number} item(s) in cart')
def verify_item_in_cart(context, number):
    context.app.cart_page.verify_items_in_cart(number)

