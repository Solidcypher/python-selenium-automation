from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TermsAndConditions(BasePage):

    def verify_pp_url(self):
        self.verify_partial_url('/terms-conditions/')