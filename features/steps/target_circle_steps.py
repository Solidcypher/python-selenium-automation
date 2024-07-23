from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify circle page has {number} benefit cells')
def verify_benefit_cells_amount(context, number):
    context.app.circle_page.verify_benefit_cells(number)
