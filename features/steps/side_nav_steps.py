from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click decline coverage')
def click_decline_coverage(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']").click()
    sleep(2)