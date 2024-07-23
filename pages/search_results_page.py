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
        self.click(*self.ADD_TO_CART_BTN)

    def verify_text(self):  # This will verify text for your search
        actual_text = self.driver.find_element(*self.SEARCH_RESULTS_TXT).text

        assert 'xbox' in actual_text, f"Expected xbox not included in {actual_text}"

        print("Test case Passed")

    def verify_url(self):  # This will verify searched item is in current URL
        url = self.driver.current_url

        assert 'xbox' in url, f"Expected xbox not in {url}"

        print("Test case Passed")

    def verify_product_image(self):
        # scroll to be able to see all products
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")

        products = self.driver.find_elements(*self.PRODUCT_CARD)

        for product in products:
            picture = self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/ProductCard/ProductCardImage/primary']")

            assert picture, f"Expected {picture} not included in {product}"

    def verify_product_title(self):
        self.driver.execute_script("window.scrollBy(0, 5000)", "")
        sleep(3)
        self.driver.execute_script("window.scrollBy(0, 5000)", "")

        products = self.driver.find_elements(*self.PRODUCT_CARD)

        for product in products:
            title = self.driver.find_element(*self.PRODUCT_TITLE).text

            assert title, f"Expected {title} not included in {product}"

