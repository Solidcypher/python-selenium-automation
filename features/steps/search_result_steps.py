from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click searched {searched_product}')
def click_on_searched_product(context, searched_product):
    # will click on first product on page
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='product-title']"))).click()


@when('Click add to cart on search page')
def click_add_to_cart_on_search(context):
    # will click on the add to cart of first product on page
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='chooseOptionsButton']"))).click()


@then('Verify search results for {expected_product}')
def verify_search_results(context, expected_product):
    # get text of the search result
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text

    assert expected_product in actual_text, f"Expected {expected_product} not included in {actual_text}"
    print('Test case Passed.')


@then('Verify all products have product name and product picture')
def verify_all_products_name_picture(context):
    # scroll to be able to see all products
    context.driver.execute_script("window.scrollBy(0, 5000)", "")
    sleep(3)
    context.driver.execute_script("window.scrollBy(0, 5000)", "")

    # Picked this CSS locator. Not sure if it makes a difference since it is different from the one used in class
    products = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")

    for product in products:
        picture = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")
        title = context.driver.find_element(By.CSS_SELECTOR, "[data-test='product-title']").text

        assert picture, f"Expected {picture} not included in {product}"
        assert title, f"Expected {title} not included in {product}"

