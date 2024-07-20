from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click pickup add to cart')
def click_pickup_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='orderPickupButton']"))).click()


@then('Verify empty cart text appears')
def verify_empty_cart_text(context):
    expected_text = "Your cart is empty"
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text

    assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

    print("Test case Passed")


@then('Verify {number} item(s) in cart')
def verify_item_in_cart(context, number):

    items = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='cartItem']")

    assert len(items) == int(number), f"Expected {number} items but got {len(items)}"
    print("Test case Passed")

