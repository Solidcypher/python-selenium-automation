from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    EMPTY_CART_TXT = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_empty_cart(self):
        expected_text = "Your cart is empty"
        actual_text = self.driver.find_element(*self.EMPTY_CART_TXT).text

        assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

        print("Test case Passed")

    def verify_items_in_cart(self, item_count):
        items = self.driver.find_elements(By.CSS_SELECTOR, "[data-test='cartItem']")

        assert len(items) == int(item_count), f"Expected {item_count} items but got {len(items)}"
        print("Test case Passed")
