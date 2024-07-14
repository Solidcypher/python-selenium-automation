from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify circle page has {number} benefit cells')
def verify_benefit_cells_amount(context, number):

    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")

    assert len(links) == int(number), f"Expected {number} benefit cells but got {len(links)}"
    print('Test case Passed.')
