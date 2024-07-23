from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click add to cart on search page')
def click_add_to_cart_on_search(context):
    context.app.search_results_page.add_to_cart_search_page()


@then('Verify search results for {expected_product}')
def verify_search_results(context, expected_product):
    context.app.search_results_page.verify_text()


@then('Verify correct search results URL opens for {expected_product}')
def verify_url(context, expected_product):
    context.app.search_results_page.verify_url()


@then('Verify all products have product name and product picture')
def verify_all_products_name_picture(context):
    context.app.search_results_page.verify_product_image()

    context.app.search_results_page.verify_product_title()


