from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target product {product_id} page')
def open_specific_product_page(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(4)


@then('Verify that the user can click on each color')
def verify_and_click_on_color(context):
    expected_colors = ['Black/White/Gray', 'Pastel', 'Jewel Tones']
    actual_colors = []

    colors = context.driver.find_elements(By.CSS_SELECTOR, "div[aria-label='Carousel'] li")  # [webelement1, webelement2, webelement3]
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div").text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

