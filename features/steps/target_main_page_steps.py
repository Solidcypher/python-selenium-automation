from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC



@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    # find search field and enter text
    context.driver.wait.until(EC.presence_of_element_located((By.ID, 'search'))).send_keys(product)
    # click search button
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']"))).click()


@when('Click on cart icon')
def click_cart_icon(context):
    # find cart icon and click on it
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/CartLink']"))).click()


@when('Click on sign in icon')
def click_signin_icon(context):
    # find signin element and click it
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='@web/AccountLink']"))).click()


@when('Click on sign in on side navigation')
def click_signin_on_side_navigation(context):
    # find sign in element on side navigation and click it
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='accountNav-signIn']"))).click()


@when('Click on Target Circle link')
def click_target_circle_link(context):
    # find target circle link and click it
    context.driver.wait.until(EC.element_to_be_clickable((By.ID, 'utilityNav-circle'))).click()


@when('Click on Target Help link')
def click_target_help_link(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[aria-label='Target Help']"))).click()


