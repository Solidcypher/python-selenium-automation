from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SignInPage(BasePage):

    def verify_sign_in_page_appears(self):
        expected_text = "Sign into your Target account"
        actual_text = self.driver.find_element(By.XPATH,
                                               "//span[contains(text(),'Sign into your Target account')]").text

        assert expected_text in actual_text, f"Expected {expected_text} is not in actual text {actual_text}"

        print("Test case Passed")
