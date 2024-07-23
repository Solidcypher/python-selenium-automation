from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target product {product_id} page')
def open_specific_product_page(context, product_id):
    context.app.product_page.open_product_page(product_id)


@then('Verify that the user can click on each color')
def verify_and_click_on_color(context):
    context.app.product_page.click_on_and_verify_color()


