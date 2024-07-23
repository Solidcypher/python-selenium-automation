from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep


class ProductPage(BasePage):
    PICKUP_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
    PRODUCT_COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li")
    INDIVIDUAL_COLOR_OPTION = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

    def open_product_page(self, product_id):
        self.driver.get(f'https://www.target.com/p/{product_id}')
        sleep(4)

    def pickup_add_to_cart(self):
        self.click(*self.PICKUP_ADD_TO_CART_BTN)

    def click_on_and_verify_color(self):
        expected_colors = ['Black/White/Gray', 'Pastel', 'Jewel Tones']
        actual_colors = []

        colors = self.driver.find_elements(*self.PRODUCT_COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
        for color in colors:
            color.click()

            selected_color = self.driver.find_element(*self.INDIVIDUAL_COLOR_OPTION).text  # 'Color\nBlack'
            print('Current color', selected_color)

            selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
            actual_colors.append(selected_color)
            print(actual_colors)

        assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

