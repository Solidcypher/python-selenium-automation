from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from pages.base_page import BasePage


class HelpPage(BasePage):
    # HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    # HEADER_DELIVERY_PICKUP = (By.XPATH, "//h1[text()=' Drive Up & Order Pickup']")
    TOPIC_HEADER = (By.XPATH, "//h1[text()=' {SUBSTRING}']")
    TOPIC_DROPDOWN = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def _get_topic_locator(self, header_text):
        return [self.TOPIC_HEADER[0], self.TOPIC_HEADER[1].replace('{SUBSTRING}', header_text)]

    def open_help_page(self):
        self.open_url('https://help.target.com/help')

    def open_help_return_page(self):
        self.open_url(
            'https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_dropdown_topic(self, dd_topic):
        dd = self.find_element(*self.TOPIC_DROPDOWN)

        select = Select(dd)
        select.select_by_value(dd_topic)

    def verify_header_text(self, header_text):
        locator = self._get_topic_locator(header_text)

        self.wait_for_element_appear(*locator)

    # def verify_returns_page_open(self):
    #     self.wait_for_element_appear(*self.HEADER_RETURNS)
    #
    # def verify_delivery_pickup_page_open(self):
    #     self.wait_for_element_appear(*self.HEADER_DELIVERY_PICKUP)

    def verify_help_ui_elements(self, number):  # I still need to fix this one.
        self.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]")
        self.find_element(By.CLASS_NAME, "search_input")
        self.find_element(By.CSS_SELECTOR, "[alt='search']")
        self.find_elements(By.CLASS_NAME, "grid_6")
        self.find_elements(By.CLASS_NAME, "grid_4")
        self.find_elelment(By.XPATH, "//h2[contains(text(),'Browse all Help pages')]")

        # I am not sure how you would assert all of these. I think the homework only asked for the locators.
