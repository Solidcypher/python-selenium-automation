from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    CART_ITEMS = (By.CSS_SELECTOR, "[data-test='cartItem']")

    def verify_empty_cart(self):
        self.wait_for_element_appear(*self.EMPTY_CART_TXT)
        self.verify_text("Your cart is empty", *self.EMPTY_CART_TXT)

    def verify_items_in_cart(self, item_count):
        items = self.find_elements(*self.CART_ITEMS)

        assert len(items) == int(item_count), f"Expected {item_count} items but got {len(items)}"
        print("Test case Passed")
