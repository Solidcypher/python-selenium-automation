from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target help page')
def open_target(context):
    context.driver.get('https://help.target.com/help')
    sleep(2)


@then('Verify Help page has all {number} UI elements')
def verify_benefit_cells_amount(context, number):
    context.driver.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]")
    context.driver.find_element(By.CLASS_NAME, "search_input")
    context.driver.find_element(By.CSS_SELECTOR, "[alt='search']")
    context.driver.find_element(By.CLASS_NAME, "box-column")
    context.driver.find_element(By.CLASS_NAME, "grid_6")
    context.driver.find_elements(By.CLASS_NAME, "grid_4")
    context.driver.find_elelment(By.XPATH, "//h2[contains(text(),'Browse all Help pages')]")


    # I am not sure how you would assert all of these. I think the homework only asked for the locators.