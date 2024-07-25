from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HelpPage(BasePage):

    def open_help_page(self):
        self.open_url('https://help.target.com/help')

    def verify_help_ui_elements(self, number): # I still need to fix this one.
        self.find_element(By.XPATH, "//h2[contains(text(),'Target Help')]")
        self.find_element(By.CLASS_NAME, "search_input")
        self.find_element(By.CSS_SELECTOR, "[alt='search']")
        self.find_elements(By.CLASS_NAME, "grid_6")
        self.find_elements(By.CLASS_NAME, "grid_4")
        self.find_elelment(By.XPATH, "//h2[contains(text(),'Browse all Help pages')]")

        # I am not sure how you would assert all of these. I think the homework only asked for the locators.