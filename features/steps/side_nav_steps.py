from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click decline coverage')
def click_decline_coverage(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='espDrawerContent-declineCoverageButton']"))).click()
