from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SearchResultsPage(BasePage):
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    PRODUCT_CARD = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardVariantDefault']")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")

    def add_to_cart_search_page(self):  # This will add the first item in your search to cart
        self.wait_and_click(*self.ADD_TO_CART_BTN)

    def verify_search_results_text(self, expected_product):  # This will verify text for your search
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_product_in_url(self, expected_product):  # This will verify searched item is in current URL
        self.verify_partial_url(expected_product)

    def verify_product_image(self):
        # scroll to be able to see all products
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")

        products = self.find_elements(*self.PRODUCT_CARD)

        for product in products:
            picture = self.find_element(*self.PRODUCT_IMAGE)

            assert picture, f"Expected {picture} not included in {product}"

    def verify_product_title(self):
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")

        products = self.find_elements(*self.PRODUCT_CARD)

        for product in products:
            title = self.find_element(*self.PRODUCT_TITLE).text

            assert title, f"Expected {title} not included in {product}"

