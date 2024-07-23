from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on close X')
def click_decline_coverage(context):
    context.app.side_nav.click_on_close_x()
