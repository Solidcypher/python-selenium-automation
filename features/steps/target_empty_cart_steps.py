from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Click on cart icon')
def click_cart_icon(context):
    # find cart icon and click on it
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(3)


@then('Verify empty cart text appears')
def verify_empty_cart_text(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text

    assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

    print("Test case Passed")