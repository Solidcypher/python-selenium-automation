from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on sign in icon')
def click_signin_icon(context):
    # find signin element and click it
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(2)


@when('Click on sign in on side navigation')
def click_signin_on_side_navigation(context):
    # find sign in element on side navigation and click it
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(1)


@then('Verify sign in page appears')
def verify_signin_page_appears(context):
    expected_text = "Sign into your Target account"
    actual_text = context.driver.find_element(By.XPATH, "//span[contains(text(),'Sign into your Target account')]").text

    assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

    print("Test case Passed")