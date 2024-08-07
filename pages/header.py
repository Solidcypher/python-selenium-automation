from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class Header(BasePage):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    HELP_LINK = (By.CSS_SELECTOR, "[aria-label='Target Help']")
    TARGET_CIRCLE = (By.ID, 'utilityNav-circle')

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.wait_and_click(*self.SEARCH_BTN)
        sleep(3)

    def click_cart_icon(self):
        self.wait_and_click(*self.CART_ICON)

    def click_signin(self):
        self.wait_and_click(*self.SIGNIN_BTN)

    def click_help_link(self):
        self.wait_and_click(*self.HELP_LINK)

    def click_target_circle(self):
        self.wait_and_click(*self.TARGET_CIRCLE)