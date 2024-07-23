from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SideNav(BasePage):
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    CLOSE_X = (By.CSS_SELECTOR, "[aria-label='close']")

    def click_signin_side_nav(self): # Clicks sign in on the side nav
        self.click(*self.SIGNIN_BTN)

    def click_on_close_x(self):
        self.click(*self.CLOSE_X)
