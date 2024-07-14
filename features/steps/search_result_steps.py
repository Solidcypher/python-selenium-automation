from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click searched {searched_product}')
def click_on_searched_product(context, searched_product):
    # will click on first product on page
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='product-title']").click()
    sleep(2)


@when('Click add to cart on search page')
def click_add_to_cart_on_search(context):
    # will click on the add to cart of first product on page
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
    sleep(2)


@then('Verify search results for {expected_product}')
def verify_search_results(context, expected_product):
    # get text of the search result
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text

    assert expected_product in actual_text, f"Expected {expected_product} not included in {actual_text}"
    print('Test case Passed.')

