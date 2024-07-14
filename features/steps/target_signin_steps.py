from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify sign in page appears')
def verify_signin_page_appears(context):
    expected_text = "Sign into your Target account"
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(),'Sign into your Target account')]").text

    assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

    print("Test case Passed")