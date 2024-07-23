from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target help page')
def open_target(context):
    context.app.help_page.open_help_page()


@then('Verify Help page has all {number} UI elements')
def verify_benefit_cells_amount(context, number):
    context.app.help_page.verify_help_ui_elements(number)
