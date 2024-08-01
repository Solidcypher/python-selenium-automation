from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target help page')
def open_target(context):
    context.app.help_page.open_help_page()


@given('Open Target Help Returns page')
def open_target_returns_page(context):
    context.app.help_page.open_help_return_page()


@when('Select {dd_topic} in dropdown menu')
def select_dd_topic(context, dd_topic):
    context.app.help_page.select_dropdown_topic(dd_topic)


@then('Verify {header_text} page opened')
def verify_returns_page(context, header_text):
    context.app.help_page.verify_header_text(header_text)


# @then('Verify Delivery & Pickup page opened')
# def verify_delivery_and_pickup_page(context):
#     context.app.help_page.verify_delivery_pickup_page_open()


@then('Verify Help page has all {number} UI elements')
def verify_benefit_cells_amount(context, number):
    context.app.help_page.verify_help_ui_elements(number)
